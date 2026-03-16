#!/usr/bin/env python3
"""
coverage_matrix_xaf.py
======================
XAF-specific adaptation of coverage_matrix.py that works with:
  - Section-level concept extraction (doc_concepts.parquet)
  - Document metadata (topics_inventory.parquet)
  - Aggregated ticket counts (xaf_support_tickets_by_feature.json)
  - Support-to-concept mapping (to be created)

Key differences from original:
  1. Aggregates section-level concepts to document level
  2. Works with aggregated ticket counts instead of individual tickets
  3. Calculates code sample presence from section data
  4. Maps feature names directly to concepts (no component hierarchy needed)
"""

import sys
from pathlib import Path
from collections import defaultdict
from datetime import datetime
import json
import pandas as pd
import yaml

# Scoring constants (same as original)
DOC_BASE = 1.0
DOC_WORD_BONUS = 0.5
DOC_CODE_BONUS = 0.5
DOC_PARTIAL_MULT = 0.4

GAP_NONE = "none"
GAP_PARTIAL = "partial"
GAP_MISSING = "missing_concept"

# Paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = PROJECT_ROOT / "config"
OUTPUT_DIR = PROJECT_ROOT / "outputs"

CONCEPTS_YML = CONFIG_DIR / "concepts.yml"
SUPPORT_MAP_YML = PROJECT_ROOT / "support_concept_map.yml"  # Use the full nested map
TICKET_JSON = PROJECT_ROOT / "xaf_support_tickets_by_feature.json"
DOC_CONCEPTS = OUTPUT_DIR / "doc_concepts.parquet"
TOPICS_INVENTORY = OUTPUT_DIR / "topics_inventory.parquet"


def load_yaml(path: Path) -> dict:
    """Load YAML file."""
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def load_concepts(path: Path) -> dict[str, dict]:
    """Load concepts.yml and return {concept_name: concept_dict}."""
    raw = load_yaml(path)
    return {
        c["name"].strip(): c
        for c in raw.get("concepts", [])
        if c.get("name", "").strip()
    }


def aggregate_doc_index(
    topics_df: pd.DataFrame,
    concepts_df: pd.DataFrame
) -> list[dict]:
    """
    Aggregate section-level concepts to document level.
    
    Returns list of dicts with:
      doc_id, url, title, concept_ids (list), word_count, has_code_sample
    """
    # Group concepts by document
    doc_concepts = concepts_df.groupby('doc_id').agg({
        'concepts': lambda x: list(set([c for sublist in x for c in sublist if c])),
        'section_id': 'count'
    }).reset_index()
    
    # Check if any section has code (you may need to add this to doc_concepts.parquet)
    # For now, we'll estimate based on API sections
    doc_has_code = concepts_df[concepts_df['is_api'] == True].groupby('doc_id').size()
    
    # Merge with topics inventory
    merged = topics_df.merge(doc_concepts, on='doc_id', how='left')
    
    docs = []
    for _, row in merged.iterrows():
        doc_id = row['doc_id']
        concepts = row.get('concepts', [])
        if isinstance(concepts, float):  # NaN
            concepts = []
        
        docs.append({
            'doc_id': doc_id,
            'url': row.get('uid', doc_id),  # Use UID as URL proxy
            'title': row.get('title', ''),
            'concept_ids': concepts,
            'word_count': row.get('word_count', 0),
            'has_code_sample': doc_id in doc_has_code
        })
    
    return docs


def load_support_map(path: Path) -> dict[str, dict]:
    """
    Load nested support map and flatten to {feature_name: entry_dict}.
    
    Handles the nested structure:
    mappings:
      - support_component: "Security Module"
        features:
          - name: "OAuth Identity Providers"
            concept_ids: [Authentication]
            gap_type: covered
    
    Returns {feature_name: {concept_ids, gap_type, component}}
    """
    raw = load_yaml(path)
    feature_map = {}
    
    # Normalize gap types
    gap_normalize = {
        'covered': GAP_NONE,
        'none': GAP_NONE,
        'partial': GAP_PARTIAL,
        'missing_docs': GAP_PARTIAL,
        'missing_concept': GAP_MISSING,
        'meta': 'meta',
        'out_of_scope': 'out_of_scope'
    }
    
    for component in raw.get('mappings', []):
        comp_name = component.get('support_component', '')
        comp_status = component.get('coverage_status', '')
        
        # Skip meta and out_of_scope components
        if comp_status in ('meta', 'out_of_scope'):
            continue
        
        for feature in component.get('features', []):
            feat_name = feature.get('name', '').strip()
            if not feat_name:
                continue
            
            concept_ids = feature.get('concept_ids', [])
            gap_type = feature.get('gap_type', '')
            
            # Normalize gap type
            gap_type = gap_normalize.get(gap_type, GAP_PARTIAL)
            
            # Skip meta/out_of_scope features
            if gap_type in ('meta', 'out_of_scope'):
                continue
            
            # Determine gap type if not explicit
            if not gap_type:
                if not concept_ids:
                    gap_type = GAP_MISSING
                elif comp_status == 'gap':
                    gap_type = GAP_PARTIAL
                else:
                    gap_type = GAP_NONE
            
            feature_map[feat_name] = {
                'concept_ids': concept_ids,
                'gap_type': gap_type,
                'component': comp_name,
                'notes': feature.get('notes', '')
            }
    
    return feature_map


def load_ticket_counts(path: Path) -> dict[str, int]:
    """Load aggregated ticket counts from JSON."""
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def build_concept_ticket_counts(
    ticket_counts: dict[str, int],
    support_map: dict[str, dict]
) -> tuple[dict[str, int], list[str]]:
    """
    Map feature ticket counts to concepts.
    
    Returns:
        concept_ticket_counts: {concept_name: total_tickets}
        unmapped_features: list of features with no mapping
    """
    concept_counts = defaultdict(int)
    unmapped = []
    
    for feature, count in ticket_counts.items():
        if feature not in support_map:
            unmapped.append(feature)
            continue
        
        entry = support_map[feature]
        concept_ids = entry.get('concept_ids', [])
        
        # Skip if out of scope
        if entry.get('gap_type') == 'out_of_scope':
            continue
        
        if not concept_ids:
            # Missing concept - track under placeholder
            concept_counts[f"[NO CONCEPT] {feature}"] += count
        else:
            # Distribute equally among mapped concepts
            for cid in concept_ids:
                concept_counts[cid] += count
    
    return dict(concept_counts), unmapped


def build_doc_scores(
    docs: list[dict],
    support_map: dict[str, dict]
) -> tuple[dict[str, float], dict[str, list[str]]]:
    """
    Calculate documentation depth score per concept.
    """
    concept_scores = defaultdict(float)
    concept_urls = defaultdict(list)
    
    # Build concept worst-gap lookup from map
    concept_gap = {}
    for entry in support_map.values():
        gap = entry.get('gap_type', GAP_NONE)
        for cid in entry.get('concept_ids', []):
            current = concept_gap.get(cid, GAP_NONE)
            if gap == GAP_MISSING or current == GAP_MISSING:
                concept_gap[cid] = GAP_MISSING
            elif gap == GAP_PARTIAL or current == GAP_PARTIAL:
                concept_gap[cid] = GAP_PARTIAL
    
    for doc in docs:
        concepts = doc.get('concept_ids', [])
        if not concepts:
            continue
        
        word_count = doc.get('word_count', 0)
        has_code = doc.get('has_code_sample', False)
        
        page_score = DOC_BASE
        if word_count >= 500:
            page_score += DOC_WORD_BONUS
        if has_code:
            page_score += DOC_CODE_BONUS
        
        for cid in concepts:
            gap = concept_gap.get(cid, GAP_NONE)
            score = page_score
            if gap == GAP_PARTIAL:
                score *= DOC_PARTIAL_MULT
            
            concept_scores[cid] += score
            concept_urls[cid].append(doc.get('url', ''))
    
    return dict(concept_scores), dict(concept_urls)


def classify_coverage(ticket_count: int, doc_score: float) -> str:
    """Four-quadrant classification."""
    high_t = ticket_count >= 20
    high_d = doc_score >= 3.0
    
    if high_t and not high_d:
        return "critical_gap"
    if high_t and high_d:
        return "well_covered"
    if not high_t and not high_d:
        return "undocumented_gap"
    return "over_documented"


def build_coverage_matrix(
    concepts: dict[str, dict],
    ticket_counts: dict[str, int],
    doc_scores: dict[str, float],
    doc_urls: dict[str, list[str]]
) -> list[dict]:
    """Build the coverage matrix."""
    rows = []
    
    for name, concept in concepts.items():
        t_count = ticket_counts.get(name, 0)
        d_score = doc_scores.get(name, 0.0)
        urls = doc_urls.get(name, [])
        
        # Filter out NaN/None and convert to strings
        clean_urls = [str(u) for u in urls if u and str(u) != 'nan']
        
        rows.append({
            'concept_name': name,
            'concept_type': concept.get('type', ''),
            'ticket_count': t_count,
            'doc_score': round(d_score, 2),
            'doc_page_count': len(clean_urls),
            'doc_urls': '|'.join(clean_urls[:10]),  # Limit to 10
            'coverage_class': classify_coverage(t_count, d_score)
        })
    
    # Add missing concept placeholders
    for name, count in ticket_counts.items():
        if name.startswith("[NO CONCEPT]"):
            rows.append({
                'concept_name': name,
                'concept_type': 'MISSING',
                'ticket_count': count,
                'doc_score': 0.0,
                'doc_page_count': 0,
                'doc_urls': '',
                'coverage_class': 'critical_gap'
            })
    
    # Sort by priority
    priority = {"critical_gap": 0, "undocumented_gap": 1, "well_covered": 2, "over_documented": 3}
    rows.sort(key=lambda r: (priority.get(r["coverage_class"], 9), -r["ticket_count"]))
    
    return rows


def write_reports(
    matrix: list[dict],
    unmapped: list[str],
    output_dir: Path
):
    """Write output files."""
    output_dir.mkdir(exist_ok=True)
    
    # Full matrix
    df = pd.DataFrame(matrix)
    df.to_csv(output_dir / "coverage_matrix.csv", index=False)
    
    # High priority gaps
    critical = df[
        (df['coverage_class'] == 'critical_gap') & 
        (df['ticket_count'] >= 10)
    ]
    critical.to_csv(output_dir / "high_priority_gaps.csv", index=False)
    
    # Missing concepts
    missing = df[df['concept_name'].str.startswith('[NO CONCEPT]')]
    missing.to_csv(output_dir / "missing_concepts.csv", index=False)
    
    # Text report
    lines = [
        "=" * 72,
        "  XAF DOCUMENTATION COVERAGE MATRIX",
        f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "=" * 72,
        "",
        f"Total concepts analyzed: {len(df)}",
        f"Critical gaps (≥10 tickets, score <3.0): {len(critical)}",
        f"Missing concepts: {len(missing)}",
        f"Unmapped features: {len(unmapped)}",
        "",
        "=" * 72,
        "TOP 20 CRITICAL GAPS",
        "=" * 72,
    ]
    
    for _, row in critical.head(20).iterrows():
        lines.append(f"\n{row['concept_name']}")
        lines.append(f"  Tickets: {row['ticket_count']}  |  Doc Score: {row['doc_score']}  |  Pages: {row['doc_page_count']}")
    
    if unmapped:
        lines.extend([
            "",
            "=" * 72,
            f"UNMAPPED FEATURES ({len(unmapped)})",
            "=" * 72,
        ])
        lines.extend(f"  - {f}" for f in unmapped[:20])
    
    (output_dir / "summary_report.txt").write_text("\n".join(lines), encoding='utf-8')
    
    print(f"\n✅ Reports written to {output_dir}/")
    print(f"   - coverage_matrix.csv ({len(df)} concepts)")
    print(f"   - high_priority_gaps.csv ({len(critical)} gaps)")
    print(f"   - missing_concepts.csv ({len(missing)} missing)")
    print(f"   - summary_report.txt")


def main():
    """Main execution."""
    print("XAF Coverage Matrix Analysis")
    print("=" * 72)
    
    # Load data
    print("Loading data...")
    concepts = load_concepts(CONCEPTS_YML)
    topics_df = pd.read_parquet(TOPICS_INVENTORY)
    concepts_df = pd.read_parquet(DOC_CONCEPTS)
    ticket_counts = load_ticket_counts(TICKET_JSON)
    
    print(f"  ✓ {len(concepts)} concepts")
    print(f"  ✓ {len(topics_df)} documents")
    print(f"  ✓ {len(concepts_df)} sections")
    print(f"  ✓ {len(ticket_counts)} support features")
    
    # Check if support map exists
    if not SUPPORT_MAP_YML.exists():
        print(f"\n⚠️  Support concept map not found: {SUPPORT_MAP_YML}")
        print("   Expected location: support_concept_map.yml in project root")
        sys.exit(1)
    
    support_map = load_support_map(SUPPORT_MAP_YML)
    print(f"  ✓ {len(support_map)} mapped features")
    
    # Show mapping coverage
    mapped_count = sum(1 for f in ticket_counts if f in support_map)
    print(f"  ✓ {mapped_count}/{len(ticket_counts)} ticket features have mappings ({100*mapped_count//len(ticket_counts)}%)")
    
    # Aggregate doc index
    print("\nAggregating section-level concepts to document level...")
    docs = aggregate_doc_index(topics_df, concepts_df)
    print(f"  ✓ {len(docs)} documents with concepts")
    
    # Map tickets to concepts
    print("\nMapping support tickets to concepts...")
    concept_tickets, unmapped = build_concept_ticket_counts(ticket_counts, support_map)
    print(f"  ✓ {sum(concept_tickets.values())} total tickets mapped")
    print(f"  ⚠️  {len(unmapped)} unmapped features")
    
    # Calculate doc scores
    print("\nCalculating documentation depth scores...")
    doc_scores, doc_urls = build_doc_scores(docs, support_map)
    print(f"  ✓ {len(doc_scores)} concepts with documentation")
    
    # Build matrix
    print("\nBuilding coverage matrix...")
    matrix = build_coverage_matrix(concepts, concept_tickets, doc_scores, doc_urls)
    
    # Write reports
    output_dir = OUTPUT_DIR / "coverage_reports"
    write_reports(matrix, unmapped, output_dir)
    
    print("\n✅ Done!")


if __name__ == "__main__":
    main()
