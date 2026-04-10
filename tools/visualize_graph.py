"""
tools/visualize_graph.py

Generate interactive HTML visualizations of the XAF knowledge graph using pyvis.

Views:
  concept-map     -- 150 concept nodes connected by shared section co-occurrence
  neighborhood    -- All nodes within N hops of a given concept
  hub-docs        -- Top hub documents and their explicit cross-links

Usage:
  python tools/visualize_graph.py --view concept-map
  python tools/visualize_graph.py --view neighborhood --concept "Security System" --hops 2
  python tools/visualize_graph.py --view hub-docs --top 30
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

import pandas as pd
from pyvis.network import Network

PROJECT_ROOT = Path(__file__).resolve().parents[1]
KG_PATH = PROJECT_ROOT / "outputs" / "knowledge_graph.json"
OUT_DIR = PROJECT_ROOT / "outputs"

# ── Colour palette ──────────────────────────────────────────────────────────
COLOURS = {
    "concept": "#4e9af1",
    "document": "#f1a14e",
    "section": "#a4d65e",
    "api": "#e76f6f",
    "uid": "#b0b0b0",
}
EDGE_COLOURS = {
    "links_to": "#999999",
    "semantic_similar": "#aad4f5",
    "tagged_with": "#c8e6c9",
    "implements_concept": "#ffe082",
    "rel:uses": "#ef9a9a",
    "rel:explains": "#80cbc4",
    "rel:requires": "#f48fb1",
    "rel:extends": "#ce93d8",
    "rel:related_to": "#cccccc",
    "rel:contrasts_with": "#ff8a65",
    "rel:applies_to": "#a5d6a7",
    "contains": "#dddddd",
}


def load_kg() -> dict:
    print(f"Loading {KG_PATH} …")
    with open(KG_PATH, encoding="utf-8") as f:
        return json.load(f)


# ── View 1: Concept Map ──────────────────────────────────────────────────────

def build_concept_map(kg: dict, min_edge_weight: int = 3) -> Network:
    """
    150-node concept graph.
    Edge weight = number of sections tagged with BOTH concepts (co-occurrence).
    """
    nodes = {n["id"]: n for n in kg["nodes"]}
    concepts = [n for n in kg["nodes"] if n["type"] == "concept"]

    # For each section, collect its tagged concepts
    section_concepts: dict[str, list[str]] = defaultdict(list)
    for e in kg["edges"]:
        if e["type"] == "tagged_with":
            sec = e["source"]
            con = e["target"]
            section_concepts[sec].append(con)

    # Count concept-concept co-occurrences
    cooc: Counter = Counter()
    for sec, cons in section_concepts.items():
        clist = sorted(set(cons))
        for i in range(len(clist)):
            for j in range(i + 1, len(clist)):
                cooc[(clist[i], clist[j])] += 1

    # Concept → section count
    concept_sections: Counter = Counter()
    for e in kg["edges"]:
        if e["type"] == "tagged_with":
            concept_sections[e["target"]] += 1

    net = Network(height="900px", width="100%", bgcolor="#1a1a2e", font_color="white",
                  heading="XAF Knowledge Graph — Concept Map")
    net.barnes_hut(spring_length=150, spring_strength=0.02, damping=0.9)

    for c in concepts:
        cid = c["id"]
        label = c.get("name") or cid.replace("con:", "")
        size = max(10, min(60, concept_sections[cid] / 8))
        net.add_node(cid, label=label, title=f"{label}\n{concept_sections[cid]} sections",
                     color=COLOURS["concept"], size=size, font={"size": 14})

    added = 0
    for (a, b), w in cooc.items():
        if w >= min_edge_weight and a in {c["id"] for c in concepts} and b in {c["id"] for c in concepts}:
            net.add_edge(a, b, value=w, title=f"{w} shared sections",
                         color={"color": "#4e9af1", "opacity": 0.4})
            added += 1

    print(f"  Concept map: {len(concepts)} nodes, {added} edges (min co-occurrence={min_edge_weight})")
    return net


# ── View 2: Concept Neighbourhood ───────────────────────────────────────────

def build_neighbourhood(kg: dict, concept_name: str, hops: int = 2,
                        max_nodes: int = 300) -> Network:
    """
    All nodes reachable from a concept within N hops.
    Strips out semantic_similar edges to keep it readable (use hops=1 for those).
    """
    nodes_by_id = {n["id"]: n for n in kg["nodes"]}

    # Find seed concept node
    seed = None
    for n in kg["nodes"]:
        if n["type"] == "concept" and concept_name.lower() in (n.get("name") or "").lower():
            seed = n["id"]
            break
    if seed is None:
        print(f"ERROR: concept '{concept_name}' not found. Available concept names:")
        for n in kg["nodes"]:
            if n["type"] == "concept":
                print(f"  {n.get('name')}")
        sys.exit(1)

    # BFS
    SKIP_TYPES = {"semantic_similar", "contains"}
    adj: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for e in kg["edges"]:
        if e["type"] not in SKIP_TYPES:
            adj[e["source"]].append((e["target"], e["type"]))
            adj[e["target"]].append((e["source"], e["type"]))

    visited: set[str] = set()
    frontier = {seed}
    edge_set: list[dict] = []
    for _ in range(hops):
        next_frontier: set[str] = set()
        for node in frontier:
            if node in visited:
                continue
            visited.add(node)
            for neighbour, etype in adj[node]:
                if neighbour not in visited:
                    next_frontier.add(neighbour)
                    edge_set.append({"source": node, "target": neighbour, "type": etype})
        frontier = next_frontier
        if len(visited) + len(frontier) > max_nodes:
            break
    visited |= frontier

    print(f"  Neighbourhood of '{concept_name}' ({hops} hops): {len(visited)} nodes")

    net = Network(height="900px", width="100%", bgcolor="#1a1a2e", font_color="white",
                  heading=f"XAF Graph — '{concept_name}' neighbourhood ({hops} hops)")
    net.barnes_hut()

    for nid in visited:
        n = nodes_by_id.get(nid, {})
        ntype = n.get("type", "uid")
        label = n.get("title") or n.get("name") or nid.split(":")[-1][:40]
        size = 30 if nid == seed else (20 if ntype == "concept" else 10)
        border = "#ffffff" if nid == seed else COLOURS.get(ntype, "#aaaaaa")
        net.add_node(nid, label=label, title=f"[{ntype}] {label}",
                     color={"background": COLOURS.get(ntype, "#aaaaaa"), "border": border},
                     size=size)

    seen_edges: set[tuple] = set()
    for e in edge_set:
        key = (min(e["source"], e["target"]), max(e["source"], e["target"]), e["type"])
        if key not in seen_edges and e["source"] in visited and e["target"] in visited:
            seen_edges.add(key)
            net.add_edge(e["source"], e["target"],
                         title=e["type"],
                         color={"color": EDGE_COLOURS.get(e["type"], "#888888"), "opacity": 0.7})

    return net


# ── View 3: Hub Documents ────────────────────────────────────────────────────

def build_hub_docs(kg: dict, top_n: int = 40) -> Network:
    """
    Top hub documents by in-degree on the explicit links_to graph.
    """
    in_degree: Counter = Counter()
    out_degree: Counter = Counter()
    edge_list = []
    for e in kg["edges"]:
        if e["type"] == "links_to":
            in_degree[e["target"]] += 1
            out_degree[e["source"]] += 1
            edge_list.append(e)

    top_ids = {nid for nid, _ in in_degree.most_common(top_n)}
    top_ids |= {nid for nid, _ in out_degree.most_common(top_n // 2)}

    nodes_by_id = {n["id"]: n for n in kg["nodes"]}

    net = Network(height="900px", width="100%", bgcolor="#1a1a2e", font_color="white",
                  heading=f"XAF Knowledge Graph — Top {top_n} Hub Documents")
    net.barnes_hut(spring_length=200)

    for nid in top_ids:
        n = nodes_by_id.get(nid, {})
        label = (n.get("title") or nid.split("/")[-1])[:35]
        deg = in_degree[nid]
        size = max(10, min(60, deg * 2))
        net.add_node(nid, label=label,
                     title=f"{label}\nin-links: {in_degree[nid]}, out-links: {out_degree[nid]}",
                     color=COLOURS.get(n.get("type", "document"), "#f1a14e"), size=size)

    added = 0
    for e in edge_list:
        if e["source"] in top_ids and e["target"] in top_ids:
            net.add_edge(e["source"], e["target"],
                         color={"color": "#999999", "opacity": 0.5},
                         arrows="to")
            added += 1

    print(f"  Hub docs: {len(top_ids)} nodes, {added} edges")
    return net


# ── CLI ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Visualize XAF knowledge graph as interactive HTML")
    parser.add_argument("--view", choices=["concept-map", "neighbourhood", "hub-docs"],
                        default="concept-map", help="Which view to render")
    parser.add_argument("--concept", default="Security System",
                        help="Concept name for neighbourhood view")
    parser.add_argument("--hops", type=int, default=2,
                        help="Number of hops for neighbourhood view")
    parser.add_argument("--top", type=int, default=40,
                        help="Top N hubs for hub-docs view")
    parser.add_argument("--min-cooc", type=int, default=3,
                        help="Min co-occurrence for concept-map edges")
    parser.add_argument("--output", default=None,
                        help="Output HTML file path (default: outputs/<view>.html)")
    args = parser.parse_args()

    kg = load_kg()

    if args.view == "concept-map":
        net = build_concept_map(kg, min_edge_weight=args.min_cooc)
        out = args.output or str(OUT_DIR / "graph_concept_map.html")
    elif args.view == "neighbourhood":
        net = build_neighbourhood(kg, args.concept, args.hops)
        slug = args.concept.lower().replace(" ", "_")
        out = args.output or str(OUT_DIR / f"graph_neighbourhood_{slug}.html")
    else:
        net = build_hub_docs(kg, args.top)
        out = args.output or str(OUT_DIR / "graph_hub_docs.html")

    net.set_options("""
    {
      "interaction": {
        "hover": true,
        "tooltipDelay": 100,
        "navigationButtons": true,
        "keyboard": { "enabled": true }
      },
      "physics": {
        "stabilization": { "iterations": 200, "fit": true }
      }
    }
    """)

    net.save_graph(out)

    # Inject JS to freeze the graph once stabilization finishes.
    # Use binary mode so we don't care about the platform encoding pyvis used.
    raw = Path(out).read_bytes()
    freeze_js = (
        b"<script>\n"
        b"  network.once('stabilizationIterationsDone', function() {\n"
        b"    network.setOptions({ physics: { enabled: false } });\n"
        b"  });\n"
        b"</script>\n"
    )
    raw = raw.replace(b"</body>", freeze_js + b"</body>")
    Path(out).write_bytes(raw)

    print(f"\nSaved: {out}")
    print("Open this file in your browser to explore the graph.")


if __name__ == "__main__":
    main()
