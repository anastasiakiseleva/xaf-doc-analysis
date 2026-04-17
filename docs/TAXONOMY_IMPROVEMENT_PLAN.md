# Taxonomy Improvement Plan

**Goal:** Fully utilize the rich `xaf-taxonomy.json` structure (domain, subdomain,
artifact_kind, facets, relations, api_surface, doc_intents) in scripts that currently
consume only 5 flat fields (name, synonyms, keywords, description, parent).

**Execution order:** A → B → C → D (each builds on the previous)

---

## Phase A — `utils/taxonomy_loader.py` (foundation)

All other phases depend on this.

- [X] **A1** Add `load_taxonomy_index()` — richer dict keyed by concept name with
  pre-computed domain, subdomain, artifact_kind, facets, api_surface, doc_intents,
  and resolved relation names (part_of, is_a, requires, related_to, replaces +
  computed inverses has_part, has_kind)
- [X] **A2** Add `get_concept_context_string(name)` — returns a rich text blob for
  semantic embedding:
  `"{name}. {description}. Also known as: {synonyms}. Key APIs: {primary_types}. Domain: {domain}/{subdomain}."`
- [X] **A3** Add `get_platform_concepts(platform)` — returns concept names whose
  `facets.platforms` includes the given platform

**Verify:** `python tests/test_taxonomy_loader.py` (new file)
- All 148 concepts produce non-empty context strings
- Relations resolve correctly (IDs → names)
- Platform filter returns expected subsets

---

## Phase B — `scripts/03_extract_concepts.py` (concept extraction)

*Depends on Phase A.*

- [X] **B0** Fix import bug in `scripts/test_semantic_extraction.py` — missing
  `from sentence_transformers import SentenceTransformer` on line 86; also removed
  import of non-existent `enhanced_concept_extraction` module; rewired to use
  `extract_concepts_semantic` + `compile_concept_index` from the real script via importlib
- [X] **B1** Replace hardcoded `AMBIGUOUS_CONCEPTS` set with taxonomy-driven logic —
  `_build_ambiguous_concepts(concepts_config)` flags feature/module/conceptual/pattern
  concepts with ≤ 2 `primary_types` as ambiguous; result cached in `_get_ambiguous_concepts()`
- [X] **B2** Use `get_concept_context_string()` in `_validate_concept_semantically()`
  instead of current minimal `"{name}. {description}. {synonyms[:3]}"` — richer
  embedding context improves precision for ambiguous concept matching
- [X] **B3** Replace 3-concept if/elif dispatch with single `_check_domain_coherence()`
  — delegates to specialized functions for known concepts, applies generic taxonomy
  keyword/primary_types signal check for all others (self-extending as taxonomy grows)
- [X] **B4** Carry extra taxonomy fields through to `doc_concepts.parquet` output:
  `concept_domains`, `concept_subdomains`, `concept_artifact_kinds`, `concept_audiences`
  (dicts keyed by concept name, same pattern as `concept_confidences`)

**Tests added:** `tests/test_extract_concepts.py` — 28 tests, 0 failed

**Verify:**
- `python scripts/test_semantic_extraction.py` — deployment false-positive suppression still works
- `python scripts/03_extract_concepts.py --sample 100` — new columns present in output
- `python tests/test_pipeline_integration.py --phase 3` — passes

---

## Phase C — `scripts/04_make_sections_embeddings.py` (embeddings)

*Depends on Phase B (needs new parquet columns from doc_concepts.parquet).*

> ⚠️ Re-embedding invalidates `semantic_pairs.parquet` — Phase 5 must be re-run after.

- [X] **C1** Enriched `assemble_text()` — appends `"Concepts: {name} ({domain}), …"` line
  after body text (after truncation, so the line is always present); uses `concept_domains`
  dict from the Phase-B4 parquet columns. Capped at 20 concepts to respect token budgets.
- [X] **C2** For API sections (`is_api=True`), prepends `"API: {sym1}, {sym2}, …"` before
  title/heading using the `apis` column from `doc_concepts.parquet` (sorted, deduped, ≤ 30
  symbols). Improves cross-corpus (API ↔ conceptual) retrieval.
- [X] **C3** Added `--no-concept-context` flag (`store_true`, default `False`). When set,
  both C1 and C2 are skipped — backwards-compatible baseline and A/B quality comparison.
  Also extracted a module-level `_safe_list()` helper used in the main records loop.

**Tests added:** `tests/test_make_sections_embeddings.py` — 24 tests, 0 failed

**Verify:**
- `python scripts/04_make_sections_embeddings.py --sample 200` — no crash, embedding
  dim still 384
- Unit test: `assemble_text()` output contains concept names when context is enabled

---

## Phase D — `scripts/06_classify_relationships.py` (LLM classification)

*Depends on Phase A only (taxonomy index). Can be implemented in parallel with C.*

- [X] **D1** Load taxonomy index once at startup in `main()`, pass as argument to
  `classify_pairs()` — eliminates per-call overhead
- [X] **D2** Inject **Taxonomy Context** block into each LLM prompt containing:
  - Known taxonomy relations between the two sections' concepts
    (e.g. "Security System requires Authentication")
  - Shared domain / subdomain
  - Platform scope overlap or mismatch note (from `facets.platforms`)
  - Audience mismatch note (from `facets.audiences`)
- [X] **D3** Add Phase 6 thresholds to `config/validation_thresholds.yml`:
  - `max_related_to_fraction: 0.65`
  - `min_avg_confidence: 0.70`
  - `min_actionable_fraction: 0.35`

**Tests added:** `tests/test_classify_relationships.py` — 19 tests, 0 failed (150 total across A–D)

**Verify:**
- `python scripts/06_classify_relationships.py --provider mock --limit 20` — prompt
  output contains "Taxonomy Context" block
- `related_to` fraction and avg confidence validated against new thresholds

---

## New Files Created by This Plan

| File | Phase | Purpose |
|---|---|---|
| `tests/test_taxonomy_loader.py` | A | Unit tests for loader additions |

---

## Decisions & Notes

- All changes are **additive/backward-compatible** — new columns in parquet, new flags
  default to improved behavior, no existing outputs removed
- Phase C re-embedding is expensive (~30 min GPU). `--no-concept-context` flag enables
  A/B comparison without fully committing to re-running Phase 5
- Taxonomy context in Phase D is a **new prompt section** added alongside the existing
  section-type and relationship-definition logic — not a replacement
- Hardcoded coherence functions for Deployment/Testing/Migration are kept until B3
  proves the generic approach matches or exceeds their behavior

---

## Open Questions

1. **Phase C cascade**: Re-embedding invalidates Phase 5 (semantic_pairs). Should
   Phase 5 run automatically after C, or be a separate manual step?
2. **Phase D cost**: Taxonomy context adds ~200 tokens/call (~$2–3 on a full re-run of
   3,076 pairs). Is this acceptable before knowing whether it improves `related_to` %?
3. **Phase 7 integration**: Should `concept_audiences` from `facets` directly override
   `classify_proficiency()` for concepts where it is explicitly set in the taxonomy?
   (e.g. a concept tagged `audiences: [beginner]` would always yield Beginner,
   bypassing heuristics)
