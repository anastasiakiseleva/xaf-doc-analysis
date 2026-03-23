#!/usr/bin/env python3
"""Extract relationships (edges) among a chosen set of sections.

This tool builds an induced subgraph over the selected sections using:
- outputs/semantic_pairs.parquet
- outputs/classified_pairs_corrected.parquet (optional)

Typical use case:
- Start from a hits CSV produced by tools/keyword_section_query.py
- Extract the direct semantic/classified edges *between* those hit sections

Example:
  python tools/section_relationships.py \
    --hits-csv outputs/lookup_property_editors_lookup_mode_fq_hits.csv \
    --out-prefix outputs/lookup_property_editors_lookup_mode_relationships
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

import pandas as pd

OUT = Path("outputs")


def safe_list(v: Any) -> List[Any]:
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


@dataclass(frozen=True)
class SectionKey:
    doc_id: str
    section_id: str

    def as_tuple(self) -> Tuple[str, str]:
        return (self.doc_id, self.section_id)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Extract relationships among selected sections")
    p.add_argument(
        "--hits-csv",
        default=str(OUT / "keyword_hits.csv"),
        help="CSV with at least doc_id, section_id (e.g., output of tools/keyword_section_query.py)",
    )
    p.add_argument(
        "--semantic-pairs",
        default=str(OUT / "semantic_pairs.parquet"),
        help="Path to semantic_pairs.parquet",
    )
    p.add_argument(
        "--classified-pairs",
        default=str(OUT / "classified_pairs_corrected.parquet"),
        help="Path to classified_pairs_corrected.parquet (optional)",
    )
    p.add_argument(
        "--out-prefix",
        default=str(OUT / "section_relationships"),
        help="Output prefix (writes *_edges.csv, *_nodes.csv, *_report.md)",
    )
    p.add_argument(
        "--prefer-classified",
        action="store_true",
        help="If set, write classified relationship fields when available (still includes semantic edges).")
    p.add_argument(
        "--dedupe-undirected",
        action="store_true",
        help="Collapse A→B and B→A into one edge row with combined neighbor_types.")
    return p.parse_args()


def _canon_pair(a: SectionKey, b: SectionKey) -> Tuple[Tuple[str, str], Tuple[str, str]]:
    return (a.as_tuple(), b.as_tuple()) if a.as_tuple() <= b.as_tuple() else (b.as_tuple(), a.as_tuple())


def main() -> int:
    args = parse_args()

    hits_path = Path(args.hits_csv)
    if not hits_path.exists():
        raise FileNotFoundError(f"Missing hits CSV: {hits_path}")

    hits = pd.read_csv(hits_path)
    if "doc_id" not in hits.columns or "section_id" not in hits.columns:
        raise ValueError("hits CSV must contain columns: doc_id, section_id")

    # Build section set + lookup metadata
    meta: Dict[Tuple[str, str], Dict[str, Any]] = {}
    section_set: set[Tuple[str, str]] = set()

    for r in hits.itertuples(index=False):
        doc_id = str(getattr(r, "doc_id"))
        section_id = str(getattr(r, "section_id"))
        section_set.add((doc_id, section_id))
        meta[(doc_id, section_id)] = {
            "title": getattr(r, "title", ""),
            "is_api": getattr(r, "is_api", None),
        }

    if not section_set:
        print("No sections found in hits CSV.")
        return 0

    sem_path = Path(args.semantic_pairs)
    if not sem_path.exists():
        raise FileNotFoundError(f"Missing semantic pairs: {sem_path}")

    sem = pd.read_parquet(sem_path)

    # Filter semantic edges to induced subgraph
    sem_mask = sem.apply(
        lambda row: (str(row.source_doc), str(row.source_section)) in section_set
        and (str(row.target_doc), str(row.target_section)) in section_set,
        axis=1,
    )
    sem_sub = sem[sem_mask].copy()

    # Optionally load classified and filter similarly
    cls_sub = pd.DataFrame()
    cls_path = Path(args.classified_pairs)
    if cls_path.exists():
        cls = pd.read_parquet(cls_path)
        cls_mask = cls.apply(
            lambda row: (str(row.source_doc), str(row.source_section)) in section_set
            and (str(row.target_doc), str(row.target_section)) in section_set,
            axis=1,
        )
        cls_sub = cls[cls_mask].copy()

    # Build edge rows (semantic is the base)
    edge_rows: List[Dict[str, Any]] = []

    # Index classified edges for quick lookup (exact direction)
    cls_idx: Dict[Tuple[str, str, str, str], Dict[str, Any]] = {}
    if not cls_sub.empty:
        for r in cls_sub.itertuples(index=False):
            cls_idx[(str(r.source_doc), str(r.source_section), str(r.target_doc), str(r.target_section))] = {
                "relationship_type": getattr(r, "relationship_type", None),
                "relationship_confidence": getattr(r, "relationship_confidence", None),
                "relationship_bidirectional": getattr(r, "relationship_bidirectional", None),
            }

    for r in sem_sub.itertuples(index=False):
        a = SectionKey(str(r.source_doc), str(r.source_section))
        b = SectionKey(str(r.target_doc), str(r.target_section))

        a_meta = meta.get(a.as_tuple(), {})
        b_meta = meta.get(b.as_tuple(), {})

        row: Dict[str, Any] = {
            "source_doc": a.doc_id,
            "source_section": a.section_id,
            "source_title": a_meta.get("title", ""),
            "source_is_api": a_meta.get("is_api", None),
            "target_doc": b.doc_id,
            "target_section": b.section_id,
            "target_title": b_meta.get("title", ""),
            "target_is_api": b_meta.get("is_api", None),
            "neighbor_type": getattr(r, "neighbor_type", None),
            "sim_score": float(getattr(r, "sim_score", 0.0)),
            "gates_passed": ", ".join([g for g in safe_list(getattr(r, "gates_passed", [])) if isinstance(g, str)]),
            "overlap_concepts": ", ".join([c for c in safe_list(getattr(r, "overlap_concepts", [])) if isinstance(c, str)]),
            "overlap_platforms": ", ".join([p for p in safe_list(getattr(r, "overlap_platforms", [])) if isinstance(p, str)]),
            "overlap_apis": ", ".join([a for a in safe_list(getattr(r, "overlap_apis", [])) if isinstance(a, str)]),
            "namespace_overlap": bool(getattr(r, "namespace_overlap", False)),
        }

        if args.prefer_classified and cls_idx:
            rel = cls_idx.get((a.doc_id, a.section_id, b.doc_id, b.section_id))
            if rel:
                row.update(rel)

        edge_rows.append(row)

    edges = pd.DataFrame(edge_rows)

    if args.dedupe_undirected and not edges.empty:
        # Canonicalize undirected pair key, then aggregate.
        def canon_key(df: pd.DataFrame) -> pd.Series:
            a = list(zip(df["source_doc"].astype(str), df["source_section"].astype(str)))
            b = list(zip(df["target_doc"].astype(str), df["target_section"].astype(str)))
            keys = []
            for aa, bb in zip(a, b):
                keys.append((aa, bb) if aa <= bb else (bb, aa))
            return pd.Series(keys)

        edges = edges.assign(_pair_key=canon_key(edges))

        def agg_neighbor_types(xs: pd.Series) -> str:
            vals = sorted({str(v) for v in xs.dropna().tolist() if str(v).strip()})
            return ",".join(vals)

        def agg_str(xs: pd.Series) -> str:
            vals = []
            for v in xs.dropna().tolist():
                s = str(v).strip()
                if s:
                    vals.extend([p.strip() for p in s.split(",") if p.strip()])
            return ", ".join(sorted(set(vals)))

        grouped = edges.groupby("_pair_key", dropna=False)

        # Keep stable representative metadata from the row with max sim
        idx_max = grouped["sim_score"].idxmax()
        base = edges.loc[idx_max].copy().set_index("_pair_key")

        base["neighbor_type"] = grouped["neighbor_type"].apply(agg_neighbor_types)
        base["gates_passed"] = grouped["gates_passed"].apply(agg_str)
        base["overlap_concepts"] = grouped["overlap_concepts"].apply(agg_str)
        base["overlap_platforms"] = grouped["overlap_platforms"].apply(agg_str)
        base["overlap_apis"] = grouped["overlap_apis"].apply(agg_str)

        edges = base.reset_index(drop=True)

        # Ensure direction is canonical (source <= target)
        def is_canonical(row: pd.Series) -> bool:
            a = (str(row["source_doc"]), str(row["source_section"]))
            b = (str(row["target_doc"]), str(row["target_section"]))
            return a <= b

        for i, row in edges.iterrows():
            if not is_canonical(row):
                # swap
                edges.loc[i, [
                    "source_doc",
                    "source_section",
                    "source_title",
                    "source_is_api",
                    "target_doc",
                    "target_section",
                    "target_title",
                    "target_is_api",
                ]] = [
                    row["target_doc"],
                    row["target_section"],
                    row["target_title"],
                    row["target_is_api"],
                    row["source_doc"],
                    row["source_section"],
                    row["source_title"],
                    row["source_is_api"],
                ]

    # Node stats
    deg: Dict[Tuple[str, str], int] = {k: 0 for k in section_set}
    if not edges.empty:
        for r in edges.itertuples(index=False):
            a = (str(getattr(r, "source_doc")), str(getattr(r, "source_section")))
            b = (str(getattr(r, "target_doc")), str(getattr(r, "target_section")))
            if a in deg:
                deg[a] += 1
            if b in deg:
                deg[b] += 1

    node_rows = []
    for (doc_id, section_id) in sorted(section_set):
        m = meta.get((doc_id, section_id), {})
        node_rows.append({
            "doc_id": doc_id,
            "section_id": section_id,
            "title": m.get("title", ""),
            "is_api": m.get("is_api", None),
            "degree_within_set": int(deg.get((doc_id, section_id), 0)),
        })

    nodes = pd.DataFrame(node_rows)

    out_prefix = Path(args.out_prefix)
    out_prefix.parent.mkdir(parents=True, exist_ok=True)

    edges_path = out_prefix.with_name(out_prefix.name + "_edges.csv")
    nodes_path = out_prefix.with_name(out_prefix.name + "_nodes.csv")
    md_path = out_prefix.with_name(out_prefix.name + "_report.md")

    edges.to_csv(edges_path, index=False, encoding="utf-8")
    nodes.to_csv(nodes_path, index=False, encoding="utf-8")

    # Markdown report (small + scannable)
    lines: List[str] = []
    lines.append(f"# Section Relationship Report")
    lines.append("")
    lines.append(f"Input hits: `{hits_path.as_posix()}`")
    lines.append(f"Sections in set: **{len(section_set)}**")
    lines.append(f"Semantic edges within set: **{len(edges)}**")
    if cls_path.exists():
        lines.append(f"Classified edges within set: **{len(cls_sub)}**")
    else:
        lines.append("Classified edges within set: **(file missing)**")
    lines.append("")

    lines.append("## Sections (degree within set)")
    for r in nodes.sort_values(["degree_within_set", "doc_id"], ascending=[False, True]).itertuples(index=False):
        lines.append(f"- {r.degree_within_set:>2}  {r.doc_id}  ({r.section_id})")

    lines.append("")
    lines.append("## Edges")
    if edges.empty:
        lines.append("- (No semantic edges between these sections at current thresholds)")
    else:
        show = edges.sort_values(["sim_score"], ascending=[False])
        for r in show.itertuples(index=False):
            sim = getattr(r, "sim_score", None)
            nt = getattr(r, "neighbor_type", "")
            lines.append(
                f"- {sim:.3f} [{nt}] {r.source_doc} ({r.source_section}) ↔ {r.target_doc} ({r.target_section})"
            )
            oc = str(getattr(r, "overlap_concepts", "") or "").strip()
            if oc:
                lines.append(f"  Overlap concepts: {oc}")

    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Sections: {len(section_set)}")
    print(f"Edges (semantic induced): {len(edges)}")
    print(f"Wrote: {edges_path}")
    print(f"Wrote: {nodes_path}")
    print(f"Wrote: {md_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
