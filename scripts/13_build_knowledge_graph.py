#!/usr/bin/env python3
"""
Phase 13: Build Unified Knowledge Graph

Goal
----
Create a single, explainable knowledge-graph artifact that merges:
- Document/section structure (Phase 1)
- Explicit cross-links (Phase 2)
- Concept/API/platform tagging (Phase 3)
- Semantic similarity edges (Phase 5)
- Optional typed relationships (Phase 6 output if present)
- API entity inventory (Phase 11)
- API→Concept mappings (Phase 12)

Output
------
- outputs/knowledge_graph.json

Graph Model (JSON)
------------------
{
  "metadata": {...},
  "nodes": [{"id": str, "type": str, ...}],
  "edges": [{"source": str, "target": str, "type": str, ...}]
}

Notes
-----
- The graph is designed for downstream tooling (MCP adapters, dashboards, future UI).
- By default, the graph does NOT embed raw section text (to keep size reasonable).
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple

import pandas as pd

# Add parent directory to path for validation imports
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils.pipeline_validators import (
    PipelineValidator, ValidationReport, ValidationResult,
    save_validation_report, load_validation_thresholds,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = PROJECT_ROOT / "outputs"

F_TOPICS = OUTPUTS / "topics_inventory.parquet"
F_CONCEPTS = OUTPUTS / "doc_concepts.parquet"
F_EXPLICIT = OUTPUTS / "explicit_graph.parquet"
F_EXPLICIT_UNRESOLVED = OUTPUTS / "explicit_unresolved_uid_edges.parquet"
F_PAIRS = OUTPUTS / "semantic_pairs.parquet"

# Optional/extra
F_CLASSIFIED = OUTPUTS / "classified_pairs_corrected.parquet"
F_API_ENTITIES = OUTPUTS / "api_entities.parquet"
F_API_IMPL = OUTPUTS / "api_implements_concept.parquet"
F_DOC_META = OUTPUTS / "document_metadata.parquet"

F_OUT = OUTPUTS / "knowledge_graph.json"


def _safe_list(val: Any) -> List[Any]:
    """Coerce parquet list-like columns (pyarrow/numpy) into plain Python lists."""
    if val is None:
        return []
    if isinstance(val, float) and pd.isna(val):
        return []
    if isinstance(val, (list, tuple, set, frozenset)):
        return list(val)
    if isinstance(val, str):
        return [val] if val else []

    tolist = getattr(val, "tolist", None)
    if callable(tolist):
        try:
            res = tolist()
            if isinstance(res, list):
                return res
            return list(res)  # type: ignore[arg-type]
        except Exception:
            pass

    try:
        return list(val)  # type: ignore[arg-type]
    except Exception:
        return []


def node_id(kind: str, value: str) -> str:
    return f"{kind}:{value}"


def section_key(doc_id: str, section_id: str) -> str:
    return f"{doc_id}#{section_id}"


@dataclass(frozen=True)
class EdgeKey:
    source: str
    target: str
    etype: str


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Build unified knowledge graph JSON artifact")

    p.add_argument("--output", type=str, default=str(F_OUT), help="Output JSON path")

    # Size controls
    p.add_argument("--include-section-nodes", type=lambda x: str(x).lower() in {"1", "true", "t", "yes", "y"}, default=True)
    p.add_argument("--include-tag-edges", type=lambda x: str(x).lower() in {"1", "true", "t", "yes", "y"}, default=True,
                   help="Include edges section→concept/platform/api.")
    p.add_argument("--include-semantic-edges", type=lambda x: str(x).lower() in {"1", "true", "t", "yes", "y"}, default=True)
    p.add_argument("--max-semantic-edges", type=int, default=0,
                   help="If >0, cap the number of semantic edges written (useful for quick runs).")

    # Typed relationship preference
    p.add_argument("--prefer-classified", type=lambda x: str(x).lower() in {"1", "true", "t", "yes", "y"}, default=True,
                   help="If classified pairs exist, emit typed relationship edges instead of raw similarity edges.")

    # Validation
    p.add_argument("--skip-validation", action="store_true", help="Skip validation checks")
    p.add_argument("--validate-quality", action="store_true", help="Run deeper quality checks")
    p.add_argument("--save-report", action="store_true", help="Save validation report JSON")

    return p.parse_args()


def load_inputs() -> Dict[str, Any]:
    """Load inputs needed to build the graph. Missing optional inputs are tolerated."""
    inputs: Dict[str, Any] = {}

    if not F_TOPICS.exists():
        raise FileNotFoundError(f"Missing required input: {F_TOPICS}")
    if not F_CONCEPTS.exists():
        raise FileNotFoundError(f"Missing required input: {F_CONCEPTS}")

    inputs["topics"] = pd.read_parquet(F_TOPICS)
    inputs["doc_concepts"] = pd.read_parquet(F_CONCEPTS)

    inputs["explicit"] = pd.read_parquet(F_EXPLICIT) if F_EXPLICIT.exists() else pd.DataFrame()
    inputs["explicit_unresolved"] = pd.read_parquet(F_EXPLICIT_UNRESOLVED) if F_EXPLICIT_UNRESOLVED.exists() else pd.DataFrame()

    inputs["pairs"] = pd.read_parquet(F_PAIRS) if F_PAIRS.exists() else pd.DataFrame()
    inputs["classified"] = pd.read_parquet(F_CLASSIFIED) if F_CLASSIFIED.exists() else pd.DataFrame()

    inputs["api_entities"] = pd.read_parquet(F_API_ENTITIES) if F_API_ENTITIES.exists() else pd.DataFrame()
    inputs["api_implements"] = pd.read_parquet(F_API_IMPL) if F_API_IMPL.exists() else pd.DataFrame()

    inputs["document_metadata"] = pd.read_parquet(F_DOC_META) if F_DOC_META.exists() else pd.DataFrame()

    return inputs


def build_nodes(inputs: Dict[str, Any], include_section_nodes: bool) -> List[Dict[str, Any]]:
    topics = inputs["topics"]
    doc_concepts = inputs["doc_concepts"]
    api_entities = inputs["api_entities"]
    explicit_unresolved = inputs["explicit_unresolved"]

    nodes: List[Dict[str, Any]] = []
    seen: Set[str] = set()

    # Language-tab headings that Phase 1 sometimes captures as document titles
    # for API pages that only contain a code example. Match by prefix to catch
    # variants like "C# (EF Core)", "C# (Integrated security)", etc.
    _LANG_TAB_PREFIXES = ("C#", "VB.NET", "C++ / CLI", "F#", "JavaScript", "TypeScript")

    # Document nodes
    for _, row in topics.iterrows():
        doc_id = str(row.get("doc_id"))
        title = row.get("title")
        uid = row.get("uid")
        doc_type = row.get("doc_type")

        # Fall back to path stem when the title is a language-tab heading
        if not title or str(title).strip().startswith(_LANG_TAB_PREFIXES):
            title = doc_id.rstrip("/").split("/")[-1]

        nid = node_id("doc", doc_id)
        if nid in seen:
            continue
        seen.add(nid)
        nodes.append({
            "id": nid,
            "type": "document",
            "doc_id": doc_id,
            "title": title,
            "uid": uid,
            "doc_type": doc_type,
        })

    # Section nodes (only for kept sections by default)
    if include_section_nodes:
        kept = doc_concepts[doc_concepts["kept"] == True].copy() if "kept" in doc_concepts.columns else doc_concepts.copy()
        for _, row in kept.iterrows():
            doc_id = str(row.get("doc_id"))
            section_id = str(row.get("section_id"))
            skey = section_key(doc_id, section_id)

            nid = node_id("sec", skey)
            if nid in seen:
                continue
            seen.add(nid)

            nodes.append({
                "id": nid,
                "type": "section",
                "doc_id": doc_id,
                "section_id": section_id,
                "h_path": _safe_list(row.get("h_path")),
                "is_api": bool(row.get("is_api", False)),
            })

    # Concept nodes
    all_concepts: Set[str] = set()
    if "concepts" in doc_concepts.columns:
        for val in doc_concepts["concepts"]:
            all_concepts.update(str(c) for c in _safe_list(val) if c)

    for concept in sorted(all_concepts):
        nid = node_id("concept", concept)
        if nid in seen:
            continue
        seen.add(nid)
        nodes.append({"id": nid, "type": "concept", "name": concept})

    # Platform nodes
    all_platforms: Set[str] = set()
    if "platforms" in doc_concepts.columns:
        for val in doc_concepts["platforms"]:
            all_platforms.update(str(p) for p in _safe_list(val) if p)

    for platform in sorted(all_platforms):
        nid = node_id("platform", platform)
        if nid in seen:
            continue
        seen.add(nid)
        nodes.append({"id": nid, "type": "platform", "name": platform})

    # API nodes (always include the UNION of api_entities + any raw identifiers in doc_concepts.apis)
    api_ids_from_entities: Set[str] = set()
    if not api_entities.empty and "api_id" in api_entities.columns:
        for _, row in api_entities.iterrows():
            api_id = str(row.get("api_id"))
            if api_id:
                api_ids_from_entities.add(api_id)

            # Emit enriched nodes from api_entities
            if not api_id:
                continue
            nid = node_id("api", api_id)
            if nid in seen:
                continue
            seen.add(nid)
            nodes.append({
                "id": nid,
                "type": "api",
                "api_id": api_id,
                "api_name": row.get("api_name"),
                "namespace": row.get("namespace"),
                "api_type": row.get("api_type"),
            })

    api_ids_from_concepts: Set[str] = set()
    if "apis" in doc_concepts.columns:
        for val in doc_concepts["apis"]:
            api_ids_from_concepts.update(str(a) for a in _safe_list(val) if a)

    for api_id in sorted(api_ids_from_concepts - api_ids_from_entities):
        nid = node_id("api", api_id)
        if nid in seen:
            continue
        seen.add(nid)
        nodes.append({"id": nid, "type": "api", "api_id": api_id})

    # Unresolved UID nodes (from explicit graph)
    if explicit_unresolved is not None and not explicit_unresolved.empty and "target_uid" in explicit_unresolved.columns:
        uids = set(str(u) for u in explicit_unresolved["target_uid"].dropna().astype(str).tolist())
        for uid in sorted(uids):
            nid = node_id("uid", uid)
            if nid in seen:
                continue
            seen.add(nid)
            nodes.append({"id": nid, "type": "uid", "uid": uid})

    return nodes


def build_edges(inputs: Dict[str, Any], *, include_tag_edges: bool, include_semantic_edges: bool,
               prefer_classified: bool, max_semantic_edges: int) -> List[Dict[str, Any]]:
    topics = inputs["topics"]
    doc_concepts = inputs["doc_concepts"]
    explicit = inputs["explicit"]
    explicit_unresolved = inputs["explicit_unresolved"]
    pairs = inputs["pairs"]
    classified = inputs["classified"]
    api_implements = inputs["api_implements"]

    edges: List[Dict[str, Any]] = []
    seen: Set[EdgeKey] = set()

    def add_edge(source: str, target: str, etype: str, **attrs):
        ek = EdgeKey(source=source, target=target, etype=etype)
        if ek in seen:
            return
        seen.add(ek)
        rec = {"source": source, "target": target, "type": etype}
        rec.update(attrs)
        edges.append(rec)

    # Document contains section
    kept = doc_concepts[doc_concepts["kept"] == True].copy() if "kept" in doc_concepts.columns else doc_concepts.copy()
    for _, row in kept.iterrows():
        doc_id = str(row.get("doc_id"))
        section_id = str(row.get("section_id"))
        add_edge(
            node_id("doc", doc_id),
            node_id("sec", section_key(doc_id, section_id)),
            "contains",
        )

    # Explicit links between docs (internal)
    if not explicit.empty and {"source_doc", "target_doc"}.issubset(explicit.columns):
        for _, row in explicit.iterrows():
            sdoc = str(row.get("source_doc"))
            tdoc = str(row.get("target_doc"))
            add_edge(
                node_id("doc", sdoc),
                node_id("doc", tdoc),
                "links_to",
                count=int(row.get("count", 1)) if pd.notna(row.get("count", 1)) else 1,
            )

    # Unresolved xref UID edges: doc -> uid bucket
    if not explicit_unresolved.empty and {"source_doc", "target_uid"}.issubset(explicit_unresolved.columns):
        for _, row in explicit_unresolved.iterrows():
            sdoc = str(row.get("source_doc"))
            uid = str(row.get("target_uid"))
            bucket = row.get("bucket")
            url = row.get("target_url")
            add_edge(
                node_id("doc", sdoc),
                node_id("uid", uid),
                "xref_unresolved",
                bucket=bucket,
                target_url=url,
            )

    # Tagging edges: section -> concept/platform/api
    if include_tag_edges:
        for _, row in kept.iterrows():
            doc_id = str(row.get("doc_id"))
            section_id = str(row.get("section_id"))
            sid = node_id("sec", section_key(doc_id, section_id))

            for concept in _safe_list(row.get("concepts")):
                if concept:
                    add_edge(sid, node_id("concept", str(concept)), "tagged_with")

            for platform in _safe_list(row.get("platforms")):
                if platform:
                    add_edge(sid, node_id("platform", str(platform)), "scoped_to")

            for api in _safe_list(row.get("apis")):
                if api:
                    add_edge(sid, node_id("api", str(api)), "mentions_api")

    # API implements concept edges (Phase 12)
    if not api_implements.empty and {"api_id", "concept_name"}.issubset(api_implements.columns):
        for _, row in api_implements.iterrows():
            api_id = str(row.get("api_id"))
            concept = str(row.get("concept_name"))
            conf = row.get("confidence")
            mapping_src = str(row.get("source"))
            add_edge(
                node_id("api", api_id),
                node_id("concept", concept),
                "implements_concept",
                confidence=float(conf) if conf is not None and pd.notna(conf) else None,
                mapping_source=mapping_src,
            )

    # Semantic / typed relationship edges between sections
    if include_semantic_edges:
        use_classified = prefer_classified and (classified is not None) and (not classified.empty)

        # If classified data exists, emit typed edges FIRST (do not exclude raw semantic edges).
        if use_classified and {"source_doc", "source_section", "target_doc", "target_section", "relationship_type"}.issubset(classified.columns):
            dfc = classified
            if max_semantic_edges and max_semantic_edges > 0:
                dfc = dfc.head(max_semantic_edges)

            for _, row in dfc.iterrows():
                sdoc = str(row.get("source_doc"))
                ssec = str(row.get("source_section"))
                tdoc = str(row.get("target_doc"))
                tsec = str(row.get("target_section"))
                rtype = str(row.get("relationship_type"))

                add_edge(
                    node_id("sec", section_key(sdoc, ssec)),
                    node_id("sec", section_key(tdoc, tsec)),
                    f"rel:{rtype}",
                    confidence=float(row.get("relationship_confidence")) if pd.notna(row.get("relationship_confidence")) else None,
                    bidirectional=bool(row.get("relationship_bidirectional", False)) if "relationship_bidirectional" in dfc.columns else False,
                    neighbor_type=row.get("neighbor_type"),
                    sim_score=float(row.get("sim_score")) if pd.notna(row.get("sim_score")) else None,
                )

        # Always emit raw semantic similarity edges if semantic_pairs are available.
        if pairs is not None and (not pairs.empty) and {"source_doc", "source_section", "target_doc", "target_section", "sim_score"}.issubset(pairs.columns):
            dfp = pairs
            if max_semantic_edges and max_semantic_edges > 0:
                dfp = dfp.head(max_semantic_edges)

            for _, row in dfp.iterrows():
                sdoc = str(row.get("source_doc"))
                ssec = str(row.get("source_section"))
                tdoc = str(row.get("target_doc"))
                tsec = str(row.get("target_section"))

                add_edge(
                    node_id("sec", section_key(sdoc, ssec)),
                    node_id("sec", section_key(tdoc, tsec)),
                    "semantic_similar",
                    neighbor_type=row.get("neighbor_type"),
                    sim_score=float(row.get("sim_score")) if pd.notna(row.get("sim_score")) else None,
                    gates_passed=_safe_list(row.get("gates_passed")),
                    overlap_concepts=_safe_list(row.get("overlap_concepts")),
                )

    return edges


def validate_graph(graph: Dict[str, Any], inputs: Dict[str, Any], run_quality_checks: bool = False) -> ValidationReport:
    """Basic validation for the knowledge graph artifact."""

    thresholds_path = PROJECT_ROOT / "config" / "validation_thresholds.yml"
    validator = PipelineValidator(thresholds_path)
    report = ValidationReport(phase_name="Build Knowledge Graph", phase_number=13)

    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])

    # Schema checks
    required_top = ["metadata", "nodes", "edges"]
    missing_top = [k for k in required_top if k not in graph]
    report.add_result(ValidationResult(
        check_name="Graph top-level keys",
        passed=len(missing_top) == 0,
        message="All required top-level keys present" if not missing_top else f"Missing keys: {missing_top}",
        severity="error" if missing_top else "info",
    ))

    # Node uniqueness
    node_ids = [n.get("id") for n in nodes]
    unique_node_ids = set(node_ids)
    report.add_result(ValidationResult(
        check_name="Unique node ids",
        passed=len(unique_node_ids) == len(node_ids),
        message=f"{len(unique_node_ids):,} unique ids / {len(node_ids):,} nodes",
        severity="error" if len(unique_node_ids) != len(node_ids) else "info",
        details={"duplicates": int(len(node_ids) - len(unique_node_ids))} if len(unique_node_ids) != len(node_ids) else None,
    ))

    # Edge endpoint existence
    missing_endpoints = 0
    for e in edges[:50000]:  # cap validation work
        if e.get("source") not in unique_node_ids or e.get("target") not in unique_node_ids:
            missing_endpoints += 1
    report.add_result(ValidationResult(
        check_name="Edge endpoints exist",
        passed=missing_endpoints == 0,
        message="All checked edges reference existing nodes" if missing_endpoints == 0 else f"{missing_endpoints} edges reference missing nodes (sampled)",
        severity="warning" if missing_endpoints > 0 else "info",
    ))

    # Threshold-based checks (if configured)
    thresholds = validator.thresholds.get("phase13_knowledge_graph", {}) if validator.thresholds else {}
    min_nodes = thresholds.get("min_nodes")
    min_edges = thresholds.get("min_edges")

    if min_nodes is not None:
        report.add_result(ValidationResult(
            check_name="Min nodes",
            passed=len(nodes) >= int(min_nodes),
            message=f"nodes={len(nodes):,} (min={min_nodes})",
            severity="error" if len(nodes) < int(min_nodes) else "info",
        ))

    if min_edges is not None:
        report.add_result(ValidationResult(
            check_name="Min edges",
            passed=len(edges) >= int(min_edges),
            message=f"edges={len(edges):,} (min={min_edges})",
            severity="error" if len(edges) < int(min_edges) else "info",
        ))

    if run_quality_checks:
        # sanity: if semantic pairs exist, ensure at least some semantic edges are present
        pairs = inputs.get("pairs")
        has_pairs = pairs is not None and hasattr(pairs, "empty") and not pairs.empty
        if has_pairs:
            semantic_edge_count = sum(1 for e in edges if e.get("type") in {"semantic_similar"} or str(e.get("type", "")).startswith("rel:"))
            report.add_result(ValidationResult(
                check_name="Semantic edges present",
                passed=semantic_edge_count > 0,
                message=f"semantic_edges={semantic_edge_count:,}",
                severity="error" if semantic_edge_count == 0 else "info",
            ))

    return report


def main() -> None:
    args = parse_args()

    print("📚 Loading inputs...")
    inputs = load_inputs()

    print("🧠 Building nodes...")
    nodes = build_nodes(inputs, include_section_nodes=args.include_section_nodes)
    print(f"  Nodes: {len(nodes):,}")

    print("🕸️  Building edges...")
    edges = build_edges(
        inputs,
        include_tag_edges=args.include_tag_edges,
        include_semantic_edges=args.include_semantic_edges,
        prefer_classified=args.prefer_classified,
        max_semantic_edges=args.max_semantic_edges,
    )
    print(f"  Edges: {len(edges):,}")

    graph = {
        "metadata": {
            "generated_at": datetime.now().isoformat(),
            "project": "xaf-doc-analysis",
            "builder": "scripts/13_build_knowledge_graph.py",
            "sources": {
                "topics_inventory": str(F_TOPICS.name),
                "doc_concepts": str(F_CONCEPTS.name),
                "explicit_graph": str(F_EXPLICIT.name) if F_EXPLICIT.exists() else None,
                "semantic_pairs": str(F_PAIRS.name) if F_PAIRS.exists() else None,
                "classified_pairs": str(F_CLASSIFIED.name) if F_CLASSIFIED.exists() else None,
                "api_entities": str(F_API_ENTITIES.name) if F_API_ENTITIES.exists() else None,
                "api_implements_concept": str(F_API_IMPL.name) if F_API_IMPL.exists() else None,
            },
            "counts": {
                "nodes": len(nodes),
                "edges": len(edges),
            },
            "options": {
                "include_section_nodes": args.include_section_nodes,
                "include_tag_edges": args.include_tag_edges,
                "include_semantic_edges": args.include_semantic_edges,
                "prefer_classified": args.prefer_classified,
                "max_semantic_edges": args.max_semantic_edges,
            },
        },
        "nodes": nodes,
        "edges": edges,
    }

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    print(f"💾 Writing {out_path} ...")
    out_path.write_text(json.dumps(graph, ensure_ascii=False), encoding="utf-8")

    if not args.skip_validation:
        print("\n🔍 Validating knowledge graph...")
        report = validate_graph(graph, inputs, run_quality_checks=args.validate_quality)
        report.print_summary()
        if args.save_report:
            save_validation_report(report, output_path=OUTPUTS / "validation_phase13.json")

        if not report.passed:
            raise SystemExit(1)

    print("✅ Knowledge graph build complete")


if __name__ == "__main__":
    main()
