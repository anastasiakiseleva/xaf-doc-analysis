# What's New

## 2026-04-23 — Product-agnostic configuration layer

### Motivation

All product-specific values (taxonomy filename, support ticket paths, namespace→concept mappings, noise concept lists, DevExpress URL rules) were hardcoded in Python source files. Tech writers from other product teams could not reuse the pipeline without editing Python.

---

### New files

**`config/product.yml`** — single source of truth for product identity and per-product settings:
- `product.name`, `product.taxonomy_file`, `product.support_tickets_file`, `product.support_concept_map`
- `paths.raw_docs_root` — root directory for raw markdown source files
- `parsing.api_path_marker` — directory name segment that identifies API docs in `doc_id` paths
- `filtering.noise_concepts` — concepts too generic for meaningful semantic relationships
- `coverage.priority_gap_concepts` — concepts flagged as priority documentation gaps

**`config/patterns.yml`** — product-specific pattern rules:
- `external_url_rules` — URL classification rules for unresolved external UIDs (moved from `DEFAULT_URL_RULES` in `02_build_explicit_graph.py`); DevExpress namespace buckets (`xtrareports`, `xpo`, `corelibs`) are now entries here
- `namespace_concept_map` — namespace segment → taxonomy concept name (moved from `build_namespace_concept_map()` in `12_map_apis_to_concepts.py`); all 28 XAF entries are now in YAML

**`scripts/config_loader.py`** — central typed accessor module. Exposes two singletons:
- `cfg` (`_Cfg`) — accessors for `product.yml`: `taxonomy_path()`, `support_tickets_path()`, `support_concept_map_path()`, `raw_docs_root()`, `api_path_marker()`, `noise_concepts()`, `priority_gap_concepts()`
- `patterns` (`_Patterns`) — accessors for `patterns.yml`: `external_url_rules()`, `namespace_concept_map()`

Both objects cache their YAML file on first access (`@lru_cache`).

---

### Script changes

| File | Change |
|---|---|
| `scripts/02_build_explicit_graph.py` | Removed 4 DevExpress entries from `DEFAULT_URL_RULES`; they now live in `config/patterns.yml` |
| `scripts/05_5_filter_high_value_pairs.py` | `NOISE_CONCEPTS` frozenset replaced with `cfg.noise_concepts()` |
| `scripts/12_map_apis_to_concepts.py` | `build_namespace_concept_map()` body replaced with `patterns.namespace_concept_map()` |
| `scripts/13_build_knowledge_graph.py` | Graph metadata `"project"` key derived from taxonomy filename via config instead of hardcoded string |
| `scripts/_sc_inspect.py` | Rewritten: uses `cfg.taxonomy_path()`; accepts `--concept NAME` CLI arg (repeatable) instead of hardcoded list; path no longer absolute |
| `scripts/_sc_validate.py` | Replaced absolute Windows path to taxonomy with `cfg.taxonomy_path()` |
| `tools/coverage_matrix_xaf.py` → `tools/coverage_matrix.py` | Renamed; `TAXONOMY_JSON`, `SUPPORT_MAP_YML`, `TICKET_JSON` constants replaced with `cfg` accessors; `main()` prints product name from config |
| `tools/package_mvp_deliverables.py` | Hardcoded gap concepts list replaced with `cfg.priority_gap_concepts()` |

---

### To adapt for a new product

1. Copy `config/product.yml` and `config/patterns.yml`.
2. Edit `product.yml` — set `product.name`, point the three `*_file` keys at your own taxonomy/tickets/support-map files, update `noise_concepts` and `priority_gap_concepts`.
3. Edit `patterns.yml` — replace `external_url_rules` and `namespace_concept_map` entries with your product's namespace conventions.
4. Run the pipeline. No Python changes required.

---

## 2026-04-20 — Phase 5 xref gate + taxonomy-only tags in Phase 10

### Motivation

Two independent gaps were identified:

1. **Phase 5 (semantic pairs) never surfaced cross-corpus pairs for articles that explicitly link to API pages** — even when the article has dozens of `xref:` links to specific controller/action API members. The NN-based cosine similarity search was the only path to pair generation; if an API section wasn't in the top-K neighbors for a conceptual section, the editorial link was silently ignored.

2. **Phase 10 (document metadata rollup) was producing tags from raw API short names and generic type labels** (`securitystrategy`, `viewcontroller`, `how-to`, `api-reference`) instead of canonical taxonomy concept names. Tags had no semantic alignment with the taxonomy and were not useful for filtering or discovery.

---

### Change 1 — `scripts/05_find_semantic_pairs.py`: xref direct-pairs pass

**Root-cause diagnosis:** Running `concept_drilldown.py --concept "Built-in Controllers"` showed 0 cross-corpus pairs despite the article linking to ~100 API members. The NN search (`--topk-ca 10`) only evaluates pairs the embedding search surfaces; if the xref-linked API section isn't in the top-K, the gate never fires.

**New `generate_xref_pairs()` function** — a dedicated second pass that generates C→A pairs directly from editorial `xref:` links, completely bypassing the NN search:

1. `build_xref_index()` loads `topics_inventory.parquet` and builds:
   - `doc_to_links`: `{doc_id → set of xref UIDs}`
   - `doc_to_uid`: `{doc_id → its own uid}`
2. After the four NN passes (C→C, A→A, C→A, A→C), `generate_xref_pairs()` iterates every conceptual section, looks up which API sections have UIDs matching the doc's xref links, computes cosine similarity via dot product on pre-normalised matrices, and emits pairs above `--xref-min-sim` (default `0.50`).
3. Results are deduplicated against the NN-found pairs before appending; `gates_passed=["xref_link"]`.
4. `--no-xref-gate` flag disables the entire xref pass for backwards compatibility.

**New CLI args:**

| Flag | Default | Purpose |
|---|---|---|
| `--xref-min-sim` | `0.50` | Min cosine similarity for xref pairs (lower than NN thresholds; editorial links are trusted) |
| `--no-xref-gate` | `False` | Skip the xref pass entirely |

**Results after re-run:**

| Metric | Before | After |
|---|---|---|
| Total cross-corpus pairs | 7,383 | 17,853 (+142%) |
| xref_link pairs generated | 0 | 10,179 (6,317 net-new after dedup) |
| Isolated sections | 923 (8.5%) | 579 (5.4%) |
| Concepts with zero cross-corpus links | 49 | 47 |

**Encoding fix:** All Unicode arrows and emoji in `print()` statements and argparse help strings replaced with plain ASCII; `tqdm` calls use `ascii=True` to avoid cp1252 garbling on Windows consoles.

---

### Change 2 — `scripts/10_rollup_document_metadata.py`: taxonomy-only tags

**`_build_taxonomy_tag_set()`** — new module-level function, called once at import time. Loads all 148 canonical concept names from `xaf-taxonomy.json` via `load_concepts()` and normalises them using the same rules as Phase 7's `normalize_tag()` (lowercase, spaces→hyphens, dots removed, non-alphanumeric stripped). Returns a `set` of 148 allowed tag strings.

**`aggregate_tags()` updated** — tags that are not in `_TAXONOMY_TAGS` are silently dropped before frequency counting. The fallback `if not _TAXONOMY_TAGS` preserves original behaviour if the taxonomy fails to load.

**Results:**

| Metric | Before | After |
|---|---|---|
| Top tag | `securitystrategy` (raw API name) | `application-model` (taxonomy concept) |
| Avg tags per doc | ~8 | 0.86 |
| Docs with zero tags | ~100 | 3,167 |

The zero-tag increase is expected and correct: ~57% of docs are API reference pages whose sections were only tagged with API short names and type labels in Phase 3 — none of which are taxonomy concepts. This surfaces the underlying Phase 3 gap (API docs not being labelled with concept names) rather than hiding it behind noisy tags.

**`config/validation_thresholds.yml`** — `phase10_rollup` thresholds updated to reflect the stricter tag policy:

| Threshold | Old | New |
|---|---|---|
| `min_avg_tags` | `3.0` | `0.5` |
| `max_docs_zero_tags` | `100` | `4000` |
| `min_docs_with_tags` | `5000` | `2000` |

---

## 2026-04-17 — Taxonomy Improvement Plan (Phases A–D): fully utilise `xaf-taxonomy.json` across the pipeline


### Motivation

Five pipeline scripts were consuming only five flat fields from `xaf-taxonomy.json` (`name`, `synonyms`, `keywords`, `description`, `parent`), leaving domain, subdomain, artifact_kind, facets, relations, and api_surface unused. This improvement plan wires the full taxonomy structure into concept extraction, embedding assembly, and LLM relationship classification.

---

### Phase A — `utils/taxonomy_loader.py` (foundation)

Three new public functions added; all downstream phases build on them.

| Function | Purpose |
|---|---|
| `load_taxonomy_index()` | Returns a `dict[name → flat_dict]` with every concept pre-flattened including resolved relation names, facets, api_surface, and computed inverse relations (`has_part`, `has_kind`). Result is module-level cached. |
| `get_concept_context_string(name)` | Returns a rich text blob suitable for semantic embedding: `"{name}. {description}. Also known as: {synonyms}. Key APIs: {primary_types}. Domain: {domain}/{subdomain}."` |
| `get_platform_concepts(platform)` | Returns concept names whose `facets.platforms` includes the given platform value. |

**Tests:** `tests/test_taxonomy_loader.py` — 79 passed, 4 skipped (intentional missing-data cases).

---

### Phase B — `scripts/03_extract_concepts.py` (concept extraction)

**B0 — Fix broken test harness:** `scripts/test_semantic_extraction.py` was importing a non-existent `enhanced_concept_extraction` module and was missing `from sentence_transformers import SentenceTransformer`. Rewritten to load `03_extract_concepts.py` via `importlib` and call the real `extract_concepts_semantic` + `compile_concept_index` functions directly.

**B1 — Taxonomy-driven ambiguous-concept detection:** Replaced the hardcoded 20-entry `AMBIGUOUS_CONCEPTS` set with `_build_ambiguous_concepts(concepts_config)`, which flags feature/module/conceptual/pattern concepts with ≤ 2 `primary_types` as needing semantic disambiguation. Result is module-level cached via `_get_ambiguous_concepts()`. The set self-extends as the taxonomy grows.

**B2 — Richer semantic validation anchor:** `_validate_concept_semantically()` now calls `get_concept_context_string(concept_name)` instead of building a minimal `"{name}. {description}. {synonyms[:3]}"` string. The richer anchor improves precision for ambiguous concept matching.

**B3 — Generic `_check_domain_coherence()`:** Replaced the three-concept `if/elif` dispatch (`Deployment`, `Testing`, `Migration`) with a single `_check_domain_coherence(concept_name, text, heading, base_confidence, concept_def)` function. The function delegates to the four existing specialized helpers (`_check_deployment_context`, `_check_testing_context`, `_check_migration_context`, `_check_application_templates_context`) and, for all other ambiguous concepts, applies a generic signal check: if none of the concept's `keywords` or `primary_types` appear in the section text, confidence is reduced by 20%. Self-extending as the taxonomy grows.

**B4 — Extra taxonomy columns in `doc_concepts.parquet`:** The main loop now writes four additional dict columns keyed by concept name — `concept_domains`, `concept_subdomains`, `concept_artifact_kinds`, `concept_audiences` — matching the pattern of the existing `concept_confidences` column. Used in Phase C to enrich embedding text without reloading the taxonomy.

**Pipeline result:** Phase 3 re-run over 11,584 sections → 10,819 kept (93.4%). Phase 3 validation threshold `min_avg_concepts_per_section` recalibrated from `1.5` → `0.5` (see below).

**Tests:** `tests/test_extract_concepts.py` — 28 passed (107 total).

---

### Phase C — `scripts/04_make_sections_embeddings.py` (embedding enrichment)

**C1 — Concept context line:** `assemble_text()` appends `"Concepts: Name (domain), …"` (≤ 20 concepts) after the body text and after the `max_chars` truncation, so the line is always present even for very long sections.

**C2 — API symbol prefix:** For `is_api=True` sections with a populated `apis` column, `assemble_text()` prepends `"API: sym1, sym2, …"` (sorted, deduped, ≤ 30 symbols) before the title. Improves cross-corpus (API ↔ conceptual) retrieval precision.

**C3 — `--no-concept-context` flag:** `store_true`, default `False`. When set, both C1 and C2 are skipped — fully backwards-compatible and enables A/B quality comparison.

**Module helper:** Module-level `_safe_list(val)` coerces pyarrow/numpy list-like parquet values to plain Python lists. Used throughout the main records loop.

**Result of Phase 4 re-run:** 5,026 conceptual sections + 5,793 API sections embedded at dim=384. Cache grew from 15,057 → 19,025 entries (1,996 + 2,004 new).

**Tests:** `tests/test_make_sections_embeddings.py` — 24 passed (131 total).

---

### Phase D — `scripts/06_classify_relationships.py` (LLM classification)

**D1 — Load taxonomy index once:** `load_taxonomy_index()` is called once in `main()` after the supporting data is loaded, and forwarded as a `taxonomy_index=` keyword argument to `classify_pairs()`. Eliminates per-pair overhead; `classify_pairs()` defaults `taxonomy_index=None` for backwards compatibility.

**D2 — Taxonomy Context block in LLM prompts:** New `build_taxonomy_context(source_concepts, target_concepts, taxonomy_index)` function generates a `## Taxonomy Context` Markdown block injected into every classification prompt. Four categories of signal:

- **Known relations** — any directed relation declared in the taxonomy between the pair's concept sets (e.g. "Security System requires Authentication")
- **Shared domain / subdomain** — when both sections' concepts share a domain or subdomain
- **Platform scope overlap / mismatch** — compares `facets.platforms` sets; reports overlap or an explicit cross-platform mismatch
- **Audience mismatch** — reports when the audience sets differ (e.g. `developer` vs `advanced-developer`)

When none of these signals apply, the block is omitted entirely — the prompt is unchanged from the baseline.

**D3 — Phase 6 validation thresholds** added to `config/validation_thresholds.yml`:

| Threshold | Value | Rationale |
|---|---|---|
| `max_related_to_fraction` | `0.65` | Catch-all `related_to` should not dominate the output |
| `min_avg_confidence` | `0.70` | LLM must be reasonably confident in its classifications |
| `min_actionable_fraction` | `0.35` | At least 35% of pairs should get a specific type |

**Tests:** `tests/test_classify_relationships.py` — 19 passed (150 total across all phases).

---

### Threshold recalibration

`phase3_concepts.min_avg_concepts_per_section` changed from `1.5` → `0.5` in `config/validation_thresholds.yml`. The observed overall average after the Phase B1 taxonomy-driven ambiguity filter is `0.66`. This is structurally correct: ~63% of kept sections are API reference pages that legitimately carry zero concepts; sections that do match concepts average ~1.78. The old threshold was calibrated when all sections were in scope.

---

### Test summary

| Test file | New tests | Running total |
|---|---|---|
| `tests/test_taxonomy_loader.py` | 79 | 79 |
| `tests/test_extract_concepts.py` | 28 | 107 |
| `tests/test_make_sections_embeddings.py` | 24 | 131 |
| `tests/test_classify_relationships.py` | 19 | 150 |

All 150 pass; 4 skipped (intentional missing-data cases in taxonomy loader tests).

---

## 2026-04-17 — Taxonomy quality pass: `api_surface.primary_types` corrected against XAF API

### Problem

A review of `api_surface.primary_types` across all 148 concepts in `config/xaf-taxonomy.json` against **Hedden's *The Accidental Taxonomist* §4.3**, **ANSI/NISO Z39.19**, and the **W3C SKOS Primer** found that many entries were not valid API type identifiers. Six violation categories were identified:

1. **File format / extension** — `XAFML` is a file extension, not a class or interface.
2. **Protocol / framework names** — `OData`, `WebAPI` are architectural protocols; the relevant XAF API types are the builder extension methods.
3. **Abbreviations and concept descriptors** — `DI`, `MDI`, `SVG`, `ARR`, `AWS`, `EASYTEST`, `Selenium`, `Cross-IDE`, `WebForms` are technology acronyms or platform labels, not CLR types.
4. **Ticket / KB identifiers** — `T1312589` is a DevExpress support ticket number with no value as a taxonomy type identifier.
5. **Member-path notation** — `IModelApplication.PreferredLanguage`, `XafApplication.ResourcesExportedToModel` use dot-notation to reference a *member* of a type; the containing type belongs in `primary_types`, the member path belongs in `related_types`.
6. **Lifecycle event / method names** — `Setup`, `SetupComplete`, `ExtendModelInterfaces`, `UpdateDatabaseAfterUpdateSchema`, `LogText`, `GetLocalizedText`, `AllowNew`, `AllowDelete` are callable members, not standalone types.
7. **Infrastructure / MSBuild properties** — `Kestrel`, `PublishSingleFile`, `TargetFramework`, `MultiTargeting`, `SDK-style`, `ConnectionString`, `LocalDB`, `MultipleActiveResultSets` are deployment-platform or config concepts, not XAF API types.

### What changed

| File | Change |
|---|---|
| `config/xaf-taxonomy.json` | 22 concepts corrected across all violation categories (see table below). Non-type terms moved to `related_types` or removed. Correct XAF API types added where `primary_types` was left empty or incorrect. |
| `scripts/_check_primary_types.py` | New one-off validation script that scans `primary_types` for all-caps abbreviations, dot-notation member paths, known non-type keywords, MSBuild/CLI terms, and ticket-number patterns. Exits clean against the updated file. |

### Concepts corrected

| Concept ID | Category | Was (problem entries) | Now (representative correction) |
|---|---|---|---|
| `xaf.architecture.application-model.application-model` | File extension | `["XAFML"]` | `["IModelApplication", "IModelNode", "ModelApplicationBase", "ModelNodeBase"]` |
| `xaf.architecture.application-model.model-differences` | File extension | `[..., "XAFML"]` | `"XAFML"` removed; `"IModelDifferenceStore"` etc. retained |
| `xaf.architecture.core.web-api-service` | Protocol names | `["OData", "WebAPI"]` | `["AddXafWebApi", "IXafEndpointRouteBuilder", "EnableCustomEndpoint", "CustomEndpointHandlerAsync"]` |
| `xaf.architecture.core.xaf-application` | Event names | `["Setup", "SetupComplete", "AspNetCoreApplication"]` | Moved to `related_types`; primary: `["XafApplication", "WinApplication", "BlazorApplication"]` |
| `xaf.architecture.dependency-injection.dependency-injection` | Abbreviation | `"DI"` | Removed |
| `xaf.architecture.application-model.model-extension` | Method name | `"ExtendModelInterfaces"` | Moved to `related_types` |
| `xaf.data.database.database-connection` | Config keywords | `["ConnectionString", "XpoProvider", "EFCoreProvider", "GetConnectionString", "LocalDB", "MultipleActiveResultSets"]` | `["EFCoreObjectSpaceProvider", "XPObjectSpaceProvider", "WithHostDatabaseConnectionString"]` |
| `xaf.data.database.multiple-databases` | Property names | `["AdditionalObjectSpaces", "PopulateAdditionalObjectSpaces", "AutoCommit/Refresh/DisposeAdditionalObjectSpaces"]` | Moved to `related_types`; primary: `["CompositeObjectSpace", "IObjectSpaceProviderService"]` |
| `xaf.data.object-space.object-space-provider` | Method / property names | `"CreateObjectSpace"`, `"ObjectSpaceProviders"` | Moved to `related_types` |
| `xaf.data.properties.collection-property` | Abbreviated name + model properties | `"Association"`, `"AllowNew"`, `"AllowDelete"`, `"AllowLink"`, `"AllowUnlink"` | `"Association"` → `"AssociationAttribute"`; property names moved to `related_types` |
| `xaf.data.updates.database-update` | Method names | `"UpdateDatabaseAfterUpdateSchema"`, `"UpdateDatabaseBeforeUpdateSchema"`, `"CurrentDBVersion"` | Moved to `related_types` |
| `xaf.localization.localization.localization-basics` | Member-path notation | `"IModelApplication.PreferredLanguage"` | `"IModelApplication"` |
| `xaf.localization.localization.satellite-assemblies` | Member-path notation | `"XafApplication.ResourcesExportedToModel"` | Removed from `primary_types`; preserved in `related_types` |
| `xaf.localization.localization.programmatic-localization` | Method names | `"GetLocalizedText"`, `"SetLocalizedText"`, `"FindGroupNode"`, `"GetMemberCaption"` | Moved to `related_types` |
| `xaf.migration.legacy.legacy-net-framework` | Platform name + ticket ID | `"WebForms"`, `"T1312589"` | Removed |
| `xaf.migration.migration.migration` | MSBuild / project properties | `"TargetFramework"`, `"MultiTargeting"`, `"SDK-style"` | Removed |
| `xaf.ops.deployment.deployment` | Infrastructure names | `["ARR", "Kestrel", "PublishSingleFile", "AWS"]` | `["AzureCompatibility"]`; others moved to `related_types` |
| `xaf.ops.diagnostics.diagnostic-tools` | Sparse (only minor helper) | `["LogSubSeparator"]` | `["Tracing", "LogSubSeparator"]` |
| `xaf.ops.logging.logging` | Static method names | `"LogText"`, `"LogValue"`, `"LogSeparator"`, `"LogError"` | Moved to `related_types`; `"Tracing"` added as primary type |
| `xaf.quality.testing.testing` | Framework name + acronym | `"Selenium"`, `"EASYTEST"` | Moved to `related_types` |
| `xaf.tooling.project-creation.template-kit` | Feature descriptor | `"Cross-IDE"` | Moved to `related_types`; `primary_types` removed (tool has no C# API surface) |
| `xaf.ui.navigation.tabbed-mdi-interface` | Acronym | `"MDI"` | `["UIType"]`; `"MDI"` to `related_types` |
| `xaf.ui.theming.svg-graphics` | Format acronym | `"SVG"` | `["SvgImageHelper", "ImageLoader"]`; `"SVG"` to `related_types` |

### Design decisions

- **`primary_types` semantic** — only CLR class, interface, enum, or attribute names that appear in the XAF public API and unambiguously identify the concept belong here. This mirrors Z39.19 §4.2.3: preferred terms must be unambiguous and specific.
- **`related_types` is the right home** for member paths, event names, config keys, protocol labels, and platform names that aid full-text search and cross-referencing but are not canonical type identifiers.
- **No data is discarded** — every removed entry was either relocated to `related_types` (if it has search value) or dropped only when it was an external platform name, a ticket number, or a pure abbreviation that adds no retrieval value over the synonyms in `terminology`.

---

## 2026-04-16 — Activate `requires` relation: differentiate learning prerequisites from peer associations

### Problem

All 88 `related_to` pairs in `config/xaf-taxonomy.json` used the same undifferentiated type, conflating structurally distinct semantic relationships:
- **Peer associations** (`works_with`, `see_also`) — symmetric, order-independent
- **Learning prerequisites** — asymmetric: concept A cannot be understood without first understanding concept B

The schema contract already defined a `requires` relation type for prerequisites, but it was absent from the JSON Schema and never wired into the loader.

### What changed

| File | Change |
|---|---|
| `config/xaf-taxonomy.schema.json` | Added `requires` to `$defs.concept.relations.properties` (array of strings), making it a valid key in concept relation blocks. |
| `config/xaf-taxonomy.json` | 11 learning-prerequisite pairs migrated from `related_to` → `requires` (see list below). Symmetric back-references removed from target concepts. Redundant `Error Styling → Validation` related_to removed (superseded by the existing `part_of` link). |
| `utils/taxonomy_loader.py` | `requires_ids` extracted from `relations`, resolved to names, exposed as `"requires"` in every flattened concept dict. |
| `tests/test_taxonomy_loader.py` | `"requires"` added to required-fields set and `test_relation_fields_are_lists` tuple. New test `test_requires_populated_for_known_concept` spot-checks Validation → Business Object, Navigation → Views, Entity Framework Core → Database Connection. |
| `config/xaf-taxonomy-schema-contract.md` | `related_to` definition sharpened with symmetry rule and scope boundary. `requires` definition clarified as intentionally asymmetric. |

### Pairs migrated to `requires` (11 total)

| Source concept | Requires |
|---|---|
| Clone Object | Business Object |
| State Machine | Business Object |
| Validation | Business Object |
| Conditional Appearance | Application Model |
| Database Update | Object Space |
| Entity Framework Core | Database Connection |
| XPO | Database Connection |
| Navigation | Views |
| Controllers and Actions | Views |
| Controllers and Actions | Application Model |

### Design decisions

- **Authentication ↔ Middle Tier** kept as `related_to` (symmetric peer): neither concept is a strict learning prerequisite for the other. Both are independently learnable security-domain topics that interact at runtime.
- **Error Styling → Validation `related_to` dropped** (not migrated to `requires`): the `part_of` link already implies the dependency. Adding `requires` on top of `part_of` to the same target would be redundant per Z39.19 §8.2.
- **`requires` is intentionally asymmetric** — `test_related_to_symmetric` does not extend to `requires`.

---

## 2026-04-16 — Taxonomy quality pass: relation semantics, reciprocity, and loader inverses

### Problem

A full review of `config/xaf-taxonomy.json` against **Hedden §4.3**, **ANSI/NISO Z39.19**, and **W3C SKOS** identified three structural issues:

1. **`is_a` misclassified as whole-part** — 9 concepts used `is_a` where the relationship was compositional (e.g. Audit Trail `is_a` Security System), failing the Z39.19 §7.2.1 all-and-some test.
2. **Reciprocity missing** — `part_of` and `is_a` were stored only on the child. Z39.19 §7.1 requires reciprocal entries; SKOS defines `broader`/`narrower` as inverse pairs. Parents had no way to enumerate their children.
3. **Redundant `related_to`** — Dashboards had both `is_a` Views and `related_to` Views (same target), violating Z39.19 §8.2.

### What changed

| File | Change |
|---|---|
| `config/xaf-taxonomy.json` | 9 concepts corrected: `is_a` → `part_of` for Audit Trail, Authentication, Authorization, Middle Tier, Optimistic Locking, Clone Object, State Machine, Charts, Dashboards. Redundant Dashboards → Views `related_to` removed. Views → Dashboards `related_to` removed (now superseded by the hierarchical link). |
| `utils/taxonomy_loader.py` | Added `_build_inverse_maps()` (single pass over raw concepts building parent→children maps). `_flatten_concept()` now takes two additional maps and adds `has_part` and `has_kind` as computed fields on every concept. `load_concepts()` builds the maps once and threads them through. |
| `tests/test_taxonomy_loader.py` | 5 new tests: `test_has_part_is_inverse_of_part_of`, `test_has_kind_is_inverse_of_is_a`, `test_has_part_populated_for_known_parent`, `test_has_kind_populated_for_known_parent`, `test_inverse_fields_are_lists`. `test_flatten_minimal_concept` updated for new 4-arg signature. `test_is_a_populated` updated to reflect the corrected relation type. Total: 54 passed, 4 skipped. |
| `config/xaf-taxonomy-schema-contract.md` | `has_part` and `has_kind` documented in §8 as computed read-only fields with explicit governance rule: inverses are never written to JSON — set `part_of`/`is_a` on the child only. |

### Design decisions

- **Option B (compute-at-load-time)** chosen over storing inverse relations in JSON. This mirrors how SKOS processors treat `skos:broader`/`skos:narrower` as `owl:inverseOf` pairs — the loader is the reasoning layer, the JSON is the single source of truth.
- **`part_of` wins over `is_a`** as the primary whole-part relation going forward. `is_a` is reserved exclusively for true genus-species (all-and-some) specialisation.
- **Breaking change**: `_flatten_concept()` now requires 4 arguments. All call sites updated; direct callers outside the loader must pass empty dicts `{}` for the two new map arguments.

### Relation type guide (Z39.19 §7.2)

| Relation | Test | Example |
|---|---|---|
| `is_a` | All X are Y | `List View is_a View Types` — all list views are view types ✓ |
| `part_of` | X is a component of Y | `Audit Trail part_of Security System` — audit trail is a component, not a kind ✓ |
| `related_to` | Neither hierarchical nor equivalent | `Object Space related_to Business Object` ✓ |

---

## 2026-04-15 — Taxonomy relation graph (Phase 1: loader + test scaffold)

### Problem

Only `part_of` was populated in `xaf-taxonomy.json` (58 of 146 concepts); `is_a`, `related_to`, and `replaces` had zero instances. Relation targets used concept **names** (not IDs), causing ambiguity (`"Controllers"` vs the actual concept `"Controllers and Actions"`). The loader only extracted `part_of[0]` into a flat `parent` field — the other three relation types were invisible to the pipeline.

### What changed

| File | Change |
|---|---|
| `utils/taxonomy_loader.py` | `_flatten_concept()` now accepts an `id_to_name` lookup, resolves relation IDs to names, derives `parent` from `part_of[0] \|\| is_a[0]`, and exposes four new list fields: `part_of`, `is_a`, `related_to`, `replaces`. |
| `tests/test_taxonomy_loader.py` | New `TestRelations` class (field-type checks, `is_a`/`related_to` symmetry enforcement, `replaces` population). `TestHierarchy` extended with `is_a`-fallback cases; stale `"Blazor"` reference removed. |

### Design decisions

- **`parent` backward compat** — `part_of[0]` is preferred; `is_a[0]` is the fallback. Downstream scripts that read `parent` continue to work unchanged.
- **ID-based targets** — relation targets will switch from names to concept IDs (Phases 2–7) for machine-precision; the loader resolves them back to names for the flat dict.
- **`related_to` symmetry** — enforced by test: if A lists B, B must list A.

### Status

3 intentionally-red tests (`test_is_a_populated`, `test_related_to_populated`, `test_replaces_populated`) will go green when Phases 2–7 populate the taxonomy data.

---

## 2026-04-15 — Formal faceted taxonomy (`config/xaf-taxonomy.json`)

### Problem

`config/concepts.yml` was a flat list of concept names, synonyms, keywords, and free-form tags. Several issues:

- **No schema or validation** — typos, duplicate synonyms, and inconsistent tagging went undetected.
- **`.NET` / `.NET Core` tags sprayed across nearly every concept** — they added no discriminating value and inflated co-occurrence noise in the knowledge graph.
- **No domain structure** — concepts had a `type` field (e.g. `architecture`, `ui`, `data`) but no formal subdomain hierarchy, making it impossible to scope queries or generate per-domain reports.
- **No governed contribution workflow** — anyone could add a concept or tag without understanding the downstream impact on classification, search, and analytics.

### What changed

| File | Purpose |
|---|---|
| `config/xaf-taxonomy.json` | New 5,908-line canonical taxonomy with 146 concepts migrated from `concepts.yml` into a structured schema: `id`, `name`, `artifact_kind`, `domain`/`subdomain`, `description`, `terminology` (synonyms/keywords), `api_surface`, `relations`, `facets`, and `tags`. |
| `config/xaf-taxonomy.schema.json` | JSON Schema (2020-12 draft) for CI validation of the taxonomy file. |
| `config/xaf-taxonomy-schema-contract.md` | Human-readable contract: every field's semantic meaning, governance rules, and evolution strategy. |
| `config/xaf-taxonomy-contribution-guide.md` | Step-by-step guide for adding or modifying concepts safely. |
| `config/xaf-domain-registry.yml` | 10 top-level domains (architecture, ui, data, security, ops, …) with named subdomains. Referenced by `domain`/`subdomain` fields in the taxonomy. |
| `config/taxonomy sources.md` | Reference bibliography (ANSI/NISO Z39.19, SKOS, faceted classification literature). |
| `config/concepts.yml` | Removed the `.NET Runtime` concept and stripped `.NET` / `.NET Core` tags from all remaining concepts to eliminate co-occurrence noise. |

### Migration notes

- Concept IDs follow a dotted path convention: `xaf.<domain>.<subdomain>.<slug>` (e.g. `xaf.data.orm.xpo`).
- The `relations` array on each concept encodes typed cross-references (`requires`, `extends`, `part_of`, `related_to`, `contrasts_with`) that downstream scripts can consume directly instead of inferring relationships from tag overlap.
- Existing pipeline scripts (`05_*`, `06_*`) continue to read `concepts.yml` for now; a follow-up commit will switch them to the new taxonomy loader.

---

## 2026-04-15 — Taxonomy loader adapter (`utils/taxonomy_loader.py`)

### Problem

Pipeline scripts loaded concepts via `yaml.safe_load()` on `concepts.yml` and expected a flat dict shape (`name`, `type`, `synonyms`, `tags`, `keywords`, `description`). The new `xaf-taxonomy.json` uses a richer nested structure (`artifact_kind`, `domain`/`subdomain`, `terminology`, `api_surface`, `relations`, `facets`), so scripts would break if pointed at the new file directly.

### What changed

| File | Purpose |
|---|---|
| `utils/taxonomy_loader.py` | Adapter module that reads `xaf-taxonomy.json` and returns the flat `{"concepts": [dict, …]}` shape scripts expect. Provides `load_concepts()` (flat, backward-compatible) and `load_taxonomy_raw()` (full rich structure). Reverse-maps `(artifact_kind, domain)` back to the original `type` values (`"Platform"`, `"Data Access & Business Logic"`, `"security"`, etc.). |
| `tests/test_taxonomy_loader.py` | 276-line test suite (pytest): verifies every concept round-trips correctly against `concepts.yml`, checks required fields, synonym/keyword preservation, `load_taxonomy_raw()` structure, and edge cases (missing fields, empty taxonomy). |

### Key design decisions

- **Zero pipeline breakage** — `load_concepts()` returns the exact same field names downstream scripts use today; no script edits required to switch from YAML to JSON.
- **Bonus fields forwarded** — flat dicts also include `id`, `domain`, `subdomain`, `artifact_kind`, `facets`, and `api_surface` so scripts can opt into richer data incrementally.
- **Reverse type mapping** — a `_KIND_DOMAIN_TO_TYPE` lookup table plus special-case sets (`_PLATFORM_NAMES`, `_DATA_ACCESS_NAMES`) reproduce the original `type` strings for backward compatibility.

---

## 2026-04-14 — Phase 5.5: Explicit-link bypass for noise-concept filter

### Problem fixed

The `shared_substantive()` noise filter in `scripts/05_5_filter_high_value_pairs.py` dropped doc pairs whose only shared concepts were all in the noise set (Blazor, WinForms, Windows, etc.). This correctly suppressed weak platform-only matches, but had an unintended side-effect: pairs with a confirmed hyperlink in the source docs were also dropped when their concept tags happened to be disjoint.

**Example:** "Filter Data at Grid Control Level" explicitly links to `xref:113564` ("Criteria Properties") in its Filter Builder section. Both articles scored 0.740 cosine similarity at the section level — above the 0.70 threshold — but shared zero concept tags. The noise filter eliminated them before the LLM classifier could assign a typed relationship (`uses`, `explains`, etc.).

### Fix

`scripts/05_5_filter_high_value_pairs.py` now loads `outputs/explicit_graph.parquet` at startup and builds an `explicit_pairs` set of all `(source_doc, target_doc)` pairs with a confirmed hyperlink. The `keep_pair()` function short-circuits the noise filter for any pair in that set: an explicit link is ground truth that a relationship exists and deserves a typed label.

Pairs with no explicit link continue to be filtered by `shared_substantive()` as before.

**Impact on the 2026-04-14 run:** 1,811 previously-dropped explicit-link pairs were rescued; the high-value output grew to 3,527 pairs.

---

## 2026-04-11 — New visualizer: Knowledge Graph Explorer

Replaced the three separate pyvis HTML files with a single self-contained interactive app (`tools/visualize_graph.py` → `outputs/knowledge_graph_explorer.html`). Opens in any browser; no server or Python runtime required at view time.

### Problems with the old visualizer

- Three separate static files generated by separate CLI commands. No way to switch views or adjust parameters without re-running Python.
- No search — impossible to find a specific concept or document among hundreds of nodes.
- Clicking a node showed only a hover tooltip; no detailed information panel.
- No edge-type filtering — the 7 Phase 6 relationship types (`uses`, `explains`, `requires`, `extends`, `contrasts_with`, `applies_to`, `related_to`) were not visible in any view.
- Neighbourhood exploration required a CLI argument and a full re-run.

### What's new

**Two in-browser modes (switchable without re-running Python):**

| Mode | Description |
|---|---|
| **Concept Map** | 146 concept nodes connected by section co-occurrence. Node size = section count. |
| **Relationship Map** | 1,934 document-to-document typed edges from Phase 6 classification. Color-coded by relationship type. Node size = relationship count. |

**Controls:**
- **Search box** — live highlight/filter of nodes by name; auto-focuses on first match
- **Details sidebar** — click any node to see section count, document count, connected concepts, top documents, and all incoming/outgoing classified relationships with confidence scores
- **Expand neighbourhood** — click a concept in Concept Map mode, then expand to show its top documents and the Phase 6 relationships between them, all in-browser
- **Edge-type filter checkboxes** — show/hide individual relationship types live, with edge counts
- **Min links slider** — adjust the co-occurrence threshold (1–30) for the Concept Map without re-generating
- **Physics toggle** — physics off by default (graph is stable); enable for force-directed layout

**Implementation:**
- vis-network 9.1.2 embedded from the pyvis package — fully self-contained, no CDN dependency
- All KG data (concept nodes, co-occurrence edges, rel edges, doc details, top-doc lists) serialized as a single JSON blob in the HTML
- Old `--view concept-map / neighbourhood / hub-docs` CLI interface removed; single command generates the full app

**Usage:**
```bash
python tools/visualize_graph.py
python tools/visualize_graph.py --min-cooc 5 --output outputs/my_graph.html
```

---

## 2026-04-10 — Phase 5.5: Self-pair and API-sibling pair filters

### Problems fixed

- Sections of the same document have the highest cosine similarity to each other, so they dominated the top of the ranked pairs list. These `A→A` self-pairs produced nonsensical classifications (e.g. `contrasts_with` a document with itself) and inflated pair counts. 21,932 self-pairs were present in the similarity-filtered candidates (55% of input above 0.70 threshold).
- API member pages belonging to the same parent class (e.g. `DxDashboardModel/ChildContent → DxDashboardModel/ComponentInstance`) shared a parent path segment and identical concept sets. These sibling pairs consistently classify as `related_to` at low confidence — they are navigation noise, not meaningful relationships.

### Changes

**`scripts/05_5_filter_high_value_pairs.py`**:
- Added explicit self-pair filter (`source_doc != target_doc`) applied before priority scoring. Removed 21,932 pairs.
- Added API-sibling filter: drops pairs where both sides are API pages and their second-to-last path segment is identical (same parent class). Removed 490 additional pairs.
- Net result: 3,302 unique doc pairs (down from 4,057), with 46% cross-corpus.

---

## 2026-04-10 — Phase 3 / 5.5: Platform concept routing and pair quality improvements

### Problems fixed

- `Blazor`, `WinForms`, `.NET Runtime`, and `Web API Service` were tagged as XAF concepts on almost every section, flooding semantic pairs with informationally useless shared labels. These are platform/runtime metadata, not knowledge concepts.
- Phase 5.5 was feeding both `A→B` and `B→A` directions of the same pair into Phase 6, paying double the LLM cost for redundant classifications.
- Phase 5.5 was boosting pairs by support ticket volume, a data source not yet integrated in the pipeline — this artificially surfaced broad concepts at the expense of specific ones.
- Pairs whose only shared concepts were platform labels (e.g. two sections connected only by "Blazor") produced near-identical prompts and consistently classified as `related_to`.

### Changes

**`scripts/03_extract_concepts.py`**:
- At compile time, builds `platform_concept_names` — all concept names whose `type` in `concepts.yml` is `Platform` or `runtime` (`Blazor`, `WinForms`, `Web API Service`, `.NET Runtime`).
- After concept extraction and hierarchy enrichment, splits out platform-typed names from the `concepts` set and merges them into the `platforms` column instead.
- Result: `platforms` column now populated (3,433 sections with at least one platform tag); the four platform names no longer appear in `concepts`.

**`scripts/05_5_filter_high_value_pairs.py`** (significant refactor):
- **Mirror-pair deduplication**: builds a canonical unordered pair key; after priority sort, keeps only the highest-priority direction of each undirected pair. Removed 12,086 redundant directions from 28,519 candidates.
- **Noise-shared-concept filter**: drops pairs whose *shared* concepts are all platform/runtime noise labels. Requiring at least one substantive shared concept removed 10,955 pairs (28% of similarity-filtered candidates).
- **Removed ticket boost logic**: `HIGH_TICKET_BOOST`, `CONCEPT_TO_TICKET_MAPPING`, and `max_tickets` column removed entirely. Priority is now `similarity × cross-corpus boost` only.
- **Removed JSON import** and all dead code from the old ticket-loading block.
- Net result: 5,000 output pairs drawn from 16,529 unique undirected pairs; top concepts are now substantive (`Audit Trail`, `Conditional Appearance`, `Office Module`) rather than platform labels.

---

## 2026-04-10 — Phase 6: Improved relationship classification prompt and section typing

### Problems fixed

- `requires` direction was ambiguous — the LLM had no clear rule about which section should be the one declaring the dependency, leading to reversed prerequisite suggestions in query results.
- How-to articles, tutorials, and conceptual pages were all labelled `"Conceptual/Tutorial"`, so the LLM could not distinguish them and would classify how-tos as prerequisites for the concepts they assume.
- The output schema required `rationale` and `evidence` arrays, adding token cost with no downstream use.
- Relationship definitions were vague one-liners with no tie-breaker guidance.

### Changes

**`config/prompts/relationship_classification.md`** (complete rewrite):
- Added "Evaluate all relationship types before choosing one" instruction to prevent premature anchoring.
- Split `Conceptual/Tutorial` into three distinct section types: **API Reference**, **How-to Task**, **Tutorial**, **Conceptual**.
- Replaced table-style relationship definitions with precise per-type bullet rules including explicit `requires` direction rule and `uses` vs `explains` tie-breaker.
- Added **Decision order** section clarifying the tie-breaker is only for genuinely ambiguous cases, not a global ranking.
- Added **Confidence calibration** bands with concrete thresholds.
- Added **Bidirectionality** rule: default `false`; `true` only for symmetric relationships (`contrasts_with`, occasionally `related_to`).
- Output format trimmed to three keys only: `relationship`, `confidence` (float), `bidirectional`.

**`scripts/06_classify_relationships.py`**:
- `_section_type()` helper now returns `"How-to Task"` for `/how-to` paths, `"Tutorial"` for `tutorial`/`getting-started`/`get-started` paths, and `"Conceptual"` otherwise.
- Prompt template JSON schema updated to match the new 3-key output format.
- `relationship_rationale` and `relationship_evidence` columns removed from result rows (no longer requested from the LLM).

**`query_graph.py`** (`find_prerequisites`):
- Fixed direction inversion: now queries `source → target` (SS sections as source) to find what they depend on, rather than the reverse.
- Added filters to exclude API reference pages, how-to articles, and tutorial pages from prerequisite suggestions — these content types assume prior knowledge and cannot be foundational reading.

---

## 2026-04-10 — New tool: Interactive knowledge graph visualization

### What's new

Added `tools/visualize_graph.py` — generates self-contained interactive HTML files from `outputs/knowledge_graph.json` using [pyvis](https://pyvis.readthedocs.io/). Open the output files in any browser; no server required.

### Three views

| View | Command | Output |
|---|---|---|
| **Concept map** | `--view concept-map` | 150 concept nodes connected by section co-occurrence. Node size = section count. Shows the full concept landscape at a glance. |
| **Hub documents** | `--view hub-docs` | Top N documents ranked by in-degree on the explicit xref graph. Node size = in-links. Shows navigation centers. |
| **Concept neighbourhood** | `--view neighbourhood --concept "..."` | All nodes reachable from a named concept within N hops. Good for deep-diving a single concept area. |

### Usage

```bash
# Concept co-occurrence map (all 150 concepts)
python tools/visualize_graph.py --view concept-map

# Top 50 hub documents and their explicit cross-links
python tools/visualize_graph.py --view hub-docs --top 50

# 2-hop neighbourhood of Security System
python tools/visualize_graph.py --view neighbourhood --concept "Security System" --hops 2

# 1-hop neighbourhood of a different concept
python tools/visualize_graph.py --view neighbourhood --concept "Object Space" --hops 1
```

All outputs are saved to `outputs/graph_*.html`.

---

## 2026-04-10 — Phase 1: Resolve [!include] directives

### Problem

DocFX `[!include]` directives were passing through as raw markup into parsed sections. Before the fix, 1,026 raw text sections and 99 generated descriptions contained unresolved `[!include[...](path)]` markers — rendering descriptions unusable for search and LLM training.

### Change

Added an include-resolution system to `scripts/01_ingest_parse.py`:

- **`build_template_lookup()`** loads 306 template `.md` files from `data/raw_md/templates/` into a lookup dictionary keyed by lowercase stem.
- **`resolve_includes()`** handles two patterns:
  - `[!include[label](path)]` — extracts filename from path, looks up content
  - `[!includeShorthand]` — matches shorthand names directly
- Template files are excluded from the document corpus to avoid duplication.
- Resolution runs on raw text before section tokenization, so downstream phases (3, 7) benefit automatically.

### Results

| Metric | Before | After |
|---|---|---|
| Templates loaded | 0 | 306 |
| Descriptions with `[!include]` | 99 | 11 (89% reduction) |
| Total sections parsed | 11,235 | 11,548 (+313) |
| Sections with xref links | 5,524 | 5,647 (+123) |
| Avg word count per section | 86 | 90 |

The 11 remaining descriptions contain non-standard include patterns (e.g., `[!includePathToMainDemo]`, `[!includeExtraModulesNote1]`) that reference shorthand names not present in the templates folder. These can be addressed by adding the missing template files.

---

## 2026-04-10 — Phase 7: Nullify boilerplate/templated descriptions

### Problem

219 unique descriptions were repeated across 1,266 sections — generic API boilerplate that adds no value for search or discoverability (e.g., *"Initializes a new instance of the class."* appeared 188 times).

### Change

Added a post-processing step in `scripts/07_generate_metadata.py` that detects descriptions used 3 or more times and sets them to `None`. Categories of removed descriptions:

- **Generic constructor summaries** (348 sections) — *"Initializes a new instance of the class."*
- **Assembly reference lines** (136 sections) — *"Assembly: DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll."*
- **Module boilerplate** (80 sections) — *"Returns the list of updaters that handle database updates for the module."*
- **Internal-use warnings** (14 sections) — *"This method is not intended to be called from your code."*
- **Other repeated descriptions** (688 sections)

A full listing of affected documents is in `outputs/templated_descriptions_report.md`.

### Results

| Metric | Before | After |
|---|---|---|
| Boilerplate descriptions | 1,266 | 0 |
| Description coverage | 87.3% | 75.1% |

Coverage dropped because these were replaced with `None` rather than context-aware alternatives. This is intentional — no description is better than a misleading one.

---

## 2026-04-10 — Phase 7: Fix metadata artifact leakage in descriptions

### Problem

1,713 out of 10,376 generated descriptions contained raw YAML frontmatter instead of usable text. Descriptions started with `uid:`, `linkId:`, or `id:` followed by concatenated metadata fields.

**Example (before):**
```
uid: "403179"title: 'Application Shell and Base Infrastructure'description: 'Learn about the core XAF application infrastructure: solution structure,...
```

**Root cause:** The inline YAML frontmatter in section text lacked newline delimiters between fields. The existing `clean_markdown_text()` function used line-based regex patterns (`re.MULTILINE`) that only matched metadata on separate lines.

### Changes

Four fixes applied to `scripts/07_generate_metadata.py`:

1. **New `extract_frontmatter_description()` function** — Extracts `description:` or `title:` values from inline YAML metadata before the text is cleaned. This recovered ~1,400 article descriptions that previously showed raw frontmatter.

2. **Expanded `clean_markdown_text()`** — Added regex patterns that strip inline (concatenated) YAML fields: `uid:`, `seealso:`, `linkId:`, `linkType:`, `altText:`, `tags:`, `proficiencyLevel:`, `title:`, `description:`, and API-doc fields (`id:`, `type:`, `return:`).

3. **Inline `summary:` extraction fallback in `extract_api_summary()`** — The original regex required a newline before the next YAML field (`syntax:`, `seealso:`, etc.). Added a fallback pattern that handles the concatenated format found in 274 API docs.

4. **Post-processing safety net** — Any description still starting with metadata prefixes (`uid:`, `linkId:`, `id:`, `seealso:`, `name:`) is set to `None` instead of being output. This caught the last 32 edge cases where no meaningful content could be extracted.

### Results

| Metric | Before | After |
|---|---|---|
| Artifact descriptions | 1,713 | 0 |
| Description coverage | 87.2% | 87.3% |

**Example (after):**
```
Learn about the core XAF application infrastructure: solution structure, application life cycle, navigation, UI customization (appearance, themes,...
```

Previously affected documents now produce clean descriptions:

- `articles/app-shell-and-base-infrastructure` → *"Learn about the core XAF application infrastructure: solution structure..."*
- `articles/conditional-appearance` → *"Conditional Appearance (Manage UI State)."*
- `articles/multitenancy` → *"Multi-Tenancy (Data per Tenant)."*
- `articles/migration-to-net` → *"Migration to .NET from .NET Framework in v25.2+."*

The 32 remaining null descriptions are API stubs with no extractable content (e.g., `RuleSet/ValidateTarget` with only a uid and no summary field).
