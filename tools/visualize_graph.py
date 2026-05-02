"""
tools/visualize_graph.py

Generate a rich self-contained interactive HTML visualisation of the XAF
knowledge graph.  Opens in any browser — no server needed.

Modes (selectable in the browser):
  Concept Map      — 100 concept nodes connected by section co-occurrence.
                     Click a concept to expand its top documents.
  Relationship Map — Document-to-document typed edges from Phase 6/7
                     (uses / explains / requires / extends / contrasts_with /
                      applies_to / related_to).  Toggle types on/off.

Controls:
  Search box       — highlight/filter nodes by name
  Details sidebar  — click any node for full info
  Edge-type filter — checkboxes per relationship type
  Min links slider — co-occurrence threshold (Concept Map)
  Fit / Physics    — standard vis-network controls

Usage:
  python tools/visualize_graph.py
  python tools/visualize_graph.py --min-cooc 5 --output outputs/my_graph.html
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
KG_PATH = PROJECT_ROOT / "outputs" / "knowledge_graph.json"
OUT_DIR = PROJECT_ROOT / "outputs"


# ── vis-network embedding ────────────────────────────────────────────────────

def _vis_js() -> str:
    """Return an inline <script> tag with vis-network JS from the pyvis package."""
    try:
        import pyvis
        for candidate in sorted(Path(pyvis.__file__).parent.glob("**/vis-network.min.js")):
            return f"<script>\n{candidate.read_text(encoding='utf-8')}\n</script>"
    except Exception:
        pass
    # Fallback to CDN
    return '<script src="https://unpkg.com/vis-network@9.1.2/dist/vis-network.min.js"></script>'


# ── Data preparation ─────────────────────────────────────────────────────────

def _sec_to_doc(sec_id: str) -> str:
    path = sec_id.removeprefix("sec:")
    if "#" in path:
        path = path.split("#")[0]
    return f"doc:{path}"


def prepare_data(kg: dict, min_cooc: int = 3) -> dict:
    """Build all graph data needed by the browser app."""

    nodes_by_id: dict[str, dict] = {n["id"]: n for n in kg["nodes"]}

    # ── Concept section/doc counts ────────────────────────────────────────
    concept_sections: Counter = Counter()
    concept_doc_set: dict[str, set] = defaultdict(set)
    section_concepts: dict[str, set] = defaultdict(set)

    for e in kg["edges"]:
        if e["type"] == "tagged_with":
            sec_id = e["source"]
            con_id = e["target"]
            concept_sections[con_id] += 1
            concept_doc_set[con_id].add(_sec_to_doc(sec_id))
            section_concepts[sec_id].add(con_id)

    # ── Concept co-occurrence ─────────────────────────────────────────────
    cooc: Counter = Counter()
    for concepts in section_concepts.values():
        for a, b in combinations(sorted(concepts), 2):
            cooc[(a, b)] += 1

    concept_ids = {n["id"] for n in kg["nodes"] if n["type"] == "concept"}

    cooc_edges = [
        {"from": a, "to": b, "weight": w}
        for (a, b), w in cooc.items()
        if w >= min_cooc and a in concept_ids and b in concept_ids
    ]

    # ── Taxonomy index (for concept domain/kind enrichment) ────────────────
    tax_index: dict = {}
    try:
        import sys as _sys
        if str(PROJECT_ROOT) not in _sys.path:
            _sys.path.insert(0, str(PROJECT_ROOT))
        from utils.taxonomy_loader import load_taxonomy_index  # noqa: PLC0415
        tax_index = load_taxonomy_index()
    except Exception:
        pass

    # ── Concept nodes ─────────────────────────────────────────────────────
    concept_nodes = [
        {
            "id": n["id"],
            "name": n.get("name", n["id"].replace("concept:", "")),
            "sectionCount": concept_sections[n["id"]],
            "docCount": len(concept_doc_set[n["id"]]),
            "domain": tax_index.get(n.get("name", ""), {}).get("domain", ""),
            "subdomain": tax_index.get(n.get("name", ""), {}).get("subdomain", ""),
            "artifactKind": tax_index.get(n.get("name", ""), {}).get("artifact_kind", ""),
        }
        for n in kg["nodes"]
        if n["type"] == "concept"
    ]

    # ── Document details (base from KG nodes) ──────────────────────────────
    doc_details: dict[str, dict] = {}
    for n in kg["nodes"]:
        if n["type"] in ("document", "api"):
            doc_details[n["id"]] = {
                "title": (n.get("title") or n["id"].split("/")[-1])[:80],
                "path": n.get("doc_id", ""),
                "isApi": n["type"] == "api",
                "tags": "",
                "description": "",
                "proficiency": "",
            }

    # ── Enrich doc_details from document_metadata.parquet ────────────────
    dm_path = PROJECT_ROOT / "outputs" / "document_metadata.parquet"
    if dm_path.exists():
        try:
            import pandas as _pd_dm  # noqa: PLC0415
            import numpy as _np_dm  # noqa: PLC0415
            _dm = _pd_dm.read_parquet(dm_path)
            for _row in _dm.itertuples(index=False):
                _did = f"doc:{_row.doc_id}"
                _tags = _row.tags
                _tags_str = ", ".join(str(t) for t in _tags if t) if hasattr(_tags, "__iter__") and not isinstance(_tags, str) else str(_tags or "")
                if _did in doc_details:
                    doc_details[_did]["tags"] = _tags_str
                    doc_details[_did]["description"] = str(_row.description or "")[:200]
                    doc_details[_did]["proficiency"] = str(_row.proficiency_level or "")
        except Exception as _dm_e:
            print(f"  Warning: could not enrich doc_details from document_metadata ({_dm_e})")

    # ── Top docs per concept (for sidebar) ───────────────────────────────
    concept_top_docs: dict[str, list] = {}
    for con_id, doc_set in concept_doc_set.items():
        top = sorted(
            doc_set,
            key=lambda d: doc_details.get(d, {}).get("title", ""),
        )[:20]
        concept_top_docs[con_id] = [
            {
                "id": d,
                "title": doc_details.get(d, {}).get("title", d.split("/")[-1]),
                "isApi": doc_details.get(d, {}).get("isApi", False),
            }
            for d in top
        ]

    # ── Classified relationship edges: parquet-first, KG rel: fallback ─────
    rel_edges: list[dict] = []
    seen_rel: set[tuple] = set()

    cp_path = PROJECT_ROOT / "outputs" / "classified_pairs.parquet"
    _loaded_from_parquet = False
    try:
        import pandas as _pd  # noqa: PLC0415
        if cp_path.exists():
            cp = _pd.read_parquet(cp_path, columns=[
                "source_doc", "target_doc", "source_is_api", "target_is_api",
                "relationship_type", "relationship_confidence", "relationship_bidirectional",
                "is_cross_corpus", "source_concepts", "target_concepts",
            ])
            # Normalise PyArrow-backed columns to plain Python types before iteration
            for _col in ("source_is_api", "target_is_api", "relationship_bidirectional", "is_cross_corpus"):
                if _col in cp.columns:
                    cp[_col] = cp[_col].fillna(False).astype(bool)
            for _col in ("source_concepts", "target_concepts"):
                if _col in cp.columns:
                    cp[_col] = cp[_col].apply(lambda x: list(x) if x is not None else [])

            for row in cp.itertuples(index=False):
                src_doc = f"doc:{row.source_doc}"
                tgt_doc = f"doc:{row.target_doc}"
                if src_doc == tgt_doc:
                    continue
                rel_type = str(row.relationship_type)
                key = (src_doc, tgt_doc, rel_type)
                if key in seen_rel:
                    continue
                seen_rel.add(key)
                # Supplement doc_details for any doc not already in the KG
                for did, is_api in [(src_doc, bool(row.source_is_api)),
                                    (tgt_doc, bool(row.target_is_api))]:
                    if did not in doc_details:
                        raw = did.replace("doc:", "")
                        doc_details[did] = {
                            "title": raw.split("/")[-1].replace(".md", "")[:80],
                            "path": raw,
                            "isApi": is_api,
                            "tags": "",
                            "description": "",
                            "proficiency": "",
                        }
                src_concepts = [str(c) for c in row.source_concepts][:5]
                tgt_concepts = [str(c) for c in row.target_concepts][:5]
                rel_edges.append({
                    "from": src_doc,
                    "to": tgt_doc,
                    "type": rel_type,
                    "confidence": round(float(row.relationship_confidence), 2),
                    "bidirectional": bool(row.relationship_bidirectional),
                    "isCrossCorpus": bool(row.is_cross_corpus),
                    "sourceConcepts": src_concepts,
                    "targetConcepts": tgt_concepts,
                    "sourceTitle": doc_details.get(src_doc, {}).get("title", src_doc.split("/")[-1]),
                    "targetTitle": doc_details.get(tgt_doc, {}).get("title", tgt_doc.split("/")[-1]),
                })
            _loaded_from_parquet = len(rel_edges) > 0
    except Exception as _e:
        print(f"  Warning: classified_pairs.parquet load failed ({_e}), falling back to KG edges")

    if not _loaded_from_parquet:
        for e in kg["edges"]:
            if not e["type"].startswith("rel:"):
                continue
            src_doc = _sec_to_doc(e["source"])
            tgt_doc = _sec_to_doc(e["target"])
            if src_doc == tgt_doc:
                continue
            rel_type = e["type"].replace("rel:", "")
            key = (src_doc, tgt_doc, rel_type)
            if key in seen_rel:
                continue
            seen_rel.add(key)
            rel_edges.append({
                "from": src_doc,
                "to": tgt_doc,
                "type": rel_type,
                "confidence": round(float(e.get("confidence", 0)), 2),
                "bidirectional": bool(e.get("bidirectional", False)),
                "isCrossCorpus": False,
                "sourceConcepts": [],
                "targetConcepts": [],
                "sourceTitle": doc_details.get(src_doc, {}).get("title", src_doc.split("/")[-1]),
                "targetTitle": doc_details.get(tgt_doc, {}).get("title", tgt_doc.split("/")[-1]),
            })

    # ── Per-concept connected concepts (for sidebar) ──────────────────────
    concept_neighbours: dict[str, list[str]] = defaultdict(list)
    for (a, b), w in cooc.items():
        if w >= min_cooc and a in concept_ids and b in concept_ids:
            concept_neighbours[a].append(b)
            concept_neighbours[b].append(a)

    # ── Isolated documents (zero semantic connections) ────────────────────
    isolated_docs: list[dict] = []
    try:
        dm_path = PROJECT_ROOT / "outputs" / "document_metadata.parquet"
        if dm_path.exists():
            import pandas as _pd2  # noqa: PLC0415
            dm = _pd2.read_parquet(dm_path)
            if "is_api_reference" in dm.columns and "is_api" not in dm.columns:
                dm = dm.rename(columns={"is_api_reference": "is_api"})
            dm["total_connections"] = dm["total_connections"].fillna(0)
            iso = dm[dm["total_connections"] == 0]
            for row in iso.itertuples(index=False):
                doc_id = f"doc:{row.doc_id}"
                d = doc_details.get(doc_id, {})
                isolated_docs.append({
                    "id":     doc_id,
                    "title":  d.get("title") or row.doc_id.split("/")[-1],
                    "path":   d.get("path") or row.doc_id,
                    "isApi":  bool(getattr(row, "is_api", False)),
                })
            isolated_docs.sort(key=lambda x: (x["isApi"], x["title"].lower()))
    except Exception as _ie:
        print(f"  Warning: could not compute isolated docs ({_ie})")

    return {
        "conceptNodes": concept_nodes,
        "coocEdges": cooc_edges,
        "relEdges": rel_edges,
        "docDetails": doc_details,
        "conceptTopDocs": concept_top_docs,
        "conceptNeighbours": {k: v for k, v in concept_neighbours.items()},
        "isolatedDocs": isolated_docs,
        "meta": {
            "conceptCount": len(concept_nodes),
            "coocEdgeCount": len(cooc_edges),
            "relEdgeCount": len(rel_edges),
            "isolatedCount": len(isolated_docs),
            "minCooc": min_cooc,
        },
    }


# ── HTML generation ──────────────────────────────────────────────────────────

_REL_COLOURS = {
    "uses":          "#ef9a9a",
    "explains":      "#80cbc4",
    "requires":      "#f48fb1",
    "extends":       "#ce93d8",
    "related_to":    "#bdbdbd",
    "contrasts_with":"#ffb74d",
    "applies_to":    "#a5d6a7",
}

_HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>__PRODUCT_NAME__ Knowledge Graph Explorer</title>
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Segoe UI', sans-serif; background: #0d1117; color: #e6edf3; height: 100vh; display: flex; flex-direction: column; overflow: hidden; }

/* ── Toolbar ── */
#toolbar { display: flex; align-items: center; gap: 10px; padding: 8px 12px; background: #161b22; border-bottom: 1px solid #30363d; flex-shrink: 0; flex-wrap: wrap; }
#toolbar h1 { font-size: 14px; font-weight: 600; color: #58a6ff; white-space: nowrap; margin-right: 4px; }
#search { padding: 5px 10px; border-radius: 6px; border: 1px solid #30363d; background: #0d1117; color: #e6edf3; font-size: 13px; width: 200px; }
#search:focus { outline: none; border-color: #58a6ff; }
.mode-btn { padding: 4px 12px; border-radius: 6px; border: 1px solid #30363d; background: #21262d; color: #8b949e; font-size: 13px; cursor: pointer; }
.mode-btn.active { background: #1f6feb; border-color: #1f6feb; color: #fff; }
.ctrl-btn { padding: 4px 10px; border-radius: 6px; border: 1px solid #30363d; background: #21262d; color: #8b949e; font-size: 13px; cursor: pointer; }
.ctrl-btn:hover { border-color: #58a6ff; color: #58a6ff; }
label.slider-label { font-size: 12px; color: #8b949e; display: flex; align-items: center; gap: 6px; white-space: nowrap; }
#min-cooc-val { color: #e6edf3; font-weight: 600; min-width: 20px; }
#cooc-ctrl { display: flex; align-items: center; gap: 6px; }

/* ── Main layout ── */
#main { display: flex; flex: 1; overflow: hidden; }
#graph-container { flex: 1; position: relative; }
#network { width: 100%; height: 100%; }

/* ── Spotlight bar ── */
#spotlight-bar { display: none; position: absolute; bottom: 12px; left: 50%; transform: translateX(-50%); background: #1f6feb; color: #fff; font-size: 13px; padding: 6px 16px; border-radius: 20px; cursor: pointer; z-index: 10; box-shadow: 0 4px 12px rgba(0,0,0,0.5); white-space: nowrap; }
#spotlight-bar:hover { background: #388bfd; }

/* ── Sidebar ── */
#resize-handle { width: 5px; background: #21262d; cursor: col-resize; flex-shrink: 0; transition: background 0.15s; }
#resize-handle:hover, #resize-handle.dragging { background: #58a6ff; }
#sidebar { width: 300px; min-width: 180px; max-width: 600px; background: #161b22; border-left: 1px solid #30363d; display: flex; flex-direction: column; overflow: hidden; transition: width 0.0s; }
#sidebar.collapsed { width: 0 !important; min-width: 0; overflow: hidden; border: none; }
#resize-handle.collapsed { background: #30363d; }
#sidebar-toggle { cursor: pointer; font-size: 12px; padding: 4px 8px; color: #58a6ff; background: none; border: none; }
#details-panel { flex: 1; overflow-y: auto; padding: 12px; border-bottom: 1px solid #30363d; }
#details-panel h3 { font-size: 13px; color: #58a6ff; margin-bottom: 8px; }
#details-panel .stat { font-size: 12px; color: #8b949e; margin-bottom: 4px; }
#details-panel .stat span { color: #e6edf3; font-weight: 600; }
#details-panel .doc-list { list-style: none; margin-top: 8px; }
#details-panel .doc-list li { font-size: 11px; padding: 3px 4px; border-radius: 4px; cursor: pointer; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
#details-panel .doc-list li:hover { background: #21262d; }
#details-panel .doc-list li.api { color: #e76f6f; }
#details-panel .doc-list li.article { color: #f1a14e; }
.expand-btn { margin-top: 8px; padding: 4px 10px; border-radius: 6px; border: 1px solid #30363d; background: #21262d; color: #8b949e; font-size: 12px; cursor: pointer; width: 100%; }
.expand-btn:hover { border-color: #58a6ff; color: #58a6ff; }
#placeholder { color: #484f58; font-size: 13px; text-align: center; padding: 40px 12px; line-height: 1.6; }

/* ── Filters ── */
#filters-panel { padding: 12px; overflow-y: auto; flex-shrink: 0; }
#filters-panel h4 { font-size: 12px; color: #8b949e; text-transform: uppercase; letter-spacing: .05em; margin-bottom: 8px; }
.filter-row { display: flex; align-items: center; gap: 8px; margin-bottom: 5px; cursor: pointer; user-select: none; }
.filter-row input[type=checkbox] { accent-color: #58a6ff; }
.filter-dot { width: 10px; height: 10px; border-radius: 50%; flex-shrink: 0; }
.filter-label { font-size: 12px; color: #c9d1d9; }
.filter-count { font-size: 11px; color: #484f58; margin-left: auto; }

/* ── Legend ── */
#legend { padding: 8px 12px; border-top: 1px solid #30363d; font-size: 11px; color: #484f58; }
.legend-item { display: inline-flex; align-items: center; gap: 4px; margin-right: 10px; }
.legend-dot { width: 8px; height: 8px; border-radius: 50%; }

/* ── Doc search autocomplete ── */
#doc-search-wrap { position: relative; }
#doc-search { padding: 5px 10px; border-radius: 6px; border: 1px solid #30363d; background: #0d1117; color: #e6edf3; font-size: 13px; width: 220px; }
#doc-search:focus { outline: none; border-color: #f1a14e; }
#doc-search-results { display: none; position: absolute; top: calc(100% + 4px); left: 0; width: 380px; max-height: 260px; overflow-y: auto; background: #161b22; border: 1px solid #30363d; border-radius: 6px; z-index: 999; box-shadow: 0 8px 24px rgba(0,0,0,0.5); }
#doc-search-results.open { display: block; }
.doc-result { padding: 6px 10px; font-size: 12px; cursor: pointer; border-bottom: 1px solid #21262d; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.doc-result:hover { background: #21262d; }
.doc-result .doc-type { font-size: 10px; color: #484f58; margin-left: 6px; }
.doc-result.is-api { color: #e76f6f; }
.doc-result.is-article { color: #f1a14e; }

/* ── Tooltip override ── */
.vis-tooltip { background: #161b22 !important; border: 1px solid #30363d !important; color: #e6edf3 !important; font-size: 12px !important; border-radius: 6px !important; padding: 6px 10px !important; }

/* ── Light theme ── */
body.light { background: #f6f8fa; color: #24292f; }
body.light #toolbar { background: #ffffff; border-bottom-color: #d0d7de; }
body.light #toolbar h1 { color: #0969da; }
body.light #search, body.light #doc-search { background: #f6f8fa; color: #24292f; border-color: #d0d7de; }
body.light .mode-btn { background: #f6f8fa; color: #57606a; border-color: #d0d7de; }
body.light .mode-btn.active { background: #0969da; border-color: #0969da; color: #fff; }
body.light .ctrl-btn { background: #f6f8fa; color: #57606a; border-color: #d0d7de; }
body.light .ctrl-btn:hover { border-color: #0969da; color: #0969da; }
body.light label.slider-label { color: #57606a; }
body.light #min-cooc-val { color: #24292f; }
body.light #resize-handle { background: #d0d7de; }
body.light #resize-handle:hover, body.light #resize-handle.dragging { background: #0969da; }
body.light #sidebar { background: #ffffff; border-left-color: #d0d7de; }
body.light #details-panel h3 { color: #0969da; }
body.light #details-panel .stat { color: #57606a; }
body.light #details-panel .stat span { color: #24292f; }
body.light #details-panel { border-bottom-color: #d0d7de; }
body.light #details-panel .doc-list li:hover { background: #f6f8fa; }
body.light #details-panel .doc-list li.api { color: #cf222e; }
body.light #details-panel .doc-list li.article { color: #953800; }
body.light .expand-btn { background: #f6f8fa; color: #57606a; border-color: #d0d7de; }
body.light .expand-btn:hover { border-color: #0969da; color: #0969da; }
body.light #placeholder { color: #8c959f; }
body.light #filters-panel h4 { color: #57606a; }
body.light .filter-label { color: #24292f; }
body.light .filter-count { color: #8c959f; }
body.light #legend { border-top-color: #d0d7de; color: #8c959f; }
body.light #doc-search-results { background: #ffffff; border-color: #d0d7de; box-shadow: 0 8px 24px rgba(0,0,0,0.12); }
body.light .doc-result { border-bottom-color: #f6f8fa; }
body.light .doc-result:hover { background: #f6f8fa; }
body.light .doc-result .doc-type { color: #8c959f; }
body.light .doc-result.is-api { color: #cf222e; }
body.light .doc-result.is-article { color: #953800; }
body.light .vis-tooltip { background: #ffffff !important; border-color: #d0d7de !important; color: #24292f !important; }
body.light #isolated-panel { background: #f6f8fa; }
body.light #isolated-panel h2 { color: #0969da; }
body.light #iso-search { background: #ffffff; color: #24292f; border-color: #d0d7de; }
body.light .iso-type-btn { background: #f6f8fa; color: #57606a; border-color: #d0d7de; }
body.light .iso-type-btn.active { background: #0969da; border-color: #0969da; color: #fff; }
body.light #iso-table th { color: #57606a; border-bottom-color: #d0d7de; }
body.light #iso-table th:hover { color: #24292f; }
body.light #iso-table th.sorted .sort-icon { color: #0969da; }
body.light #iso-table td { border-bottom-color: #f6f8fa; }
body.light #iso-table tr:hover td { background: #eaeef2; }
body.light .iso-title { color: #24292f; }
body.light .iso-title:hover { color: #0969da; }
body.light .iso-badge-api { background: #ffebe9; color: #cf222e; }
body.light .iso-badge-art { background: #fff8c5; color: #7d4e00; }
body.light .iso-path { color: #8c959f; }
body.light #resize-handle.collapsed { background: #d0d7de; }

/* ── Isolated docs panel ── */
#isolated-panel { display: none; position: absolute; inset: 0; background: #0d1117; overflow-y: auto; padding: 16px; }
#isolated-panel h2 { font-size: 14px; color: #58a6ff; margin-bottom: 10px; }
#iso-search { padding: 5px 10px; border-radius: 6px; border: 1px solid #30363d; background: #161b22; color: #e6edf3; font-size: 13px; width: 300px; margin-bottom: 10px; }
#iso-search:focus { outline: none; border-color: #58a6ff; }
#iso-type-btns { display: inline-flex; gap: 6px; margin-left: 10px; vertical-align: middle; }
.iso-type-btn { padding: 3px 10px; border-radius: 6px; border: 1px solid #30363d; background: #21262d; color: #8b949e; font-size: 12px; cursor: pointer; }
.iso-type-btn.active { background: #1f6feb; border-color: #1f6feb; color: #fff; }
#iso-table { width: 100%; border-collapse: collapse; font-size: 12px; }
#iso-table th { text-align: left; padding: 6px 8px; color: #8b949e; border-bottom: 1px solid #30363d; font-weight: 600; font-size: 11px; text-transform: uppercase; letter-spacing: .04em; cursor: pointer; user-select: none; white-space: nowrap; }
#iso-table th:hover { color: #e6edf3; }
#iso-table th .sort-icon { margin-left: 4px; opacity: 0.4; }
#iso-table th.sorted .sort-icon { opacity: 1; color: #58a6ff; }
#iso-table td { padding: 5px 8px; border-bottom: 1px solid #21262d; vertical-align: top; }
#iso-table tr:hover td { background: #161b22; }
.iso-title { color: #e6edf3; cursor: pointer; }
.iso-title:hover { color: #58a6ff; text-decoration: underline; }
.iso-badge { display: inline-block; padding: 1px 6px; border-radius: 4px; font-size: 10px; font-weight: 600; margin-right: 4px; }
.iso-badge-api { background: #4a1515; color: #e76f6f; }
.iso-badge-art { background: #4a2800; color: #f1a14e; }
.iso-path { font-size: 10px; color: #484f58; word-break: break-all; }
</style>
</head>
<body>

<div id="toolbar">
  <h1>__PRODUCT_NAME__ Knowledge Graph</h1>
  <input id="search" type="text" placeholder="&#128269; Search nodes..." oninput="onSearch(this.value)" />
  <div id="doc-search-wrap">
    <input id="doc-search" type="text" placeholder="&#128196; Find document..." oninput="onDocSearch(this.value)" onblur="closeDocResults()" autocomplete="off" />
    <div id="doc-search-results"></div>
  </div>
  <button class="mode-btn active" id="btn-concept" onclick="setMode('concept')">Concept Map</button>
  <button class="mode-btn" id="btn-rel" onclick="setMode('relationship')">Relationship Map</button>
  <button class="mode-btn" id="btn-isolated" onclick="setMode('isolated')">Isolated Docs <span id="iso-badge-count" style="font-size:11px;opacity:0.7"></span></button>
  <div id="cooc-ctrl">
    <label class="slider-label">Min links: <input type="range" id="min-cooc" min="1" max="30" value="3" oninput="onMinCooc(this.value)" /> <span id="min-cooc-val">3</span></label>
  </div>
  <button class="ctrl-btn" onclick="fitGraph()">&#8862; Fit</button>
  <button class="ctrl-btn" id="phys-btn" onclick="togglePhysics()">&#9881; Physics: Off</button>
  <button class="ctrl-btn" id="theme-btn" onclick="toggleTheme()" style="margin-left:auto">&#9788; Light</button>
</div>

<div id="main">
  <div id="graph-container">
    <div id="network"></div>
    <div id="spotlight-bar" onclick="clearSpotlight()">&#10005; Clear highlight &mdash; click to restore graph</div>
    <div id="isolated-panel">
      <h2>Isolated Documents &mdash; <span id="iso-count"></span></h2>
      <input id="iso-search" type="text" placeholder="&#128269; Filter by title or path..." oninput="filterIsolated()" />
      <span id="iso-type-btns">
        <button class="iso-type-btn active" id="iso-btn-all" onclick="setIsoType('all')">All</button>
        <button class="iso-type-btn" id="iso-btn-article" onclick="setIsoType('article')">Articles</button>
        <button class="iso-type-btn" id="iso-btn-api" onclick="setIsoType('api')">API</button>
      </span>
      <table id="iso-table">
        <thead><tr>
          <th onclick="sortIsolated('title')" data-col="title">Title <span class="sort-icon">&#8597;</span></th>
          <th onclick="sortIsolated('type')" data-col="type">Type <span class="sort-icon">&#8597;</span></th>
          <th onclick="sortIsolated('path')" data-col="path">Path <span class="sort-icon">&#8597;</span></th>
        </tr></thead>
        <tbody id="iso-tbody"></tbody>
      </table>
    </div>
  </div>
  <div id="resize-handle" title="Drag to resize · Double-click to collapse"></div>
  <div id="sidebar">
    <div id="details-panel">
      <div id="placeholder">&#128270; Click a node to explore its connections</div>
    </div>
    <div id="filters-panel">
      <h4>Edge filters</h4>
      <div id="filter-list"></div>
    </div>
    <div id="legend">
      <span class="legend-item"><span class="legend-dot" style="background:#4e9af1"></span>Concept</span>
      <span class="legend-item"><span class="legend-dot" style="background:#4fc3f7;border-radius:2px"></span>UI</span>
      <span class="legend-item"><span class="legend-dot" style="background:#a5d6a7;border-radius:2px"></span>Arch</span>
      <span class="legend-item"><span class="legend-dot" style="background:#f48fb1;border-radius:2px"></span>Security</span>
      <span class="legend-item"><span class="legend-dot" style="background:#90caf9;border-radius:2px"></span>Data</span>
      <span class="legend-item"><span class="legend-dot" style="background:#ffcc80;border-radius:2px"></span>Modules</span>
      <span class="legend-item"><span class="legend-dot" style="background:#f1a14e"></span>Article</span>
      <span class="legend-item"><span class="legend-dot" style="background:#e76f6f"></span>API</span>
    </div>
  </div>
</div>

VIS_SCRIPT_PLACEHOLDER

<script>
// ── Data injected by Python ───────────────────────────────────────────────
const DATA = DATA_JSON_PLACEHOLDER;

// ── Colour constants ──────────────────────────────────────────────────────
const NODE_COLOURS = {
  concept: { background: '#1e3a5f', border: '#4e9af1', highlight: { background: '#2a5298', border: '#7ec8e3' } },
  article: { background: '#4a2800', border: '#f1a14e', highlight: { background: '#7a4200', border: '#ffc085' } },
  api:     { background: '#4a1515', border: '#e76f6f', highlight: { background: '#7a2020', border: '#ff9a9a' } },
};
const REL_COLOURS = DATA_REL_COLOURS_PLACEHOLDER;
const DOMAIN_COLOURS = {
  ui:           { background: '#1a3545', border: '#4fc3f7', hbg: '#1f4a60', hb: '#80d8ff' },
  data:         { background: '#1a2e45', border: '#90caf9', hbg: '#1f3a60', hb: '#b3d9ff' },
  security:     { background: '#3a1a2e', border: '#f48fb1', hbg: '#50202e', hb: '#ffb3cb' },
  architecture: { background: '#1a3020', border: '#a5d6a7', hbg: '#203a28', hb: '#c8e6ca' },
  modules:      { background: '#3a2e1a', border: '#ffcc80', hbg: '#50401a', hb: '#ffe0b2' },
  ops:          { background: '#2e1a3a', border: '#ce93d8', hbg: '#3a2050', hb: '#e1bee7' },
  quality:      { background: '#1a2e2e', border: '#80cbc4', hbg: '#1f3c3c', hb: '#b2dfdb' },
  tooling:      { background: '#2e2e1a', border: '#fff176', hbg: '#3c3c20', hb: '#fff9c4' },
  migration:    { background: '#3a1a1a', border: '#ef9a9a', hbg: '#50202a', hb: '#ffcdd2' },
  localization: { background: '#1a2a3a', border: '#b0bec5', hbg: '#20364a', hb: '#cfd8e0' },
};
function domainColour(domain) {
  const d = DOMAIN_COLOURS[domain];
  if (!d) return NODE_COLOURS.concept;
  return { background: d.background, border: d.border, highlight: { background: d.hbg, border: d.hb } };
}
const COOC_COLOUR = { color: '#4e9af1', opacity: 0.25 };

// ── State ─────────────────────────────────────────────────────────────────
let network = null;
let nodesDS = null;
let edgesDS = null;
let currentMode = 'concept';
let physicsEnabled = false;
let selectedNodeId = null;
let expandedConcept = null;
let minCooc = 3;
const hiddenEdgeTypes = new Set();
let _spotlitNodeId = null;  // currently spotlit doc node

// ── vis-network options ───────────────────────────────────────────────────
const NET_OPTIONS = {
  nodes: { shape: 'dot', borderWidth: 2, shadow: false, font: { color: '#c9d1d9', size: 13 } },
  edges: { smooth: { type: 'continuous', roundness: 0.2 }, shadow: false, selectionWidth: 2 },
  physics: { enabled: false, forceAtlas2Based: { gravitationalConstant: -60, springLength: 120, avoidOverlap: 0.5 }, solver: 'forceAtlas2Based', stabilization: { iterations: 500, fit: true } },
  interaction: { hover: true, tooltipDelay: 150, hideEdgesOnDrag: true, multiselect: false },
};

// ── Initialisation ────────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  buildFilterUI();
  initConceptMap();
  const count = (DATA.isolatedDocs || []).length;
  if (count) document.getElementById('iso-badge-count').textContent = `(${count})`;
});

function initNetwork(nodes, edges) {
  nodesDS = new vis.DataSet(nodes);
  edgesDS = new vis.DataSet(edges);
  const container = document.getElementById('network');
  if (network) network.destroy();
  network = new vis.Network(container, { nodes: nodesDS, edges: edgesDS }, NET_OPTIONS);
  network.on('click', onNodeClick);
  network.on('stabilizationIterationsDone', () => { network.setOptions({ physics: { enabled: false } }); });
  enableRightClickPan(container);
}

// ── Mode: Concept Map ─────────────────────────────────────────────────────
function initConceptMap() {
  const nodes = DATA.conceptNodes.map(c => ({
    id: c.id,
    label: c.name,
    title: `${c.name}${c.domain ? '\ndomain: ' + c.domain + (c.subdomain ? ' / ' + c.subdomain : '') : ''}${c.artifactKind ? '\nkind: ' + c.artifactKind : ''}\n${c.sectionCount} sections · ${c.docCount} docs`,
    size: Math.max(8, Math.min(50, c.sectionCount / 6)),
    color: domainColour(c.domain),
    group: 'concept',
    _data: c,
  }));

  const edges = coocEdgesFiltered();
  initNetwork(nodes, edges);
  expandedConcept = null;
  resetDetails();
}

function coocEdgesFiltered() {
  return DATA.coocEdges
    .filter(e => e.weight >= minCooc && !hiddenEdgeTypes.has('cooccurrence'))
    .map(e => ({
      id: `cooc_${e.from}_${e.to}`,
      from: e.from, to: e.to,
      value: e.weight,
      title: `${e.weight} shared sections`,
      color: { color: '#4e9af1', opacity: Math.min(0.8, 0.15 + e.weight / 60) },
      _edgeType: 'cooccurrence',
    }));
}

// Add/remove document neighbourhood for a clicked concept
function expandNeighbourhood(conceptId) {
  if (expandedConcept === conceptId) {
    collapseNeighbourhood();
    return;
  }
  collapseNeighbourhood();
  expandedConcept = conceptId;

  const docs = DATA.conceptTopDocs[conceptId] || [];

  // Position new nodes in a circle around the concept node's current canvas position.
  const centre = network.getPosition(conceptId);
  const radius = 180 + docs.length * 8;
  const docNodes = docs.map((d, i) => {
    const angle = (2 * Math.PI * i) / docs.length;
    const nc = _lightTheme ? LIGHT_NODE_COLOURS : NODE_COLOURS;
    return {
      id: d.id,
      label: d.title.length > 35 ? d.title.slice(0, 33) + '…' : d.title,
      title: d.title,
      size: 10,
      color: d.isApi ? nc.api : nc.article,
      group: d.isApi ? 'api' : 'article',
      _expanded: true,
      x: centre.x + radius * Math.cos(angle),
      y: centre.y + radius * Math.sin(angle),
    };
  });

  // Edges: concept → doc (belongs-to)
  const docEdges = docs.map(d => ({
    id: `exp_${d.id}`,
    from: conceptId, to: d.id,
    color: { color: '#4e9af1', opacity: 0.3 },
    dashes: true,
    _expanded: true,
    _edgeType: 'cooccurrence',
  }));

  // Rel edges between these docs
  const docIds = new Set(docs.map(d => d.id));
  const relEdges = DATA.relEdges
    .filter(e => docIds.has(e.from) && docIds.has(e.to) && !hiddenEdgeTypes.has(e.type))
    .map(e => ({
      id: `rel_exp_${e.from}_${e.to}_${e.type}`,
      from: e.from, to: e.to,
      title: `${e.type} (conf ${e.confidence})`,
      color: { color: REL_COLOURS[e.type] || '#888', opacity: 0.8 },
      arrows: e.bidirectional ? { to: true, from: true } : { to: true },
      width: 2,
      _expanded: true,
      _edgeType: e.type,
    }));

  nodesDS.add(docNodes);
  edgesDS.add([...docEdges, ...relEdges]);
  document.getElementById('exp-btn') && (document.getElementById('exp-btn').textContent = '▲ Collapse neighbourhood');
}

function collapseNeighbourhood() {
  if (!expandedConcept) return;
  const toRemoveNodes = nodesDS.get({ filter: n => n._expanded }).map(n => n.id);
  const toRemoveEdges = edgesDS.get({ filter: e => e._expanded }).map(e => e.id);
  nodesDS.remove(toRemoveNodes);
  edgesDS.remove(toRemoveEdges);
  expandedConcept = null;
}

// ── Mode: Relationship Map ────────────────────────────────────────────────
function initRelationshipMap() {
  // Collect unique doc IDs from active rel edges
  const activeTypes = new Set(
    Object.keys(REL_COLOURS).filter(t => !hiddenEdgeTypes.has(t))
  );
  const activeEdges = DATA.relEdges.filter(e => activeTypes.has(e.type));
  const docIds = new Set(activeEdges.flatMap(e => [e.from, e.to]));

  // Count relationships per node for sizing
  const relCount = {};
  for (const e of activeEdges) {
    relCount[e.from] = (relCount[e.from] || 0) + 1;
    relCount[e.to] = (relCount[e.to] || 0) + 1;
  }

  const nodes = [...docIds].map(id => {
    const d = DATA.docDetails[id] || {};
    const cnt = relCount[id] || 1;
    const nc = _lightTheme ? LIGHT_NODE_COLOURS : NODE_COLOURS;
    return {
      id,
      label: (d.title || id.split('/').pop()).slice(0, 30),
      title: d.title || id,
      size: Math.max(6, Math.min(40, cnt * 3)),
      color: d.isApi ? nc.api : nc.article,
      group: d.isApi ? 'api' : 'article',
      _data: d,
    };
  });

  const edges = activeEdges.map((e, i) => ({
    id: `rel_${i}`,
    from: e.from, to: e.to,
    title: `${e.type} (conf ${e.confidence})${e.isCrossCorpus ? ' \u21c4 cross-corpus' : ''}${e.sourceConcepts && e.sourceConcepts.length ? '\nA: ' + e.sourceConcepts.join(', ') : ''}${e.targetConcepts && e.targetConcepts.length ? '\nB: ' + e.targetConcepts.join(', ') : ''}`,
    color: { color: REL_COLOURS[e.type] || '#888', opacity: 0.7 },
    arrows: e.bidirectional ? { to: true, from: true } : { to: true },
    width: 1 + e.confidence,
    _edgeType: e.type,
  }));

  initNetwork(nodes, edges);
  resetDetails();
}

// ── Mode: Isolated Docs ───────────────────────────────────────────────────
let _isoTypeFilter = 'all';
let _isoSortCol = 'title';
let _isoSortAsc = true;

function initIsolatedMap() {
  const count = DATA.isolatedDocs.length;
  document.getElementById('iso-badge-count').textContent = count ? `(${count})` : '';
  document.getElementById('iso-search').value = '';
  _isoTypeFilter = 'all';
  _isoSortCol = 'title';
  _isoSortAsc = true;
  ['all','article','api'].forEach(t => {
    document.getElementById(`iso-btn-${t}`).classList.toggle('active', t === _isoTypeFilter);
  });
  // update sort icons
  document.querySelectorAll('#iso-table th').forEach(th => th.classList.remove('sorted'));
  const th = document.querySelector(`#iso-table th[data-col="${_isoSortCol}"]`);
  if (th) th.classList.add('sorted');
  renderIsolatedTable();
}

function setIsoType(type) {
  _isoTypeFilter = type;
  ['all','article','api'].forEach(t => {
    document.getElementById(`iso-btn-${t}`).classList.toggle('active', t === type);
  });
  renderIsolatedTable();
}

function filterIsolated() { renderIsolatedTable(); }

function sortIsolated(col) {
  if (_isoSortCol === col) _isoSortAsc = !_isoSortAsc;
  else { _isoSortCol = col; _isoSortAsc = true; }
  document.querySelectorAll('#iso-table th').forEach(th => {
    th.classList.toggle('sorted', th.dataset.col === col);
    if (th.dataset.col === col) {
      th.querySelector('.sort-icon').textContent = _isoSortAsc ? '\u25b2' : '\u25bc';
    } else {
      th.querySelector('.sort-icon').textContent = '\u21c5';
    }
  });
  renderIsolatedTable();
}

function renderIsolatedTable() {
  const q = (document.getElementById('iso-search').value || '').trim().toLowerCase();
  const allRows = Array.isArray(DATA.isolatedDocs) ? DATA.isolatedDocs : [];
  let rows = allRows.filter(d => {
    const title = String(d.title || '');
    const path = String(d.path || '');
    if (_isoTypeFilter === 'article' && d.isApi) return false;
    if (_isoTypeFilter === 'api' && !d.isApi) return false;
    if (q && !title.toLowerCase().includes(q) && !path.toLowerCase().includes(q)) return false;
    return true;
  });

  rows.sort((a, b) => {
    let va, vb;
    if (_isoSortCol === 'type') { va = a.isApi ? 1 : 0; vb = b.isApi ? 1 : 0; }
    else if (_isoSortCol === 'path') { va = String(a.path || '').toLowerCase(); vb = String(b.path || '').toLowerCase(); }
    else { va = String(a.title || '').toLowerCase(); vb = String(b.title || '').toLowerCase(); }
    if (va < vb) return _isoSortAsc ? -1 : 1;
    if (va > vb) return _isoSortAsc ? 1 : -1;
    return 0;
  });

  document.getElementById('iso-count').textContent =
    `${rows.length} of ${allRows.length} docs`;

  const tbody = document.getElementById('iso-tbody');
  tbody.innerHTML = rows.map(d => {
    const badge = d.isApi
      ? '<span class="iso-badge iso-badge-api">API</span>'
      : '<span class="iso-badge iso-badge-art">Article</span>';
    const shortPath = String(d.path || '').replace('data/raw_md/', '');
    const safeId = String(d.id || '').replace(/\\/g, '\\\\').replace(/'/g, "\\'");
    const safeTitle = String(d.title || d.id || '').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    return `<tr>
      <td><span class="iso-title" onclick="onIsoRowClick('${safeId}')">${safeTitle || String(d.id || '').split('/').pop()}</span></td>
      <td>${badge}</td>
      <td><span class="iso-path">${shortPath}</span></td>
    </tr>`;
  }).join('');
}

function onIsoRowClick(docId) {
  showDocDetails(docId);
}

// ── Mode switching ────────────────────────────────────────────────────────
function setMode(mode) {
  currentMode = mode;
  document.getElementById('btn-concept').classList.toggle('active', mode === 'concept');
  document.getElementById('btn-rel').classList.toggle('active', mode === 'relationship');
  document.getElementById('btn-isolated').classList.toggle('active', mode === 'isolated');
  document.getElementById('cooc-ctrl').style.display = mode === 'concept' ? '' : 'none';
  document.getElementById('network').style.display = mode === 'isolated' ? 'none' : '';
  document.getElementById('isolated-panel').style.display = mode === 'isolated' ? 'block' : 'none';
  document.getElementById('spotlight-bar').style.display = 'none';
  selectedNodeId = null;
  if (mode === 'concept') initConceptMap();
  else if (mode === 'relationship') initRelationshipMap();
  else initIsolatedMap();
  rebuildFilterUI();
}

// ── Node click handler ────────────────────────────────────────────────────
function onNodeClick(params) {
  if (!params.nodes.length) { resetDetails(); selectedNodeId = null; return; }
  const id = params.nodes[0];
  selectedNodeId = id;

  if (id.startsWith('concept:')) {
    showConceptDetails(id);
  } else {
    showDocDetails(id);
  }
}

function showConceptDetails(id) {
  const node = nodesDS.get(id);
  const d = node ? node._data : null;
  const nei = (DATA.conceptNeighbours[id] || []).map(cid => {
    const cn = nodesDS.get(cid);
    return cn ? cn.label : cid.replace('concept:', '');
  }).sort().slice(0, 12);

  const docs = (DATA.conceptTopDocs[id] || []).slice(0, 15);
  const docsHtml = docs.map(doc =>
    `<li class="${doc.isApi ? 'api' : 'article'}" title="${doc.title}" onclick="highlightRelDoc('${doc.id}')">${doc.isApi ? '⚙ ' : '📄 '}${doc.title}</li>`
  ).join('');

  const neiHtml = nei.map(n =>
    `<span style="display:inline-block;background:#21262d;border-radius:4px;padding:2px 6px;margin:2px;font-size:11px;cursor:pointer" onclick="selectConcept('concept:${n}')">${n}</span>`
  ).join('');

  document.getElementById('details-panel').innerHTML = `
    <h3>${d ? d.name : id.replace('concept:', '')}</h3>
    ${d ? `<div class="stat">Sections: <span>${d.sectionCount}</span></div>
    <div class="stat">Documents: <span>${d.docCount}</span></div>
    ${d.domain ? '<div class="stat">Domain: <span>' + d.domain + (d.subdomain ? ' / ' + d.subdomain : '') + '</span></div>' : ''}
    ${d.artifactKind ? '<div class="stat">Kind: <span>' + d.artifactKind + '</span></div>' : ''}` : ''}
    ${nei.length ? `<div class="stat" style="margin-top:10px">Connected concepts:</div><div style="margin-top:4px">${neiHtml}</div>` : ''}
    ${docs.length ? `<div class="stat" style="margin-top:10px">Top documents:</div><ul class="doc-list">${docsHtml}</ul>` : ''}
    <button class="expand-btn" id="exp-btn" onclick="expandNeighbourhood('${id}')">▼ Expand document neighbourhood</button>
  `;
}

function showDocDetails(id) {
  const d = DATA.docDetails[id] || {};
  const title = d.title || id.split('/').pop();
  const path = (d.path || id.replace('doc:', '')).replace('data/raw_md/', '');

  // Find rel edges involving this doc
  const outgoing = DATA.relEdges.filter(e => e.from === id).slice(0, 15);
  const incoming = DATA.relEdges.filter(e => e.to === id).slice(0, 10);

  const relHtml = (edges, dir) => edges.map(e => {
    const other = dir === 'out' ? e.targetTitle : e.sourceTitle;
    const otherId = dir === 'out' ? e.to : e.from;
    const concepts = dir === 'out' ? (e.targetConcepts || []) : (e.sourceConcepts || []);
    const arrow = dir === 'out' ? '→' : '←';
    const col = REL_COLOURS[e.type] || '#888';
    const crossTag = e.isCrossCorpus ? '<span style="color:#888;font-size:10px;margin-left:4px">⇄</span>' : '';
    const conceptTag = concepts.length ? `<div style="font-size:10px;color:#6e7681;margin-top:2px">${concepts.slice(0, 3).join(' · ')}</div>` : '';
    return `<li style="font-size:11px;padding:4px 0;border-bottom:1px solid #21262d" onclick="highlightRelDoc('${otherId}')">
      <div><span style="color:${col};font-weight:600">${e.type}</span> ${arrow}
      <span style="color:#c9d1d9">${other}</span>
      <span style="color:#484f58"> (${e.confidence})</span>${crossTag}</div>${conceptTag}
    </li>`;
  }).join('');

  document.getElementById('details-panel').innerHTML = `
    <h3>${title}</h3>
    <div class="stat">Type: <span>${d.isApi ? 'API Reference' : 'Article'}</span></div>
    ${d.proficiency ? `<div class="stat">Proficiency: <span>${d.proficiency}</span></div>` : ''}
    <div class="stat" style="word-break:break-all;font-size:11px;color:#484f58;margin-top:4px">${path}</div>
    ${d.description ? `<div style="font-size:11px;color:#8b949e;margin-top:6px;line-height:1.5;padding:6px 0;border-top:1px solid #21262d">${d.description}</div>` : ''}
    ${d.tags ? `<div style="margin-top:6px;display:flex;flex-wrap:wrap;gap:3px">${d.tags.split(',').map(t=>t.trim()).filter(Boolean).map(t=>`<span style="font-size:10px;padding:1px 6px;border-radius:3px;background:#21262d;color:#8b949e">${t}</span>`).join('')}</div>` : ''}
    ${outgoing.length ? `<div class="stat" style="margin-top:10px">Outgoing relationships:</div><ul class="doc-list" style="list-style:none">${relHtml(outgoing, 'out')}</ul>` : ''}
    ${incoming.length ? `<div class="stat" style="margin-top:8px">Incoming relationships:</div><ul class="doc-list" style="list-style:none">${relHtml(incoming, 'in')}</ul>` : ''}
    ${!outgoing.length && !incoming.length ? '<div class="stat" style="margin-top:10px;color:#484f58">No classified relationships for this document.</div>' : ''}
  `;
}

function highlightRelDoc(id) {
  if (nodesDS.get(id)) {
    network.selectNodes([id]);
    network.focus(id, { animation: true, scale: 0.8 });
    showDocDetails(id);
  }
}

function selectConcept(id) {
  network.selectNodes([id]);
  network.focus(id, { animation: true, scale: 0.8 });
  showConceptDetails(id);
}

function resetDetails() {
  document.getElementById('details-panel').innerHTML =
    '<div id="placeholder">&#128270; Click a node to explore its connections</div>';
}

// ── Node search (concept/doc labels in current view) ───────────────────────
function onSearch(q) {
  q = q.trim().toLowerCase();
  const updates = nodesDS.get().map(n => {
    const match = !q || (n.label || '').toLowerCase().includes(q) || (n.title || '').toLowerCase().includes(q);
    return { id: n.id, opacity: match ? 1 : 0.12 };
  });
  nodesDS.update(updates);
  if (q) {
    const first = nodesDS.get().find(n => (n.label || '').toLowerCase().includes(q));
    if (first) network.focus(first.id, { animation: true, scale: 0.8 });
  }
}

// ── Document title search ─────────────────────────────────────────────────
let _docResultsTimeout = null;

function onDocSearch(q) {
  clearTimeout(_docResultsTimeout);
  const box = document.getElementById('doc-search-results');
  q = q.trim().toLowerCase();
  if (q.length < 2) { box.classList.remove('open'); box.innerHTML = ''; return; }

  const matches = Object.entries(DATA.docDetails)
    .filter(([, d]) => (d.title || '').toLowerCase().includes(q))
    .sort((a, b) => {
      // Exact start-of-title matches first
      const as = a[1].title.toLowerCase().startsWith(q) ? 0 : 1;
      const bs = b[1].title.toLowerCase().startsWith(q) ? 0 : 1;
      return as - bs || a[1].title.localeCompare(b[1].title);
    })
    .slice(0, 30);

  if (!matches.length) { box.innerHTML = '<div class="doc-result" style="color:#484f58">No results</div>'; box.classList.add('open'); return; }

  box.innerHTML = matches.map(([id, d]) =>
    `<div class="doc-result ${d.isApi ? 'is-api' : 'is-article'}" onmousedown="selectDocResult('${String(id).replace(/\\/g, '\\\\').replace(/'/g, "\\'")}')">
      ${d.isApi ? '⚙' : '📄'} ${d.title}<span class="doc-type">${d.isApi ? 'API' : 'Article'}</span>
    </div>`
  ).join('');
  box.classList.add('open');
}

function selectDocResult(docId) {
  document.getElementById('doc-search').value = DATA.docDetails[docId]?.title || '';
  document.getElementById('doc-search-results').classList.remove('open');

  // Switch to relationship map so the doc node exists
  if (currentMode !== 'relationship') setMode('relationship');

  // Wait one tick for the mode switch to settle, then spotlight
  setTimeout(() => {
    spotlightDoc(docId);
    showDocDetails(docId);
  }, 50);
}

function spotlightDoc(docId) {
  clearSpotlight(false); // clear previous without hiding bar yet
  _spotlitNodeId = docId;

  const target = nodesDS.get(docId);
  if (!target) {
    // Node not in current view — just show details
    return;
  }

  // Dim all other nodes
  const updates = nodesDS.get().map(n => {
    if (n.id === docId) return null;
    return { id: n.id, opacity: 0.08 };
  }).filter(Boolean);
  nodesDS.update(updates);

  // Enlarge and highlight the target node
  const d = DATA.docDetails[docId] || {};
  nodesDS.update([{
    id: docId,
    size: 32,
    borderWidth: 4,
    color: {
      background: d.isApi ? '#7a2020' : '#7a4200',
      border: '#ffffff',
      highlight: { background: d.isApi ? '#ff6b6b' : '#ffc27a', border: '#ffffff' },
    },
    font: { size: 16, color: '#ffffff', bold: true },
    shadow: { enabled: true, color: '#ffffff', size: 20, x: 0, y: 0 },
    opacity: 1,
  }]);

  network.selectNodes([docId]);
  network.focus(docId, { animation: { duration: 600, easingFunction: 'easeInOutQuad' }, scale: 2.0 });

  document.getElementById('spotlight-bar').style.display = 'block';
}

function clearSpotlight(showBar) {
  if (!_spotlitNodeId) return;
  const prevId = _spotlitNodeId;
  _spotlitNodeId = null;

  // Restore all node opacities
  const updates = nodesDS.get().map(n => ({ id: n.id, opacity: 1 }));
  nodesDS.update(updates);

  // Restore the spotlit node's original appearance
  const d = DATA.docDetails[prevId] || {};
  const nc = _lightTheme ? LIGHT_NODE_COLOURS : NODE_COLOURS;
  nodesDS.update([{
    id: prevId,
    size: undefined,
    borderWidth: 2,
    color: d.isApi ? nc.api : nc.article,
    font: { size: 13, color: _lightTheme ? '#24292f' : '#c9d1d9', bold: false },
    shadow: false,
    opacity: 1,
  }]);

  if (showBar !== false) {
    document.getElementById('spotlight-bar').style.display = 'none';
    document.getElementById('doc-search').value = '';
  }
}

function closeDocResults() {
  // Short delay so onmousedown on a result fires before blur hides it
  _docResultsTimeout = setTimeout(() => {
    document.getElementById('doc-search-results').classList.remove('open');
  }, 150);
}

// ── Filters ───────────────────────────────────────────────────────────────
function buildFilterUI() {
  rebuildFilterUI();
}

function rebuildFilterUI() {
  const container = document.getElementById('filter-list');
  const panel = document.getElementById('filters-panel');
  container.innerHTML = '';

  if (currentMode === 'isolated') {
    panel.style.display = 'none';
    return;
  }
  panel.style.display = '';

  const types = currentMode === 'concept'
    ? [{ type: 'cooccurrence', label: 'Co-occurrence', colour: '#4e9af1', count: DATA.coocEdges.filter(e => e.weight >= minCooc).length }]
    : [];

  for (const [type, colour] of Object.entries(REL_COLOURS)) {
    const count = DATA.relEdges.filter(e => e.type === type).length;
    if (count > 0) types.push({ type, label: type.replace('_', ' '), colour, count });
  }

  for (const { type, label, colour, count } of types) {
    const checked = !hiddenEdgeTypes.has(type);
    const row = document.createElement('label');
    row.className = 'filter-row';
    row.innerHTML = `
      <input type="checkbox" ${checked ? 'checked' : ''} data-etype="${type}" onchange="onFilterChange(this)">
      <span class="filter-dot" style="background:${colour}"></span>
      <span class="filter-label">${label}</span>
      <span class="filter-count">${count}</span>
    `;
    container.appendChild(row);
  }
}

function onFilterChange(el) {
  const type = el.dataset.etype;
  if (el.checked) hiddenEdgeTypes.delete(type);
  else hiddenEdgeTypes.add(type);
  refreshEdges();
}

function refreshEdges() {
  if (currentMode === 'concept') {
    // Remove all cooc edges and re-add filtered ones
    const allEdges = edgesDS.get();
    const coocIds = allEdges.filter(e => e._edgeType === 'cooccurrence' && !e._expanded).map(e => e.id);
    edgesDS.remove(coocIds);
    edgesDS.add(coocEdgesFiltered());
    // Also toggle visibility of rel edges in expanded neighbourhood
    const expEdges = edgesDS.get({ filter: e => e._expanded && e._edgeType !== 'cooccurrence' });
    edgesDS.update(expEdges.map(e => ({
      id: e.id,
      hidden: hiddenEdgeTypes.has(e._edgeType),
    })));
  } else {
    // Relationship map: rebuild entirely
    initRelationshipMap();
  }
}

// ── Min co-occurrence slider ──────────────────────────────────────────────
function onMinCooc(val) {
  minCooc = parseInt(val, 10);
  document.getElementById('min-cooc-val').textContent = val;
  if (currentMode === 'concept') {
    const coocIds = edgesDS.get().filter(e => e._edgeType === 'cooccurrence' && !e._expanded).map(e => e.id);
    edgesDS.remove(coocIds);
    edgesDS.add(coocEdgesFiltered());
    rebuildFilterUI();
  }
}

// ── Physics ───────────────────────────────────────────────────────────────
function togglePhysics() {
  physicsEnabled = !physicsEnabled;
  network.setOptions({ physics: { enabled: physicsEnabled } });
  document.getElementById('phys-btn').textContent = `⚙ Physics: ${physicsEnabled ? 'On' : 'Off'}`;
}

// ── Theme ─────────────────────────────────────────────────────────────────
let _lightTheme = false;
const LIGHT_NODE_COLOURS = {
  concept: { background: '#dbeafe', border: '#2563eb', highlight: { background: '#bfdbfe', border: '#1d4ed8' } },
  article: { background: '#fff7ed', border: '#ea580c', highlight: { background: '#fed7aa', border: '#c2410c' } },
  api:     { background: '#fef2f2', border: '#dc2626', highlight: { background: '#fecaca', border: '#b91c1c' } },
};
const LIGHT_DOMAIN_COLOURS = {
  ui:           { background: '#e0f2fe', border: '#0284c7', hbg: '#bae6fd', hb: '#0369a1' },
  data:         { background: '#eff6ff', border: '#2563eb', hbg: '#dbeafe', hb: '#1d4ed8' },
  security:     { background: '#fdf4ff', border: '#c026d3', hbg: '#f5d0fe', hb: '#a21caf' },
  architecture: { background: '#f0fdf4', border: '#16a34a', hbg: '#dcfce7', hb: '#15803d' },
  modules:      { background: '#fffbeb', border: '#d97706', hbg: '#fde68a', hb: '#b45309' },
  ops:          { background: '#faf5ff', border: '#9333ea', hbg: '#e9d5ff', hb: '#7e22ce' },
  quality:      { background: '#f0fdfa', border: '#0d9488', hbg: '#ccfbf1', hb: '#0f766e' },
  tooling:      { background: '#fefce8', border: '#ca8a04', hbg: '#fef08a', hb: '#a16207' },
  migration:    { background: '#fff1f2', border: '#e11d48', hbg: '#fecdd3', hb: '#be123c' },
  localization: { background: '#f8fafc', border: '#475569', hbg: '#e2e8f0', hb: '#334155' },
};
function lightDomainColour(domain) {
  const d = LIGHT_DOMAIN_COLOURS[domain];
  if (!d) return LIGHT_NODE_COLOURS.concept;
  return { background: d.background, border: d.border, highlight: { background: d.hbg, border: d.hb } };
}
function toggleTheme() {
  _lightTheme = !_lightTheme;
  document.body.classList.toggle('light', _lightTheme);
  document.getElementById('theme-btn').textContent = _lightTheme ? '\u263d Dark' : '\u2600 Light';
  // Recolour network nodes to match theme
  if (network && nodesDS) {
    const updates = nodesDS.get().map(n => {
      if (n.group === 'concept') {
        const domain = n._data && n._data.domain;
        return { id: n.id, color: _lightTheme ? lightDomainColour(domain) : domainColour(domain) };
      } else if (n.group === 'article') {
        return { id: n.id, color: _lightTheme ? LIGHT_NODE_COLOURS.article : NODE_COLOURS.article };
      } else if (n.group === 'api') {
        return { id: n.id, color: _lightTheme ? LIGHT_NODE_COLOURS.api : NODE_COLOURS.api };
      }
      return null;
    }).filter(Boolean);
    nodesDS.update(updates);
    // Also update edge/canvas background via vis options
    network.setOptions({
      nodes: { font: { color: _lightTheme ? '#24292f' : '#c9d1d9' } },
    });
  }
}

function fitGraph() { network.fit({ animation: true }); }

// ── Right-click pan ───────────────────────────────────────────────────────
function enableRightClickPan(container) {
  // Remove any listener attached by a previous network instance
  if (container._rmRightPan) container._rmRightPan();

  let dragging = false;
  let lastX = 0, lastY = 0;

  function onContextMenu(e) { e.preventDefault(); }
  function onMouseDown(e) {
    if (e.button !== 2) return;
    dragging = true;
    lastX = e.clientX;
    lastY = e.clientY;
    container.style.cursor = 'grabbing';
    e.preventDefault();
  }
  function onMouseMove(e) {
    if (!dragging) return;
    const dx = e.clientX - lastX;
    const dy = e.clientY - lastY;
    lastX = e.clientX;
    lastY = e.clientY;
    const scale = network.getScale();
    const pos = network.getViewPosition();
    network.moveTo({ position: { x: pos.x - dx / scale, y: pos.y - dy / scale }, scale });
  }
  function onMouseUp(e) {
    if (e.button !== 2) return;
    dragging = false;
    container.style.cursor = '';
  }

  container.addEventListener('contextmenu', onContextMenu);
  container.addEventListener('mousedown', onMouseDown);
  window.addEventListener('mousemove', onMouseMove);
  window.addEventListener('mouseup', onMouseUp);

  // Cleanup hook for when network is re-initialised
  container._rmRightPan = () => {
    container.removeEventListener('contextmenu', onContextMenu);
    container.removeEventListener('mousedown', onMouseDown);
    window.removeEventListener('mousemove', onMouseMove);
    window.removeEventListener('mouseup', onMouseUp);
  };
}

// ── Sidebar resize ────────────────────────────────────────────────────────
(function () {
  const handle = document.getElementById('resize-handle');
  const sidebar = document.getElementById('sidebar');
  let dragging = false;
  let lastWidth = 300;

  handle.addEventListener('mousedown', e => {
    dragging = true;
    handle.classList.add('dragging');
    document.body.style.cursor = 'col-resize';
    document.body.style.userSelect = 'none';
    e.preventDefault();
  });

  document.addEventListener('mousemove', e => {
    if (!dragging) return;
    const mainRect = document.getElementById('main').getBoundingClientRect();
    const newWidth = Math.max(180, Math.min(600, mainRect.right - e.clientX));
    sidebar.style.width = newWidth + 'px';
    sidebar.classList.remove('collapsed');
    handle.classList.remove('collapsed');
    lastWidth = newWidth;
    if (network) network.redraw();
  });

  document.addEventListener('mouseup', () => {
    if (!dragging) return;
    dragging = false;
    handle.classList.remove('dragging');
    document.body.style.cursor = '';
    document.body.style.userSelect = '';
  });

  // Double-click handle to collapse/expand
  handle.addEventListener('dblclick', () => {
    if (sidebar.classList.contains('collapsed')) {
      sidebar.style.width = lastWidth + 'px';
      sidebar.classList.remove('collapsed');
      handle.classList.remove('collapsed');
    } else {
      lastWidth = sidebar.offsetWidth;
      sidebar.classList.add('collapsed');
      handle.classList.add('collapsed');
    }
    if (network) setTimeout(() => network.redraw(), 50);
  });
})();
</script>
</body>
</html>
"""


def build_html(data: dict, vis_js: str) -> str:
    rel_colours_js = json.dumps(_REL_COLOURS)
    data_js = json.dumps(data, ensure_ascii=False)

    import sys as _sys
    _root = Path(__file__).resolve().parent.parent
    if str(_root) not in _sys.path:
        _sys.path.insert(0, str(_root))
    try:
        from scripts.config_loader import cfg as _cfg
        product_name = _cfg.product_name()
    except Exception:
        product_name = "Doc"
    html = _HTML_TEMPLATE
    html = html.replace("VIS_SCRIPT_PLACEHOLDER", vis_js)
    html = html.replace("DATA_JSON_PLACEHOLDER", data_js)
    html = html.replace("DATA_REL_COLOURS_PLACEHOLDER", rel_colours_js)
    html = html.replace("__PRODUCT_NAME__", product_name)
    return html


# ── CLI ──────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate rich interactive HTML knowledge graph visualisation"
    )
    parser.add_argument("--min-cooc", type=int, default=3,
                        help="Minimum co-occurrence weight to show an edge in concept map (default: 3)")
    parser.add_argument("--output", default=None,
                        help="Output HTML path (default: outputs/knowledge_graph_explorer.html)")
    args = parser.parse_args()

    print(f"Loading {KG_PATH} …")
    with open(KG_PATH, encoding="utf-8") as f:
        kg = json.load(f)

    print("Preparing graph data …")
    data = prepare_data(kg, min_cooc=args.min_cooc)
    m = data["meta"]
    print(f"  {m['conceptCount']} concepts, {m['coocEdgeCount']} co-occurrence edges "
          f"(min {m['minCooc']}), {m['relEdgeCount']} relationship edges")

    print("Loading vis-network …")
    vis_js = _vis_js()

    print("Generating HTML …")
    html = build_html(data, vis_js)

    out = Path(args.output) if args.output else OUT_DIR / "knowledge_graph_explorer.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")

    size_kb = out.stat().st_size // 1024
    print(f"\nSaved: {out}  ({size_kb} KB)")

    # Auto-copy to docs/ for GitHub Pages deployment (only for the default output path)
    if not args.output:
        import shutil
        docs_path = PROJECT_ROOT / "docs" / "knowledge_graph_explorer.html"
        try:
            shutil.copy2(out, docs_path)
            print(f"Copied to {docs_path} (GitHub Pages)")
        except Exception as e:
            print(f"Warning: could not copy to docs/: {e}")

    print("Open this file in your browser to explore the graph.")


if __name__ == "__main__":
    main()


