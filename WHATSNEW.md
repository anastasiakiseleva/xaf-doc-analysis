# What's New

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
