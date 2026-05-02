#!/usr/bin/env python3
"""
Phase 7: Post-Process Classification Results

Corrects over-aggressive bidirectional marking from Claude while preserving
Ollama's more conservative approach.

Usage:
    python scripts/07_postprocess_classifications.py
    python scripts/07_postprocess_classifications.py --input outputs/classified_pairs.parquet --output outputs/classified_pairs_corrected.parquet
    python scripts/07_postprocess_classifications.py --dry-run  # Preview changes without saving
"""

import argparse
from pathlib import Path
import pandas as pd


def reclassify_conceptual_to_api(df: pd.DataFrame, min_sim: float = 0.75, dry_run: bool = False) -> pd.DataFrame:
    """
    C1: Reclassify Conceptual->API related_to pairs with sim_score >= min_sim as `uses`.

    Rationale: Conceptual docs that semantically overlap strongly with an API page
    are structurally `uses` relationships — the concept page references the API page
    as the implementation. This is confirmed by the structural shortcut in the
    classification prompt: Conceptual/How-to/Tutorial -> API Reference with shared
    concepts should default to `uses`.

    Rule:
        related_to AND source_is_api=False AND target_is_api=True AND sim_score >= min_sim
        -> relationship_type = 'uses', confidence = 0.65, bidirectional = False
    """
    mask = (
        (df['relationship_type'] == 'related_to') &
        (df['source_is_api'] == False) &
        (df['target_is_api'] == True) &
        (df['sim_score'] >= min_sim)
    )
    count = mask.sum()

    print("\n" + "=" * 70)
    print(f"C1: CONCEPTUAL->API RECLASSIFICATION (related_to -> uses, sim >= {min_sim})")
    print("=" * 70)

    if count == 0:
        print("  No qualifying Conceptual->API related_to pairs found.")
        return df

    if dry_run:
        print(f"  [DRY RUN] {count:,} pairs WOULD BE reclassified: related_to -> uses (confidence 0.72)")
        below = ((df['relationship_type'] == 'related_to') & (df['source_is_api'] == False) & (df['target_is_api'] == True)).sum()
        print(f"  (of {below:,} total Conceptual->API related_to pairs; {count/below*100:.0f}% meet sim >= {min_sim})")
        return df

    df_out = df.copy()
    df_out.loc[mask, 'relationship_type'] = 'uses'
    df_out.loc[mask, 'relationship_confidence'] = 0.72
    df_out.loc[mask, 'relationship_bidirectional'] = False
    print(f"  Reclassified {count:,} pairs: related_to -> uses (confidence 0.72)")
    return df_out


def flag_low_confidence_related_to(df: pd.DataFrame, max_conf: float = 0.60, dry_run: bool = False) -> pd.DataFrame:
    """
    C2: Add needs_review=True flag to related_to pairs with confidence < max_conf.

    Rationale: Low-confidence related_to pairs are noisy edges — the LLM could not
    identify any directional signal and classified with near-random confidence (~0.50).
    Flagging these allows downstream KG build to filter them out or treat them as
    weak edges rather than hard graph edges.
    """
    if 'needs_review' not in df.columns:
        df = df.copy()
        df['needs_review'] = False

    mask = (
        (df['relationship_type'] == 'related_to') &
        (df['relationship_confidence'] < max_conf)
    )
    count = mask.sum()

    print("\n" + "=" * 70)
    print(f"C2: FLAG LOW-CONFIDENCE related_to (confidence < {max_conf})")
    print("=" * 70)

    if count == 0:
        print("  No low-confidence related_to pairs found.")
        return df

    if dry_run:
        print(f"  [DRY RUN] {count:,} pairs WOULD BE flagged needs_review=True")
        return df

    df_out = df.copy() if 'needs_review' not in df.columns else df
    df_out.loc[mask, 'needs_review'] = True
    already = df_out['needs_review'].sum() - count
    print(f"  Flagged {count:,} pairs as needs_review=True")
    if already > 0:
        print(f"  ({already:,} were already flagged)")
    return df_out


def reclassify_api_to_conceptual(df: pd.DataFrame, dry_run: bool = False) -> pd.DataFrame:
    """
    Reclassify API→Conceptual `related_to` pairs as `extends`.

    Rationale (thesaurus theory, Hedden Ch.4):
    An API Reference page is a concrete named instance of the concept it
    implements. The standard thesaurus BTI/NTI (broader/narrower term,
    instance) relationship maps cleanly to `extends` in this schema, since
    `extends` already covers "A is a specialization/realization of B."

    Rule:
        related_to AND source_is_api=True AND target_is_api=False
        -> relationship_type = 'extends', confidence = 0.60, bidirectional = False
    """
    mask = (
        (df['relationship_type'] == 'related_to') &
        (df['source_is_api'] == True) &
        (df['target_is_api'] == False)
    )
    count = mask.sum()

    print("\n" + "=" * 70)
    print("API->CONCEPTUAL RECLASSIFICATION (related_to -> extends)")
    print("=" * 70)

    if count == 0:
        print("  No API->Conceptual related_to pairs found.")
        return df

    if dry_run:
        print(f"  [DRY RUN] {count:,} pairs WOULD BE reclassified: related_to -> extends (confidence 0.72)")
        return df

    df_out = df.copy()
    df_out.loc[mask, 'relationship_type'] = 'extends'
    df_out.loc[mask, 'relationship_confidence'] = 0.72
    df_out.loc[mask, 'relationship_bidirectional'] = False
    print(f"  Reclassified {count:,} pairs: related_to -> extends (confidence 0.72)")
    return df_out


def correct_bidirectional_marking(df: pd.DataFrame, dry_run: bool = False) -> pd.DataFrame:
    """
    Apply heuristics to correct over-aggressive bidirectional marking.

    Rules:
    1. "uses" relationships: Only bidirectional if similarity >= 0.90 AND confidence >= 0.85
       - Rationale: Tutorial using an API doesn't mean API "uses" tutorial
       - Exception: Very high similarity suggests mutual reference

    2. "explains" relationships: Keep existing (seems reasonable at 56%)

    3. "requires" relationships: Keep existing (already conservative at 0%)

    4. "extends" relationships: Keep existing

    5. "related_to" relationships: Keep existing
    """
    
    df_corrected = df.copy()
    
    # Track changes
    original_bidir = df_corrected['relationship_bidirectional'].sum()
    changes = []
    
    # Rule 1: Correct "uses" relationships
    uses_mask = (
        (df_corrected['relationship_type'] == 'uses') &
        (df_corrected['relationship_bidirectional'] == True) &
        ((df_corrected['sim_score'] < 0.90) | (df_corrected['relationship_confidence'] < 0.85))
    )
    
    uses_changes = uses_mask.sum()
    if uses_changes > 0:
        if dry_run:
            changes.append(f"  'uses' relationships: {uses_changes} WOULD BE changed from bidirectional to unidirectional")
        else:
            changes.append(f"  'uses' relationships: {uses_changes} changed from bidirectional to unidirectional")
            df_corrected.loc[uses_mask, 'relationship_bidirectional'] = False
    
    # Rule 2: Flag suspicious "explains" bidirectional (but don't change)
    explains_bidir_mask = (
        (df_corrected['relationship_type'] == 'explains') &
        (df_corrected['relationship_bidirectional'] == True) &
        (df_corrected['sim_score'] < 0.85)
    )
    
    if explains_bidir_mask.sum() > 0:
        changes.append(f"  'explains' relationships: {explains_bidir_mask.sum()} flagged for manual review (not changed)")
    
    new_bidir = df_corrected['relationship_bidirectional'].sum()
    actual_changes = original_bidir - new_bidir if not dry_run else uses_changes
    
    print("\n" + "=" * 70)
    print("BIDIRECTIONAL CORRECTION SUMMARY")
    print("=" * 70)
    print(f"Original bidirectional relationships: {original_bidir} ({100*original_bidir/len(df):.1f}%)")
    if dry_run:
        projected_bidir = original_bidir - uses_changes
        print(f"Projected bidirectional relationships: {projected_bidir} ({100*projected_bidir/len(df):.1f}%)")
        print(f"Projected corrections: {uses_changes}")
    else:
        print(f"Corrected bidirectional relationships: {new_bidir} ({100*new_bidir/len(df_corrected):.1f}%)")
        print(f"Total corrections: {actual_changes}")
    
    print("\nChanges applied:" if not dry_run else "\nChanges that WOULD BE applied:")
    for change in changes:
        print(change)
    
    # Show breakdown after correction
    print("\nBidirectional by relationship type (after correction):" if not dry_run else "\nBidirectional by relationship type (projected):")
    for rel_type in df_corrected['relationship_type'].unique():
        subset = df_corrected[df_corrected['relationship_type'] == rel_type]
        bidir_count = subset['relationship_bidirectional'].sum()
        bidir_pct = 100 * bidir_count / len(subset)
        print(f"  {rel_type:15} {bidir_count:3}/{len(subset):3} ({bidir_pct:5.1f}%)")
    
    return df_corrected


def main():
    parser = argparse.ArgumentParser(
        description="Post-process classification results to correct bidirectional over-marking"
    )
    parser.add_argument(
        "--input",
        type=str,
        default="outputs/classified_pairs_before_merge.parquet",
        help="Input classified pairs file"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="outputs/classified_pairs_corrected.parquet",
        help="Output corrected file"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without saving"
    )
    parser.add_argument(
        "--in-place",
        action="store_true",
        help="Overwrite input file (use with caution)"
    )
    parser.add_argument(
        "--min-confidence",
        type=float,
        default=0.70,
        help="Drop pairs below this confidence threshold (default: 0.70)"
    )
    parser.add_argument(
        "--c1-min-sim",
        type=float,
        default=0.75,
        help="C1: min sim_score for Conceptual->API related_to -> uses reclassification (default: 0.75)"
    )
    parser.add_argument(
        "--c2-max-conf",
        type=float,
        default=0.60,
        help="C2: max confidence for related_to needs_review flag (default: 0.60)"
    )
    parser.add_argument(
        "--skip-c1",
        action="store_true",
        help="Skip C1 Conceptual->API reclassification"
    )
    parser.add_argument(
        "--skip-c2",
        action="store_true",
        help="Skip C2 needs_review flagging"
    )

    args = parser.parse_args()
    
    print("=" * 70)
    print("Phase 7: Post-Process Classifications")
    print("=" * 70)
    
    # Load data
    print(f"\nLoading classifications from {args.input}...")
    df = pd.read_parquet(args.input, engine="pyarrow")
    print(f"  Loaded {len(df):,} classified pairs")
    
    # Show original statistics
    print(f"\nOriginal statistics:")
    print(f"  Bidirectional: {df['relationship_bidirectional'].sum()} ({100*df['relationship_bidirectional'].sum()/len(df):.1f}%)")
    print(f"  Relationship types: {df['relationship_type'].nunique()}")
    print(f"  Average confidence: {df['relationship_confidence'].mean():.3f}")

    # Apply heuristic reclassifications BEFORE confidence filter so rescued
    # pairs (assigned new confidence >= 0.70) survive the filter.
    if not args.skip_c1:
        df = reclassify_conceptual_to_api(df, min_sim=args.c1_min_sim, dry_run=args.dry_run)

    if not args.skip_c2:
        df = flag_low_confidence_related_to(df, max_conf=args.c2_max_conf, dry_run=args.dry_run)

    df = reclassify_api_to_conceptual(df, dry_run=args.dry_run)

    # Drop low-confidence pairs (after heuristics so rescued pairs survive)
    if args.min_confidence > 0:
        before_conf = len(df)
        low_conf = df[df['relationship_confidence'] < args.min_confidence]
        if args.dry_run:
            print(f"\n[DRY RUN] Confidence filter (>= {args.min_confidence}): would drop {len(low_conf):,} pairs")
            print(f"  Breakdown of pairs that would be dropped:")
            print(low_conf['relationship_type'].value_counts().to_string())
        else:
            df = df[df['relationship_confidence'] >= args.min_confidence].copy()
            dropped = before_conf - len(df)
            print(f"\nConfidence filter (>= {args.min_confidence}): dropped {dropped:,} pairs -> {len(df):,} remaining")
            if dropped > 0:
                print(f"  Dropped by type:")
                print(low_conf['relationship_type'].value_counts().to_string())

    df_corrected = correct_bidirectional_marking(df, dry_run=args.dry_run)
    
    # Save results
    if not args.dry_run:
        output_path = args.input if args.in_place else args.output
        print(f"\nSaving corrected classifications to {output_path}...")
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        df_corrected.to_parquet(output_path, engine="pyarrow", index=False)
        print(f"✓ Saved {len(df_corrected):,} pairs to {output_path}")
    else:
        print("\n[DRY RUN] No changes saved. Run without --dry-run to apply corrections.")
    
    print("\n" + "=" * 70)
    print("Post-processing complete!")
    print("=" * 70)


if __name__ == "__main__":
    main()
