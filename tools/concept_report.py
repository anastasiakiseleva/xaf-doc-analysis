#!/usr/bin/env python3
"""Generate a concept-level report from pipeline outputs.

Outputs:
- outputs/concept_report.csv
- outputs/concept_report.json

Includes:
- sections per concept (kept only)
- avg semantic connections per section (from outputs/semantic_pairs.parquet)
- cross-corpus pair counts per concept (ca/ac only, from overlap_concepts)
- unique APIs mapped per concept (from outputs/api_implements_concept.parquet)

Usage:
  python tools/concept_report.py
"""

from __future__ import annotations

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


def main() -> int:
    concepts_df = pd.read_parquet(OUT / "doc_concepts.parquet")
    pairs_df = pd.read_parquet(OUT / "semantic_pairs.parquet")

    api_impl_path = OUT / "api_implements_concept.parquet"
    api_impl = pd.read_parquet(api_impl_path) if api_impl_path.exists() else pd.DataFrame()

    kept = concepts_df[concepts_df["kept"] == True].copy()

    # Concept frequency
    all_concepts = []
    for cs in kept["concepts"]:
        all_concepts.extend([c for c in safe_list(cs) if isinstance(c, str) and c])
    concept_counts = pd.Series(all_concepts).value_counts()

    # Connection counts per section
    conn = Counter()
    for r in pairs_df.itertuples(index=False):
        conn[(r.source_doc, r.source_section)] += 1
        conn[(r.target_doc, r.target_section)] += 1

    # Cross-corpus counts per concept (from overlap_concepts on ca/ac)
    cross_pairs = pairs_df[pairs_df["neighbor_type"].isin(["ca", "ac"])].copy()
    cross_counts = Counter()
    if "overlap_concepts" in cross_pairs.columns:
        for v in cross_pairs["overlap_concepts"]:
            for c in safe_list(v):
                if isinstance(c, str) and c:
                    cross_counts[c] += 1

    # API mapping coverage per concept
    api_per_concept = {}
    if not api_impl.empty and {"concept_name", "api_id"}.issubset(api_impl.columns):
        api_per_concept = api_impl.groupby("concept_name")["api_id"].nunique().to_dict()

    rows = []
    for concept, n_sections in concept_counts.items():
        mask = kept["concepts"].apply(lambda cs: concept in safe_list(cs))
        sec = kept[mask]

        total_connections = 0
        for rr in sec.itertuples(index=False):
            total_connections += conn.get((rr.doc_id, rr.section_id), 0)

        avg_conn = (total_connections / len(sec)) if len(sec) else 0

        rows.append(
            {
                "concept": concept,
                "sections": int(n_sections),
                "avg_connections_per_section": round(avg_conn, 2),
                "cross_corpus_pairs": int(cross_counts.get(concept, 0)),
                "unique_apis_mapped": int(api_per_concept.get(concept, 0)),
            }
        )

    report = pd.DataFrame(rows)

    (OUT / "concept_report.csv").write_text(report.to_csv(index=False), encoding="utf-8")
    (OUT / "concept_report.json").write_text(report.to_json(orient="records"), encoding="utf-8")

    # Console summary
    by_sections = report.sort_values(["sections", "avg_connections_per_section"], ascending=[False, False])
    under_connected = report.sort_values(["avg_connections_per_section", "sections"], ascending=[True, False])
    zero_cross = report[(report["sections"] >= 10) & (report["cross_corpus_pairs"] == 0)].sort_values("sections", ascending=False)

    print("Concept report saved:")
    print(" - outputs/concept_report.csv")
    print(" - outputs/concept_report.json")

    print("\n=== Quick Summary ===")
    print("Kept sections:", len(kept))
    print("Unique concepts used:", int(concept_counts.shape[0]))

    print("\nTop concepts by sections:")
    print(by_sections.head(15).to_string(index=False))

    print("\nMost under-connected (avg connections/section):")
    print(under_connected.head(15).to_string(index=False))

    print("\nConcepts (>=10 sections) with ZERO cross-corpus pairs:")
    if len(zero_cross) == 0:
        print("(none)")
    else:
        print(zero_cross.head(20).to_string(index=False))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
