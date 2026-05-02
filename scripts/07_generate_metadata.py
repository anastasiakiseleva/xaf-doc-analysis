#!/usr/bin/env python3
"""
Phase 7: Generate AI-Friendly Metadata for XAF Documentation

Leverages concept tagging, semantic analysis, and connectivity metrics to generate
metadata fields (tags, descriptions, proficiencyLevel) that make XAF docs more accessible
to AI chatbots and RAG systems.

Output: metadata_suggestions.parquet with proposed tags for each document
"""

import argparse
import re
import sys
import yaml
from pathlib import Path
import pandas as pd
import numpy as np

# Add parent directory to path for validation imports
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils.pipeline_validators import (
    PipelineValidator, ValidationReport, ValidationResult,
    save_validation_report, load_validation_thresholds
)
from utils.taxonomy_loader import load_concepts
from scripts.config_loader import cfg as _cfg


def _load_audience_concept_sets() -> tuple[frozenset, frozenset]:
    """Load expert/beginner concept name sets from XAF taxonomy audience facets.

    Taxonomy audience levels: beginner, intermediate, advanced, architect.
    Mapping: advanced + architect → expert_concepts, beginner → beginner_concepts.
    Falls back to hard-coded sets if taxonomy cannot be loaded.
    """
    try:
        concepts_cfg = load_concepts()
        all_concepts = concepts_cfg.get('concepts', [])
        expert = frozenset(
            c['name'] for c in all_concepts
            if any(a in ('advanced', 'architect') for a in c.get('facets', {}).get('audiences', []))
        )
        beginner = frozenset(
            c['name'] for c in all_concepts
            if 'beginner' in c.get('facets', {}).get('audiences', [])
        )
        return expert, beginner
    except Exception:
        return (
            frozenset({'Performance Optimization', 'Migration', 'Custom', 'Legacy .NET Framework'}),
            frozenset({'Getting Started', 'Tutorial'}),
        )


_EXPERT_CONCEPTS, _BEGINNER_CONCEPTS = _load_audience_concept_sets()


def _build_taxonomy_vocab() -> tuple[dict, frozenset]:
    """Build controlled vocabulary from XAF taxonomy for tag generation.

    Returns:
        term_to_tag: maps any normalized term (concept name, keyword, synonym) to
                     the canonical normalized tag for that concept (normalize_tag(concept.name)).
                     Ensures all emitted tags correspond to actual taxonomy concepts.
        platform_set: set of known platform values from facets.platforms (e.g. 'blazor', 'winforms').
    """
    try:
        concepts_cfg = load_concepts()
        all_concepts = concepts_cfg.get('concepts', [])
    except Exception:
        return {}, frozenset()

    def _norm(text: str) -> str:
        """Inline normalizer (normalize_tag not yet defined at call time)."""
        tag = text.lower().replace('.', '').replace(' ', '-')
        import re as _re
        tag = _re.sub(r'[^a-z0-9-]', '', tag)
        tag = _re.sub(r'-+', '-', tag).strip('-')
        return tag

    term_to_tag: dict = {}
    platform_set: set = set()

    for concept in all_concepts:
        canonical_tag = _norm(concept['name'])
        # Map canonical name itself
        term_to_tag[_norm(concept['name'])] = canonical_tag
        # Map every synonym and keyword → canonical tag
        # load_concepts() flattens terminology.* to top-level fields
        for term in (concept.get('synonyms', []) or []) + (concept.get('keywords', []) or []):
            if term:
                term_to_tag[_norm(term)] = canonical_tag
        # Collect platform values
        for plat in concept.get('facets', {}).get('platforms', []):
            if plat:
                platform_set.add(plat.lower())

    return term_to_tag, frozenset(platform_set)


_TAXONOMY_TERM_TO_TAG, _TAXONOMY_PLATFORMS = _build_taxonomy_vocab()


# ============================================================================
# Helper Functions
# ============================================================================

def safe_list(val):
    """Handle numpy arrays from parquet files"""
    if val is None or (isinstance(val, float) and pd.isna(val)):
        return []
    if isinstance(val, (list, tuple)):
        return list(val)
    if hasattr(val, '__iter__') and not isinstance(val, str):
        return list(val)
    return []


def normalize_tag(text):
    """
    Convert concept/platform/API name to XAF tag format:
    - lowercase
    - no spaces (replace with hyphens)
    - no dots (remove)
    - no PascalCase
    
    Examples:
        "Blazor UI" -> "blazor-ui"
        "ASP.NET Core" -> "asp-net-core"
        "SecurityStrategy" -> "securitystrategy"
        "DevExpress.ExpressApp" -> "devexpressexpressapp"
    """
    tag = text.lower()
    tag = tag.replace('.', '')  # Remove dots
    tag = tag.replace(' ', '-')  # Spaces to hyphens
    tag = re.sub(r'[^a-z0-9-]', '', tag)  # Remove other special chars
    tag = re.sub(r'-+', '-', tag)  # Collapse multiple hyphens
    tag = tag.strip('-')  # Remove leading/trailing hyphens
    return tag


def classify_proficiency(row, connections_dict, relationship_profiles=None):
    """
    Classify proficiency level using concept heuristics and relationship types.
    
    When classified pairs are available, relationship types provide strong signals:
    - Section is a frequent 'explains' SOURCE → Beginner (it teaches)
    - Section is a frequent 'requires' TARGET → Beginner (it's foundational/prerequisite)
    - Section has many 'requires' OUTGOING → Advanced/Expert (depends on many prereqs)
    - Section has 'extends' or 'uses' outgoing → Advanced (builds on other content)
    
    Falls back to the original heuristics when classified pairs are absent.
    """
    concepts = safe_list(row.get('concepts', []))
    is_api = row.get('is_api', False)
    section_key = (row['doc_id'], row['section_id'])
    num_connections = connections_dict.get(section_key, 0)
    
    # --- Relationship-based signals (when available) ---
    profile = (relationship_profiles or {}).get(section_key)
    if profile and profile['classified_connections'] >= 3:
        incoming = profile['incoming']
        outgoing = profile['outgoing']
        
        # Strong Expert signal: many outgoing 'requires' (needs lots of prereqs)
        if outgoing.get('requires', 0) >= 3:
            return 'Expert'
        
        # Strong Beginner signal: frequently explains things to others
        if outgoing.get('explains', 0) >= 3:
            return 'Beginner'
        
        # Strong Beginner signal: many sections require THIS section (foundational)
        if incoming.get('requires', 0) >= 3:
            return 'Beginner'
        
        # Advanced signal: extends or uses other content
        extends_uses = outgoing.get('extends', 0) + outgoing.get('uses', 0)
        if extends_uses >= 3:
            return 'Advanced'
    
    # --- Concept-based heuristics (original logic, still useful) ---

    # Expert signals (taxonomy audience: advanced, architect)
    if any(c in _EXPERT_CONCEPTS for c in concepts):
        return 'Expert'

    # Beginner signals (taxonomy audience: beginner)
    if any(c in _BEGINNER_CONCEPTS for c in concepts):
        return 'Beginner'
    
    # High connectivity + conceptual = tutorial content (Beginner)
    if not is_api and num_connections > 10:
        return 'Beginner'
    
    # Low connectivity = specialized (Advanced or Expert)
    if num_connections < 5:
        return 'Advanced' if not is_api else 'Expert'
    
    # API reference = Advanced
    if is_api:
        return 'Advanced'
    
    # Default
    return 'Beginner'


def parse_yaml_frontmatter(text):
    """
    Parse YAML frontmatter from markdown text
    
    Returns:
        tuple: (frontmatter_dict, remaining_content)
    """
    if not text or not text.startswith('---'):
        return {}, text
    
    # Find the closing ---
    parts = text.split('---', 2)
    if len(parts) < 3:
        return {}, text
    
    try:
        # Parse the YAML between the --- markers
        frontmatter = yaml.safe_load(parts[1])
        content = parts[2].strip()
        return frontmatter or {}, content
    except yaml.YAMLError:
        return {}, text


def extract_api_summary(raw_text):
    """
    Extract summary and remarks from API documentation
    
    For API docs, prioritize:
    1. YAML frontmatter 'summary' field (with or without --- delimiters)
    2. Content after frontmatter (remarks, examples)
    3. First substantial paragraph
    
    Returns a clean, informative description string
    """
    # Try to extract summary using regex (handles both delimited and non-delimited YAML)
    # Pattern matches: summary: followed by the text until the next field or newline
    # Also handles inline format where fields are concatenated without newlines
    summary_match = re.search(r'summary:\s*(.+?)(?=\n(?:syntax:|seealso:|remarks:|$))', raw_text, re.DOTALL | re.IGNORECASE)
    
    # Fallback: try inline format (no newline before next field)
    if not summary_match:
        summary_match = re.search(r'summary:\s*(.+?)(?=syntax:|seealso:|remarks:|$)', raw_text, re.DOTALL | re.IGNORECASE)
    
    if summary_match:
        summary = summary_match.group(1).strip()
        # Clean the summary
        summary = re.sub(r'\[\]\(xref:[^\)]+\)', '', summary)  # Remove xref links
        summary = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', summary)  # Keep link text, remove URL
        summary = re.sub(r'\*\*([^\*]+)\*\*', r'\1', summary)  # Remove bold
        summary = re.sub(r'`([^`]+)`', r'\1', summary)  # Remove code formatting
        summary = re.sub(r'\s+', ' ', summary).strip()
        
        if len(summary) > 20:  # If summary is substantial
            return summary
    
    # If no summary found or it's too short, try to get content after syntax/seealso section
    # Look for remarks or paragraphs after the YAML-like structure
    content_match = re.search(r'seealso:\s*\[\](.+)', raw_text, re.DOTALL)
    if content_match:
        content = content_match.group(1).strip()
        # Clean and extract first substantial sentence
        clean_content = clean_markdown_text(content)
        if len(clean_content) > 40:
            # Get first sentence or two
            sentences = re.split(r'[.!?]\s+', clean_content)
            for sentence in sentences:
                sent = sentence.strip()
                if 40 <= len(sent) <= 160:
                    if not sent.endswith(('.', '!', '?')):
                        sent += '.'
                    return sent
            # If no perfect sentence, take first 150 chars
            if len(clean_content) >= 40:
                truncated = clean_content[:150].rsplit(' ', 1)[0]
                return truncated + '...'
    
    return None


def extract_frontmatter_description(text):
    """
    Extract a usable description or title from inline YAML frontmatter.
    
    Handles text like:
      uid: "403179"title: 'Application Shell...'description: 'Learn about...'
    
    Returns the description value if found, else the title, else None.
    """
    if not text:
        return None
    
    # Try to extract description: value (quoted or unquoted)
    desc_match = re.search(
        r"""description:\s*['"](.+?)['"](?=\s*(?:tags:|proficiencyLevel:|seealso:|linkId:|linkType:|$))""",
        text, re.IGNORECASE
    )
    if desc_match:
        val = desc_match.group(1).strip()
        if len(val) >= 30 and not val.startswith(('uid:', 'linkId:')):
            return val
    
    # Fallback: extract title: value
    title_match = re.search(
        r"""title:\s*['"]?(.+?)['"]?(?=\s*(?:description:|seealso:|linkId:|linkType:|tags:|proficiencyLevel:|$))""",
        text, re.IGNORECASE
    )
    if title_match:
        val = title_match.group(1).strip().strip("'\"")
        if len(val) >= 5 and not val.startswith(('uid:', 'linkId:')):
            return val
    
    return None


def clean_markdown_text(text):
    """
    Remove markdown artifacts and extract clean content
    """
    if not text:
        return ""
    
    # Remove inline YAML frontmatter fields (may be concatenated on one line)
    # Order matters: remove uid/seealso/linkId/linkType/altText/tags/proficiencyLevel first,
    # then title/description since those may contain useful content handled elsewhere.
    text = re.sub(r'uid:\s*["\']?[^"\'\n]*?["\']?(?=\s*(?:title:|description:|seealso:|linkId:|linkType:|tags:|proficiencyLevel:|$))', '', text, flags=re.IGNORECASE)
    text = re.sub(r'seealso:\s*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'linkId:\s*["\']?[^\s"\']*["\']?\s*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'linkType:\s*\S+\s*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'altText:\s*["\']?[^"\'\n]*?["\']?(?=\s*(?:linkId:|linkType:|title:|$))', '', text, flags=re.IGNORECASE)
    text = re.sub(r'proficiencyLevel:\s*\S+', '', text, flags=re.IGNORECASE)
    text = re.sub(r'tags:\s*\n(?:\s*\S+\s*\n?)*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'title:\s*["\']?[^"\'\n]*?["\']?(?=\s*(?:description:|seealso:|tags:|proficiencyLevel:|$))', '', text, flags=re.IGNORECASE)
    text = re.sub(r'description:\s*["\']?[^"\'\n]*?["\']?(?=\s*(?:tags:|proficiencyLevel:|seealso:|$))', '', text, flags=re.IGNORECASE)
    
    # Remove API-doc inline metadata fields (id:, type:, return:type: patterns)
    text = re.sub(r'\bid:\s*\w+(?:type:|$)', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\btype:\s*[\w.`<>]+', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\breturn:\s*', '', text, flags=re.IGNORECASE)
    
    # Also remove line-based metadata (original patterns)
    text = re.sub(r'^uid:\s*["\']?[^"\'\n]*["\']?\s*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'^title:\s*["\']?[^"\'\n]*["\']?\s*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'^description:\s*["\']?[^"\'\n]*["\']?\s*$', '', text, flags=re.MULTILINE)
    
    # Remove markdown tips/notes/warnings
    text = re.sub(r'\[!(TIP|NOTE|IMPORTANT|WARNING|CAUTION)\]', '', text, flags=re.IGNORECASE)
    
    # Remove code blocks
    text = re.sub(r'```[\s\S]*?```', '', text)
    text = re.sub(r'`[^`]+`', '', text)
    
    # Remove xref links but keep the text
    text = re.sub(r'<xref[^>]*>', '', text)

    # Remove empty-text markdown links (e.g. [](xref:...) or [](https://...)) before
    # processing regular links — otherwise they leave dangling articles ("The is a...")
    text = re.sub(r'\[\]\([^\)]+\)', '', text)

    # Remove markdown links but keep link text
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    
    # Remove HTML comments
    text = re.sub(r'<!--[\s\S]*?-->', '', text)
    
    # Clean up multiple spaces/newlines
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text


def generate_description(row, inventory_df):
    """
    Generate a concise description (120-160 chars) from section content
    
    Strategy:
    1. For API: Extract from documentation or generate context-aware description
    2. For conceptual: Use first meaningful clean sentence
    3. Use headings as hints
    """
    doc_id = row['doc_id']
    section_id = row['section_id']
    is_api = row.get('is_api', False)
    concepts = safe_list(row.get('concepts', []))
    
    # Get section text from inventory
    doc_row = inventory_df[inventory_df['doc_id'] == doc_id]
    if doc_row.empty:
        return None
    
    sections = safe_list(doc_row.iloc[0].get('sections', []))
    section = next((s for s in sections if s.get('section_id') == section_id), None)
    
    if not section:
        return None
    
    raw_text = section.get('text', '').strip()
    heading = section.get('heading', '').strip()
    
    # For non-API content, try to extract description/title from inline frontmatter first
    if not is_api:
        fm_desc = extract_frontmatter_description(raw_text)
        if fm_desc:
            # We got a description from the frontmatter - clean and use it
            fm_desc = re.sub(r'\s+', ' ', fm_desc).strip()
            if len(fm_desc) > 160:
                truncated = fm_desc[:150].rsplit(' ', 1)[0]
                fm_desc = truncated + '...'
            if not fm_desc.endswith(('.', '!', '?', '...')):
                fm_desc += '.'
            return fm_desc
    
    # For API reference - parse structured documentation
    if is_api:
        # Use specialized API summary extraction
        api_description = extract_api_summary(raw_text)
        
        if api_description:
            # Ensure description is in good length range
            if len(api_description) > 160:
                # Truncate at sentence boundary if possible
                sentences = re.split(r'[.!?]\s+', api_description)
                if sentences and len(sentences[0]) >= 40:
                    return sentences[0] + '.'
                # Otherwise truncate at word boundary
                truncated = api_description[:150].rsplit(' ', 1)[0]
                return truncated + '...'
            
            # Add period if missing
            if not api_description.endswith(('.', '!', '?', '...')):
                api_description += '.'
            
            return api_description
        
        # Fallback: Generate context-aware template
        apis = safe_list(row.get('apis', []))
        if apis:
            api_name = apis[0].split('.')[-1]
            
            if concepts:
                primary_concept = concepts[0]
                return f"API reference for {api_name} used in {primary_concept}. See documentation for details."
            
            return f"API reference for {api_name}. See documentation for properties, methods, and usage examples."
    
    # For conceptual content - extract first clean sentence
    text = clean_markdown_text(raw_text)
    if text:
        # Split into sentences
        sentences = re.split(r'[.!?]\s+', text)
        
        for sentence in sentences:
            clean_sent = sentence.strip()
            # Look for sentence in good length range
            if 50 <= len(clean_sent) <= 160:
                # Ensure it ends with punctuation
                if not clean_sent.endswith(('.', '!', '?')):
                    clean_sent += '.'
                return clean_sent
        
        # If no perfect sentence, take first substantial text
        if len(text) >= 50:
            # Truncate at word boundary
            if len(text) > 150:
                truncated = text[:150].rsplit(' ', 1)[0]
                return truncated + '...'
            else:
                if not text.endswith(('.', '!', '?')):
                    text += '.'
                return text
    
    # Fallback: use heading with concepts if available
    if heading and concepts and len(heading) > 5:
        primary_concept = concepts[0] if concepts else _cfg.product_name()
        return f"Learn about {heading.lower()} in {primary_concept}."
    
    return None


def consolidate_tags(row):
    """
    Build tag list constrained to the XAF taxonomy controlled vocabulary.

    Only emits tags that correspond to an actual taxonomy concept (via its name,
    keyword, or synonym), ensuring documentation tags share vocabulary with the
    support-ticket taxonomy.  Non-taxonomy terms are silently dropped.

    XAF tag categories:
    - Concept: normalized taxonomy concept name (e.g. 'security-system', 'actions')
    - Platform: 'blazor' or 'winforms' (from taxonomy facets.platforms)
    - Type: 'api-reference' or 'how-to' (structural, not domain vocabulary)
    """
    tags = set()

    # Concepts and API names → look up against taxonomy controlled vocabulary
    for concept in safe_list(row.get('concepts', [])):
        tag = _TAXONOMY_TERM_TO_TAG.get(normalize_tag(concept))
        if tag:
            tags.add(tag)

    for api in safe_list(row.get('apis', [])):
        # Try full name first, then short name (last namespace segment)
        for term in (api, api.split('.')[-1]):
            tag = _TAXONOMY_TERM_TO_TAG.get(normalize_tag(term))
            if tag:
                tags.add(tag)
                break

    # Platforms → only those present in taxonomy facets
    for platform in safe_list(row.get('platforms', [])):
        norm = platform.lower().strip()
        if norm in _TAXONOMY_PLATFORMS:
            tags.add(norm)

    # Structural type tag (not domain vocabulary — always included)
    tags.add('api-reference' if row.get('is_api', False) else 'how-to')

    return sorted(tags)


def calculate_tag_statistics(metadata_df):
    """Calculate statistics about generated tags"""
    all_tags = []
    for tag_list in metadata_df['suggested_tags']:
        all_tags.extend(safe_list(tag_list))
    
    tag_counts = pd.Series(all_tags).value_counts()
    
    print("\n" + "="*80)
    print("TAG STATISTICS")
    print("="*80)
    print(f"Total documents: {len(metadata_df)}")
    print(f"Unique tags: {len(tag_counts)}")
    print(f"Avg tags per doc: {len(all_tags) / len(metadata_df):.1f}")
    print(f"\nTop 20 most common tags:")
    print(tag_counts.head(20).to_string())
    
    # Proficiency distribution
    print(f"\n{'='*80}")
    print("PROFICIENCY LEVEL DISTRIBUTION")
    print("="*80)
    print(metadata_df['proficiency_level'].value_counts().to_string())


# ============================================================================
# Main Processing
# ============================================================================

def load_data():
    """Load all required data files, including classified pairs when available"""
    print("Loading data files...")
    
    inventory = pd.read_parquet('outputs/topics_inventory.parquet')
    concepts = pd.read_parquet('outputs/doc_concepts.parquet')
    pairs = pd.read_parquet('outputs/semantic_pairs.parquet')
    
    # Filter to kept sections only
    concepts = concepts[concepts['kept'] == True].copy()
    
    print(f"  Loaded {len(inventory)} documents")
    print(f"  Loaded {len(concepts)} sections (kept only)")
    print(f"  Loaded {len(pairs)} semantic pairs")
    
    # Load classified pairs
    classified = None
    cp_path = 'outputs/classified_pairs.parquet'
    if Path(cp_path).exists():
        classified = pd.read_parquet(cp_path)
        print(f"  Loaded {len(classified)} classified pairs from {cp_path}")
    
    if classified is None:
        print("  No classified pairs found — proficiency will use heuristics only")
    
    return inventory, concepts, pairs, classified


def build_connections_dict(pairs_df):
    """Build dictionary of connection counts per section"""
    connections = {}
    
    for _, row in pairs_df.iterrows():
        src = (row['source_doc'], row['source_section'])
        tgt = (row['target_doc'], row['target_section'])
        
        connections[src] = connections.get(src, 0) + 1
        connections[tgt] = connections.get(tgt, 0) + 1
    
    return connections


def build_related_sections_index(classified_df, max_per_section: int = 5) -> dict:
    """
    Build a per-section index of top-N classified neighbours.

    For each section, collects all outgoing and incoming classified edges,
    sorts by confidence descending, and keeps the top `max_per_section` entries.

    Each entry is a dict:
        {
            'doc_id': str,           # neighbour's doc_id
            'section_id': str,        # neighbour's section_id
            'relationship': str,      # e.g. 'uses', 'requires', 'explains'
            'direction': str,         # 'outgoing' or 'incoming'
            'confidence': float,
        }

    Outgoing = this section IS the source (it points to neighbour).
    Incoming = this section IS the target (neighbour points to it).

    The distinction matters for AI: "this page USES [API]" vs
    "this page IS USED BY [how-to guide]".
    """
    if classified_df is None or classified_df.empty:
        return {}

    from collections import defaultdict

    index: dict[tuple, list] = defaultdict(list)

    for _, row in classified_df.iterrows():
        rel = row.get('relationship_type')
        conf = float(row.get('relationship_confidence', 0.5))
        if not rel or pd.isna(rel):
            continue

        src_key = (row['source_doc'], row['source_section'])
        tgt_key = (row['target_doc'], row['target_section'])

        index[src_key].append({
            'doc_id': row['target_doc'],
            'section_id': row['target_section'],
            'relationship': rel,
            'direction': 'outgoing',
            'confidence': round(conf, 3),
        })
        index[tgt_key].append({
            'doc_id': row['source_doc'],
            'section_id': row['source_section'],
            'relationship': rel,
            'direction': 'incoming',
            'confidence': round(conf, 3),
        })

    # Sort each section's neighbours by confidence desc, keep top N
    result = {}
    for key, neighbours in index.items():
        neighbours.sort(key=lambda x: x['confidence'], reverse=True)
        result[key] = neighbours[:max_per_section]

    return result


def build_relationship_profiles(classified_df):
    """
    Build per-section relationship profiles from classified pairs.
    
    For each section, counts how many times it appears as source or target
    for each relationship type, and tracks the dominant incoming/outgoing types.
    This lets classify_proficiency use relationship semantics rather than
    raw connection counts alone.
    
    Returns:
        dict mapping (doc_id, section_id) -> {
            'incoming': Counter of relationship types where this section is target,
            'outgoing': Counter of relationship types where this section is source,
            'avg_confidence': mean confidence across all classified edges,
            'classified_connections': total classified edges touching this section,
        }
    """
    if classified_df is None or classified_df.empty:
        return {}
    
    from collections import Counter
    
    profiles = {}
    
    for _, row in classified_df.iterrows():
        rel_type = row.get('relationship_type')
        confidence = row.get('relationship_confidence', 0.5)
        if not rel_type or pd.isna(rel_type):
            continue
        
        src = (row['source_doc'], row['source_section'])
        tgt = (row['target_doc'], row['target_section'])
        
        # Initialize profiles
        for key in (src, tgt):
            if key not in profiles:
                profiles[key] = {
                    'incoming': Counter(),
                    'outgoing': Counter(),
                    'confidences': [],
                    'classified_connections': 0,
                }
        
        # Source has outgoing edge, target has incoming edge
        profiles[src]['outgoing'][rel_type] += 1
        profiles[src]['confidences'].append(confidence)
        profiles[src]['classified_connections'] += 1
        
        profiles[tgt]['incoming'][rel_type] += 1
        profiles[tgt]['confidences'].append(confidence)
        profiles[tgt]['classified_connections'] += 1
    
    # Compute avg confidence and convert counters to plain dicts for storage
    for key, prof in profiles.items():
        confs = prof.pop('confidences')
        prof['avg_confidence'] = sum(confs) / len(confs) if confs else 0.0
        prof['incoming'] = dict(prof['incoming'])
        prof['outgoing'] = dict(prof['outgoing'])
    
    return profiles


def generate_metadata(concepts_df, inventory_df, connections_dict,
                      relationship_profiles=None, related_sections_index=None,
                      sample_size=None):
    """
    Generate metadata for all documents
    
    Args:
        concepts_df: Sections with concept/platform/API tags
        inventory_df: Full document text
        connections_dict: Connection counts per section
        relationship_profiles: Per-section relationship type profiles (from classified pairs)
        related_sections_index: Per-section top-N classified neighbours (from classified pairs)
        sample_size: If provided, process only this many random documents (for testing)
    """
    print("\nGenerating metadata...")
    
    # Sample if requested
    if sample_size:
        print(f"  Processing random sample of {sample_size} sections...")
        concepts_df = concepts_df.sample(n=min(sample_size, len(concepts_df)), random_state=42)
    
    metadata_rows = []
    
    for idx, row in concepts_df.iterrows():
        if idx % 1000 == 0 and idx > 0:
            print(f"  Processed {idx}/{len(concepts_df)} sections...")
        
        # Generate all metadata fields
        tags = consolidate_tags(row)
        description = generate_description(row, inventory_df)
        proficiency = classify_proficiency(row, connections_dict, relationship_profiles)
        
        # Calculate connectivity score
        section_key = (row['doc_id'], row['section_id'])
        num_connections = connections_dict.get(section_key, 0)
        
        # Extract dominant relationship type from profile (if available)
        profile = (relationship_profiles or {}).get(section_key)
        dominant_rel = None
        classified_connections = 0
        if profile:
            classified_connections = profile['classified_connections']
            # Combine incoming + outgoing to find the dominant type
            all_rels = {}
            for rel, count in profile['incoming'].items():
                all_rels[rel] = all_rels.get(rel, 0) + count
            for rel, count in profile['outgoing'].items():
                all_rels[rel] = all_rels.get(rel, 0) + count
            if all_rels:
                dominant_rel = max(all_rels, key=all_rels.get)
        
        metadata_rows.append({
            'doc_id': row['doc_id'],
            'section_id': row['section_id'],
            'suggested_tags': tags,
            'suggested_description': description,
            'proficiency_level': proficiency,
            'num_semantic_connections': num_connections,
            'num_classified_connections': classified_connections,
            'dominant_relationship_type': dominant_rel,
            'related_sections': (related_sections_index or {}).get(section_key, []),
            'is_api': row.get('is_api', False),
            'original_concepts': safe_list(row.get('concepts', [])),
            'original_platforms': safe_list(row.get('platforms', [])),
            'original_apis': safe_list(row.get('apis', []))
        })
    
    result_df = pd.DataFrame(metadata_rows)
    
    # Post-processing: nullify descriptions that still contain metadata artifacts
    _artifact_prefixes = ('uid:', 'linkId:', 'id:', 'seealso:', 'name:')
    artifact_mask = result_df['suggested_description'].apply(
        lambda d: isinstance(d, str) and d.strip().startswith(_artifact_prefixes)
    )
    if artifact_mask.any():
        count = artifact_mask.sum()
        print(f"  Post-processing: removed {count} descriptions with leaked metadata artifacts")
        result_df.loc[artifact_mask, 'suggested_description'] = None
    
    # Post-processing: nullify boilerplate/templated descriptions (used 3+ times)
    desc_col = 'suggested_description'
    valid_mask = result_df[desc_col].notna() & (result_df[desc_col] != 'nan')
    desc_counts = result_df.loc[valid_mask, desc_col].value_counts()
    boilerplate_descs = set(desc_counts[desc_counts >= 3].index)
    if boilerplate_descs:
        boilerplate_mask = result_df[desc_col].isin(boilerplate_descs)
        count = boilerplate_mask.sum()
        print(f"  Post-processing: removed {count} boilerplate descriptions (used 3+ times, {len(boilerplate_descs)} unique)")
        result_df.loc[boilerplate_mask, desc_col] = None
    
    return result_df


def validate_phase7_output(df: pd.DataFrame, run_quality_checks: bool = False) -> ValidationReport:
    """
    Validate Phase 7 output data.
    
    Args:
        df: The metadata_suggestions DataFrame
        run_quality_checks: Whether to run deeper quality validation
    
    Returns:
        ValidationReport with validation results
    """
    config_path = Path(__file__).resolve().parents[1] / "config" / "validation_thresholds.yml"
    validator = PipelineValidator(config_path)
    report = ValidationReport(phase_name="Generate Metadata", phase_number=7)
    
    # Level 1: Quick Sanity Checks
    print("\n🔍 Running Level 1 validation (quick sanity checks)...")
    
    # Check schema
    required_cols = ["doc_id", "section_id", "suggested_tags", "suggested_description", 
                     "proficiency_level", "num_semantic_connections", "related_sections"]
    column_types = {
        "doc_id": str,
        "section_id": str,
        "suggested_tags": list,
        "suggested_description": str,
        "proficiency_level": str
    }
    report.add_result(validator.validate_schema(df, required_cols, column_types, "Schema validation"))
    
    # Check row count
    report.add_result(validator.validate_row_count(df, min_rows=10000, check_name="Minimum sections"))
    
    # Check description coverage
    non_empty_desc = df['suggested_description'].apply(lambda x: isinstance(x, str) and len(x.strip()) > 0).sum()
    desc_coverage_pct = (non_empty_desc / len(df) * 100) if len(df) > 0 else 0
    
    report.add_result(validator.validate_threshold(
        actual_value=desc_coverage_pct,
        threshold_key='min_docs_with_description',
        phase_key='phase7_metadata',
        comparison='>=',
        check_name="Description coverage"
    ))
    
    # Check average tags per document
    avg_tags = df['suggested_tags'].apply(len).mean()
    report.add_result(validator.validate_threshold(
        actual_value=avg_tags,
        threshold_key='min_avg_tags_per_doc',
        phase_key='phase7_metadata',
        comparison='>=',
        check_name="Minimum avg tags"
    ))
    
    report.add_result(validator.validate_threshold(
        actual_value=avg_tags,
        threshold_key='max_avg_tags_per_doc',
        phase_key='phase7_metadata',
        comparison='<=',
        check_name="Maximum avg tags"
    ))
    
    # Check proficiency distribution
    valid_proficiency = {'Beginner', 'Intermediate', 'Advanced', 'Expert'}
    report.add_result(validator.validate_vocabulary(
        df,
        'proficiency_level',
        valid_proficiency,
        check_name="Proficiency level vocabulary"
    ))
    
    if run_quality_checks:
        print("\n🔍 Running Level 2 validation (quality checks)...")
        
        # Check tag normalization
        invalid_tags = []
        for tags in df['suggested_tags'].head(100):  # Sample for performance
            for tag in safe_list(tags):
                if not isinstance(tag, str):
                    invalid_tags.append(f"Non-string: {type(tag)}")
                elif ' ' in tag or tag != tag.lower():
                    invalid_tags.append(tag)
        
        if invalid_tags:
            report.add_result(ValidationResult(
                check_name="Tag normalization",
                passed=False,
                message=f"Found {len(invalid_tags)} improperly normalized tags (sample)",
                severity="warning",
                details={"sample_invalid": invalid_tags[:5]}
            ))
        else:
            report.add_result(ValidationResult(
                check_name="Tag normalization",
                passed=True,
                message="All sampled tags are properly normalized (lowercase, no spaces)",
                severity="info"
            ))
        
        # Check description length
        desc_lengths = df['suggested_description'].apply(len)
        avg_desc_len = desc_lengths.mean()
        min_desc_len = desc_lengths.min()
        max_desc_len = desc_lengths.max()
        
        report.add_result(ValidationResult(
            check_name="Description length",
            passed=True,
            message=f"Description lengths: min={min_desc_len}, avg={avg_desc_len:.0f}, max={max_desc_len}",
            severity="info",
            details={"min": int(min_desc_len), "avg": int(avg_desc_len), "max": int(max_desc_len)}
        ))
        
        # Check proficiency distribution
        prof_dist = df['proficiency_level'].value_counts(normalize=True) * 100
        prof_dict = prof_dist.to_dict()
        
        report.add_result(ValidationResult(
            check_name="Proficiency distribution",
            passed=True,
            message=f"Proficiency levels: " + ", ".join([f"{k}: {v:.1f}%" for k, v in prof_dict.items()]),
            severity="info",
            details=prof_dict
        ))
    
    return report


def main():
    parser = argparse.ArgumentParser(
        description=f'Generate AI-friendly metadata for {_cfg.product_name()} documentation'
    )
    parser.add_argument(
        '--sample',
        type=int,
        help='Process only N random sections (for testing)'
    )
    parser.add_argument(
        '--output',
        default='outputs/metadata_suggestions.parquet',
        help='Output file path'
    )
    parser.add_argument(
        '--export-csv',
        action='store_true',
        help='Also export as CSV for manual review'
    )
    parser.add_argument('--skip-validation', action='store_true', help='Skip validation checks')
    parser.add_argument('--validate-quality', action='store_true', help='Run deeper quality validation (Level 2)')
    parser.add_argument('--save-report', action='store_true', help='Save validation report to JSON')
    
    args = parser.parse_args()
    
    print("="*70)
    print("Phase 7: Generate Metadata")
    print("="*70)
    
    # Load data
    inventory_df, concepts_df, pairs_df, classified_df = load_data()
    
    # Build connections dictionary
    print("\nBuilding connectivity index...")
    connections_dict = build_connections_dict(pairs_df)
    print(f"  Indexed {len(connections_dict)} sections with semantic connections")
    
    # Build relationship profiles from classified pairs
    relationship_profiles = build_relationship_profiles(classified_df)
    if relationship_profiles:
        print(f"  Built relationship profiles for {len(relationship_profiles)} sections")
    
    # Build related sections index (top-N neighbours per section with relationship type)
    related_sections_index = build_related_sections_index(classified_df)
    if related_sections_index:
        covered = sum(1 for v in related_sections_index.values() if v)
        print(f"  Built related-sections index for {covered:,} sections")

    # Generate metadata
    metadata_df = generate_metadata(
        concepts_df,
        inventory_df,
        connections_dict,
        relationship_profiles=relationship_profiles,
        related_sections_index=related_sections_index,
    )
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    metadata_df.to_parquet(args.output, index=False)
    
    if args.export_csv:
        csv_path = args.output.replace('.parquet', '.csv')
        print(f"Exporting to {csv_path}...")
        metadata_df.to_csv(csv_path, index=False)
    
    # Show statistics
    calculate_tag_statistics(metadata_df)
    
    # Show examples
    print(f"\n{'='*80}")
    print("SAMPLE METADATA (First 5 Documents)")
    print("="*80)
    for idx, row in metadata_df.head(5).iterrows():
        print(f"\nDocument: {row['doc_id']}")
        print(f"  Tags: {', '.join(row['suggested_tags'][:8])}")
        print(f"  Description: {row['suggested_description']}")
        print(f"  Proficiency: {row['proficiency_level']}")
        print(f"  Connections: {row['num_semantic_connections']}")
        rels = row.get('related_sections', [])
        if rels:
            print(f"  Related sections ({len(rels)}):")
            for r in rels[:3]:
                arrow = '-->' if r['direction'] == 'outgoing' else '<--'
                print(f"    {arrow} [{r['relationship']}] {r['doc_id']} (conf={r['confidence']:.2f})")
    # Run validation
    if not args.skip_validation:
        report = validate_phase7_output(metadata_df, run_quality_checks=args.validate_quality)
        report.print_summary()
        
        if args.save_report:
            report_path = Path(args.output).parent / 'validation_phase7.json'
            save_validation_report(report, report_path)
        
        if report.has_errors:
            print("\n❌ Phase 7 validation failed with errors. Review issues above.")
            sys.exit(1)
    else:
        print("\n⏭️  Validation skipped")
    
    print(f"\n✅ Phase 7 complete! Generated metadata for {len(metadata_df):,} sections")
    print(f"   Output: {args.output}")


if __name__ == '__main__':
    main()
