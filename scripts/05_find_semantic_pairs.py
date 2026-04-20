#!/usr/bin/env python
"""
05_find_semantic_pairs.py

Compute semantically similar SECTION pairs from conceptual and API corpora,
apply domain-aware gating (concept/platform/API/namespace overlap),
and write a unified candidate set for relationship classification (Phase 5).

Inputs
------
- outputs/sections_embeddings_conceptual.parquet
- outputs/sections_embeddings_api.parquet
- outputs/topics_inventory.parquet  (for xref link gate; optional)

Output
------
- outputs/semantic_pairs.parquet

Row schema (per kept pair)
--------------------------
- source_doc, source_section, source_is_api, source_concepts, source_platforms, source_apis
- target_doc, target_section, target_is_api, target_concepts, target_platforms, target_apis
- neighbor_type: one of {"cc","aa","ca","ac"}  (source→target direction)
- sim_score: float in [0,1]
- overlap_concepts: list[str]
- overlap_platforms: list[str]
- overlap_apis: list[str]
- namespace_overlap: bool
- gates_passed: list[str]   (names of gates that accepted the pair)
"""

from __future__ import annotations

import sys
import math
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Iterable, Set

import numpy as np
import pandas as pd
from tqdm import tqdm
from sklearn.neighbors import NearestNeighbors


# ------------------------------ Paths ------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR   = PROJECT_ROOT / "outputs"

F_CONCEPTUAL = OUTPUT_DIR / "sections_embeddings_conceptual.parquet"
F_API        = OUTPUT_DIR / "sections_embeddings_api.parquet"
F_OUT        = OUTPUT_DIR / "semantic_pairs.parquet"
F_TOPICS     = OUTPUT_DIR / "topics_inventory.parquet"


# ------------------------------ CLI ------------------------------
def parse_args():
    p = argparse.ArgumentParser(description="Find semantic section pairs with domain-aware gating.")
    # Top-K per category
    p.add_argument("--topk-cc", type=int, default=15, help="Top-K neighbors for conceptual→conceptual.")
    p.add_argument("--topk-aa", type=int, default=5,  help="Top-K neighbors for API→API.")
    p.add_argument("--topk-ca", type=int, default=10, help="Top-K neighbors for conceptual→API.")
    p.add_argument("--topk-ac", type=int, default=10, help="Top-K neighbors for API→conceptual.")

    # Similarity thresholds
    p.add_argument("--min-sim-cc", type=float, default=0.60, help="Min cosine similarity for C→C.")
    p.add_argument("--min-sim-aa", type=float, default=0.70, help="Min cosine similarity for A→A.")
    p.add_argument("--min-sim-cross", type=float, default=0.65, help="Min cosine similarity for cross pairs.")

    # Fallback if no overlap (still allow very high-sim content)
    p.add_argument("--cc-fallback-sim", type=float, default=0.75,
                   help="C→C: allow with no concept/platform overlap if sim ≥ this.")
    p.add_argument("--cross-fallback-sim", type=float, default=0.80,
                   help="Cross: allow with no overlap if sim ≥ this.")
    p.add_argument("--aa-fallback-sim", type=float, default=0.85,
                   help="A→A: allow with no namespace/platform overlap if sim ≥ this (fallback when apis column is empty).")

    # Ns prefix length for API namespace overlap
    p.add_argument("--ns-prefix-levels", type=int, default=3,
                   help="Compare first N namespace segments for API namespace overlap (e.g. DevExpress.ExpressApp).")

    # Xref link gate
    p.add_argument("--xref-min-sim", type=float, default=0.50,
                   help="Min cosine similarity for cross pairs accepted via explicit xref link gate.")
    p.add_argument("--no-xref-gate", action="store_true",
                   help="Disable the xref link gate (accept only overlap/similarity gates).")

    # Misc
    p.add_argument("--metric", type=str, default="cosine", choices=["cosine"],
                   help="Distance metric for NN search (cosine recommended).")
    p.add_argument("--verbose", action="store_true", help="Verbose logging.")
    return p.parse_args()


# ------------------------------ Helpers ------------------------------
def ensure_exists(path: Path, what: str):
    if not path.exists():
        print(f"❌ Missing {what}: {path}")
        sys.exit(1)

def to_np_matrix(emb_series: pd.Series) -> np.ndarray:
    # emb_series holds lists of floats; convert to 2D float32 matrix
    return np.vstack([np.asarray(v, dtype=np.float32) for v in emb_series.to_list()])

def ns_root(api: str, levels: int) -> str:
    """
    Get first N segments of a namespace-like symbol.
    Example:
      api = "DevExpress.ExpressApp.Security.SecurityStrategyComplex"
      levels=3  ->  "DevExpress.ExpressApp.Security"
    """
    if not api:
        return ""
    parts = api.split(".")
    if len(parts) < levels:
        return ".".join(parts)
    return ".".join(parts[:levels])

def namespace_overlap(apis1: Iterable[str], apis2: Iterable[str], levels: int) -> bool:
    roots1 = {ns_root(a, levels) for a in apis1 if a}
    roots2 = {ns_root(a, levels) for a in apis2 if a}
    roots1.discard("")
    roots2.discard("")
    return len(roots1.intersection(roots2)) > 0


def doc_id_ns_root(doc_id: str, levels: int) -> str:
    """Extract a namespace root from a doc_id path for API docs.

    API docs live under paths like:
      data/raw_md/apidoc/DevExpress.ExpressApp.Security/SecurityStrategyComplex
    The namespace segment is the second-to-last component before the class name.
    If the path has no recognisable namespace segment, returns the last path component.
    """
    parts = Path(doc_id).parts
    # Find the apidoc segment and take the next one as namespace
    for i, p in enumerate(parts):
        if p == "apidoc" and i + 1 < len(parts):
            ns = parts[i + 1]   # e.g. "DevExpress.ExpressApp.Security"
            return ns_root(ns, levels)
    # Fallback: use the last component (the class/file name itself)
    return parts[-1] if parts else ""


def doc_id_namespace_overlap(doc_id1: str, doc_id2: str, levels: int) -> bool:
    """Compare namespace roots derived from the doc_id paths for two API sections."""
    r1 = doc_id_ns_root(doc_id1, levels)
    r2 = doc_id_ns_root(doc_id2, levels)
    return bool(r1 and r2 and r1 == r2)

# ------------------------------ Xref index ------------------------------
def build_xref_index(topics_path: Path) -> Tuple[Dict[str, Set[str]], Dict[str, str]]:
    """
    Build two lookup tables from topics_inventory.parquet:
      doc_to_links : {doc_id -> set of internal_link UIDs (strings)}
      doc_to_uid   : {doc_id -> its own uid string}

    Used by gate_cross to check whether a conceptual article explicitly
    links (via xref:) to an API section's document.
    """
    if not topics_path.exists():
        print("⚠️  topics_inventory.parquet not found; xref gate disabled.")
        return {}, {}

    df = pd.read_parquet(topics_path, engine="pyarrow", columns=["doc_id", "uid", "internal_links"])

    doc_to_links: Dict[str, Set[str]] = {}
    doc_to_uid: Dict[str, str] = {}

    for row in df.itertuples(index=False):
        doc_id = row.doc_id
        uid    = row.uid
        links  = row.internal_links

        if uid and isinstance(uid, str):
            doc_to_uid[doc_id] = uid

        if links is not None:
            raw = links.tolist() if hasattr(links, "tolist") else list(links)
            doc_to_links[doc_id] = {str(lnk) for lnk in raw if lnk}

    return doc_to_links, doc_to_uid


def intersect(a: Iterable[str], b: Iterable[str]) -> List[str]:
    sa = {x for x in a if x}
    sb = {x for x in b if x}
    return sorted(sa.intersection(sb))

def nn_pairs(X: np.ndarray, topk: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Return (indices, sims) for each row in X against X (self NN),
    excluding the self neighbor at position 0.
    """
    if len(X) == 0:
        return np.empty((0,0), dtype=int), np.empty((0,0), dtype=float)
    # sklearn returns distances; for cosine, distance = 1 - cosine_sim
    k = min(len(X), topk + 1)  # +1 for self
    nn = NearestNeighbors(n_neighbors=k, metric="cosine").fit(X)
    dist, idx = nn.kneighbors(X)
    sim = 1.0 - dist
    # drop self neighbor (index 0) if present
    idx = idx[:, 1:]
    sim = sim[:, 1:]
    return idx, sim

def nn_pairs_cross(Xq: np.ndarray, Xk: np.ndarray, topk: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Return (indices, sims) for each row in Xq against Xk (cross-corpus).
    """
    if len(Xq) == 0 or len(Xk) == 0:
        return np.empty((0,0), dtype=int), np.empty((0,0), dtype=float)
    k = min(len(Xk), topk)
    nn = NearestNeighbors(n_neighbors=k, metric="cosine").fit(Xk)
    dist, idx = nn.kneighbors(Xq)
    sim = 1.0 - dist
    return idx, sim


# ------------------------------ Gates ------------------------------
def gate_cc(s_row, t_row, sim: float, args) -> Tuple[bool, List[str]]:
    """
    Conceptual→Conceptual
    - require (concept overlap OR platform overlap) OR sim ≥ cc_fallback_sim
    - sim must be ≥ min_sim_cc
    """
    gates = []
    if sim < args.min_sim_cc:
        return False, gates

    overlap_concepts = intersect(s_row["concepts"], t_row["concepts"])
    overlap_platforms = intersect(s_row["platforms"], t_row["platforms"])
    
    # Check for concept or platform overlap
    if overlap_concepts or overlap_platforms:
        if overlap_concepts:
            gates.append("concept_overlap")
        if overlap_platforms:
            gates.append("platform_overlap")
        return True, gates
    
    # Fallback for high similarity without overlap
    if sim >= args.cc_fallback_sim:
        gates.append("high_similarity_fallback")
        return True, gates
    
    return False, gates


def gate_aa(s_row, t_row, sim: float, args) -> Tuple[bool, List[str]]:
    """
    API→API
    - Primary: namespace overlap (from apis column) OR platform overlap
    - Secondary: namespace overlap derived from doc_id path (when apis column is empty,
      e.g. config/patterns.yml does not exist)
    - Fallback: sim ≥ aa_fallback_sim for any high-similarity API pair
    - sim must be ≥ min_sim_aa
    """
    gates = []
    if sim < args.min_sim_aa:
        return False, gates

    ns_overlap = namespace_overlap(s_row["apis"], t_row["apis"], args.ns_prefix_levels)
    overlap_platforms = intersect(s_row["platforms"], t_row["platforms"])

    if ns_overlap:
        gates.append("namespace_overlap")
    if overlap_platforms:
        gates.append("platform_overlap")

    if ns_overlap or overlap_platforms:
        return True, gates

    # Secondary: namespace derived from doc_id path (self-contained, no patterns.yml needed)
    if doc_id_namespace_overlap(s_row["doc_id"], t_row["doc_id"], args.ns_prefix_levels):
        gates.append("doc_id_namespace_overlap")
        return True, gates

    # Fallback: very high similarity API sections are almost certainly related
    if sim >= args.aa_fallback_sim:
        gates.append("high_similarity_fallback")
        return True, gates

    return False, gates


def gate_cross(
    s_row,
    t_row,
    sim: float,
    args,
    doc_to_links: Dict[str, Set[str]] = None,
    doc_to_uid:   Dict[str, str]      = None,
) -> Tuple[bool, List[str]]:
    """
    Cross-corpus (C→A or A→C)
    - require (concept/API/namespace overlap) OR (platform overlap) OR sim ≥ cross_fallback_sim
      OR (explicit xref from conceptual doc to API doc and sim ≥ xref_min_sim)
    - sim must be ≥ min_sim_cross  (bypassed for the xref gate, which uses xref_min_sim instead)
    """
    gates = []

    # ----------------------------------------------------------------
    # Xref link gate — runs BEFORE the similarity floor so that explicit
    # editorial links are never discarded purely on embedding distance.
    # ----------------------------------------------------------------
    if not args.no_xref_gate and doc_to_links is not None and doc_to_uid is not None:
        if sim >= args.xref_min_sim:
            s_doc = s_row["doc_id"]
            t_doc = t_row["doc_id"]
            # Check both directions: source links to target, or target links to source
            t_uid = doc_to_uid.get(t_doc, "")
            s_uid = doc_to_uid.get(s_doc, "")
            s_links = doc_to_links.get(s_doc, set())
            t_links = doc_to_links.get(t_doc, set())
            if (t_uid and t_uid in s_links) or (s_uid and s_uid in t_links):
                gates.append("xref_link")
                return True, gates

    if sim < args.min_sim_cross:
        return False, gates

    overlap_concepts = intersect(s_row["concepts"], t_row["concepts"])
    overlap_platforms = intersect(s_row["platforms"], t_row["platforms"])
    overlap_apis = intersect(s_row["apis"], t_row["apis"])
    ns_overlap = namespace_overlap(s_row["apis"], t_row["apis"], args.ns_prefix_levels)

    if overlap_concepts:
        gates.append("concept_overlap")
    if overlap_platforms:
        gates.append("platform_overlap")
    if overlap_apis:
        gates.append("api_overlap")
    if ns_overlap:
        gates.append("namespace_overlap")

    if overlap_concepts or overlap_platforms or overlap_apis or ns_overlap:
        return True, gates

    # High similarity fallback
    if sim >= args.cross_fallback_sim:
        gates.append("high_similarity_fallback")
        return True, gates

    return False, gates


# ------------------------------ Main ------------------------------
def main():
    args = parse_args()
    
    # Load inputs
    ensure_exists(F_CONCEPTUAL, "conceptual embeddings")
    ensure_exists(F_API, "API embeddings")

    print("📚 Loading embeddings...")
    df_c = pd.read_parquet(F_CONCEPTUAL, engine="pyarrow")
    df_a = pd.read_parquet(F_API, engine="pyarrow")

    print(f"  Conceptual: {len(df_c):,} sections")
    print(f"  API:        {len(df_a):,} sections")

    # Build xref index
    if not args.no_xref_gate:
        print("📎 Building xref index from topics_inventory...")
        doc_to_links, doc_to_uid = build_xref_index(F_TOPICS)
        xref_linked_pairs = sum(1 for links in doc_to_links.values() for _ in links)
        print(f"   {len(doc_to_links):,} docs with links, {xref_linked_pairs:,} total xref edges")
    else:
        doc_to_links, doc_to_uid = {}, {}
        print("⚠️  Xref gate disabled via --no-xref-gate")
    
    # Convert embeddings to matrices
    X_c = to_np_matrix(df_c["embedding"])
    X_a = to_np_matrix(df_a["embedding"])
    
    pairs = []
    
    # C→C pairs
    if len(X_c) > 0:
        print(f"\n🔍 Finding C→C neighbors (top-{args.topk_cc})...")
        idx_cc, sim_cc = nn_pairs(X_c, args.topk_cc)
        for i in tqdm(range(len(df_c)), desc="C→C"):
            s_row = df_c.iloc[i]
            for j_rank in range(idx_cc.shape[1]):
                j = idx_cc[i, j_rank]
                sim = sim_cc[i, j_rank]
                t_row = df_c.iloc[j]
                
                passed, gates = gate_cc(s_row, t_row, sim, args)
                if not passed:
                    continue
                
                pairs.append({
                    "source_doc": s_row["doc_id"],
                    "source_section": s_row["section_id"],
                    "source_is_api": False,
                    "source_concepts": s_row["concepts"],
                    "source_platforms": s_row["platforms"],
                    "source_apis": s_row["apis"],
                    "target_doc": t_row["doc_id"],
                    "target_section": t_row["section_id"],
                    "target_is_api": False,
                    "target_concepts": t_row["concepts"],
                    "target_platforms": t_row["platforms"],
                    "target_apis": t_row["apis"],
                    "neighbor_type": "cc",
                    "sim_score": float(sim),
                    "overlap_concepts": intersect(s_row["concepts"], t_row["concepts"]),
                    "overlap_platforms": intersect(s_row["platforms"], t_row["platforms"]),
                    "overlap_apis": [],
                    "namespace_overlap": False,
                    "gates_passed": gates,
                })
    
    # A→A pairs
    if len(X_a) > 0:
        print(f"\n🔍 Finding A→A neighbors (top-{args.topk_aa})...")
        idx_aa, sim_aa = nn_pairs(X_a, args.topk_aa)
        for i in tqdm(range(len(df_a)), desc="A→A"):
            s_row = df_a.iloc[i]
            for j_rank in range(idx_aa.shape[1]):
                j = idx_aa[i, j_rank]
                sim = sim_aa[i, j_rank]
                t_row = df_a.iloc[j]
                
                passed, gates = gate_aa(s_row, t_row, sim, args)
                if not passed:
                    continue
                
                ns_overlap = namespace_overlap(s_row["apis"], t_row["apis"], args.ns_prefix_levels)
                
                pairs.append({
                    "source_doc": s_row["doc_id"],
                    "source_section": s_row["section_id"],
                    "source_is_api": True,
                    "source_concepts": s_row["concepts"],
                    "source_platforms": s_row["platforms"],
                    "source_apis": s_row["apis"],
                    "target_doc": t_row["doc_id"],
                    "target_section": t_row["section_id"],
                    "target_is_api": True,
                    "target_concepts": t_row["concepts"],
                    "target_platforms": t_row["platforms"],
                    "target_apis": t_row["apis"],
                    "neighbor_type": "aa",
                    "sim_score": float(sim),
                    "overlap_concepts": intersect(s_row["concepts"], t_row["concepts"]),
                    "overlap_platforms": intersect(s_row["platforms"], t_row["platforms"]),
                    "overlap_apis": intersect(s_row["apis"], t_row["apis"]),
                    "namespace_overlap": ns_overlap,
                    "gates_passed": gates,
                })
    
    # C→A pairs
    if len(X_c) > 0 and len(X_a) > 0:
        print(f"\n🔍 Finding C→A neighbors (top-{args.topk_ca})...")
        idx_ca, sim_ca = nn_pairs_cross(X_c, X_a, args.topk_ca)
        for i in tqdm(range(len(df_c)), desc="C→A"):
            s_row = df_c.iloc[i]
            for j_rank in range(idx_ca.shape[1]):
                j = idx_ca[i, j_rank]
                sim = sim_ca[i, j_rank]
                t_row = df_a.iloc[j]
                
                passed, gates = gate_cross(s_row, t_row, sim, args, doc_to_links, doc_to_uid)
                if not passed:
                    continue

                ns_overlap = namespace_overlap(s_row["apis"], t_row["apis"], args.ns_prefix_levels)

                pairs.append({
                    "source_doc": s_row["doc_id"],
                    "source_section": s_row["section_id"],
                    "source_is_api": False,
                    "source_concepts": s_row["concepts"],
                    "source_platforms": s_row["platforms"],
                    "source_apis": s_row["apis"],
                    "target_doc": t_row["doc_id"],
                    "target_section": t_row["section_id"],
                    "target_is_api": True,
                    "target_concepts": t_row["concepts"],
                    "target_platforms": t_row["platforms"],
                    "target_apis": t_row["apis"],
                    "neighbor_type": "ca",
                    "sim_score": float(sim),
                    "overlap_concepts": intersect(s_row["concepts"], t_row["concepts"]),
                    "overlap_platforms": intersect(s_row["platforms"], t_row["platforms"]),
                    "overlap_apis": intersect(s_row["apis"], t_row["apis"]),
                    "namespace_overlap": ns_overlap,
                    "gates_passed": gates,
                })
    
    # A→C pairs
    if len(X_a) > 0 and len(X_c) > 0:
        print(f"\n🔍 Finding A→C neighbors (top-{args.topk_ac})...")
        idx_ac, sim_ac = nn_pairs_cross(X_a, X_c, args.topk_ac)
        for i in tqdm(range(len(df_a)), desc="A→C"):
            s_row = df_a.iloc[i]
            for j_rank in range(idx_ac.shape[1]):
                j = idx_ac[i, j_rank]
                sim = sim_ac[i, j_rank]
                t_row = df_c.iloc[j]
                
                passed, gates = gate_cross(s_row, t_row, sim, args, doc_to_links, doc_to_uid)
                if not passed:
                    continue

                ns_overlap = namespace_overlap(s_row["apis"], t_row["apis"], args.ns_prefix_levels)

                pairs.append({
                    "source_doc": s_row["doc_id"],
                    "source_section": s_row["section_id"],
                    "source_is_api": True,
                    "source_concepts": s_row["concepts"],
                    "source_platforms": s_row["platforms"],
                    "source_apis": s_row["apis"],
                    "target_doc": t_row["doc_id"],
                    "target_section": t_row["section_id"],
                    "target_is_api": False,
                    "target_concepts": t_row["concepts"],
                    "target_platforms": t_row["platforms"],
                    "target_apis": t_row["apis"],
                    "neighbor_type": "ac",
                    "sim_score": float(sim),
                    "overlap_concepts": intersect(s_row["concepts"], t_row["concepts"]),
                    "overlap_platforms": intersect(s_row["platforms"], t_row["platforms"]),
                    "overlap_apis": intersect(s_row["apis"], t_row["apis"]),
                    "namespace_overlap": ns_overlap,
                    "gates_passed": gates,
                })
    
    # Create output dataframe
    print(f"\n📊 Total pairs found: {len(pairs):,}")
    if len(pairs) == 0:
        print("⚠️  No pairs passed gates. Consider adjusting thresholds.")
        sys.exit(0)
    
    df_out = pd.DataFrame(pairs)
    
    # Stats
    print("\n📈 Breakdown by type:")
    print(df_out["neighbor_type"].value_counts())
    print("\n📈 Average similarity by type:")
    print(df_out.groupby("neighbor_type")["sim_score"].mean().round(3))
    
    # Save
    print(f"\n💾 Writing → {F_OUT}")
    df_out.to_parquet(F_OUT, engine="pyarrow", index=False)
    print("✅ Phase 5 complete!")


if __name__ == "__main__":
    main()
