#!/usr/bin/env python
"""
03_extract_concepts.py (XAF-tuned, API-aware)

Purpose
-------
Section-level extraction of:
 - Canonical concepts (from config/concepts.yml, with synonyms)
 - API symbols/namespaces (regex from config/patterns.yml)
 - Platform scope (Blazor / WinForms / Web API) from text cues

Enhancements for API Reference Docs
-----------------------------------
 - Detects API docs via path markers (configurable) and optional regex
 - Keeps only high-signal headings in API docs (Summary/Remarks/etc.)
 - Skips boilerplate headings (Parameters/Returns/etc.)
 - Light de-duplication of API sections per document

Inputs
------
 - outputs/topics_inventory.parquet (from 01_ingest_parse.py)
 - config/concepts.yml
 - config/patterns.yml (optional sections are auto-defaulted)

Output
------
 - outputs/doc_concepts.parquet

Schema (one row per SECTION)
----------------------------
doc_id, section_id, h_path, concepts[], apis[], platforms[], concept_density (float),
is_api (bool), kept (bool), skip_reason (str or None)
"""
from __future__ import annotations

import re
import sys
import hashlib
import argparse
from pathlib import Path
from typing import Dict, List, Set, Optional, Any
import pandas as pd
from tqdm import tqdm

# Add parent directory to path for validation imports
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils.pipeline_validators import (
    PipelineValidator, ValidationReport, ValidationResult,
    save_validation_report, load_validation_thresholds
)

# Semantic extraction enhancement
try:
    from sentence_transformers import SentenceTransformer
    SEMANTIC_AVAILABLE = True
except ImportError:
    SEMANTIC_AVAILABLE = False
    print("⚠️  sentence-transformers not available. Falling back to lexical matching only.")

# ---------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = PROJECT_ROOT / "config"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
TOPICS_INVENTORY = OUTPUT_DIR / "topics_inventory.parquet"
CONCEPTS_YML = CONFIG_DIR / "concepts.yml"
PATTERNS_YML = CONFIG_DIR / "patterns.yml"
OUT_PARQUET = OUTPUT_DIR / "doc_concepts.parquet"

# ---------------------------------------------------------------------
# YAML helpers
# ---------------------------------------------------------------------
try:
    import yaml
except Exception:
    yaml = None

def load_yaml(path: Path, *, required: bool) -> dict:
    if not path.exists():
        if required:
            raise FileNotFoundError(f"Missing required file: {path}")
        return {}
    if yaml is None:
        raise RuntimeError("PyYAML is required to load configuration files.")
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

def get_cfg_section(cfg: dict, key: str, default: list) -> list:
    val = cfg.get(key)
    return val if isinstance(val, list) else default

# ---------------------------------------------------------------------
# Normalization & hashing
# ---------------------------------------------------------------------
def normalize_text_for_match(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "")).strip().lower()

def strip_code_fences(text: str) -> str:
    # Conservative removal of fenced code blocks (```...``` or ~~~...~~~)
    return re.sub(r"(^|\n)(```|~~~)[^\n]*\n.*?\n[ \t]*\2[ \t]*\n", "\n", text or "", flags=re.DOTALL)

def normalize_text_for_hash(text: str) -> str:
    t = strip_code_fences(text or "")
    t = re.sub(r"\s+", " ", t).strip().lower()
    return t

def stable_hash(text: str) -> str:
    return hashlib.md5(text.encode("utf-8")).hexdigest()

# ---------------------------------------------------------------------
# Safe list coercion (handles Arrow/NumPy/Pandas list-likes)
# ---------------------------------------------------------------------
from collections.abc import Iterable

def as_list(x: Any) -> List[Any]:
    """Return a real Python list for any iterable that isn't a scalar or dict."""
    if x is None:
        return []
    # Handle pandas NaN specifically
    try:
        import math
        if isinstance(x, float) and math.isnan(x):
            return []
    except Exception:
        pass
    if isinstance(x, (str, bytes, dict)):
        s = x.strip() if isinstance(x, str) else None
        return [s] if s else []
    if isinstance(x, Iterable):
        try:
            return list(x)
        except TypeError:
            return []
    try:
        return list(x)
    except Exception:
        return []

def as_list_of_dicts(x: Any) -> List[dict]:
    lst = as_list(x)
    out: List[dict] = []
    for item in lst:
        if isinstance(item, dict):
            out.append(item)
        else:
            # Best-effort coercion of dict-like structures; ignore if not possible
            try:
                out.append(dict(item))
            except Exception:
                pass
    return out

# ---------------------------------------------------------------------
# Compile concept index and regexes
# ---------------------------------------------------------------------
def compile_concept_index(concepts_cfg: dict) -> Dict[str, dict]:
    """
    Build lookup:
      normalized_term -> {name, type, tags}
    """
    index: Dict[str, dict] = {}
    for c in concepts_cfg.get("concepts", []):
        name = c["name"]
        meta = {"name": name, "type": c.get("type"), "tags": c.get("tags", [])}
        index[normalize_text_for_match(name)] = meta
        for syn in c.get("synonyms", []) or []:
            index[normalize_text_for_match(syn)] = meta
    return index

def build_hierarchy_map(concepts_cfg: dict) -> Dict[str, Optional[str]]:
    """
    Build parent lookup:
      concept_name -> parent_name (or None if top-level)
    """
    hierarchy: Dict[str, Optional[str]] = {}
    for c in concepts_cfg.get("concepts", []):
        name = c["name"]
        parent = c.get("parent")
        hierarchy[name] = parent
    return hierarchy

def get_all_ancestors(concept: str, hierarchy: Dict[str, Optional[str]]) -> List[str]:
    """
    Get all ancestor concepts in order (immediate parent first, then grandparent, etc.)
    Returns empty list if concept has no parents.
    """
    ancestors: List[str] = []
    current = concept
    seen: Set[str] = {current}  # Prevent infinite loops in misconfigured hierarchies
    
    while True:
        parent = hierarchy.get(current)
        if not parent or parent in seen:
            break
        ancestors.append(parent)
        seen.add(parent)
        current = parent
    
    return ancestors

def enrich_with_hierarchy(
    concepts: Set[str], 
    hierarchy: Dict[str, Optional[str]]
) -> Set[str]:
    """
    Add all parent concepts for the given concepts based on hierarchy.
    Example: If 'Simple Action' is found, add 'Action Types' and 'Actions'.
    """
    enriched = set(concepts)
    for concept in list(concepts):
        ancestors = get_all_ancestors(concept, hierarchy)
        enriched.update(ancestors)
    return enriched

def compile_regexes(patterns_cfg: dict) -> dict:
    """
    Compile regex patterns from patterns.yml.
    Expected optional sections (with safe defaults if missing):
      - apis
      - platform_qualifiers
      - xref_targets
      - api_headings_keep
      - api_headings_skip
      - api_doc_path_regex
      - api_doc_path_markers
    """
    compiled: dict = {}

    def _compile_list(key: str) -> list:
        items = patterns_cfg.get(key) or []
        out = []
        for item in items:
            pat_str = item.get("pattern")
            if not pat_str:
                continue
            flags = re.MULTILINE | re.IGNORECASE
            pat = re.compile(pat_str, flags)
            out.append({**item, "regex": pat})
        return out

    compiled["apis"] = _compile_list("apis")
    compiled["platform_qualifiers"] = _compile_list("platform_qualifiers")
    compiled["xref_targets"] = _compile_list("xref_targets")
    compiled["api_headings_keep"] = _compile_list("api_headings_keep")
    compiled["api_headings_skip"] = _compile_list("api_headings_skip")
    compiled["api_doc_path_regex"] = _compile_list("api_doc_path_regex")

    # Provide defaults for common API doc path markers (used if YAML absent)
    compiled["api_doc_path_markers"] = patterns_cfg.get("api_doc_path_markers") or [
        "/api/",
        "/apidoc/",
        "/reference/",
        "/api-docs/",
        "/namespaces/",
        "/classes/",
    ]
    return compiled

# ---------------------------------------------------------------------
# Extraction functions
# ---------------------------------------------------------------------
def extract_concepts(text: str, concept_index: dict) -> Set[str]:
    """Legacy lexical concept extraction (kept for backward compatibility)"""
    found: Set[str] = set()
    norm = normalize_text_for_match(text)
    for term, meta in concept_index.items():
        # word-boundary match on normalized text
        if re.search(rf"\b{re.escape(term)}\b", norm):
            found.add(meta["name"])
    return found


def extract_concepts_semantic(
    text: str,
    heading: str,
    concept_index: dict,
    concepts_config: list,
    model: Optional[Any] = None,
    min_confidence: float = 0.60
) -> tuple[List[str], Dict[str, float]]:
    """
    Enhanced concept extraction with selective semantic validation.
    Only validates ambiguous concepts for performance.
    
    Returns:
        (concept_list, confidence_dict)
    """
    # Step 1: Lexical matching (fast first pass)
    lexical_matches = extract_concepts(text, concept_index)
    
    if not SEMANTIC_AVAILABLE or model is None:
        # Fallback: return lexical matches with default confidence
        return list(lexical_matches), {c: 1.0 for c in lexical_matches}
    
    # Ambiguous concepts that need semantic validation (common words that could be false positives)
    # Note: Application Templates removed - has dedicated domain coherence check already
    AMBIGUOUS_CONCEPTS = {
        'Deployment', 'Testing', 'Logging', 'Validation', 'Actions', 'Views', 
        'Reports', 'Navigation', 'Migration', 'Controllers and Actions',
        'Security System', 'Layout', 'Modules', 'Charts', 'Maps',
        'Authentication', 'Authorization', 'Filtering UI', 'Theming', 'Notifications'
    }
    
    # Step 2: Selective semantic validation (only for ambiguous concepts)
    import numpy as np
    
    concepts_with_confidence = {}
    concept_definitions = {c['name']: c for c in concepts_config}
    
    for concept_name in lexical_matches:
        is_ambiguous = concept_name in AMBIGUOUS_CONCEPTS
        concept_def = concept_definitions.get(concept_name, {})
        
        # Only validate ambiguous concepts semantically
        if is_ambiguous:
            confidence = _validate_concept_semantically(
                text=text,
                heading=heading,
                concept_name=concept_name,
                concept_def=concept_def,
                model=model
            )
            
            # Apply domain coherence filtering
            if concept_name == 'Deployment':
                confidence = _check_deployment_context(text, heading, confidence)
            elif concept_name == 'Testing':
                confidence = _check_testing_context(text, heading, confidence)
            elif concept_name == 'Migration':
                confidence = _check_migration_context(text, heading, confidence)
            elif concept_name == 'Application Templates':
                confidence = _check_application_templates_context(text, heading, confidence)
        else:
            # Trust lexical match for unambiguous concepts
            confidence = 1.0
        
        # Apply keyword validation (for ALL concepts)
        confidence = _apply_keyword_validation(
            text=text,
            heading=heading,
            concept_name=concept_name,
            concept_def=concept_def,
            base_confidence=confidence,
            is_ambiguous=is_ambiguous
        )
        
        if confidence >= min_confidence:
            concepts_with_confidence[concept_name] = confidence
    
    # Sort by confidence
    sorted_concepts = sorted(
        concepts_with_confidence.items(),
        key=lambda x: x[1],
        reverse=True
    )
    
    concept_list = [name for name, _ in sorted_concepts]
    confidence_dict = dict(sorted_concepts)
    
    return concept_list, confidence_dict


def _validate_concept_semantically(
    text: str,
    heading: str,
    concept_name: str,
    concept_def: dict,
    model: Any
) -> float:
    """Validate concept match using semantic similarity"""
    import numpy as np
    
    # Build concept description
    concept_parts = [concept_name]
    if 'description' in concept_def:
        concept_parts.append(concept_def['description'])
    synonyms = concept_def.get('synonyms', [])[:3]
    if synonyms:
        concept_parts.append(f"Also known as: {', '.join(synonyms)}")
    concept_desc = " ".join(concept_parts)
    
    # Build section description (heading + first 500 chars)
    section_desc = f"{heading}\n\n{text[:500]}"
    
    # Calculate similarity
    try:
        embeddings = model.encode([concept_desc, section_desc])
        similarity = np.dot(embeddings[0], embeddings[1]) / (
            np.linalg.norm(embeddings[0]) * np.linalg.norm(embeddings[1])
        )
        
        # Map similarity [0.4, 0.8] -> confidence [0.6, 1.0]
        MIN_SIM = 0.4
        if similarity < MIN_SIM:
            return 0.0
        
        confidence = 0.6 + (similarity - MIN_SIM) * (0.4 / 0.4)
        return min(1.0, max(0.0, confidence))
    except Exception:
        return 1.0  # Fallback to accepting the match


def _check_deployment_context(text: str, heading: str, base_confidence: float) -> float:
    """
    Domain coherence check for Deployment concept.
    Suppress if workflow/BPM context detected without infrastructure keywords.
    """
    text_lower = (text or "").lower()
    heading_lower = (heading or "").lower()
    combined = heading_lower + " " + text_lower[:500]
    
    # Detect workflow/BPM context
    workflow_keywords = ['state machine', 'workflow designer', 'workflow definition',
                         'workflow activity', 'workflow instance', 'transition',
                         'business process']
    workflow_matches = sum(1 for kw in workflow_keywords if kw in combined)
    
    # Detect infrastructure deployment context
    infra_keywords = ['iis', 'azure', 'docker', 'kubernetes', 'nginx', 'apache',
                      'certificate', 'ssl', 'https', 'server configuration',
                      'production environment', 'hosting', 'deploy to', 'deployment guide']
    infra_matches = sum(1 for kw in infra_keywords if kw in combined)
    
    # If strong workflow signal but weak infra signal, reduce confidence
    if workflow_matches >= 2 and infra_matches == 0:
        return base_confidence * 0.4  # Likely false positive
    elif workflow_matches >= 1 and infra_matches == 0:
        return base_confidence * 0.7  # Possibly false positive
    
    return base_confidence


def _check_testing_context(text: str, heading: str, base_confidence: float) -> float:
    """
    Domain coherence check for Testing concept.
    Suppress if casual testing mention vs XAF Testing strategies.
    """
    text_lower = (text or "").lower()
    heading_lower = (heading or "").lower()
    combined = heading_lower + " " + text_lower[:500]
    
    # Testing as XAF topic
    testing_topic_keywords = ['unit test', 'integration test', 'test application',
                              'test project', 'automated testing', 'testing strategy',
                              'test database', 'mock', 'fixture']
    testing_topic_matches = sum(1 for kw in testing_topic_keywords if kw in combined)
    
    # Casual testing mentions
    casual_keywords = ['when testing', 'after testing', 'while testing', 'test this',
                       'test the', 'for testing purposes']
    casual_matches = sum(1 for kw in casual_keywords if kw in combined)
    
    # If casual usage without testing topic keywords, reduce confidence
    if casual_matches >= 1 and testing_topic_matches == 0:
        return base_confidence * 0.5
    
    return base_confidence


def _check_migration_context(text: str, heading: str, base_confidence: float) -> float:
    """
    Domain coherence check for Migration concept.
    Suppress generic "migration" vs EF Core Migrations topic.
    """
    text_lower = (text or "").lower()
    heading_lower = (heading or "").lower()
    combined = heading_lower + " " + text_lower[:500]
    
    # EF Core Migration topic
    ef_migration_keywords = ['ef core migration', 'database migration', 'migration file',
                             'add-migration', 'update-database', 'migration script',
                             'migration strategy', 'code-first migration']
    ef_matches = sum(1 for kw in ef_migration_keywords if kw in combined)
    
    # Generic migration usage
    generic_keywords = ['migration guide', 'migration path', 'migrating from',
                        'migration process']
    generic_matches = sum(1 for kw in generic_keywords if kw in combined)
    
    # If generic usage without EF keywords, reduce confidence
    if generic_matches >= 1 and ef_matches == 0:
        return base_confidence * 0.6
    
    return base_confidence


def _check_application_templates_context(text: str, heading: str, base_confidence: float) -> float:
    """
    Domain coherence check for Application Templates concept.
    Suppress IDE project/item templates vs XAF UI Application Templates (IFrameTemplate/IWindowTemplate).
    """
    text_lower = (text or "").lower()
    heading_lower = (heading or "").lower()
    combined = heading_lower + " " + text_lower[:500]
    
    # XAF Application Templates (UI controls)
    xaf_template_keywords = ['iframetemplate', 'iwindowtemplate', 'frametemplate', 'windowtemplate',
                             'detailformtemplate', 'mainformtemplate', 'popupform', 'lookupform',
                             'applicationwindowtemplate', 'ribbonformtemplate', 'nestedframetemplate',
                             'templatecontext', 'createtemplate', 'window layout', 'frame site',
                             'template customization', 'blazor application template', 'winforms application template']
    xaf_matches = sum(1 for kw in xaf_template_keywords if kw in combined)
    
    # IDE Template Kit (project/item scaffolding)
    ide_template_keywords = ['template kit', 'project template', 'item template', 'solution wizard',
                             'cross-ide', 'visual studio template', 'add new item', 'new project',
                             'scaffolding', 'devexpress template kit', 'file → new', 'create new project']
    ide_matches = sum(1 for kw in ide_template_keywords if kw in combined)
    
    # If IDE template context without XAF UI keywords, likely false positive
    if ide_matches >= 2 and xaf_matches == 0:
        return base_confidence * 0.3  # Strong IDE signal, no XAF signal
    elif ide_matches >= 1 and xaf_matches == 0:
        return base_confidence * 0.5  # Moderate IDE signal
    
    return base_confidence


def _apply_keyword_validation(
    text: str,
    heading: str,
    concept_name: str,
    concept_def: dict,
    base_confidence: float,
    is_ambiguous: bool
) -> float:
    """
    Keyword-based precision validation.
    
    Strategy:
    - If API keywords present: BOOST confidence (high precision match)
    - If no keywords defined: No change (can't validate)
    - If has keywords but none found: SLIGHT reduction for ambiguous concepts
    
    Args:
        text: Section text
        heading: Section heading
        concept_name: Concept being validated
        concept_def: Concept definition from config
        base_confidence: Confidence score before keyword validation
        is_ambiguous: Whether concept is in AMBIGUOUS_CONCEPTS set
    
    Returns:
        Adjusted confidence score
    """
    keywords = concept_def.get('keywords', [])
    
    # If no keywords defined, can't validate
    if not keywords:
        return base_confidence
    
    # Count keyword matches (case-insensitive)
    combined = (heading + " " + text).lower()
    keyword_matches = sum(1 for kw in keywords if kw.lower() in combined)
    
    # BOOST: API symbols found (high precision)
    if keyword_matches > 0:
        # More keywords = higher boost (cap at +0.20)
        boost = min(0.20, 0.05 * keyword_matches)
        return min(0.98, base_confidence + boost)
    
    # SLIGHT SUPPRESS: No keywords + ambiguous concept (but don't eliminate)
    # Only apply modest reduction - domain coherence checks are primary filter
    if is_ambiguous:
        return base_confidence * 0.85  # Gentle -15% penalty instead of -50%
    
    # NEUTRAL: No keywords + specific concept = general language match is OK
    return base_confidence


def extract_apis(text: str, api_patterns: List[dict]) -> Set[str]:
    found: Set[str] = set()
    # Common YAML/metadata field names that get incorrectly appended to API names
    STRIP_SUFFIXES = ["description", "summary", "remarks", "syntax", "type", "name", "uid", 
                      "content", "title", "seealso", "linkid"]
    
    for p in api_patterns:
        for m in p["regex"].findall(text or ""):
            if isinstance(m, tuple):
                m = next((x for x in m if x), "")
            m = (m or "").strip()
            if m:
                # Remove incorrectly appended YAML field names
                # Check if the match ends with a lowercase suffix (YAML keys are lowercase)
                m_lower = m.lower()
                for suffix in STRIP_SUFFIXES:
                    # Match should end with the suffix directly (no delimiter)
                    if m_lower.endswith(suffix) and len(m) > len(suffix):
                        # Verify the part before suffix looks like an API name (ends with letter/number)
                        candidate = m[:-len(suffix)]
                        if candidate and candidate[-1].isalnum():
                            m = candidate
                            break
                found.add(m)
    return found

def extract_platforms(text: str, platform_patterns: List[dict]) -> Set[str]:
    found: Set[str] = set()
    t = text or ""
    for p in platform_patterns:
        if p["regex"].search(t):
            lab = p.get("platform")
            if lab:
                found.add(lab)
    return found

# ---------------------------------------------------------------------
# API-doc specific logic
# ---------------------------------------------------------------------
def looks_like_api_doc(path: str, regexes: dict) -> bool:
    """Heuristics: path markers OR any configured regex match."""
    p = (path or "").replace("\\", "/").lower()
    # Path markers
    for marker in regexes.get("api_doc_path_markers", []):
        if marker.lower() in p:
            return True
    # Regexes
    for r in regexes.get("api_doc_path_regex", []):
        if r["regex"].search(p):
            return True
    return False

def should_skip_api_section(
    h_path_list: List[str],
    keep_patterns: List[dict],
    skip_patterns: List[dict],
) -> tuple[bool, Optional[str], bool]:
    """
    Returns:
      (skip: bool, reason: str|None, forced_keep: bool)

    Rules:
      - If last heading matches any 'keep' pattern => forced_keep
      - Else if matches any 'skip' pattern      => skip (reason="api_headings_skip")
      - Else => not skip
    """
    last = ""
    if isinstance(h_path_list, list) and len(h_path_list) > 0:
        last = str(h_path_list[-1])
    last_norm = (last or "").strip()

    # Forced keep
    for p in keep_patterns:
        if p["regex"].search(last_norm):
            return False, None, True

    # Skip boilerplate
    for p in skip_patterns:
        if p["regex"].search(last_norm):
            return True, "api_headings_skip", False

    return False, None, False

# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------
def validate_phase3_output(df: pd.DataFrame, concepts_cfg: dict, run_quality_checks: bool = False) -> ValidationReport:
    """
    Validate Phase 3 output data.
    
    Args:
        df: The doc_concepts DataFrame
        concepts_cfg: The concepts configuration dictionary
        run_quality_checks: Whether to run deeper quality validation
    
    Returns:
        ValidationReport with validation results
    """
    config_path = Path(__file__).resolve().parents[1] / "config" / "validation_thresholds.yml"
    validator = PipelineValidator(config_path)
    report = ValidationReport(phase_name="Extract Concepts", phase_number=3)
    
    # Level 1: Quick Sanity Checks
    print("\n🔍 Running Level 1 validation (quick sanity checks)...")
    
    # Check schema
    required_cols = ["doc_id", "section_id", "h_path", "concepts", "apis", "platforms", 
                     "concept_density", "concept_confidences", "is_api", "kept", "skip_reason"]
    column_types = {
        "doc_id": str,
        "section_id": str,
        "h_path": str,
        "concepts": list,
        "apis": list,
        "platforms": list,
        "concept_density": float,
        "concept_confidences": dict,
        "is_api": bool,
        "kept": bool
    }
    report.add_result(validator.validate_schema(df, required_cols, column_types, "Schema validation"))
    
    # Check row count
    thresholds = load_validation_thresholds(config_path)
    report.add_result(validator.validate_row_count(df, min_rows=10000, check_name="Minimum sections"))
    
    # Check kept percentage
    total = len(df)
    kept = int(df["kept"].sum()) if total else 0
    kept_pct = (kept / total * 100) if total > 0 else 0
    
    report.add_result(validator.validate_threshold(
        actual_value=kept_pct,
        threshold_key='min_kept_percentage',
        phase_key='phase3_concepts',
        comparison='>=',
        check_name="Minimum kept percentage"
    ))
    
    report.add_result(validator.validate_threshold(
        actual_value=kept_pct,
        threshold_key='max_kept_percentage',
        phase_key='phase3_concepts',
        comparison='<=',
        check_name="Maximum kept percentage"
    ))
    
    # Check average concepts per section
    kept_mask = df['kept'] == True
    if kept_mask.sum() > 0:
        avg_concepts = df.loc[kept_mask, 'concepts'].apply(len).mean()
        report.add_result(validator.validate_threshold(
            actual_value=avg_concepts,
            threshold_key='min_avg_concepts_per_section',
            phase_key='phase3_concepts',
            comparison='>=',
            check_name="Minimum avg concepts/section"
        ))
        
        report.add_result(validator.validate_threshold(
            actual_value=avg_concepts,
            threshold_key='max_avg_concepts_per_section',
            phase_key='phase3_concepts',
            comparison='<=',
            check_name="Maximum avg concepts/section"
        ))
    
    # Check concept density range
    report.add_result(validator.validate_range(
        df[df['kept'] == True] if 'kept' in df.columns else df,
        'concept_density',
        min_value=0.0,
        max_value=1.0,
        allow_null=False,
        check_name="Concept density range [0.0-1.0]"
    ))
    
    # Check API sections
    api_rows = df[df["is_api"] == True]
    api_count = len(api_rows)
    report.add_result(validator.validate_threshold(
        actual_value=api_count,
        threshold_key='min_api_sections',
        phase_key='phase3_concepts',
        comparison='>=',
        check_name="Minimum API sections"
    ))
    
    if run_quality_checks:
        print("\n🔍 Running Level 2 validation (quality checks)...")
        
        # Validate concepts match vocabulary
        if concepts_cfg:
            allowed_concepts = set()
            for entry in concepts_cfg.get('concepts', []):
                if isinstance(entry, dict):
                    concept_name = entry.get('name', '')
                    if concept_name:
                        allowed_concepts.add(concept_name)
            
            if allowed_concepts:
                report.add_result(validator.validate_vocabulary(
                    df[df['kept'] == True] if 'kept' in df.columns else df,
                    'concepts',
                    allowed_concepts,
                    check_name="Concepts match vocabulary"
                ))
        
        # Check for sections with zero concepts (kept sections only)
        kept_df = df[df['kept'] == True] if 'kept' in df.columns else df
        zero_concepts = kept_df[kept_df['concepts'].apply(len) == 0]
        
        if len(zero_concepts) > 0:
            zero_pct = len(zero_concepts) / len(kept_df) * 100
            report.add_result(ValidationResult(
                check_name="Sections with zero concepts",
                passed=zero_pct < 5.0,  # Less than 5% is acceptable
                message=f"{len(zero_concepts)} kept sections ({zero_pct:.1f}%) have zero concepts",
                severity="warning" if zero_pct < 5.0 else "error",
                details={"count": len(zero_concepts), "percentage": zero_pct}
            ))
        else:
            report.add_result(ValidationResult(
                check_name="Sections with zero concepts",
                passed=True,
                message="All kept sections have at least one concept",
                severity="info"
            ))
        
        # Check skip reason distribution
        skip_reasons = df[df['kept'] == False]['skip_reason'].value_counts().to_dict()
        report.add_result(ValidationResult(
            check_name="Skip reason distribution",
            passed=True,
            message=f"Found {len(skip_reasons)} different skip reasons",
            severity="info",
            details=skip_reasons
        ))
    
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description="Phase 3: Extract concepts from sections")
    parser.add_argument('--skip-validation', action='store_true', help='Skip validation checks')
    parser.add_argument('--validate-quality', action='store_true', help='Run deeper quality validation (Level 2)')
    parser.add_argument('--save-report', action='store_true', help='Save validation report to JSON')
    args = parser.parse_args()
    
    # Load config
    print("="*70)
    print("Phase 3: Extract Concepts")
    print("="*70)
    print("\n🔧 Loading configuration…")
    if not TOPICS_INVENTORY.exists():
        print(f"❌ Missing input: {TOPICS_INVENTORY}")
        sys.exit(1)

    concepts_cfg = load_yaml(CONCEPTS_YML, required=True)             # required
    patterns_cfg = load_yaml(PATTERNS_YML, required=False)            # optional
    concept_index = compile_concept_index(concepts_cfg)
    hierarchy = build_hierarchy_map(concepts_cfg)
    regexes = compile_regexes(patterns_cfg)

    # Names whose type is Platform or runtime — route to platforms column, not concepts
    platform_concept_names = frozenset(
        c["name"]
        for c in concepts_cfg.get("concepts", [])
        if c.get("type") in ("Platform", "runtime")
    )
    print(f"  Platform/runtime concepts (routed to platforms column): {sorted(platform_concept_names)}")

    # Load docs
    print("📚 Loading topics inventory…")
    docs_df = pd.read_parquet(TOPICS_INVENTORY, engine="pyarrow")

    # Normalize list-like columns coming from Parquet/Arrow
    if "sections" in docs_df.columns:
        docs_df["sections"] = docs_df["sections"].apply(as_list_of_dicts)
    if "headings" in docs_df.columns:
        docs_df["headings"] = docs_df["headings"].apply(as_list_of_dicts)
    if "internal_links" in docs_df.columns:
        docs_df["internal_links"] = docs_df["internal_links"].apply(as_list)

    # Work with plain dicts to avoid dtype surprises
    docs = docs_df.to_dict(orient="records")

    # Prep collectors
    rows: List[dict] = []
    # For API duplicate suppression (per doc_id)
    api_seen_hashes_per_doc: Dict[str, Set[str]] = {}

    # Fallback thresholds (tunable)
    MIN_TOKENS_GENERAL = 5           # very short fragments are noise
    MIN_TOKENS_API_LOW_SIGNAL = 30   # low-signal API sections must meet length unless forced keep

    # Load semantic model if available
    semantic_model = None
    if SEMANTIC_AVAILABLE:
        print("🤖 Loading semantic model (sentence-transformers/all-MiniLM-L6-v2)...")
        try:
            semantic_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
            print("   ✅ Semantic validation enabled")
        except Exception as e:
            print(f"   ⚠️  Could not load semantic model: {e}")
            print("   ⚠️  Falling back to lexical matching")

    print("🧠 Extracting concepts/APIs/platforms (section-level)…")
    for doc in tqdm(docs, total=len(docs)):
        doc_id: str = doc["doc_id"]
        path: str = doc.get("path", "") or ""
        title: str = doc.get("title", "") or ""
        sections: List[dict] = doc.get("sections", []) or []
        is_api = looks_like_api_doc(path, regexes)

        if is_api and doc_id not in api_seen_hashes_per_doc:
            api_seen_hashes_per_doc[doc_id] = set()

        for s in sections:
            # Pull fields safely
            section_id = s.get("section_id") or f"{Path(doc_id).stem}::unknown"
            h_path_list = as_list(s.get("h_path"))
            h_path = " > ".join([str(x) for x in h_path_list if isinstance(x, (str, int))])

            # Build section text (Title + Heading trail + Body + first code block)
            code_blocks = as_list(s.get("code_blocks"))
            first_code = code_blocks[0] if code_blocks else ""
            section_text = "\n".join([title, h_path, s.get("text", "") or "", first_code]).strip()

            # Skip tiny fragments everywhere
            token_count = len(section_text.split())
            if token_count < MIN_TOKENS_GENERAL:
                rows.append({
                    "doc_id": doc_id,
                    "section_id": section_id,
                    "h_path": h_path,
                    "concepts": [],
                    "apis": [],
                    "platforms": [],
                    "concept_density": 0.0,
                    "is_api": bool(is_api),
                    "kept": False,
                    "skip_reason": "too_short",
                })
                continue

            # API-doc specific filtering
            skip_reason = None
            forced_keep = False
            if is_api:
                skip_api, reason, forced_keep = should_skip_api_section(
                    h_path_list,
                    regexes.get("api_headings_keep", []),
                    regexes.get("api_headings_skip", []),
                )
                if skip_api and not forced_keep:
                    rows.append({
                        "doc_id": doc_id,
                        "section_id": section_id,
                        "h_path": h_path,
                        "concepts": [],
                        "apis": [],
                        "platforms": [],
                        "concept_density": 0.0,
                        "is_api": True,
                        "kept": False,
                        "skip_reason": reason or "api_skip",
                    })
                    continue

                # Length gating for low-signal API sections (unless forced keep)
                if not forced_keep and token_count < MIN_TOKENS_API_LOW_SIGNAL:
                    rows.append({
                        "doc_id": doc_id,
                        "section_id": section_id,
                        "h_path": h_path,
                        "concepts": [],
                        "apis": [],
                        "platforms": [],
                        "concept_density": 0.0,
                        "is_api": True,
                        "kept": False,
                        "skip_reason": "api_low_signal_short",
                    })
                    continue

                # De-duplicate API sections per doc (after normalization)
                norm_hash = stable_hash(normalize_text_for_hash(section_text))
                seen = api_seen_hashes_per_doc[doc_id]
                if norm_hash in seen:
                    rows.append({
                        "doc_id": doc_id,
                        "section_id": section_id,
                        "h_path": h_path,
                        "concepts": [],
                        "apis": [],
                        "platforms": [],
                        "concept_density": 0.0,
                        "is_api": True,
                        "kept": False,
                        "skip_reason": "api_dup_section",
                    })
                    continue
                seen.add(norm_hash)

            # Extraction with semantic validation
            if SEMANTIC_AVAILABLE and 'semantic_model' in locals():
                concepts_list, concept_confidences = extract_concepts_semantic(
                    text=section_text,
                    heading=h_path,
                    concept_index=concept_index,
                    concepts_config=concepts_cfg['concepts'],
                    model=semantic_model,
                    min_confidence=0.60
                )
                concepts = set(concepts_list)
            else:
                concepts = extract_concepts(section_text, concept_index)
                concept_confidences = {c: 1.0 for c in concepts}
            
            # Enrich with hierarchical parents
            concepts = enrich_with_hierarchy(concepts, hierarchy)

            # Split platform/runtime-typed concepts into the platforms column
            platform_from_concepts = {c for c in concepts if c in platform_concept_names}
            concepts -= platform_from_concepts

            apis = extract_apis(section_text, regexes.get("apis", []))
            platforms = extract_platforms(section_text, regexes.get("platform_qualifiers", []))
            platforms |= platform_from_concepts  # merge in concept-derived platforms

            # Density
            concept_density = round(len(concepts) / max(token_count, 1), 4)

            rows.append({
                "doc_id": doc_id,
                "section_id": section_id,
                "h_path": h_path,
                "concepts": sorted(concepts),
                "concept_confidences": concept_confidences,
                "apis": sorted(apis),
                "platforms": sorted(platforms),
                "concept_density": concept_density,
                "is_api": bool(is_api),
                "kept": True,
                "skip_reason": skip_reason,
            })

    out_df = pd.DataFrame(rows)

    # Persist
    OUT_PARQUET.parent.mkdir(parents=True, exist_ok=True)
    print(f"\n💾 Writing output → {OUT_PARQUET}")
    out_df.to_parquet(OUT_PARQUET, index=False, engine="pyarrow")

    # Summary
    total = len(out_df)
    kept = int(out_df["kept"].sum()) if total else 0
    api_rows = out_df[out_df["is_api"] == True]
    api_kept = int(api_rows["kept"].sum()) if len(api_rows) else 0
    api_total = len(api_rows)

    print("\n📊 Summary Statistics:")
    if total:
        print(f"   └─ Total sections: {total:,} | kept: {kept:,} ({(kept/total)*100:.1f}%)")
    if api_total > 0:
        print(f"   └─ API sections: {api_total:,} | kept: {api_kept:,} ({(api_kept/api_total)*100:.1f}%)")
    if total:
        print(f"   └─ Unique docs: {out_df['doc_id'].nunique():,}")
        kept_mask = out_df['kept'] if 'kept' in out_df.columns else []
        avg_concepts = out_df.loc[kept_mask, 'concepts'].apply(len).mean() if len(out_df.loc[kept_mask]) else 0.0
        print(f"   └─ Avg concepts/section (kept): {avg_concepts:.2f}")
    
    # Run validation
    if not args.skip_validation:
        report = validate_phase3_output(out_df, concepts_cfg, run_quality_checks=args.validate_quality)
        report.print_summary()
        
        if args.save_report:
            report_path = OUT_PARQUET.parent / 'validation_phase3.json'
            save_validation_report(report, report_path)
        
        if report.has_errors:
            print("\n❌ Phase 3 validation failed with errors. Review issues above.")
            sys.exit(1)
    else:
        print("\n⏭️  Validation skipped")
    
    print("\n✅ Phase 3 complete!")

if __name__ == "__main__":
    main()