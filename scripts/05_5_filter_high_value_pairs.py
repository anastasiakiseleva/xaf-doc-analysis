"""
Filter semantic pairs to high-value subset for relationship classification.

Focus on:
1. High similarity scores (confident relationships)
2. Substantive shared concepts (non-noise overlap)
3. Cross-corpus links (conceptual ↔ API reference) boosted
"""

import pandas as pd
from pathlib import Path

# Configuration
OUTPUT_DIR = Path("outputs")
MIN_SIMILARITY = 0.70  # High-confidence pairs only
MAX_PAIRS = 5000  # Target output size
CROSS_CORPUS_BOOST = 1.5  # Boost score for conceptual ↔ API links

# Concepts that are too generic to produce distinguishable relationships.
# Pairs whose only shared concepts are from this set are filtered out.
NOISE_CONCEPTS = frozenset([
    'Blazor', 'WinForms', '.NET Runtime', 'Windows',
    'Actions', 'Controllers', 'Built-in Controllers', 'Built-in Actions',
    'Views',
])


def safe_list(val):
    """Convert various formats to list."""
    if val is None:
        return []
    if hasattr(val, 'tolist'):
        return val.tolist()
    if isinstance(val, float) and pd.isna(val):
        return []
    return list(val) if val else []


def main():
    print("="*70)
    print("High-Value Semantic Pairs Filter")
    print("="*70)

    # Load semantic pairs
    pairs_path = OUTPUT_DIR / "semantic_pairs.parquet"
    print(f"\nLoading semantic pairs from {pairs_path}...")
    pairs_df = pd.read_parquet(pairs_path)
    print(f"  Total pairs: {len(pairs_df):,}")

    # Rename similarity column if needed
    if 'similarity' not in pairs_df.columns and 'sim_score' in pairs_df.columns:
        pairs_df = pairs_df.rename(columns={'sim_score': 'similarity'})

    # Filter by minimum similarity
    print(f"\nApplying similarity filter (>= {MIN_SIMILARITY})...")
    high_sim = pairs_df[pairs_df['similarity'] >= MIN_SIMILARITY].copy()
    print(f"  Remaining: {len(high_sim):,} pairs ({len(high_sim)/len(pairs_df)*100:.1f}%)")

    # Remove self-pairs (same document on both sides).
    # frozenset dedup below won't catch these since frozenset([a, a]) == frozenset([a]).
    before_self = len(high_sim)
    high_sim = high_sim[high_sim['source_doc'] != high_sim['target_doc']].copy()
    print(f"\nRemoved {before_self - len(high_sim):,} self-pairs → {len(high_sim):,} remaining")

    # Drop pairs where the shared (overlapping) concepts are all noise.
    # Pairs whose only common ground is e.g. "Blazor" and "WinForms" produce
    # near-identical prompts and mostly classify as related_to at unnecessary cost.
    print("\nFiltering out noise-only shared-concept pairs...")
    def shared_substantive(row):
        src = set(safe_list(row['source_concepts']))
        tgt = set(safe_list(row['target_concepts']))
        shared = src & tgt
        return any(c not in NOISE_CONCEPTS for c in shared)
    substantive_mask = high_sim.apply(shared_substantive, axis=1)
    before_noise = len(high_sim)
    high_sim = high_sim[substantive_mask].copy()
    print(f"  Removed {before_noise - len(high_sim):,} noise-shared pairs → {len(high_sim):,} remaining")

    # Drop API-to-API sibling pairs that share a common parent path segment.
    # E.g. DxDashboardModel/ChildContent → DxDashboardModel/ComponentInstance
    # are sibling members of the same class — not useful relationship targets.
    print("\nFiltering out API-sibling (same-parent) pairs...")
    def same_api_parent(row):
        if not (row['source_is_api'] and row['target_is_api']):
            return False
        src_parts = str(row['source_doc']).rstrip('/').split('/')
        tgt_parts = str(row['target_doc']).rstrip('/').split('/')
        # Same parent = last two path segments share the second-to-last segment
        return len(src_parts) >= 2 and len(tgt_parts) >= 2 and src_parts[-2] == tgt_parts[-2]
    sibling_mask = high_sim.apply(same_api_parent, axis=1)
    before_sib = len(high_sim)
    high_sim = high_sim[~sibling_mask].copy()
    print(f"  Removed {before_sib - len(high_sim):,} API-sibling pairs → {len(high_sim):,} remaining")

    # Drop broad-intro section pairs: early sections (index ≤ 2) of conceptual
    # articles with few concepts (≤ 5) paired with API pages.
    # These are overview/hub article preambles that match API pages purely due
    # to shared vocabulary, not specific content relevance.
    # E.g. views::2 (5 generic concepts) → DataAccessMode1137762 (a specific API property).
    print("\nFiltering out broad-intro section pairs (article→API)...")
    high_sim['_src_sec_idx'] = high_sim['source_section'].str.extract(r'::(\d+)$').astype(float)
    high_sim['_src_n_concepts'] = high_sim['source_concepts'].apply(lambda x: len(safe_list(x)))
    broad_intro_mask = (
        (~high_sim['source_is_api']) &
        high_sim['target_is_api'] &
        (high_sim['_src_sec_idx'] <= 2) &
        (high_sim['_src_n_concepts'] <= 5)
    )
    before_intro = len(high_sim)
    high_sim = high_sim[~broad_intro_mask].drop(columns=['_src_sec_idx', '_src_n_concepts']).copy()
    print(f"  Removed {before_intro - len(high_sim):,} broad-intro pairs → {len(high_sim):,} remaining")

    # Calculate priority scores
    print("\nCalculating priority scores...")

    high_sim['source_concepts_list'] = high_sim['source_concepts'].apply(safe_list)
    high_sim['target_concepts_list'] = high_sim['target_concepts'].apply(safe_list)

    # Check if cross-corpus (conceptual ↔ API)
    high_sim['is_cross_corpus'] = high_sim['source_is_api'] != high_sim['target_is_api']

    # Priority = similarity, boosted for cross-corpus pairs
    high_sim['priority_score'] = high_sim['similarity']
    high_sim.loc[high_sim['is_cross_corpus'], 'priority_score'] *= CROSS_CORPUS_BOOST

    # Sort by priority
    high_sim = high_sim.sort_values('priority_score', ascending=False)

    # Deduplicate at doc level: keep only the highest-priority section pair
    # per unique (source_doc, target_doc) undirected combination.
    # This prevents multiple sections of the same two documents from all
    # appearing as separate pairs and dominating the top of the ranked list.
    high_sim['_pair_key'] = high_sim.apply(
        lambda r: frozenset([str(r['source_doc']), str(r['target_doc'])]),
        axis=1,
    )
    before_dedup = len(high_sim)
    high_sim = high_sim.drop_duplicates(subset=['_pair_key']).drop(columns=['_pair_key'])
    print(f"Doc-level mirror deduplication: {before_dedup:,} → {len(high_sim):,} pairs "
          f"({before_dedup - len(high_sim):,} removed)")

    # Take top N
    filtered = high_sim.head(MAX_PAIRS)

    # Print summary statistics
    print("\n" + "="*70)
    print("FILTERED RESULTS SUMMARY")
    print("="*70)
    print(f"Total filtered pairs: {len(filtered):,}")
    print(f"\nSimilarity range: {filtered['similarity'].min():.3f} - {filtered['similarity'].max():.3f}")
    print(f"  Mean:   {filtered['similarity'].mean():.3f}")
    print(f"  Median: {filtered['similarity'].median():.3f}")

    cross_corpus_count = filtered['is_cross_corpus'].sum()
    print(f"\nCross-corpus links (conceptual ↔ API): {cross_corpus_count:,} ({cross_corpus_count/len(filtered)*100:.1f}%)")

    # Top concepts by frequency
    all_concepts = []
    for concepts in filtered['source_concepts_list']:
        all_concepts.extend(concepts)
    for concepts in filtered['target_concepts_list']:
        all_concepts.extend(concepts)
    concept_counts = pd.Series(all_concepts).value_counts()
    print(f"\nTop 10 concepts in filtered pairs:")
    for concept, count in concept_counts.head(10).items():
        print(f"  {concept}: {count:,} pairs")

    # Save filtered pairs
    output_path = OUTPUT_DIR / "semantic_pairs_high_value.parquet"
    print(f"\nSaving filtered pairs to {output_path}...")

    essential_cols = [
        'source_doc', 'source_section', 'source_is_api', 'source_concepts',
        'target_doc', 'target_section', 'target_is_api', 'target_concepts',
        'similarity', 'priority_score', 'is_cross_corpus',
    ]
    filtered[essential_cols].to_parquet(output_path, index=False)

    csv_path = OUTPUT_DIR / "semantic_pairs_high_value.csv"
    print(f"Saving CSV preview to {csv_path}...")
    filtered[essential_cols].head(100).to_csv(csv_path, index=False)

    print("\n" + "="*70)
    print("✅ FILTERING COMPLETE")
    print("="*70)
    print(f"\nNext step: Run relationship classification on {output_path.name}")
    print(f"  Command: python scripts/06_classify_relationships.py --input {output_path.name}")
    print(f"\nEstimated classification time:")
    print(f"  With local model (Ollama): ~2-3 hours")
    print(f"  With cloud API (GPT-4/Claude): ~30-60 minutes")
    print(f"  Estimated cost (cloud): ~${len(filtered) * 0.005:.2f} - ${len(filtered) * 0.01:.2f}")


if __name__ == "__main__":
    main()
