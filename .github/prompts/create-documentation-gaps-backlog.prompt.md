## Plan: Generate Documentation Gaps Backlog

Create a single, up-to-date backlog document in `docs/` by re-running the existing gap report generators (where they exist) and adding one small “backlog generator” tool that consolidates the current pipeline outputs (taxonomy, doc concepts, semantic/classified pairs, explicit links, API mappings) into a prioritized Markdown backlog with clear acceptance criteria.

**Steps**
1. Refresh core pipeline-derived inputs (only if not already current)
   - Ensure Phase 13 artifacts exist and are current (knowledge graph build is already done per session summary).
   - Confirm these files exist before proceeding: `outputs/doc_concepts.parquet`, `outputs/topics_inventory.parquet`, `outputs/semantic_pairs.parquet`, `outputs/classified_pairs.parquet` (optional but preferred), `outputs/api_entities.parquet`, `outputs/api_implements_concept.parquet`, `outputs/explicit_graph.parquet`.

2. Rerun the existing “gap generator” reports (freshness requirement)
   - Run `python tools/coverage_matrix_xaf.py` to regenerate `outputs/coverage_reports/coverage_matrix.csv`, `high_priority_gaps.csv`, `missing_concepts.csv`, `summary_report.txt`.
   - Run `python query_graph.py --mode gaps > outputs/query_graph_gaps.txt` to capture current gap statistics (under-connected concepts, cross-corpus gaps, isolated sections). This script prints; redirect to a file for traceability.
   - Keep `tools/suggest_isolated_links.py` as an on-demand deep dive tool rather than running it for all concepts (it can be slow). We’ll surface “which concepts to run it for” in the backlog.

3. Add one new consolidator tool (new script)
   - Create `tools/generate_documentation_gaps_backlog.py` that reads the current outputs and writes a single Markdown backlog.
   - Inputs (read-only):
     - Taxonomy: `config/xaf-taxonomy.json`
     - Section concepts: `outputs/doc_concepts.parquet` (use only `kept == True`)
     - Explicit links: `outputs/explicit_graph.parquet` and/or `outputs/topics_inventory.parquet` (`internal_doc_links` if available)
     - Semantic edges: `outputs/semantic_pairs.parquet` (`gates_passed`, `neighbor_type`, `overlap_concepts`, `sim_score`)
     - Classified edges: `outputs/classified_pairs.parquet` (if present, for relationship-type breakdown)
     - API coverage: `outputs/api_entities.parquet` + `outputs/api_implements_concept.parquet`
     - Cross-linking suggestions (if present): `outputs/cross_linking_recommendations.csv`
     - Coverage matrix outputs from step 2.

4. Compute the backlog datasets inside the consolidator
   - Unused taxonomy concepts
     - Build `taxonomy_concepts` from `config/xaf-taxonomy.json`.
     - Build `used_concepts` from `doc_concepts.parquet` concepts among kept sections.
     - Emit: list of unused concepts and recommendation: add at least 1–3 anchor sections per concept OR merge/remove if obsolete.
   - Rare concepts (<5 kept sections)
     - Count sections per concept from kept `doc_concepts` and list concepts with count < 5.
     - Emit: top rare concepts (sorted ascending) and suggested remediation (targeted linking + add overview content).
   - Underlinked documents (regenerate, since prior CSV may be stale)
     - For each `doc_id`, compute `concept_count` (unique concepts across kept sections).
     - Compute `link_count` using explicit internal edges:
       - Prefer `explicit_graph.parquet` internal edges; if schema is inconvenient, fall back to `topics_inventory.parquet`’s `internal_doc_links` if present.
     - Compute `link_ratio = link_count / max(concept_count, 1)`.
     - Emit: a ranked list (lowest ratio first), plus a “zero-link” subset.
   - Missing descriptions
     - Prefer section-level description signal if available in `doc_concepts.parquet` or the phase-7/phase-9b artifacts:
       - If `outputs/article_descriptions.parquet` exists, use it to identify missing/empty descriptions.
       - Else, use `outputs/metadata_suggestions.parquet` columns (discover which column flags missing descriptions; implement a robust fallback based on null/empty strings).
     - Emit: counts + top documents with most missing descriptions.
   - Unmapped APIs
     - From `api_entities.parquet` compute total APIs.
     - From `api_implements_concept.parquet` compute mapped APIs (distinct `api_id`).
     - Emit: coverage %, count unmapped, and top namespaces/roots with the most unmapped APIs.
   - Semantic fallback rate
     - From `semantic_pairs.parquet`, define “fallback” as `gates_passed` contains `high_similarity_fallback` (and/or no overlap gates).
     - Emit: fallback percentage overall + breakdown by `neighbor_type` (cc/aa/ca/ac).
   - Cross-linking recommendations rollup
     - If `outputs/cross_linking_recommendations.csv` exists, include summary counts and top N actionable rows.

5. Write the backlog markdown document (requested output)
   - Create `docs/DOCUMENTATION_GAPS_BACKLOG.md` containing:
     - Header with generation timestamp and the exact input files used.
     - Executive summary: key metrics (unused concepts, rare concepts, underlinked docs, missing descriptions, unmapped APIs, fallback %).
     - Prioritized backlog sections (P0/P1/P2), each item with:
       - What/Why
       - Data evidence (counts, top offenders)
       - Acceptance criteria (measurable, e.g., reduce zero-link docs to 0; increase API mapping coverage to X%; reduce fallback to Y%).
     - “How to refresh” section listing the exact commands from step 2 + the new consolidator command.

6. Run and iterate
   - Run `python tools/generate_documentation_gaps_backlog.py`.
   - Review the produced Markdown for correctness and adjust thresholds (rare cutoff, underlinked criteria) if the lists are too noisy.

**Relevant files**
- `query_graph.py` — has `--mode gaps` for connectivity + isolated section counts (prints only).
- `tools/coverage_matrix_xaf.py` — regenerates ticket/coverage-driven gaps into `outputs/coverage_reports/`.
- `tools/suggest_isolated_links.py` — on-demand per-concept isolated-link suggestions.
- `scripts/02_build_explicit_graph.py` — source of `outputs/explicit_graph.parquet`.
- `config/xaf-taxonomy.json` — canonical concept vocabulary.
- `docs/DOCUMENTATION_GAPS_BACKLOG.md` — new backlog doc (deliverable).

**Verification**
1. Confirm refreshed artifacts exist: `outputs/coverage_reports/high_priority_gaps.csv` timestamp updates and `outputs/query_graph_gaps.txt` created.
2. Run `python tools/generate_documentation_gaps_backlog.py` and verify it writes `docs/DOCUMENTATION_GAPS_BACKLOG.md`.
3. Spot-check a few items:
   - An “unused concept” is truly absent from `doc_concepts.parquet`.
   - An “underlinked doc” has low explicit link count per `explicit_graph.parquet` / `internal_doc_links`.
   - API mapping coverage matches distinct counts from the two parquet files.

**Decisions**
- Backlog location: `docs/` (per your choice).
- Freshness: rerun `coverage_matrix_xaf.py` and capture `query_graph.py --mode gaps` output; regenerate underlinked stats inside the consolidator (no existing generator found).
- Scope included: unused concepts, rare concepts, underlinked docs, missing descriptions, unmapped APIs, semantic fallback, cross-linking recs.

**Further considerations**
1. Naming: keep a stable file (`docs/DOCUMENTATION_GAPS_BACKLOG.md`) vs a dated snapshot (`docs/DOCUMENTATION_GAPS_BACKLOG_YYYY-MM-DD.md`). Recommendation: stable file with generation timestamp to minimize clutter unless you explicitly want historical snapshots.
2. Underlinked definition: default to “concept_count ≥ 10 and link_ratio < 0.2” plus a “zero-link” subset; adjust after first run.
