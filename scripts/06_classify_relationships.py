#!/usr/bin/env python3
"""
Phase 6: Classify Semantic Relationships

Takes semantic pairs from Phase 5 and uses LLM to classify the relationship type
(explains, requires, uses, extends, applies_to, contrasts_with, related_to).

Usage:
    python scripts/06_classify_relationships.py --threshold 0.80 --limit 100
    python scripts/06_classify_relationships.py --types ca,ac --max-chars 2000
    python scripts/06_classify_relationships.py --resume classified_pairs_checkpoint.parquet
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Optional, Dict, List, Any
import glob

# Ensure project root is on sys.path when invoked as `python scripts/06_...py`
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd
from tqdm import tqdm

# Placeholder for LLM API - uncomment and configure based on your provider
from openai import OpenAI
import anthropic

from utils.taxonomy_loader import load_taxonomy_index


def safe_list(val):
    """Handle numpy arrays from parquet."""
    # Check for None or empty
    if val is None:
        return []
    # Handle numpy arrays
    if hasattr(val, 'tolist'):
        return val.tolist()
    # Handle scalar NaN (float)
    if isinstance(val, float) and pd.isna(val):
        return []
    # Convert to list if possible
    return list(val) if val else []


def load_relationship_prompt() -> str:
    """Load the relationship classification prompt."""
    prompt_path = Path("config/prompts/relationship_classification.md")
    if not prompt_path.exists():
        print(f"Warning: {prompt_path} not found, using default prompt")
        return """You are classifying the directional relationship FROM Section A TO Section B in XAF documentation.

Section types: API Reference, How-to Task (single scenario), Tutorial (multi-step end-to-end walkthrough), Conceptual (explains what and why).

Prefer 'requires' when A cannot be understood without first reading B (B is more foundational). Prefer 'uses' when A invokes an API or feature B documents. Prefer 'explains' when A is a conceptual overview describing what B implements. Use 'extends' when A customises or subclasses B. Use 'contrasts_with' for alternatives. Use 'applies_to' for platform/version scoping. Fall back to 'related_to' if none fit.

Return ONLY valid JSON."""
    
    return prompt_path.read_text(encoding='utf-8')


def extract_code_comments(code: str) -> str:
    """Extract comments from code blocks (C-style single and multi-line)."""
    import re
    comments = []
    
    # Multi-line comments /* ... */
    multi_line = re.findall(r'/\*\*?(.*?)\*/', code, re.DOTALL)
    for comment in multi_line:
        cleaned = ' '.join(line.strip().lstrip('*') for line in comment.split('\n'))
        comments.append(cleaned.strip())
    
    # Single-line comments //
    single_line = re.findall(r'//(.+?)$', code, re.MULTILINE)
    comments.extend([c.strip() for c in single_line if c.strip()])
    
    return ' '.join(comments)


def extract_code_identifiers(code: str) -> List[str]:
    """Extract class names, method names, namespaces from code."""
    import re
    identifiers = []
    
    # Namespaces: using X.Y.Z;
    namespaces = re.findall(r'using\s+([\w\.]+);', code)
    identifiers.extend(namespaces)
    
    # Class declarations: class ClassName, public class ClassName
    classes = re.findall(r'(?:public|private|protected|internal)?\s*(?:static|sealed|abstract)?\s*class\s+(\w+)', code)
    identifiers.extend(classes)
    
    # Interface declarations: interface IName
    interfaces = re.findall(r'(?:public|private|protected|internal)?\s*interface\s+(\w+)', code)
    identifiers.extend(interfaces)
    
    # Method declarations: void Method(), public async Task<T> Method()
    methods = re.findall(r'(?:public|private|protected|internal|static)?\s+(?:async\s+)?(?:\w+<?\w*>?\s+)?(\w+)\s*\(', code)
    identifiers.extend(methods)
    
    # Property declarations: public string Prop { get; set; }
    properties = re.findall(r'(?:public|private|protected|internal)?\s+\w+(?:<\w+>)?\s+(\w+)\s*\{', code)
    identifiers.extend(properties)
    
    # Filter out common language keywords
    keywords = {'void', 'int', 'string', 'bool', 'var', 'if', 'else', 'for', 'foreach', 
                'while', 'return', 'new', 'this', 'base', 'get', 'set', 'public', 'private'}
    identifiers = [i for i in identifiers if i not in keywords and len(i) > 2]
    
    return identifiers


def build_heading_context(h_path: List[str]) -> str:
    """Build contextual text from heading hierarchy."""
    if not h_path:
        return ""
    return "Navigation: " + " > ".join(h_path)


def build_fallback_text(section: Dict, parent_section: Optional[Dict] = None) -> str:
    """
    Build synthetic text from section metadata when text field is empty.
    Uses h_path, code blocks, and parent context.
    """
    text_parts = []
    
    # 1. Heading hierarchy provides context
    h_path = safe_list(section.get('h_path', []))
    if h_path:
        text_parts.append(build_heading_context(h_path))
    
    # 2. Section heading
    heading = section.get('heading', '')
    if heading:
        text_parts.append(f"Section: {heading}")
    
    # 3. Extract from code blocks
    code_blocks = safe_list(section.get('code_blocks', []))
    if code_blocks:
        all_comments = []
        all_identifiers = []
        
        for code_block in code_blocks[:3]:  # Limit to first 3 code blocks
            code_content = code_block.get('code', '') if isinstance(code_block, dict) else str(code_block)
            
            # Extract comments
            comments = extract_code_comments(code_content)
            if comments:
                all_comments.append(comments)
            
            # Extract identifiers
            identifiers = extract_code_identifiers(code_content)
            all_identifiers.extend(identifiers)
        
        if all_comments:
            text_parts.append("Code comments: " + ' '.join(all_comments[:200]))  # First 200 chars
        
        if all_identifiers:
            # Deduplicate and limit
            unique_identifiers = list(dict.fromkeys(all_identifiers))[:20]
            text_parts.append("Code elements: " + ', '.join(unique_identifiers))
    
    # 4. Use parent section text as context (if available)
    if parent_section:
        parent_text = parent_section.get('text', '')
        if parent_text:
            text_parts.append(f"Parent context: {parent_text[:300]}")
    
    return ' | '.join(text_parts) if text_parts else ""


def get_section_text(inventory_df: pd.DataFrame, doc_id: str, section_id: str, max_chars: int = 2000) -> str:
    """
    Extract section text from topics inventory with enhanced fallback.
    
    If section has no text content, builds synthetic text from:
    - Heading hierarchy (h_path)
    - Code block comments and identifiers
    - Parent section context
    """
    row = inventory_df[inventory_df["doc_id"] == doc_id]
    if row.empty:
        return ""
    
    sections = safe_list(row.iloc[0]["sections"])
    target_section = None
    parent_section = None
    
    # Find target section and its parent
    for i, section in enumerate(sections):
        if section.get("section_id") == section_id:
            target_section = section
            # Find parent by looking at previous sections with lower level
            if i > 0:
                target_level = section.get('level', 0)
                for j in range(i - 1, -1, -1):
                    if sections[j].get('level', 999) < target_level:
                        parent_section = sections[j]
                        break
            break
    
    if not target_section:
        return ""
    
    # Get text and heading
    text = target_section.get("text", "").strip()
    heading = target_section.get("heading", "")
    
    # If text exists, return it with heading
    if text:
        full_text = f"# {heading}\n\n{text}" if heading else text
        return full_text[:max_chars]
    
    # FALLBACK: Build synthetic text from metadata
    # This handles the 1,669 code-only sections
    fallback_text = build_fallback_text(target_section, parent_section)
    
    if fallback_text:
        # Add heading to fallback text
        full_text = f"# {heading}\n\n{fallback_text}" if heading else fallback_text
        return full_text[:max_chars]
    
    return ""


def build_taxonomy_context(
    source_concepts: List[str],
    target_concepts: List[str],
    taxonomy_index: Dict[str, Any],
) -> str:
    """Build a Taxonomy Context block summarising what the taxonomy knows about these concepts."""
    if not taxonomy_index or not (source_concepts or target_concepts):
        return ""

    lines: List[str] = []

    # -- Known directed relations between any (source, target) concept pair --
    relation_labels = {
        "requires": "requires",
        "part_of": "is part of",
        "is_a": "is a kind of",
        "related_to": "is related to",
        "has_part": "has part",
        "has_kind": "has kind",
        "replaces": "replaces",
    }
    found_relations: List[str] = []
    for src in source_concepts:
        entry = taxonomy_index.get(src, {})
        for rel_key, rel_label in relation_labels.items():
            for tgt in target_concepts:
                if tgt in (entry.get(rel_key) or []):
                    found_relations.append(f"{src} {rel_label} {tgt}")
    if found_relations:
        lines.append("Known relations: " + "; ".join(found_relations))

    # -- Shared domain / subdomain --
    def _domains(concepts: List[str], field: str) -> set:
        return {taxonomy_index.get(c, {}).get(field, "") for c in concepts} - {""}

    shared_domains = _domains(source_concepts, "domain") & _domains(target_concepts, "domain")
    if shared_domains:
        lines.append("Shared domain: " + ", ".join(sorted(shared_domains)))

    shared_subdomains = _domains(source_concepts, "subdomain") & _domains(target_concepts, "subdomain")
    if shared_subdomains:
        lines.append("Shared subdomain: " + ", ".join(sorted(shared_subdomains)))

    # -- Platform scope overlap / mismatch --
    def _platforms(concepts: List[str]) -> set:
        plats: set = set()
        for c in concepts:
            facets = taxonomy_index.get(c, {}).get("facets") or {}
            plats.update(facets.get("platforms") or [])
        return plats

    src_plats = _platforms(source_concepts)
    tgt_plats = _platforms(target_concepts)
    if src_plats and tgt_plats:
        overlap = src_plats & tgt_plats
        if overlap:
            lines.append("Platform overlap: " + ", ".join(sorted(overlap)))
        else:
            lines.append(
                f"Platform mismatch: A={sorted(src_plats)} vs B={sorted(tgt_plats)}"
            )

    # -- Audience mismatch --
    def _audiences(concepts: List[str]) -> set:
        auds: set = set()
        for c in concepts:
            facets = taxonomy_index.get(c, {}).get("facets") or {}
            auds.update(facets.get("audiences") or [])
        return auds

    src_auds = _audiences(source_concepts)
    tgt_auds = _audiences(target_concepts)
    if src_auds and tgt_auds and src_auds != tgt_auds:
        lines.append(f"Audience mismatch: A={sorted(src_auds)} vs B={sorted(tgt_auds)}")

    if not lines:
        return ""
    return "## Taxonomy Context\n" + "\n".join(f"- {l}" for l in lines)


def build_classification_prompt(
    base_prompt: str,
    source_doc: str,
    source_section: str,
    source_text: str,
    source_concepts: List[str],
    source_is_api: bool,
    target_doc: str,
    target_section: str,
    target_text: str,
    target_concepts: List[str],
    target_is_api: bool,
    similarity: float,
    taxonomy_context: str = "",
) -> str:
    """Build the full classification prompt for an LLM."""
    
    def _section_type(is_api: bool, doc_path: str) -> str:
        if is_api:
            return "API Reference"
        p = doc_path.lower()
        if "/how-to" in p:
            return "How-to Task"
        if "tutorial" in p or "getting-started" in p or "get-started" in p:
            return "Tutorial"
        return "Conceptual"

    shared_concepts = sorted(set(source_concepts) & set(target_concepts))

    taxonomy_section = f"\n\n{taxonomy_context}" if taxonomy_context else ""

    prompt = f"""{base_prompt}

## Section A (Source)
**Document**: {source_doc}
**Section ID**: {source_section}
**Type**: {_section_type(source_is_api, source_doc)}
**Concepts**: {', '.join(source_concepts) if source_concepts else 'None'}
**Content**:
{source_text}

## Section B (Target)
**Document**: {target_doc}
**Section ID**: {target_section}
**Type**: {_section_type(target_is_api, target_doc)}
**Concepts**: {', '.join(target_concepts) if target_concepts else 'None'}
**Content**:
{target_text}

## Context
- Semantic similarity: {similarity:.3f}
- Shared concepts: {', '.join(shared_concepts) if shared_concepts else 'None'}{taxonomy_section}

Classify the relationship FROM Section A TO Section B. Return ONLY valid JSON with exactly these keys:
{{
  "relationship": "<one of: requires|explains|uses|extends|applies_to|contrasts_with|related_to>",
  "confidence": <number between 0 and 1>,
  "bidirectional": <true|false>
}}
No additional keys. No prose."""

    return prompt


def robust_json_parse(text: str) -> Optional[Dict]:
    """
    Attempt to parse JSON with multiple strategies to handle common LLM output issues.
    
    Strategies:
    1. Direct parse
    2. Extract from markdown code blocks
    3. Fix common escape sequence issues
    4. Remove trailing commas
    5. Try to recover partial JSON
    """
    import re
    
    original_text = text
    
    # Strategy 1: Try direct parse
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    
    # Strategy 2: Extract from markdown code blocks
    if "```json" in text:
        text = text.split("```json")[1].split("```")[0].strip()
    elif "```" in text:
        text = text.split("```")[1].split("```")[0].strip()
    
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    
    # Strategy 3: Fix common escape sequence issues
    # Replace invalid escape sequences with valid ones
    try:
        # Fix common invalid escapes like \: \- \( \) etc
        # Valid JSON escapes are: \" \\ \/ \b \f \n \r \t \uXXXX
        # Replace invalid escapes by escaping the backslash
        fixed_text = text
        # Find all backslash sequences that aren't valid JSON escapes
        invalid_escape_pattern = r'\\(?!["\\/bfnrtu])'
        fixed_text = re.sub(invalid_escape_pattern, r'\\\\', fixed_text)
        
        return json.loads(fixed_text)
    except json.JSONDecodeError:
        pass
    
    # Strategy 4: Remove trailing commas
    try:
        # Remove trailing commas before } or ]
        fixed_text = re.sub(r',(\s*[}\]])', r'\1', text)
        return json.loads(fixed_text)
    except json.JSONDecodeError:
        pass
    
    # Strategy 5: Try to find and extract the JSON object
    try:
        # Look for the outermost { ... } structure
        start = text.find('{')
        if start != -1:
            # Find matching closing brace
            depth = 0
            for i in range(start, len(text)):
                if text[i] == '{':
                    depth += 1
                elif text[i] == '}':
                    depth -= 1
                    if depth == 0:
                        extracted = text[start:i+1]
                        return json.loads(extracted)
    except (json.JSONDecodeError, ValueError):
        pass
    
    # All strategies failed
    print(f"  JSON parsing failed after all strategies")
    print(f"  Original text (first 300 chars): {original_text[:300]}")
    return None


def classify_with_llm(prompt: str, api_config: Dict[str, Any]) -> Optional[Dict]:
    """
    Call LLM API to classify relationship.
    
    Configure this function based on your LLM provider:
    - OpenAI GPT-4
    - Anthropic Claude
    - Azure OpenAI
    - Local LLM (Ollama, etc.)
    """
    
    provider = api_config.get("provider", "mock")
    
    if provider == "mock":
        # Mock response for testing - replace with actual API call
        return {
            "relationship": "related_to",
            "confidence": 0.5,
            "rationale": [],
            "evidence": [],
            "bidirectional": True
        }
    
    elif provider == "ollama":
        # Ollama local model
        import requests
        
        model = api_config.get("model", "llama3.1:8b")
        url = "http://localhost:11434/api/generate"
        
        # Use session from api_config for connection pooling
        session = api_config.get("session")
        if not session:
            session = requests.Session()
            api_config["session"] = session
        
        payload = {
            "model": model,
            "prompt": prompt + "\n\nReturn ONLY valid JSON with no additional text:",
            "stream": False,
            "keep_alive": "60m",  # Keep model loaded for 60 minutes
            "options": {
                "temperature": 0.3,
                "num_predict": 512
            }
        }
        
        try:
            # Reduced timeout from 120s to 60s to fail faster
            response = session.post(url, json=payload, timeout=60)
            response.raise_for_status()
            result = response.json()
            response_text = result.get("response", "")
            
            # Use robust JSON parser
            return robust_json_parse(response_text)
            
        except requests.exceptions.Timeout:
            print(f"  Timeout calling Ollama (60s limit)")
            return None
        except requests.exceptions.RequestException as e:
            print(f"  Error calling Ollama: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"  Error parsing Ollama response: {e}")
            print(f"  Response: {response_text[:200]}")
            return None
    
    elif provider == "openai":
        # OpenAI GPT API
        api_key = api_config.get("api_key") or os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OpenAI API key not found in config or OPENAI_API_KEY env var")
        
        client = OpenAI(api_key=api_key)
        
        try:
            response = client.chat.completions.create(
                model=api_config.get("model", "gpt-4o-mini"),
                messages=[{"role": "user", "content": prompt + "\n\nReturn ONLY valid JSON with no additional text."}],
                response_format={"type": "json_object"},
                temperature=0.3,
                max_tokens=512
            )
            response_text = response.choices[0].message.content
            return robust_json_parse(response_text)
        except Exception as e:
            print(f"  Error calling OpenAI: {e}")
            return None
    
    elif provider == "anthropic":
        api_key = api_config.get("api_key") or os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("Anthropic API key not found in config or ANTHROPIC_API_KEY env var")
        
        client = anthropic.Anthropic(api_key=api_key)
        
        max_retries = 5
        for attempt in range(max_retries):
            try:
                response = client.messages.create(
                    model=api_config.get("model", "claude-3-haiku-20240307"),
                    max_tokens=1024,
                    messages=[{"role": "user", "content": prompt + "\n\nReturn ONLY valid JSON with no additional text."}]
                )
                
                # Extract text from response and use robust JSON parser
                response_text = response.content[0].text
                return robust_json_parse(response_text)
            except anthropic.APIStatusError as e:
                if e.status_code in (429, 529, 503) and attempt < max_retries - 1:
                    wait = 2 ** attempt * 2  # 2, 4, 8, 16, 32 seconds
                    print(f"  Retryable error {e.status_code}, waiting {wait}s (attempt {attempt+1}/{max_retries})")
                    time.sleep(wait)
                    continue
                print(f"  Error calling Anthropic: {e}")
                return None
            except Exception as e:
                print(f"  Error calling Anthropic: {e}")
                return None
    
    else:
        raise ValueError(f"Unknown provider: {provider}")


def classify_pairs(
    pairs_df: pd.DataFrame,
    inventory_df: pd.DataFrame,
    concepts_df: pd.DataFrame,
    base_prompt: str,
    api_config: Dict[str, Any],
    taxonomy_index: Optional[Dict[str, Any]] = None,
    max_chars: int = 2000,
    checkpoint_every: int = 100
) -> pd.DataFrame:
    """Classify relationships for all pairs with checkpointing."""
    
    results = []
    skipped_count = 0
    # Use process-specific checkpoint to avoid conflicts in parallel processing
    process_id = os.getpid()
    checkpoint_path = Path(f"outputs/classified_pairs_checkpoint_pid_{process_id}.parquet")
    
    for idx, row in tqdm(pairs_df.iterrows(), total=len(pairs_df), desc="Classifying"):
        # Get section metadata
        source_concepts = safe_list(row.get("source_concepts", []))
        target_concepts = safe_list(row.get("target_concepts", []))
        
        # Get section text (now with enhanced fallback)
        source_text = get_section_text(
            inventory_df, row["source_doc"], row["source_section"], max_chars
        )
        target_text = get_section_text(
            inventory_df, row["target_doc"], row["target_section"], max_chars
        )
        
        # Skip only if BOTH texts are empty (should be rare now with fallback)
        if not source_text or not target_text:
            skipped_count += 1
            if skipped_count <= 10:  # Only show first 10 warnings
                print(f"\nWarning: Missing text for pair {idx} - skipping (source empty: {not source_text}, target empty: {not target_text})")
            continue
        
        # D2: Build taxonomy context for this pair
        taxonomy_ctx = build_taxonomy_context(
            source_concepts, target_concepts, taxonomy_index or {}
        )

        # Build prompt
        prompt = build_classification_prompt(
            base_prompt,
            row["source_doc"],
            row["source_section"],
            source_text,
            source_concepts,
            row["source_is_api"],
            row["target_doc"],
            row["target_section"],
            target_text,
            target_concepts,
            row["target_is_api"],
            row["sim_score"],
            taxonomy_context=taxonomy_ctx,
        )
        
        # Classify
        try:
            classification = classify_with_llm(prompt, api_config)
            
            if classification:
                result_row = {
                    **row.to_dict(),
                    "relationship_type": classification.get("relationship"),
                    "relationship_confidence": classification.get("confidence"),
                    "relationship_bidirectional": classification.get("bidirectional", False)
                }
                results.append(result_row)
            
            # Rate limiting
            time.sleep(api_config.get("delay", 0.5))
            
        except Exception as e:
            print(f"\nError classifying pair {idx}: {e}")
            continue
        
        # Checkpoint
        if len(results) > 0 and len(results) % checkpoint_every == 0:
            temp_df = pd.DataFrame(results)
            temp_df.to_parquet(checkpoint_path, engine="pyarrow", index=False)
            print(f"\nCheckpoint saved: {len(results)} pairs classified, {skipped_count} skipped")
    
    if skipped_count > 10:
        print(f"\nTotal skipped pairs: {skipped_count}")
    
    return pd.DataFrame(results)


def main():
    parser = argparse.ArgumentParser(description="Classify semantic relationships using LLM")
    parser.add_argument(
        "--threshold",
        type=float,
        default=None,
        help="Only classify pairs with similarity >= threshold (e.g., 0.80)"
    )
    parser.add_argument(
        "--types",
        type=str,
        default=None,
        help="Comma-separated pair types to classify: cc,aa,ca,ac (default: all)"
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Maximum number of pairs to classify (for testing)"
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        help="Skip the large-batch confirmation prompt"
    )
    parser.add_argument(
        "--max-chars",
        type=int,
        default=2000,
        help="Maximum characters of section text to include"
    )
    parser.add_argument(
        "--provider",
        type=str,
        default="mock",
        choices=["mock", "ollama", "openai", "anthropic"],
        help="LLM provider to use"
    )
    parser.add_argument(
        "--api-key",
        type=str,
        default=None,
        help="API key for LLM provider (or set env var)"
    )
    parser.add_argument(
        "--model",
        type=str,
        default=None,
        help="Model name (e.g., gpt-4-turbo-preview, claude-3-5-sonnet-20241022)"
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.5,
        help="Delay between API calls in seconds"
    )
    parser.add_argument(
        "--input",
        type=str,
        default="outputs/semantic_pairs.parquet",
        help="Input semantic pairs file (default or filtered version)"
    )
    parser.add_argument(
        "--resume",
        type=str,
        default=None,
        help="Resume from checkpoint file"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="outputs/classified_pairs.parquet",
        help="Output file path"
    )
    
    args = parser.parse_args()
    
    print("=" * 70)
    print("Phase 6: Relationship Classification")
    print("=" * 70)
    
    # Load base prompt
    base_prompt = load_relationship_prompt()
    print(f"\nLoaded classification prompt ({len(base_prompt)} chars)")
    
    # Load data
    print(f"\nLoading semantic pairs from {args.input}...")
    pairs_df = pd.read_parquet(args.input, engine="pyarrow")
    print(f"  Loaded {len(pairs_df):,} semantic pairs")
    
    # Handle both 'similarity' and 'sim_score' column names
    if "similarity" in pairs_df.columns and "sim_score" not in pairs_df.columns:
        pairs_df["sim_score"] = pairs_df["similarity"]
    elif "sim_score" not in pairs_df.columns:
        print("\nError: No similarity score column found (expected 'similarity' or 'sim_score')")
        return
    
    # Resume from checkpoint(s) - merge all process-specific checkpoints
    # Pattern matches only pid-specific files (e.g. classified_pairs_checkpoint_pid_12345.parquet)
    # Excludes backup files (which contain "backup" in the name)
    checkpoint_pattern = "outputs/classified_pairs_checkpoint_pid_*.parquet"
    checkpoint_files = [f for f in glob.glob(checkpoint_pattern) if "backup" not in Path(f).name]
    
    # Also check for explicit --resume file
    if args.resume and Path(args.resume).exists():
        checkpoint_files.append(args.resume)
        print(f"\nResuming from: {args.resume}")
    
    if checkpoint_files:
        print(f"\nFound {len(checkpoint_files)} checkpoint file(s), merging...")
        classified_dfs = []
        for cp_file in checkpoint_files:
            try:
                df = pd.read_parquet(cp_file, engine="pyarrow")
                classified_dfs.append(df)
                print(f"  Loaded {Path(cp_file).name}: {len(df):,} pairs")
            except Exception as e:
                print(f"  Warning: Could not load {Path(cp_file).name}: {e}")
        
        if classified_dfs:
            classified_df = pd.concat(classified_dfs, ignore_index=True)
            # Remove duplicates (in case of overlapping checkpoints)
            classified_df = classified_df.drop_duplicates(
                subset=["source_doc", "source_section", "target_doc", "target_section"],
                keep="first"
            )
            print(f"  Total unique classified pairs: {len(classified_df):,}")
            
            classified_pairs = set(
                zip(classified_df["source_doc"], classified_df["source_section"],
                    classified_df["target_doc"], classified_df["target_section"])
            )
            
            # Filter out already classified
            pairs_df = pairs_df[
                ~pairs_df.apply(
                    lambda r: (r["source_doc"], r["source_section"],
                              r["target_doc"], r["target_section"]) in classified_pairs,
                    axis=1
                )
            ]
            print(f"  Remaining: {len(pairs_df):,} pairs")
        else:
            classified_df = None
    else:
        classified_df = None
        print("\nNo existing checkpoints found, starting fresh")
    
    # Filter by similarity threshold
    if args.threshold:
        pairs_df = pairs_df[pairs_df["sim_score"] >= args.threshold]
        print(f"\nFiltered to {len(pairs_df):,} pairs with similarity >= {args.threshold}")
    
    # Filter by pair types
    if args.types:
        types = [t.strip() for t in args.types.split(",")]
        pairs_df = pairs_df[pairs_df["neighbor_type"].isin(types)]
        print(f"\nFiltered to {len(pairs_df):,} pairs with types: {', '.join(types)}")
    
    # Limit for testing
    if args.limit:
        pairs_df = pairs_df.head(args.limit)
        print(f"\nLimited to {len(pairs_df):,} pairs for testing")
    
    # Safety warning for large batches
    if len(pairs_df) > 1000 and args.provider != "mock" and not args.yes:
        print(f"\nWARNING: About to classify {len(pairs_df):,} pairs!")
        est_hours = (len(pairs_df) * 3.5) / 3600  # Conservative estimate
        print(f"   Estimated time: ~{est_hours:.1f} hours")
        print(f"   Consider using --limit 100 for testing first")
        response = input("\nContinue? (yes/no): ")
        if response.lower() not in ("yes", "y"):
            print("Aborted.")
            return
    
    if len(pairs_df) == 0:
        print("\nNo pairs to classify!")
        return
    
    # Load supporting data
    print("\nLoading supporting data...")
    inventory_df = pd.read_parquet("outputs/topics_inventory.parquet", engine="pyarrow")
    concepts_df = pd.read_parquet("outputs/doc_concepts.parquet", engine="pyarrow")
    print(f"  Topics inventory: {len(inventory_df):,} documents")
    print(f"  Concepts: {len(concepts_df):,} sections")

    # D1: Load taxonomy index once at startup
    print("\nLoading taxonomy index...")
    taxonomy_index = load_taxonomy_index()
    print(f"  Loaded {len(taxonomy_index):,} concepts into taxonomy index")

    # Configure API
    api_config = {
        "provider": args.provider,
        "api_key": args.api_key or os.getenv(f"{args.provider.upper()}_API_KEY"),
        "model": args.model,
        "delay": args.delay
    }

    # Apply provider-specific model defaults when --model is not specified
    if api_config["model"] is None:
        _model_defaults = {
            "anthropic": "claude-sonnet-4-20250514",
            "openai": "gpt-4o-mini",
            "ollama": "llama3.1:8b",
        }
        api_config["model"] = _model_defaults.get(args.provider)
    
    # Ollama is local and doesn't need an API key
    if args.provider not in ("mock", "ollama") and not api_config["api_key"]:
        print(f"\nError: API key required for provider '{args.provider}'")
        print(f"  Set --api-key or {args.provider.upper()}_API_KEY environment variable")
        return
    
    print(f"\nClassification settings:")
    print(f"  Provider: {args.provider}")
    print(f"  Model: {args.model or 'default'}")
    print(f"  Max text length: {args.max_chars:,} chars")
    print(f"  Rate limit delay: {args.delay}s")
    
    # Classify relationships
    print(f"\nClassifying {len(pairs_df):,} relationships...")
    
    # Estimate time
    if args.provider == "ollama":
        est_time_per_pair = 3 + args.delay  # ~3s per Ollama call + delay
    elif args.provider in ("openai", "anthropic"):
        est_time_per_pair = 1 + args.delay  # ~1s per cloud API call + delay
    else:
        est_time_per_pair = 0.1  # Mock is instant
    
    total_est_minutes = (len(pairs_df) * est_time_per_pair) / 60
    print(f"Estimated time: {total_est_minutes:.1f} minutes ({total_est_minutes/60:.1f} hours)")
    print(f"(Based on {est_time_per_pair:.1f}s per pair)")
    
    start_time = time.time()
    
    classified_new = classify_pairs(
        pairs_df,
        inventory_df,
        concepts_df,
        base_prompt,
        api_config,
        taxonomy_index=taxonomy_index,
        max_chars=args.max_chars
    )
    
    elapsed = time.time() - start_time
    
    # Combine with existing classifications if resuming
    if classified_df is not None and len(classified_df) > 0:
        result_df = pd.concat([classified_df, classified_new], ignore_index=True)
    else:
        result_df = classified_new
    
    # Merge ALL checkpoint files into final output
    print(f"\nMerging all checkpoint files into final output...")
    all_checkpoint_files = glob.glob("outputs/classified_pairs_checkpoint*.parquet")
    if all_checkpoint_files:
        all_dfs = [result_df]  # Start with what we just classified
        for cp_file in all_checkpoint_files:
            try:
                df = pd.read_parquet(cp_file, engine="pyarrow")
                all_dfs.append(df)
            except:
                pass
        
        result_df = pd.concat(all_dfs, ignore_index=True)
        # Remove duplicates
        result_df = result_df.drop_duplicates(
            subset=["source_doc", "source_section", "target_doc", "target_section"],
            keep="first"
        )
        print(f"  Merged to {len(result_df):,} unique classified pairs")
    
    # Save results
    print(f"\nSaving results to {args.output}...")
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    result_df.to_parquet(args.output, engine="pyarrow", index=False)
    
    print("\n" + "=" * 70)
    print("Classification Complete!")
    print("=" * 70)
    print(f"Total classified: {len(result_df):,} pairs")
    print(f"New classifications: {len(classified_new):,} pairs")
    print(f"Time elapsed: {elapsed/60:.1f} minutes")
    
    if len(result_df) > 0:
        print(f"\nRelationship type breakdown:")
        rel_counts = result_df["relationship_type"].value_counts()
        for rel_type, count in rel_counts.items():
            pct = 100 * count / len(result_df)
            print(f"  {rel_type:20} {count:6,} ({pct:5.1f}%)")
        
        print(f"\nAverage confidence: {result_df['relationship_confidence'].mean():.3f}")
        print(f"Bidirectional relationships: {result_df['relationship_bidirectional'].sum():,}")
    
    # Cleanup HTTP session if it exists
    if "session" in api_config:
        api_config["session"].close()
    
    print(f"\nOutput saved to: {args.output}")


if __name__ == "__main__":
    main()
