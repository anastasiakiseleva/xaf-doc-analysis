"""
Filter semantic pairs to high-value subset for relationship classification.

Focus on:
1. High similarity scores (confident relationships)
2. Substantive shared concepts (non-noise overlap)
3. Cross-corpus links (conceptual ↔ API reference) boosted
"""

import argparse
import pandas as pd
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config_loader import cfg

# Configuration defaults
OUTPUT_DIR = Path("outputs")
MIN_SIMILARITY = 0.75  # Raised from 0.70 — low-sim pairs mostly classify as related_to
MAX_PAIRS = 25000  # Raised to accommodate xref_link pairs (~19K) plus high-sim pairs
CROSS_CORPUS_BOOST = 1.5  # Boost score for conceptual <-> API links

# Path to the explicit link graph produced by Phase 2.
# Pairs whose (source_doc, target_doc) appear here bypass the noise-concept
# filter — an explicit hyperlink is ground truth that a relationship exists.
F_EXPLICIT = OUTPUT_DIR / "explicit_graph.parquet"

# Concepts that are too generic to produce distinguishable relationships.
# Pairs whose only shared concepts are from this set are filtered out.
# Loaded from config/product.yml (filtering.noise_concepts).
NOISE_CONCEPTS = cfg.noise_concepts()


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
    parser = argparse.ArgumentParser(
        description="Filter semantic pairs to high-value subset for classification"
    )
    parser.add_argument(
        "--min-sim", type=float, default=MIN_SIMILARITY,
        help=f"Minimum similarity for non-xref pairs (default: {MIN_SIMILARITY})"
    )
    parser.add_argument(
        "--max-pairs", type=int, default=MAX_PAIRS,
        help=f"Maximum pairs to keep (default: {MAX_PAIRS})"
    )
    cli_args = parser.parse_args()

    min_similarity = cli_args.min_sim
    max_pairs = cli_args.max_pairs

    print("="*70)
    print("High-Value Semantic Pairs Filter")
    print("="*70)

    # Load explicit cross-links (Phase 2 output) to build a bypass set.
    # Any (source_doc, target_doc) pair that already has a confirmed hyperlink
    # will skip the substantive-concept noise filter below.
    explicit_pairs: set[frozenset] = set()
    if F_EXPLICIT.exists():
        eg = pd.read_parquet(F_EXPLICIT)
        for _, row in eg.iterrows():
            explicit_pairs.add(frozenset([str(row['source_doc']), str(row['target_doc'])]))
        print(f"\nLoaded {len(explicit_pairs):,} explicit doc-pairs from {F_EXPLICIT.name}")
    else:
        print(f"\n[WARN] {F_EXPLICIT} not found — explicit-link bypass disabled")

    # Load semantic pairs
    pairs_path = OUTPUT_DIR / "semantic_pairs.parquet"
    print(f"\nLoading semantic pairs from {pairs_path}...")
    pairs_df = pd.read_parquet(pairs_path)
    print(f"  Total pairs: {len(pairs_df):,}")

    # Rename similarity column if needed
    if 'similarity' not in pairs_df.columns and 'sim_score' in pairs_df.columns:
        pairs_df = pairs_df.rename(columns={'sim_score': 'similarity'})

    # Split out xref_link pairs — these bypass the sim floor and noise filter
    # because editorial xref: links are ground truth regardless of embedding sim.
    # Mean sim of xref pairs is ~0.62; 82% fall below the 0.70 floor.
    def _has_xref(g):
        return g is not None and 'xref_link' in g
    xref_mask = pairs_df['gates_passed'].apply(_has_xref)
    xref_pairs = pairs_df[xref_mask].copy()
    non_xref = pairs_df[~xref_mask].copy()
    print(f"\nSplit out {len(xref_pairs):,} xref_link pairs (bypass sim floor + noise filter)")
    print(f"  Non-xref pairs to filter: {len(non_xref):,}")

    # Filter by minimum similarity (non-xref only)
    print(f"\nApplying similarity filter (>= {min_similarity}) to non-xref pairs...")
    high_sim = non_xref[non_xref['similarity'] >= min_similarity].copy()
    print(f"  Remaining: {len(high_sim):,} pairs ({len(high_sim)/len(non_xref)*100:.1f}%)")

    # Remove self-pairs (same document on both sides).
    # frozenset dedup below won't catch these since frozenset([a, a]) == frozenset([a]).
    before_self = len(high_sim)
    high_sim = high_sim[high_sim['source_doc'] != high_sim['target_doc']].copy()
    print(f"\nRemoved {before_self - len(high_sim):,} self-pairs -> {len(high_sim):,} remaining")

    # Drop pairs where the shared (overlapping) concepts are all noise.
    # Pairs whose only common ground is e.g. "Blazor" and "WinForms" produce
    # near-identical prompts and mostly classify as related_to at unnecessary cost.
    # Exception: pairs that already appear as an explicit hyperlink in the docs
    # are kept regardless — the link itself is ground truth that a relationship
    # exists and deserves a typed label from the classifier.
    print("\nFiltering out noise-only shared-concept pairs (with explicit-link bypass)...")
    def shared_substantive(row):
        src = set(safe_list(row['source_concepts']))
        tgt = set(safe_list(row['target_concepts']))
        shared = src & tgt
        return any(c not in NOISE_CONCEPTS for c in shared)
    def keep_pair(row):
        if frozenset([str(row['source_doc']), str(row['target_doc'])]) in explicit_pairs:
            return True  # explicit hyperlink — bypass noise filter
        return shared_substantive(row)
    keep_mask = high_sim.apply(keep_pair, axis=1)
    substantive_mask = high_sim.apply(shared_substantive, axis=1)
    bypassed = keep_mask.sum() - substantive_mask.sum()
    before_noise = len(high_sim)
    high_sim = high_sim[keep_mask].copy()
    print(f"  Removed {before_noise - len(high_sim):,} noise-shared pairs → {len(high_sim):,} remaining")
    if bypassed > 0:
        print(f"  (Kept {bypassed:,} explicit-link pairs that would otherwise have been dropped)")

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

    # Deduplicate non-xref pairs at doc level: keep only the highest-priority
    # section pair per unique (source_doc, target_doc) undirected combination.
    high_sim['_pair_key'] = high_sim.apply(
        lambda r: frozenset([str(r['source_doc']), str(r['target_doc'])]),
        axis=1,
    )
    before_dedup = len(high_sim)
    high_sim = high_sim.drop_duplicates(subset=['_pair_key']).drop(columns=['_pair_key'])
    print(f"Doc-level mirror deduplication: {before_dedup:,} -> {len(high_sim):,} pairs "
          f"({before_dedup - len(high_sim):,} removed)")

    # Merge xref pairs back in, deduped against the filtered non-xref set.
    # xref pairs are NOT doc-level deduped — multiple sections of the same doc
    # pair can appear if the author linked them separately (each is a distinct signal).
    # We do remove xref pairs whose (source_section, target_section) key already
    # appears in the non-xref filtered set (avoids double-counting NN+xref overlap).
    print(f"\nMerging {len(xref_pairs):,} xref_link pairs back in...")
    existing_section_keys = set(
        zip(high_sim['source_section'], high_sim['target_section'])
    )
    xref_new = xref_pairs[
        ~xref_pairs.apply(
            lambda r: (r['source_section'], r['target_section']) in existing_section_keys,
            axis=1,
        )
    ].copy()
    print(f"  {len(xref_new):,} net-new xref pairs (after dedup with non-xref set)")

    # Compute priority score for xref pairs too (cross-corpus boost applies)
    xref_new['source_concepts_list'] = xref_new['source_concepts'].apply(safe_list)
    xref_new['target_concepts_list'] = xref_new['target_concepts'].apply(safe_list)
    xref_new['is_cross_corpus'] = xref_new['source_is_api'] != xref_new['target_is_api']
    xref_new['priority_score'] = xref_new['similarity']
    xref_new.loc[xref_new['is_cross_corpus'], 'priority_score'] *= CROSS_CORPUS_BOOST

    high_sim = pd.concat([high_sim, xref_new], ignore_index=True)
    print(f"  Combined total: {len(high_sim):,} pairs")

    # Section-level mirror dedup: if both (A->B) and (B->A) exist, keep only
    # the higher-priority direction.  Doc-level dedup above handles non-xref
    # rows, but section-level mirrors can survive via the xref merge.
    print("\nSection-level mirror deduplication...")
    high_sim['_sec_pair_key'] = high_sim.apply(
        lambda r: frozenset([str(r['source_section']), str(r['target_section'])]),
        axis=1,
    )
    before_sec_dedup = len(high_sim)
    high_sim = high_sim.sort_values('priority_score', ascending=False)
    high_sim = high_sim.drop_duplicates(subset=['_sec_pair_key']).drop(columns=['_sec_pair_key'])
    print(f"  {before_sec_dedup:,} -> {len(high_sim):,} pairs "
          f"({before_sec_dedup - len(high_sim):,} section-level mirrors removed)")

    # Take top N
    filtered = high_sim.head(max_pairs)

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
        'similarity', 'priority_score', 'is_cross_corpus', 'gates_passed',
    ]
    # gates_passed may not exist in older non-xref rows; fill with empty list
    if 'gates_passed' not in filtered.columns:
        filtered['gates_passed'] = [[] for _ in range(len(filtered))]
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
