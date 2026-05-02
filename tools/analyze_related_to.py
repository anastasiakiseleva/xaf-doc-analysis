#!/usr/bin/env python3
"""Diagnostic analysis of `related_to` classified relationships.

Helps identify why so many pairs fall into the `related_to` catch-all type
and where prompt/heuristic improvements would have the most impact.

Outputs:
- outputs/related_to_analysis.csv   — all related_to pairs with enriched columns
- outputs/related_to_summary.txt    — printed summary (also saved to file)

Usage:
  python tools/analyze_related_to.py
  python tools/analyze_related_to.py --min-confidence 0.6 --sample 20
"""

from __future__ import annotations

import argparse
import textwrap
from collections import Counter
from pathlib import Path

import pandas as pd


OUT = Path("outputs")

CONF_BANDS = [
    ("< 0.50", 0.00, 0.50),
    ("0.50–0.60", 0.50, 0.60),
    ("0.60–0.70", 0.60, 0.70),
    ("0.70–0.80", 0.70, 0.80),
    ("0.80–0.90", 0.80, 0.90),
    ("≥ 0.90",   0.90, 1.01),
]

NEIGHBOR_LABELS = {
    "cc": "Concept→Concept",
    "aa": "API→API",
    "ca": "Concept→API",
    "ac": "API→Concept",
}


def safe_list(v):
    if v is None:
        return []
    if isinstance(v, float) and pd.isna(v):
        return []
    if isinstance(v, (list, tuple)):
        return list(v)
    tolist = getattr(v, "tolist", None)
    if callable(tolist):
        try:
            r = tolist()
            return r if isinstance(r, list) else list(r)
        except Exception:
            return []
    if hasattr(v, "__iter__") and not isinstance(v, str):
        try:
            return list(v)
        except Exception:
            return []
    return []


def _doc_type(doc_id: str, is_api: bool) -> str:
    if is_api:
        return "API Reference"
    p = doc_id.lower()
    if "how-to" in p or "howto" in p:
        return "How-to Task"
    if "tutorial" in p or "get-started" in p:
        return "Tutorial"
    return "Conceptual"


def main() -> int:
    ap = argparse.ArgumentParser(description="Analyze related_to relationships")
    ap.add_argument(
        "--sample",
        type=int,
        default=0,
        help="Print N random example pairs per confidence band (0 = skip)",
    )
    ap.add_argument(
        "--min-confidence",
        type=float,
        default=0.0,
        help="Only include pairs with confidence >= this value",
    )
    ap.add_argument(
        "--top-concept-pairs",
        type=int,
        default=30,
        help="Number of top concept pairs to show",
    )
    args = ap.parse_args()

    # ── Load data ────────────────────────────────────────────────────────────
    classified_path = OUT / "classified_pairs.parquet"
    if not classified_path.exists():
        print(f"ERROR: {classified_path} not found. Run Phase 6 first.")
        return 1

    df = pd.read_parquet(classified_path, engine="pyarrow")
    total_all = len(df)

    rt = df[df["relationship_type"] == "related_to"].copy()
    if args.min_confidence > 0:
        rt = rt[rt["relationship_confidence"] >= args.min_confidence]

    total_rt = len(rt)

    lines: list[str] = []

    def p(*args_):
        line = " ".join(str(a) for a in args_)
        lines.append(line)
        print(line)

    def sep(char="─", width=70):
        p(char * width)

    sep("═")
    p("RELATED_TO RELATIONSHIP ANALYSIS")
    sep("═")
    p(f"\nTotal classified pairs    : {total_all:,}")
    p(f"related_to pairs          : {total_rt:,}  ({100 * total_rt / total_all:.1f}%)")
    p(f"All other types           : {total_all - total_rt:,}  ({100 * (total_all - total_rt) / total_all:.1f}%)")

    # ── Breakdown: all relationship types ────────────────────────────────────
    p("\n")
    sep()
    p("RELATIONSHIP TYPE BREAKDOWN")
    sep()
    type_counts = df["relationship_type"].value_counts()
    for rtype, count in type_counts.items():
        marker = " ← FOCUS" if rtype == "related_to" else ""
        p(f"  {rtype:20} {count:6,}  ({100 * count / total_all:5.1f}%){marker}")

    # ── Confidence band distribution ─────────────────────────────────────────
    p("\n")
    sep()
    p("CONFIDENCE BANDS (related_to only)")
    sep()
    for label, lo, hi in CONF_BANDS:
        subset = rt[(rt["relationship_confidence"] >= lo) & (rt["relationship_confidence"] < hi)]
        pct_of_rt = 100 * len(subset) / total_rt if total_rt else 0
        pct_of_all = 100 * len(subset) / total_all if total_all else 0
        p(f"  {label:12}  {len(subset):5,}  ({pct_of_rt:5.1f}% of related_to | {pct_of_all:4.1f}% of all pairs)")

    p(f"\n  Median confidence : {rt['relationship_confidence'].median():.3f}")
    p(f"  Mean confidence   : {rt['relationship_confidence'].mean():.3f}")
    p(f"  Min / Max         : {rt['relationship_confidence'].min():.3f} / {rt['relationship_confidence'].max():.3f}")

    # ── Neighbor type breakdown ───────────────────────────────────────────────
    p("\n")
    sep()
    p("NEIGHBOR TYPE BREAKDOWN (related_to only)")
    sep()
    if "neighbor_type" in rt.columns:
        for ntype, label in NEIGHBOR_LABELS.items():
            subset = rt[rt["neighbor_type"] == ntype]
            # Rate: what % of all pairs of this neighbor_type are related_to?
            all_of_ntype = df[df["neighbor_type"] == ntype] if "neighbor_type" in df.columns else pd.DataFrame()
            rate = 100 * len(subset) / len(all_of_ntype) if len(all_of_ntype) else 0
            p(
                f"  {ntype}  {label:20}  {len(subset):5,} related_to  "
                f"/ {len(all_of_ntype):5,} total ({rate:5.1f}% of {ntype} pairs)"
            )

            # Show avg sim_score for this group
            if len(subset) and "sim_score" in subset.columns:
                p(f"       avg sim_score: {subset['sim_score'].mean():.3f}  "
                  f"| avg confidence: {subset['relationship_confidence'].mean():.3f}")

    # ── Section-type pair breakdown ───────────────────────────────────────────
    p("\n")
    sep()
    p("SECTION TYPE PAIR BREAKDOWN (related_to only)")
    sep()
    if "source_is_api" in rt.columns and "target_is_api" in rt.columns:
        rt["src_type"] = rt.apply(lambda r: _doc_type(r["source_doc"], bool(r["source_is_api"])), axis=1)
        rt["tgt_type"] = rt.apply(lambda r: _doc_type(r["target_doc"], bool(r["target_is_api"])), axis=1)
        type_pair_counts = rt.groupby(["src_type", "tgt_type"]).size().sort_values(ascending=False)
        for (src_t, tgt_t), count in type_pair_counts.items():
            pct = 100 * count / total_rt
            p(f"  {src_t:20} → {tgt_t:20}  {count:5,}  ({pct:5.1f}%)")

    # ── Similarity score distribution ─────────────────────────────────────────
    if "sim_score" in rt.columns:
        p("\n")
        sep()
        p("SIMILARITY SCORE DISTRIBUTION (related_to only)")
        sep()
        sim_bands = [(f"< 0.60", 0.0, 0.60), ("0.60–0.70", 0.60, 0.70),
                     ("0.70–0.80", 0.70, 0.80), ("0.80–0.90", 0.80, 0.90),
                     ("≥ 0.90", 0.90, 1.01)]
        for label, lo, hi in sim_bands:
            sub = rt[(rt["sim_score"] >= lo) & (rt["sim_score"] < hi)]
            p(f"  {label:12}  {len(sub):5,}  ({100 * len(sub) / total_rt:.1f}%)")
        p(f"\n  Mean sim_score    : {rt['sim_score'].mean():.3f}")
        p(f"  High sim (≥0.80)  : {len(rt[rt['sim_score'] >= 0.80]):,}  "
          f"({100 * len(rt[rt['sim_score'] >= 0.80]) / total_rt:.1f}%) "
          f"← strong candidates for reclassification")

    # ── Top concept pairs ─────────────────────────────────────────────────────
    p("\n")
    sep()
    p(f"TOP {args.top_concept_pairs} CONCEPT PAIRS IN related_to")
    sep()
    concept_pair_counter: Counter = Counter()
    for _, row in rt.iterrows():
        src_cs = safe_list(row.get("source_concepts", []))
        tgt_cs = safe_list(row.get("target_concepts", []))
        for sc in src_cs:
            for tc in tgt_cs:
                if sc != tc:
                    concept_pair_counter[(sc, tc)] += 1
    for (sc, tc), cnt in concept_pair_counter.most_common(args.top_concept_pairs):
        p(f"  {cnt:4}  {sc}  →  {tc}")

    # ── classification_source breakdown ──────────────────────────────────────
    if "classification_source" in rt.columns:
        p("\n")
        sep()
        p("CLASSIFICATION SOURCE (related_to only)")
        sep()
        src_counts = rt["classification_source"].value_counts()
        for src, cnt in src_counts.items():
            p(f"  {str(src):20}  {cnt:5,}  ({100 * cnt / total_rt:.1f}%)")

    # ── High-sim related_to: prime reclassification candidates ───────────────
    p("\n")
    sep()
    p("HIGH-CONFIDENCE related_to (≥ 0.70) — Reclassification Candidates")
    sep()
    candidates = rt[rt["relationship_confidence"] >= 0.70].copy()
    p(f"  {len(candidates):,} pairs ({100 * len(candidates) / total_rt:.1f}% of related_to)")
    p(f"  These were classified as related_to with HIGH confidence → most")
    p(f"  likely to yield a more specific type upon prompt improvement.")

    if "neighbor_type" in candidates.columns:
        p("\n  By neighbor type:")
        for ntype, label in NEIGHBOR_LABELS.items():
            sub = candidates[candidates["neighbor_type"] == ntype]
            p(f"    {ntype}  {label:20}  {len(sub):,}")

    # ── Sample examples ───────────────────────────────────────────────────────
    if args.sample > 0:
        p("\n")
        sep()
        p(f"SAMPLE PAIRS PER CONFIDENCE BAND (n={args.sample})")
        sep()
        for label, lo, hi in CONF_BANDS:
            band = rt[(rt["relationship_confidence"] >= lo) & (rt["relationship_confidence"] < hi)]
            if band.empty:
                continue
            sample = band.sample(min(args.sample, len(band)), random_state=42)
            p(f"\n  [{label}]  ({len(band):,} pairs total)")
            for _, row in sample.iterrows():
                src = "/".join(row["source_doc"].split("/")[-2:])
                tgt = "/".join(row["target_doc"].split("/")[-2:])
                conf = row["relationship_confidence"]
                sim = row.get("sim_score", 0)
                sc = safe_list(row.get("source_concepts", []))
                tc = safe_list(row.get("target_concepts", []))
                ntype = row.get("neighbor_type", "?")
                p(f"    conf={conf:.2f} sim={sim:.2f} [{ntype}]")
                p(f"      {src}")
                p(f"      → {tgt}")
                p(f"      concepts: {sc} / {tc}")

    # ── Actionable summary ────────────────────────────────────────────────────
    p("\n")
    sep("═")
    p("ACTIONABLE IMPROVEMENT TARGETS")
    sep("═")

    high_sim_rt = rt[rt.get("sim_score", pd.Series(dtype=float)) >= 0.75] if "sim_score" in rt.columns else pd.DataFrame()
    ca_rt = rt[rt["neighbor_type"] == "ca"] if "neighbor_type" in rt.columns else pd.DataFrame()
    low_conf_rt = rt[rt["relationship_confidence"] < 0.60]

    p(f"\n  1. HIGH SIM related_to (sim ≥ 0.75): {len(high_sim_rt):,} pairs")
    p(f"     → These share strong vocabulary — prompt B1/B2 should capture them.")
    p(f"     → Post-processing heuristic C1 can auto-reclassify `ca` subset as `uses`.")

    p(f"\n  2. Concept→API (ca) related_to: {len(ca_rt):,} pairs")
    p(f"     → Structurally almost always `uses`; strongest win from heuristic C1.")

    p(f"\n  3. LOW CONFIDENCE related_to (< 0.60): {len(low_conf_rt):,} pairs")
    p(f"     → These are genuinely ambiguous/noisy — candidates for `needs_review` flag.")
    p(f"     → Consider excluding from KG edges (lower signal quality).")

    if "neighbor_type" in rt.columns:
        cc_rt = rt[rt["neighbor_type"] == "cc"]
        p(f"\n  4. Concept→Concept related_to: {len(cc_rt):,} pairs")
        p(f"     → Examine top concept pairs above — taxonomy gaps likely here.")
        p(f"     → Review taxonomy `related_to` links that should be directed.")

    sep("═")

    # ── Save outputs ──────────────────────────────────────────────────────────
    # Save enriched CSV
    csv_cols = [
        "source_doc", "source_section", "target_doc", "target_section",
        "relationship_type", "relationship_confidence", "relationship_bidirectional",
        "sim_score", "neighbor_type", "source_concepts", "target_concepts",
        "source_is_api", "target_is_api", "classification_source",
        "overlap_concepts",
    ]
    export_cols = [c for c in csv_cols if c in rt.columns]
    if "src_type" in rt.columns:
        export_cols += ["src_type", "tgt_type"]
    rt[export_cols].to_csv(OUT / "related_to_analysis.csv", index=False)
    p(f"\n💾 Detailed CSV → outputs/related_to_analysis.csv  ({total_rt:,} rows)")

    # Save summary text
    summary_path = OUT / "related_to_summary.txt"
    summary_path.write_text("\n".join(lines), encoding="utf-8")
    p(f"💾 Summary text → outputs/related_to_summary.txt")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
