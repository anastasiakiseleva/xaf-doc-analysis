# What's New

## April 11, 2026

### Metadata Review Tool
- New `outputs/metadata_reviewer.html` — self-contained interactive review app for all 5,517 docs
- Filters by type (API/Article), proficiency, status, connectivity; live search
- Per-doc editable YAML textarea, Approve / Flag / Skip verdict with notes
- Keyboard shortcuts (`a`/`f`/`s`, `j`/`k` navigation); decisions persist in `localStorage`
- "Export results ↓" downloads a CSV with all verdicts and edited YAMLs
- Deployable to GitHub Pages as-is (no backend required)

### LLM Description Generation (`scripts/09b_generate_descriptions.py`)
- Generates metadata descriptions for all 695 article docs using Claude Haiku
- Uses lightweight signals only: title, slug, doc type, platforms, H2 section headings — no body text sent to LLM
- New `config/prompts/metadata_description.md` — engineered system prompt with role framing, type-specific patterns, 5 few-shot examples, negative examples table, and grounding rules
- Results cached in `outputs/article_descriptions.parquet`; safe to interrupt and resume
- If response exceeds 150 chars, a follow-up turn asks the model to shorten — never truncates mid-sentence
- Fixed: `.NET Runtime` filtered from platform signals (it is a runtime, not a UI framework)
- Reviewer priority order: LLM cache → heuristic raw-markdown extraction → Phase 7 fallback

### Phase 8 (YAML Metadata Export)
- `outputs/metadata_review.csv` — 10,819 rows, average 4.0 tags per doc, 73% description coverage
