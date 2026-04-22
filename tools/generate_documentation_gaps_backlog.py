#!/usr/bin/env python3
"""Generate a consolidated documentation gaps backlog markdown report."""

from __future__ import annotations

import argparse
import ast
import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = PROJECT_ROOT / "config"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"
DOCS_DIR = PROJECT_ROOT / "docs"


@dataclass
class BacklogData:
    taxonomy_count: int
    used_count: int
    unused_concepts: list[str]
    rare_concepts: list[tuple[str, int]]
    underlinked_docs: pd.DataFrame
    zero_link_docs: pd.DataFrame
    missing_desc_docs: pd.DataFrame
    missing_desc_count: int
    api_total: int
    api_mapped: int
    api_unmapped: int
    unmapped_namespace_roots: list[tuple[str, int]]
    semantic_total: int
    semantic_fallback: int
    semantic_fallback_pct: float
    fallback_by_neighbor: pd.DataFrame
    crosslink_count: int
    crosslink_top: pd.DataFrame
    critical_gap_count: int
    critical_gap_top: pd.DataFrame
    input_files: list[str]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate docs/DOCUMENTATION_GAPS_BACKLOG.md")
    parser.add_argument("--rare-cutoff", type=int, default=5, help="Concept section count threshold for rare concepts")
    parser.add_argument(
        "--underlinked-min-concepts",
        type=int,
        default=10,
        help="Minimum concept count for underlinked document candidates",
    )
    parser.add_argument(
        "--underlinked-ratio-threshold",
        type=float,
        default=0.2,
        help="Maximum link_ratio for an underlinked document",
    )
    parser.add_argument("--top-n", type=int, default=20, help="Default top-N rows per backlog section")
    parser.add_argument(
        "--output",
        type=Path,
        default=DOCS_DIR / "DOCUMENTATION_GAPS_BACKLOG.md",
        help="Output markdown file",
    )
    return parser.parse_args()


def load_taxonomy_concepts(path: Path) -> set[str]:
    with path.open("r", encoding="utf-8") as f:
        raw = json.load(f)
    return {
        c.get("name", "").strip()
        for c in raw.get("taxonomy", {}).get("concepts", [])
        if c.get("name", "").strip()
    }


def normalize_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    if isinstance(value, tuple):
        return list(value)
    if isinstance(value, set):
        return list(value)
    if hasattr(value, "tolist") and not isinstance(value, (str, bytes)):
        converted = value.tolist()
        if isinstance(converted, list):
            return converted
        if converted is None:
            return []
        return [converted]
    if value is None:
        return []
    if isinstance(value, float) and pd.isna(value):
        return []
    if isinstance(value, str):
        text = value.strip()
        if not text:
            return []
        if text.startswith("[") and text.endswith("]"):
            try:
                parsed = ast.literal_eval(text)
                if isinstance(parsed, list):
                    return parsed
            except (ValueError, SyntaxError):
                pass
        if "|" in text:
            return [chunk.strip() for chunk in text.split("|") if chunk.strip()]
        return [text]
    return [value]


def compute_concept_usage(doc_concepts: pd.DataFrame) -> tuple[set[str], pd.Series]:
    if "kept" in doc_concepts.columns:
        kept = doc_concepts[doc_concepts["kept"] == True].copy()
    else:
        kept = doc_concepts.copy()

    kept["concepts_norm"] = kept["concepts"].apply(normalize_list)
    exploded = kept.explode("concepts_norm")
    exploded["concepts_norm"] = exploded["concepts_norm"].astype(str).str.strip()
    exploded = exploded[exploded["concepts_norm"] != ""]

    used = set(exploded["concepts_norm"].unique())
    counts = exploded.groupby("concepts_norm")["section_id"].nunique().sort_values()
    return used, counts


def compute_doc_concept_count(doc_concepts: pd.DataFrame) -> pd.Series:
    if "kept" in doc_concepts.columns:
        kept = doc_concepts[doc_concepts["kept"] == True].copy()
    else:
        kept = doc_concepts.copy()
    kept["concepts_norm"] = kept["concepts"].apply(normalize_list)
    exploded = kept.explode("concepts_norm")
    exploded["concepts_norm"] = exploded["concepts_norm"].astype(str).str.strip()
    exploded = exploded[exploded["concepts_norm"] != ""]
    return exploded.groupby("doc_id")["concepts_norm"].nunique()


def compute_link_counts(explicit_graph: pd.DataFrame, topics_inventory: pd.DataFrame) -> pd.Series:
    if {"source_doc", "count"}.issubset(explicit_graph.columns):
        links = explicit_graph.groupby("source_doc")["count"].sum()
        links.index.name = "doc_id"
        return links

    if "internal_links" in topics_inventory.columns:
        tmp = topics_inventory[["doc_id", "internal_links"]].copy()
        tmp["link_count"] = tmp["internal_links"].apply(lambda v: len(normalize_list(v)))
        return tmp.set_index("doc_id")["link_count"]

    return pd.Series(dtype=float)


def compute_missing_descriptions(
    topics_inventory: pd.DataFrame,
    article_descriptions_path: Path,
    metadata_suggestions_path: Path,
    doc_concept_counts: pd.Series,
) -> tuple[pd.DataFrame, int]:
    # Descriptions are only meaningful for articles, not API reference docs
    articles_inv = topics_inventory[
        topics_inventory["doc_id"].str.contains("/raw_md/articles/", na=False)
    ]

    if article_descriptions_path.exists():
        article = pd.read_parquet(article_descriptions_path)
        article = article[["doc_id", "description"]].copy()
        article["description"] = article["description"].fillna("").astype(str)
        article["has_description"] = article["description"].str.strip() != ""

        docs = articles_inv[["doc_id", "path", "title"]].drop_duplicates().copy()
        merged = docs.merge(article[["doc_id", "has_description"]], on="doc_id", how="left")
        merged["has_description"] = merged["has_description"].fillna(False)
        missing = merged[merged["has_description"] == False].copy()
    elif metadata_suggestions_path.exists():
        meta = pd.read_parquet(metadata_suggestions_path)
        col = "suggested_description" if "suggested_description" in meta.columns else None
        if col is None:
            return pd.DataFrame(columns=["doc_id", "path", "title", "concept_count"]), 0
        grp = meta.groupby("doc_id")[col].apply(
            lambda s: any(str(v).strip() for v in s.fillna(""))
        )
        docs = articles_inv[["doc_id", "path", "title"]].drop_duplicates().copy()
        merged = docs.merge(grp.rename("has_description"), on="doc_id", how="left")
        merged["has_description"] = merged["has_description"].fillna(False)
        missing = merged[merged["has_description"] == False].copy()
    else:
        return pd.DataFrame(columns=["doc_id", "path", "title", "concept_count"]), 0

    missing["concept_count"] = missing["doc_id"].map(doc_concept_counts).fillna(0).astype(int)
    missing = missing.sort_values(["concept_count", "doc_id"], ascending=[False, True])
    return missing, int(len(missing))


def parse_gate_tokens(value: Any) -> list[str]:
    values = normalize_list(value)
    out: list[str] = []
    for v in values:
        text = str(v).strip()
        if not text:
            continue
        if "," in text:
            out.extend([part.strip() for part in text.split(",") if part.strip()])
        else:
            out.append(text)
    return out


def compute_semantic_fallback(semantic_pairs: pd.DataFrame) -> tuple[int, int, float, pd.DataFrame]:
    tmp = semantic_pairs[["neighbor_type", "gates_passed"]].copy()
    tmp["gate_tokens"] = tmp["gates_passed"].apply(parse_gate_tokens)
    tmp["is_fallback"] = tmp["gate_tokens"].apply(lambda gates: "high_similarity_fallback" in gates)

    total = int(len(tmp))
    fallback = int(tmp["is_fallback"].sum())
    pct = (100.0 * fallback / total) if total else 0.0

    by_neighbor = (
        tmp.groupby("neighbor_type")
        .agg(total_pairs=("is_fallback", "count"), fallback_pairs=("is_fallback", "sum"))
        .reset_index()
    )
    by_neighbor["fallback_pct"] = by_neighbor.apply(
        lambda r: (100.0 * r["fallback_pairs"] / r["total_pairs"]) if r["total_pairs"] else 0.0,
        axis=1,
    )
    by_neighbor = by_neighbor.sort_values("fallback_pct", ascending=False)
    return total, fallback, pct, by_neighbor


def compute_unmapped_apis(
    api_entities: pd.DataFrame,
    api_implements_concept: pd.DataFrame,
) -> tuple[int, int, int, list[tuple[str, int]]]:
    api_entities = api_entities.dropna(subset=["api_id"]).copy()
    api_implements_concept = api_implements_concept.dropna(subset=["api_id"]).copy()

    all_ids = set(api_entities["api_id"].astype(str))
    mapped_ids = set(api_implements_concept["api_id"].astype(str))
    unmapped_ids = all_ids - mapped_ids

    subset = api_entities[api_entities["api_id"].astype(str).isin(unmapped_ids)].copy()
    subset["namespace"] = subset.get("namespace", "").fillna("").astype(str)
    subset["namespace_root"] = subset["namespace"].apply(
        lambda n: n.split(".")[0].strip() if n.strip() else "(none)"
    )
    root_counts = (
        subset.groupby("namespace_root")["api_id"]
        .nunique()
        .sort_values(ascending=False)
    )
    roots = [(idx, int(val)) for idx, val in root_counts.items()]

    return int(len(all_ids)), int(len(mapped_ids)), int(len(unmapped_ids)), roots


def gather_inputs() -> dict[str, Path]:
    return {
        "taxonomy": CONFIG_DIR / "xaf-taxonomy.json",
        "doc_concepts": OUTPUTS_DIR / "doc_concepts.parquet",
        "topics_inventory": OUTPUTS_DIR / "topics_inventory.parquet",
        "explicit_graph": OUTPUTS_DIR / "explicit_graph.parquet",
        "semantic_pairs": OUTPUTS_DIR / "semantic_pairs.parquet",
        "classified_pairs": OUTPUTS_DIR / "classified_pairs.parquet",
        "api_entities": OUTPUTS_DIR / "api_entities.parquet",
        "api_implements": OUTPUTS_DIR / "api_implements_concept.parquet",
        "coverage_gaps": OUTPUTS_DIR / "coverage_reports" / "high_priority_gaps.csv",
        "article_descriptions": OUTPUTS_DIR / "article_descriptions.parquet",
        "metadata_suggestions": OUTPUTS_DIR / "metadata_suggestions.parquet",
        "crosslinks": OUTPUTS_DIR / "cross_linking_filtered_actionable.csv",
        "query_graph_gaps": OUTPUTS_DIR / "query_graph_gaps.txt",
    }


def validate_required(inputs: dict[str, Path]) -> None:
    required = [
        "taxonomy",
        "doc_concepts",
        "topics_inventory",
        "explicit_graph",
        "semantic_pairs",
        "api_entities",
        "api_implements",
        "coverage_gaps",
    ]
    missing = [key for key in required if not inputs[key].exists()]
    if missing:
        joined = ", ".join(f"{key}: {inputs[key]}" for key in missing)
        raise FileNotFoundError(f"Missing required inputs: {joined}")


def format_table(df: pd.DataFrame, columns: list[str], top_n: int) -> list[str]:
    if df.empty:
        return ["No rows."]
    view = df[columns].head(top_n).copy()

    def _fmt(value: Any) -> str:
        if isinstance(value, float):
            return f"{value:.3f}".rstrip("0").rstrip(".")
        return str(value)

    headers = [str(c) for c in columns]
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for _, row in view.iterrows():
        cells = [_fmt(row[c]).replace("\n", " ") for c in columns]
        out.append("| " + " | ".join(cells) + " |")
    return out


def build_backlog_data(args: argparse.Namespace) -> BacklogData:
    inputs = gather_inputs()
    validate_required(inputs)

    taxonomy = load_taxonomy_concepts(inputs["taxonomy"])
    doc_concepts = pd.read_parquet(inputs["doc_concepts"])
    topics_inventory = pd.read_parquet(inputs["topics_inventory"])
    explicit_graph = pd.read_parquet(inputs["explicit_graph"])
    semantic_pairs = pd.read_parquet(inputs["semantic_pairs"])
    api_entities = pd.read_parquet(inputs["api_entities"])
    api_implements = pd.read_parquet(inputs["api_implements"])
    critical_gaps = pd.read_csv(inputs["coverage_gaps"])

    used_concepts, concept_section_counts = compute_concept_usage(doc_concepts)
    unused_concepts = sorted(taxonomy - used_concepts)
    rare = concept_section_counts[concept_section_counts < args.rare_cutoff]
    rare_concepts = [(name, int(count)) for name, count in rare.items()]

    doc_concept_counts = compute_doc_concept_count(doc_concepts)
    doc_counts_df = doc_concept_counts.rename("concept_count").reset_index()

    link_counts = compute_link_counts(explicit_graph, topics_inventory)
    link_df = link_counts.rename("link_count").reset_index()

    docs_base = topics_inventory[["doc_id", "path", "title"]].drop_duplicates()
    underlinked = docs_base.merge(doc_counts_df, on="doc_id", how="left").merge(link_df, on="doc_id", how="left")
    underlinked["concept_count"] = underlinked["concept_count"].fillna(0).astype(int)
    underlinked["link_count"] = underlinked["link_count"].fillna(0).astype(int)
    underlinked["link_ratio"] = underlinked.apply(
        lambda r: (r["link_count"] / r["concept_count"]) if r["concept_count"] > 0 else 0.0,
        axis=1,
    )
    underlinked_ranked = underlinked[
        (underlinked["concept_count"] >= args.underlinked_min_concepts)
        & (underlinked["link_ratio"] < args.underlinked_ratio_threshold)
    ].sort_values(["link_ratio", "concept_count"], ascending=[True, False])

    zero_link = underlinked[
        (underlinked["concept_count"] >= args.underlinked_min_concepts)
        & (underlinked["link_count"] == 0)
    ].sort_values(["concept_count", "doc_id"], ascending=[False, True])

    missing_desc, missing_desc_count = compute_missing_descriptions(
        topics_inventory,
        inputs["article_descriptions"],
        inputs["metadata_suggestions"],
        doc_concept_counts,
    )

    api_total, api_mapped, api_unmapped, unmapped_roots = compute_unmapped_apis(api_entities, api_implements)

    sem_total, sem_fallback, sem_pct, sem_breakdown = compute_semantic_fallback(semantic_pairs)

    if inputs["crosslinks"].exists():
        crosslinks = pd.read_csv(inputs["crosslinks"])
        if "uid" in crosslinks.columns:
            crosslinks = crosslinks[crosslinks["uid"].notna()].copy()
        # Recent dataset is ticket-weighted and already filtered for actionability.
        sort_col = "realistic_score" if "realistic_score" in crosslinks.columns else crosslinks.columns[0]
        cross_top = crosslinks.sort_values(sort_col, ascending=False)
        cross_count = int(len(crosslinks))
    else:
        cross_top = pd.DataFrame()
        cross_count = 0

    existing = [str(path.relative_to(PROJECT_ROOT)) for path in inputs.values() if path.exists()]

    return BacklogData(
        taxonomy_count=len(taxonomy),
        used_count=len(used_concepts),
        unused_concepts=unused_concepts,
        rare_concepts=rare_concepts,
        underlinked_docs=underlinked_ranked,
        zero_link_docs=zero_link,
        missing_desc_docs=missing_desc,
        missing_desc_count=missing_desc_count,
        api_total=api_total,
        api_mapped=api_mapped,
        api_unmapped=api_unmapped,
        unmapped_namespace_roots=unmapped_roots,
        semantic_total=sem_total,
        semantic_fallback=sem_fallback,
        semantic_fallback_pct=sem_pct,
        fallback_by_neighbor=sem_breakdown,
        crosslink_count=cross_count,
        crosslink_top=cross_top,
        critical_gap_count=int(len(critical_gaps)),
        critical_gap_top=critical_gaps.sort_values("ticket_count", ascending=False),
        input_files=existing,
    )


def write_backlog(args: argparse.Namespace, data: BacklogData) -> None:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    api_cov_pct = (100.0 * data.api_mapped / data.api_total) if data.api_total else 0.0

    lines: list[str] = []
    lines.append("# Documentation Gaps Backlog")
    lines.append("")
    lines.append(f"Generated: {now}")
    lines.append("")
    lines.append("## Input Files")
    for path in data.input_files:
        lines.append(f"- {path}")

    lines.append("")
    lines.append("## Executive Summary")
    lines.append(f"- Unused taxonomy concepts: {len(data.unused_concepts)} / {data.taxonomy_count}")
    lines.append(f"- Rare concepts (<{args.rare_cutoff} kept sections): {len(data.rare_concepts)}")
    lines.append(
        f"- Underlinked docs (concept_count >= {args.underlinked_min_concepts} and link_ratio < {args.underlinked_ratio_threshold:.2f}): {len(data.underlinked_docs)}"
    )
    lines.append(f"- Zero-link docs (same concept threshold): {len(data.zero_link_docs)}")
    lines.append(f"- Missing descriptions: {data.missing_desc_count}")
    lines.append(f"- API mapping coverage: {data.api_mapped}/{data.api_total} ({api_cov_pct:.1f}%)")
    lines.append(f"- Semantic fallback rate: {data.semantic_fallback}/{data.semantic_total} ({data.semantic_fallback_pct:.1f}%)")
    lines.append(f"- High-priority ticket-driven gaps: {data.critical_gap_count}")
    lines.append(f"- Cross-linking recommendations available: {data.crosslink_count}")

    lines.append("")
    lines.append("## P0 - Immediate Priority")
    lines.append("")
    lines.append("### Item P0.1 - Resolve Ticket-Driven Critical Gaps")
    lines.append("- What: Close high-volume support concepts flagged as critical gaps.")
    lines.append("- Why: These concepts have high ticket demand but insufficient documentation depth.")
    lines.append(f"- Data evidence: {data.critical_gap_count} critical gaps from coverage matrix.")
    lines.append("- Acceptance criteria:")
    lines.append("  - Reduce critical gaps by at least 30% in the next refresh.")
    lines.append("  - Each resolved concept has at least one overview page and one task-oriented page.")
    lines.append("  - coverage_reports/high_priority_gaps.csv count is lower than the current baseline.")
    lines.extend(format_table(data.critical_gap_top, ["concept_name", "ticket_count", "doc_score", "coverage_class"], args.top_n))

    lines.append("")
    lines.append("### Item P0.2 - Fix Underlinked High-Concept Documents")
    lines.append("- What: Add internal links for concept-dense documents with very low link_ratio.")
    lines.append("- Why: Discoverability and navigability are bottlenecked by sparse explicit linking.")
    lines.append(
        f"- Data evidence: {len(data.underlinked_docs)} underlinked docs, including {len(data.zero_link_docs)} zero-link docs."
    )
    lines.append("- Acceptance criteria:")
    lines.append("  - Zero-link docs in this bucket reduced to 0.")
    lines.append("  - Median link_ratio for this bucket reaches at least 0.5.")
    lines.append("  - No doc with concept_count >= threshold remains below link_ratio 0.1.")
    lines.extend(format_table(data.underlinked_docs, ["doc_id", "concept_count", "link_count", "link_ratio", "path"], args.top_n))

    lines.append("")
    lines.append("### Item P0.3 - Improve API-to-Concept Mapping")
    lines.append("- What: Map unmapped APIs to taxonomy concepts, prioritizing heavy namespaces.")
    lines.append("- Why: Unmapped APIs weaken semantic connections and concept-level coverage analytics.")
    lines.append(
        f"- Data evidence: {data.api_unmapped} unmapped APIs out of {data.api_total} total ({api_cov_pct:.1f}% mapped)."
    )
    lines.append("- Acceptance criteria:")
    lines.append("  - Raise API mapping coverage to at least 90%.")
    lines.append("  - Top 5 unmapped namespace roots each reduced by at least 50%.")
    lines.append("  - Regenerated api_implements_concept.parquet includes new mappings.")
    if data.unmapped_namespace_roots:
        root_df = pd.DataFrame(data.unmapped_namespace_roots, columns=["namespace_root", "unmapped_api_count"])
        lines.extend(format_table(root_df, ["namespace_root", "unmapped_api_count"], args.top_n))
    else:
        lines.append("No unmapped API namespace roots found.")

    lines.append("")
    lines.append("## P1 - High Value Next")
    lines.append("")
    lines.append("### Item P1.1 - Handle Unused Taxonomy Concepts")
    lines.append("- What: Either add anchor documentation for unused concepts or deprecate/merge obsolete concepts.")
    lines.append("- Why: Unused taxonomy nodes indicate vocabulary drift or missing content coverage.")
    lines.append(f"- Data evidence: {len(data.unused_concepts)} concepts appear nowhere in kept doc concepts.")
    lines.append("- Acceptance criteria:")
    lines.append("  - For each retained concept, add 1-3 anchor sections with explicit concept tags.")
    lines.append("  - Or remove/merge obsolete concepts in config/xaf-taxonomy.json with rationale.")
    for concept in data.unused_concepts[: args.top_n]:
        lines.append(f"- {concept}")
    if len(data.unused_concepts) > args.top_n:
        lines.append(f"- ... and {len(data.unused_concepts) - args.top_n} more")

    lines.append("")
    lines.append("### Item P1.2 - Expand Rare Concepts")
    lines.append("- What: Increase depth and cross-linking for concepts with sparse section coverage.")
    lines.append("- Why: Low section counts reduce retrieval confidence and concept discoverability.")
    lines.append(f"- Data evidence: {len(data.rare_concepts)} concepts have < {args.rare_cutoff} kept sections.")
    lines.append("- Acceptance criteria:")
    lines.append("  - No active concept remains below the rare threshold without an explicit exception.")
    lines.append("  - Each rare concept gains at least one overview and one linked task/reference section.")
    if data.rare_concepts:
        rare_df = pd.DataFrame(data.rare_concepts, columns=["concept_name", "section_count"])
        lines.extend(format_table(rare_df, ["concept_name", "section_count"], args.top_n))
    else:
        lines.append("No rare concepts under current threshold.")

    lines.append("")
    lines.append("### Item P1.3 - Fill Missing Descriptions")
    lines.append("- What: Add concise descriptions for docs missing metadata summaries.")
    lines.append("- Why: Missing descriptions degrade search snippets, metadata quality, and triage UX.")
    lines.append(f"- Data evidence: {data.missing_desc_count} docs missing descriptions.")
    lines.append("- Acceptance criteria:")
    lines.append("  - Missing description count reduced by at least 70%.")
    lines.append("  - Remaining missing entries are intentional (redirect/index/special pages).")
    lines.extend(format_table(data.missing_desc_docs, ["doc_id", "concept_count", "path", "title"], args.top_n))

    lines.append("")
    lines.append("## P2 - Optimization")
    lines.append("")
    lines.append("### Item P2.1 - Reduce Semantic Fallback Dependence")
    lines.append("- What: Increase concept/API overlap links so fewer pairs rely on high_similarity_fallback.")
    lines.append("- Why: Fallback-heavy linkage is less explainable and can be lower precision.")
    lines.append(
        f"- Data evidence: fallback appears in {data.semantic_fallback}/{data.semantic_total} pairs ({data.semantic_fallback_pct:.1f}%)."
    )
    lines.append("- Acceptance criteria:")
    lines.append("  - Reduce fallback rate by at least 20% relative.")
    lines.append("  - Each neighbor_type bucket shows non-increasing fallback share.")
    lines.extend(format_table(data.fallback_by_neighbor, ["neighbor_type", "total_pairs", "fallback_pairs", "fallback_pct"], args.top_n))

    lines.append("")
    lines.append("### Item P2.2 - Execute Cross-Link Recommendation Queue")
    lines.append("- What: Process top ticket-weighted actionable cross-link suggestions into explicit internal links.")
    lines.append("- Why: Recommendations identify high-yield links that improve navigation and are weighted by customer pain.")
    lines.append(f"- Data evidence: {data.crosslink_count} recommendation rows available.")
    lines.append("- Acceptance criteria:")
    lines.append("  - Complete top 50 recommendations and regenerate explicit_graph.parquet.")
    lines.append("  - Recomputed underlinked bucket shrinks by at least 25%.")
    if data.crosslink_count:
        cols = [
            c
            for c in [
                "uid",
                "title",
                "realistic_score",
                "ticket_weight",
                "ticket_count",
                "num_actual_useful_apis",
                "path",
            ]
            if c in data.crosslink_top.columns
        ]
        if cols:
            lines.extend(format_table(data.crosslink_top, cols, args.top_n))
    else:
        lines.append("No recent actionable cross-linking file detected (outputs/cross_linking_filtered_actionable.csv).")

    lines.append("")
    lines.append("## How To Refresh")
    lines.append("1. `$env:PYTHONUTF8=1; & .venv\\Scripts\\python.exe tools/coverage_matrix_xaf.py`")
    lines.append("2. `$env:PYTHONUTF8=1; & .venv\\Scripts\\python.exe query_graph.py --mode gaps | Out-File outputs/query_graph_gaps.txt -Encoding utf8`")
    lines.append("3. `$env:PYTHONUTF8=1; & .venv\\Scripts\\python.exe tools/generate_documentation_gaps_backlog.py`")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    args = parse_args()
    data = build_backlog_data(args)
    write_backlog(args, data)
    print(f"Wrote backlog: {args.output}")


if __name__ == "__main__":
    main()
