#!/usr/bin/env python3
"""Suggest links for isolated sections within a concept.

This tool answers: "Which isolated sections should link to what?"

It identifies kept sections tagged with a given concept that have 0 semantic
connections in outputs/semantic_pairs.parquet, then uses the embedding corpora
(conceptual + API) to find nearest neighbors and emits link suggestions.

Outputs
-------
- outputs/isolated_<concept>_link_suggestions.csv (long format)
- outputs/isolated_<concept>_link_suggestions.md  (human-readable summary)

Usage
-----
python tools/suggest_isolated_links.py --concept "Criteria" --top-sources 50 --topk 8
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors


OUT = Path("outputs")


def safe_list(v: Any) -> List[Any]:
    if v is None:
        return []
    if isinstance(v, float) and pd.isna(v):
        return []
    if isinstance(v, (list, tuple, set, frozenset)):
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


def to_matrix(emb_series: pd.Series) -> np.ndarray:
    return np.vstack([np.asarray(v, dtype=np.float32) for v in emb_series.to_list()])


def intersect(a: Iterable[str], b: Iterable[str]) -> List[str]:
    sa = {x for x in a if isinstance(x, str) and x}
    sb = {x for x in b if isinstance(x, str) and x}
    return sorted(sa.intersection(sb))


def ns_root(api: str, levels: int = 3) -> str:
    if not api:
        return ""
    parts = api.split(".")
    return ".".join(parts[:levels]) if len(parts) >= levels else ".".join(parts)


def namespace_overlap(apis1: Iterable[str], apis2: Iterable[str], levels: int = 3) -> bool:
    r1 = {ns_root(a, levels) for a in apis1 if isinstance(a, str) and a}
    r2 = {ns_root(a, levels) for a in apis2 if isinstance(a, str) and a}
    r1.discard("")
    r2.discard("")
    return len(r1.intersection(r2)) > 0


def gate_cc(overlap_concepts: List[str], overlap_platforms: List[str], sim: float, min_sim: float = 0.60, fallback_sim: float = 0.75) -> Tuple[bool, List[str]]:
    if sim < min_sim:
        return False, []
    gates: List[str] = []
    if overlap_concepts:
        gates.append("concept_overlap")
    if overlap_platforms:
        gates.append("platform_overlap")
    if gates:
        return True, gates
    if sim >= fallback_sim:
        return True, ["high_similarity_fallback"]
    return False, []


def gate_cross(overlap_concepts: List[str], overlap_platforms: List[str], overlap_apis: List[str], ns_overlap: bool,
              sim: float, min_sim: float = 0.65, fallback_sim: float = 0.80) -> Tuple[bool, List[str]]:
    if sim < min_sim:
        return False, []
    gates: List[str] = []
    if overlap_concepts:
        gates.append("concept_overlap")
    if overlap_platforms:
        gates.append("platform_overlap")
    if overlap_apis:
        gates.append("api_overlap")
    if ns_overlap:
        gates.append("namespace_overlap")
    if gates:
        return True, gates
    if sim >= fallback_sim:
        return True, ["high_similarity_fallback"]
    return False, []


@dataclass
class SectionMeta:
    doc_id: str
    section_id: str
    is_api: bool
    concepts: List[str]
    platforms: List[str]
    apis: List[str]
    title: str
    h_path: str


def build_meta_lookup(df_emb: pd.DataFrame) -> Dict[Tuple[str, str], SectionMeta]:
    lookup: Dict[Tuple[str, str], SectionMeta] = {}
    for r in df_emb.itertuples(index=False):
        key = (str(r.doc_id), str(r.section_id))
        lookup[key] = SectionMeta(
            doc_id=str(r.doc_id),
            section_id=str(r.section_id),
            is_api=bool(getattr(r, "is_api", False)),
            concepts=safe_list(getattr(r, "concepts", [])),
            platforms=safe_list(getattr(r, "platforms", [])),
            apis=safe_list(getattr(r, "apis", [])),
            title=str(getattr(r, "title", "")) if getattr(r, "title", None) is not None else "",
            h_path=str(getattr(r, "h_path", "")) if getattr(r, "h_path", None) is not None else "",
        )
    return lookup


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Suggest links for isolated sections within a concept")
    p.add_argument("--concept", required=True, help="Concept name (exact match)")
    p.add_argument("--top-sources", type=int, default=50, help="How many isolated sections to include in the report")
    p.add_argument("--topk", type=int, default=8, help="Neighbors to retrieve from each corpus")
    p.add_argument("--min-sim", type=float, default=0.72, help="Minimum similarity to include as a suggestion")
    p.add_argument("--include-weak", action="store_true", help="Include suggestions even if gate would not pass")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    concept = args.concept

    # Inputs
    dc = pd.read_parquet(OUT / "doc_concepts.parquet")
    pairs = pd.read_parquet(OUT / "semantic_pairs.parquet")
    emb_c = pd.read_parquet(OUT / "sections_embeddings_conceptual.parquet")
    emb_a = pd.read_parquet(OUT / "sections_embeddings_api.parquet")

    kept = dc[dc["kept"] == True].copy()

    # Connection counts from semantic_pairs
    conn = Counter()
    for r in pairs.itertuples(index=False):
        conn[(r.source_doc, r.source_section)] += 1
        conn[(r.target_doc, r.target_section)] += 1

    # Find isolated sections for this concept
    mask = kept["concepts"].apply(lambda cs: concept in safe_list(cs))
    sec = kept[mask].copy()
    sec["connections"] = sec.apply(lambda r: conn.get((r["doc_id"], r["section_id"]), 0), axis=1)

    isolated = sec[sec["connections"] == 0].copy()

    print(f"Concept: {concept}")
    print(f"Tagged sections (kept): {len(sec):,}")
    print(f"Isolated sections (0 connections): {len(isolated):,}")

    if len(isolated) == 0:
        print("✅ No isolated sections for this concept")
        return 0

    # Build embedding indices
    Xc = to_matrix(emb_c["embedding"])
    Xa = to_matrix(emb_a["embedding"])

    nn_c = NearestNeighbors(n_neighbors=min(len(emb_c), args.topk + 1), metric="cosine").fit(Xc)
    nn_a = NearestNeighbors(n_neighbors=min(len(emb_a), args.topk + 1), metric="cosine").fit(Xa)

    # Fast lookup from section -> embedding row index
    idx_c = {(str(r.doc_id), str(r.section_id)): i for i, r in enumerate(emb_c.itertuples(index=False))}
    idx_a = {(str(r.doc_id), str(r.section_id)): i for i, r in enumerate(emb_a.itertuples(index=False))}

    meta_c = build_meta_lookup(emb_c)
    meta_a = build_meta_lookup(emb_a)

    suggestions: List[Dict[str, Any]] = []

    def add_suggestion(src: SectionMeta, tgt: SectionMeta, sim: float, pair_kind: str, gates: List[str], would_pass: bool):
        suggestions.append({
            "source_doc": src.doc_id,
            "source_section": src.section_id,
            "source_is_api": src.is_api,
            "source_title": src.title,
            "source_h_path": src.h_path,
            "target_doc": tgt.doc_id,
            "target_section": tgt.section_id,
            "target_is_api": tgt.is_api,
            "target_title": tgt.title,
            "target_h_path": tgt.h_path,
            "similarity": round(float(sim), 4),
            "pair_kind": pair_kind,
            "shared_concepts": ", ".join(intersect(src.concepts, tgt.concepts)[:12]),
            "shared_platforms": ", ".join(intersect(src.platforms, tgt.platforms)[:12]),
            "shared_apis": ", ".join(intersect(src.apis, tgt.apis)[:8]),
            "gates": ", ".join(gates),
            "would_pass_gate": bool(would_pass),
        })

    # Score isolated sources by their best available suggestion (for prioritization)
    scored_sources: List[Tuple[float, Tuple[str, str], bool]] = []

    for r in isolated.itertuples(index=False):
        key = (str(r.doc_id), str(r.section_id))
        is_api = bool(r.is_api)

        # Find its embedding row
        if is_api:
            if key not in idx_a:
                continue
            src_i = idx_a[key]
            src_vec = Xa[src_i:src_i+1]
            # same corpus neighbors
            dist, ind = nn_a.kneighbors(src_vec, n_neighbors=min(len(emb_a), args.topk + 1))
            sims_same = 1.0 - dist[0]
            inds_same = ind[0]
            # cross corpus neighbors
            distx, indx = nn_c.kneighbors(src_vec, n_neighbors=min(len(emb_c), args.topk))
            sims_cross = 1.0 - distx[0]
            inds_cross = indx[0]

            src_meta = meta_a.get(key)
            if not src_meta:
                continue

            best_sim = 0.0

            # Same corpus (AA-like, but we don't have aa edges in current pairs; still useful for link suggestions)
            for sim, j in zip(sims_same, inds_same):
                if j == src_i:
                    continue
                if sim < args.min_sim:
                    continue
                tgt_key = (str(emb_a.iloc[j]["doc_id"]), str(emb_a.iloc[j]["section_id"]))
                tgt_meta = meta_a.get(tgt_key)
                if not tgt_meta:
                    continue

                ov_c = intersect(src_meta.concepts, tgt_meta.concepts)
                ov_p = intersect(src_meta.platforms, tgt_meta.platforms)
                ov_a = intersect(src_meta.apis, tgt_meta.apis)
                ns_ov = namespace_overlap(src_meta.apis, tgt_meta.apis)

                would_pass, gates = gate_cross(ov_c, ov_p, ov_a, ns_ov, sim)  # treat as cross gating heuristic
                if (would_pass or args.include_weak):
                    add_suggestion(src_meta, tgt_meta, sim, "api→api", gates, would_pass)
                best_sim = max(best_sim, float(sim))

            # Cross (A→C)
            for sim, j in zip(sims_cross, inds_cross):
                if sim < args.min_sim:
                    continue
                tgt_key = (str(emb_c.iloc[j]["doc_id"]), str(emb_c.iloc[j]["section_id"]))
                tgt_meta = meta_c.get(tgt_key)
                if not tgt_meta:
                    continue

                ov_c = intersect(src_meta.concepts, tgt_meta.concepts)
                ov_p = intersect(src_meta.platforms, tgt_meta.platforms)
                ov_a = intersect(src_meta.apis, tgt_meta.apis)
                ns_ov = namespace_overlap(src_meta.apis, tgt_meta.apis)

                would_pass, gates = gate_cross(ov_c, ov_p, ov_a, ns_ov, sim)
                if (would_pass or args.include_weak):
                    add_suggestion(src_meta, tgt_meta, sim, "api→conceptual", gates, would_pass)
                best_sim = max(best_sim, float(sim))

            scored_sources.append((best_sim, key, True))

        else:
            if key not in idx_c:
                continue
            src_i = idx_c[key]
            src_vec = Xc[src_i:src_i+1]

            dist, ind = nn_c.kneighbors(src_vec, n_neighbors=min(len(emb_c), args.topk + 1))
            sims_same = 1.0 - dist[0]
            inds_same = ind[0]

            distx, indx = nn_a.kneighbors(src_vec, n_neighbors=min(len(emb_a), args.topk))
            sims_cross = 1.0 - distx[0]
            inds_cross = indx[0]

            src_meta = meta_c.get(key)
            if not src_meta:
                continue

            best_sim = 0.0

            # Same corpus (C→C)
            for sim, j in zip(sims_same, inds_same):
                if j == src_i:
                    continue
                if sim < args.min_sim:
                    continue
                tgt_key = (str(emb_c.iloc[j]["doc_id"]), str(emb_c.iloc[j]["section_id"]))
                tgt_meta = meta_c.get(tgt_key)
                if not tgt_meta:
                    continue

                ov_c = intersect(src_meta.concepts, tgt_meta.concepts)
                ov_p = intersect(src_meta.platforms, tgt_meta.platforms)
                would_pass, gates = gate_cc(ov_c, ov_p, sim)

                if (would_pass or args.include_weak):
                    add_suggestion(src_meta, tgt_meta, sim, "conceptual→conceptual", gates, would_pass)
                best_sim = max(best_sim, float(sim))

            # Cross (C→A)
            for sim, j in zip(sims_cross, inds_cross):
                if sim < args.min_sim:
                    continue
                tgt_key = (str(emb_a.iloc[j]["doc_id"]), str(emb_a.iloc[j]["section_id"]))
                tgt_meta = meta_a.get(tgt_key)
                if not tgt_meta:
                    continue

                ov_c = intersect(src_meta.concepts, tgt_meta.concepts)
                ov_p = intersect(src_meta.platforms, tgt_meta.platforms)
                ov_a = intersect(src_meta.apis, tgt_meta.apis)
                ns_ov = namespace_overlap(src_meta.apis, tgt_meta.apis)

                would_pass, gates = gate_cross(ov_c, ov_p, ov_a, ns_ov, sim)
                if (would_pass or args.include_weak):
                    add_suggestion(src_meta, tgt_meta, sim, "conceptual→api", gates, would_pass)
                best_sim = max(best_sim, float(sim))

            scored_sources.append((best_sim, key, False))

    # Prioritize sources with the strongest available suggestion
    scored_sources.sort(key=lambda t: t[0], reverse=True)
    top_keys = set(k for _, k, _ in scored_sources[: args.top_sources])

    df = pd.DataFrame(suggestions)
    if df.empty:
        print("⚠️ No suggestions met the similarity threshold. Try lowering --min-sim.")
        return 0

    df = df[df.apply(lambda r: (str(r["source_doc"]), str(r["source_section"])) in top_keys, axis=1)].copy()

    # Sort within each source: prefer gate-pass, then similarity
    df["_pass"] = df["would_pass_gate"].astype(int)
    df = df.sort_values(["source_doc", "source_section", "_pass", "similarity"], ascending=[True, True, False, False])
    df = df.drop(columns=["_pass"])

    out_csv = OUT / f"isolated_{slug(concept)}_link_suggestions.csv"
    df.to_csv(out_csv, index=False)

    # Markdown summary
    out_md = OUT / f"isolated_{slug(concept)}_link_suggestions.md"
    lines: List[str] = []
    lines.append(f"# Link Suggestions for Isolated Sections — {concept}\n")
    lines.append(f"- Tagged sections (kept): {len(sec):,}\n")
    lines.append(f"- Isolated sections (0 semantic connections): {len(isolated):,}\n")
    lines.append(f"- Sources included in this report: {len(top_keys):,} (prioritized by best similarity)\n")
    lines.append(f"- Similarity threshold: {args.min_sim}\n")
    lines.append("\n---\n")

    for (src_doc, src_sec), g in df.groupby(["source_doc", "source_section"], sort=False):
        g2 = g.sort_values(["would_pass_gate", "similarity"], ascending=[False, False]).head(8)
        src_title = g2.iloc[0]["source_title"]
        src_h = g2.iloc[0]["source_h_path"]
        src_is_api = g2.iloc[0]["source_is_api"]
        lines.append(f"## {src_doc}\n")
        lines.append(f"- Section: {src_sec}\n")
        lines.append(f"- Type: {'API' if src_is_api else 'Conceptual'}\n")
        if src_title:
            lines.append(f"- Title: {src_title}\n")
        if src_h:
            lines.append(f"- Path: {src_h}\n")
        lines.append("\nSuggested links:\n")
        for _, row in g2.iterrows():
            tgt_doc = row["target_doc"]
            sim = row["similarity"]
            kind = row["pair_kind"]
            gates = row["gates"]
            pass_gate = row["would_pass_gate"]
            shared = row["shared_concepts"]
            lines.append(f"- {tgt_doc} — sim={sim} — {kind} — gate={'PASS' if pass_gate else 'weak'} ({gates})")
            if shared:
                lines.append(f"  - shared concepts: {shared}")
        lines.append("\n---\n")

    out_md.write_text("\n".join(lines), encoding="utf-8")

    print("\nWrote:")
    print(f" - {out_csv}")
    print(f" - {out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
