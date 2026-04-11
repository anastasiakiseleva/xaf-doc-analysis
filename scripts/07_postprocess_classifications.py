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
        default="outputs/classified_pairs.parquet",
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

    # Drop low-confidence pairs
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
            print(f"\nConfidence filter (>= {args.min_confidence}): dropped {dropped:,} pairs → {len(df):,} remaining")
            if dropped > 0:
                print(f"  Dropped by type:")
                print(low_conf['relationship_type'].value_counts().to_string())

    # Apply corrections
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
