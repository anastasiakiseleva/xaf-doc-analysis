#!/usr/bin/env python3
"""Concept drill-down helper.

Prints:
- sections tagged with the concept (kept-only)
- API vs conceptual split
- platform distribution
- connectivity stats (avg/median/isolated)
- cross-corpus pair count (ca/ac where overlap_concepts includes the concept)
- top/least connected sections
- top mapped APIs for the concept (from api_implements_concept.parquet)

Also saves:
- outputs/concept_<concept>_sections.csv

Usage:
  python tools/concept_drilldown.py --concept "Criteria"
"""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

import pandas as pd


OUT = Path("outputs")


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


def slug(text: str) -> str:
    return "".join(ch.lower() if ch.isalnum() else "_" for ch in (text or "")).strip("_")


def main() -> int:
    ap = argparse.ArgumentParser(description="Concept drill-down")
    ap.add_argument("--concept", required=True, help="Concept name (must match tagging)")
    ap.add_argument("--top", type=int, default=10, help="How many sections to print in top/low lists")
    args = ap.parse_args()

    concept = args.concept

    concepts_df = pd.read_parquet(OUT / "doc_concepts.parquet")
    pairs_df = pd.read_parquet(OUT / "semantic_pairs.parquet")

    kept = concepts_df[concepts_df["kept"] == True].copy()

    mask = kept["concepts"].apply(lambda cs: concept in safe_list(cs))
    sec = kept[mask].copy()

    print("Concept:", concept)
    print("Sections tagged (kept):", len(sec))
    print(" - API sections:", int((sec["is_api"] == True).sum()))
    print(" - Conceptual sections:", int((sec["is_api"] == False).sum()))

    # Platforms
    plats = Counter()
    for v in sec.get("platforms", []):
        plats.update([p for p in safe_list(v) if p])

    print("\nTop platforms:")
    if plats:
        for p, c in plats.most_common(12):
            print(f"  {p:25} {c}")
    else:
        print("  (none)")

    # Connectivity per section
    conn = Counter()
    for r in pairs_df.itertuples(index=False):
        conn[(r.source_doc, r.source_section)] += 1
        conn[(r.target_doc, r.target_section)] += 1

    sec["connections"] = sec.apply(lambda r: conn.get((r["doc_id"], r["section_id"]), 0), axis=1)

    print("\nConnectivity:")
    if len(sec):
        print(" - avg connections/section:", round(float(sec["connections"].mean()), 2))
        print(" - median:", float(sec["connections"].median()))
        print(" - isolated (0):", int((sec["connections"] == 0).sum()))
    else:
        print(" - (no sections)")

    # Cross-corpus pairs involving this concept
    cross = pairs_df[pairs_df["neighbor_type"].isin(["ca", "ac"])]
    cross_count = 0
    if "overlap_concepts" in cross.columns:
        for v in cross["overlap_concepts"]:
            if concept in safe_list(v):
                cross_count += 1

    print("\nCross-corpus pairs (ca/ac) with overlap_concepts including concept:", cross_count)

    # Top/low sections
    if len(sec):
        print(f"\nTop {args.top} most connected sections:")
        for _, r in sec.sort_values("connections", ascending=False).head(args.top).iterrows():
            print(f"  {int(r['connections']):3d}  {r['doc_id']}")

        print(f"\nTop {args.top} least connected sections:")
        for _, r in sec.sort_values("connections", ascending=True).head(args.top).iterrows():
            print(f"  {int(r['connections']):3d}  {r['doc_id']}")

    # API mapping
    api_impl_path = OUT / "api_implements_concept.parquet"
    if api_impl_path.exists():
        api_impl = pd.read_parquet(api_impl_path)
        if {"concept_name", "api_id"}.issubset(api_impl.columns):
            mapped = api_impl[api_impl["concept_name"] == concept].copy()
            print("\nAPI mappings:")
            print(" - unique APIs mapped:", mapped["api_id"].nunique())
            if len(mapped):
                cols = [c for c in ["api_id", "confidence", "source", "count"] if c in mapped.columns]
                show = mapped.sort_values(["confidence"], ascending=False)
                print(f"\nTop {min(20, len(show))} API mappings by confidence:")
                print(show[cols].head(20).to_string(index=False))
    else:
        print("\nAPI mappings: (api_implements_concept.parquet not found)")

    out_csv = OUT / f"concept_{slug(concept)}_sections.csv"
    sec[["doc_id", "section_id", "is_api", "platforms", "connections", "concepts"]].to_csv(out_csv, index=False)
    print("\nSaved:", out_csv)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
