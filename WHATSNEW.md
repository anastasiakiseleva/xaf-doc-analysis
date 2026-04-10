# What's New

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
