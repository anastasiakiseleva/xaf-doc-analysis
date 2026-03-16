# XAF Documentation Analysis Project

## Overview

This project analyzes DevExpress XAF (eXpressApp Framework) documentation to:
1. **Build a semantic knowledge graph** of 11,000+ documentation sections
2. **Identify documentation gaps** (missing links, isolated content, under-connected concepts)
3. **Measure documentation quality** with quantifiable metrics
4. **Track improvements** over time with baseline comparison tools
5. **Guide documentation improvements** with actionable recommendations
6. **Generate AI-friendly metadata** for enhanced discoverability
7. **Map APIs to concepts** for better navigation and understanding

The project consists of three main pipelines:
- **Knowledge Graph Pipeline** (Phases 1-5): Build semantic understanding
- **Quality Analysis Pipeline** (Phases 6-8): Measure, analyze, and improve
- **Advanced Enrichment Pipeline** (Phases 5.5-12): Metadata generation, API mapping, and LLM classification

---

## Pipeline 1: Knowledge Graph Construction

### Goal
Transform raw documentation into a semantic knowledge graph that AI and humans can query, navigate, and reason about.

### Phases

## Phase 1 — Read the documentation like a human would

### Script
`01_ingest_parse.py`

### What this step does
It reads every Markdown file and breaks it into:
- Documents
- Section titles
- Sections of text
- Code blocks
- Explicit links between pages

### Why it matters
Before AI can understand documentation, it has to be structured. Humans understand that:
_“Object Space > Create, Read, Update and Delete Data”_ is more specific than _“Data Manipulation”_.
This step preserves document structure, instead of flattening text.

### Output
`topics_inventory.parquet`

This is your source of truth:
- “Which sections exist?”
- “Where do they live?”
- “How long are they?”

Think of it as an indexed table of contents for the entire documentation set.

## Phase 2 — Capture how authors intended docs to connect

### Script
`02_build_explicit_graph.py`

### What this step does
It looks at:
- “See also”
- Cross‑references
- Internal links

And builds a graph like: Page A → Page B → Page C

### Why it matters
Links are human intent. If an author linked two pages, that relationship matters—even if the text doesn’t look similar.

### Output
`explicit_graph.parquet`

This answers questions like:
- Which pages are popular hubs?
- Which pages are never linked?
- Where navigation might be broken?

This is the “hallway map” of the documentation.

## Phase 3 — Teach the system XAF language

### Script
`03_extract_concepts.py`

### What this step does
It identifies:
- XAF concepts (Object Space, Validation, Security System…)
- Platforms (Blazor, WinForms, Web API)
- API names (DevExpress.ExpressApp.ObjectSpace, etc.)

It does this section by section.

### Why it matters
AI doesn’t automatically know what matters in XAF. You explicitly teach it: “This section is about Object Space and applies to Blazor.”

That prevents:
- Mixing concepts
- Platform confusion
- API answers without context

### Output
`doc_concepts.parquet`

This is the semantic tagging layer:
- Every section now has labels
- You can filter by concept, platform, or API

This is where docs stop being text and start being knowledge.

## Phase 3.5 — Measure documentation readiness before AI

### Purpose
Before we invest time and compute in embeddings or AI models, this step measures whether the documentation is *structurally and semantically ready* for AI consumption.

Think of this as a **health check** and **calibration step**.

### Script / Artifact
- Notebook: `phase_3_5_metrics_snapshot.ipynb`
- Report: `phase_3_5_metrics_report.md`

### What this step does
Using the outputs of Phases 1–3, it computes objective metrics such as:
- How many sections are kept vs. discarded (overall and API‑specific)
- API documentation retention after gating (Summary / Remarks / Examples)
- Section length distribution (to detect very short, noisy fragments)
- Concept density (are sections clearly about *something specific*?)
- Platform coverage (Blazor / WinForms / Web API balance)
- Orphan pages and link hubs (if the explicit link graph is available)
- Candidate terms that appear frequently but are **not yet modeled as concepts**

It also produces distributions and tables that make threshold decisions visible and explainable.

### Why it matters
Without this step:
- Similarity thresholds are guessed instead of calibrated
- API docs can silently dominate or pollute embeddings
- AI results may *look* intelligent but be inconsistent or noisy
- Stakeholders have no quantitative proof that the documentation is AI‑ready

With Phase 3.5:
- Thresholds (min similarity, minimum section length, API gating rules) are **evidence‑based**
- Documentation issues are detected *before* AI is involved
- Writers and SMEs can validate quality using familiar metrics
- Trust is established before downstream automation

This phase turns “AI experimentation” into a **controlled, auditable process**.

### Key outputs
- A **metrics snapshot** answering:
  - “Is the corpus clean enough to embed?”
  - “Are API docs filtered to the right signal level?”
  - “Are concepts explicit and well‑distributed?”
- Recommended **initial thresholds** for:
  - Embedding inclusion
  - Semantic similarity gates
  - API vs. conceptual balance

Only after this step do we proceed to embeddings.

## Phase 4 — Turn text into “meaning coordinates”

### Script
`04_make_sections_embeddings.py`

### What this step does
For each section:
- It creates an embedding (a numeric meaning representation)
- Stores it alongside section metadata

It produces two separate maps:
- Conceptual sections
- API reference sections

### Why it matters
This is what enables:
- Semantic search
- AI question answering
- Automatic “related topics”

Instead of keyword matching “save” ≠ “save” we get: “persist data”, “commit changes”, “save object” → same idea

### Output
`sections_embeddings_conceptual.parquet`
`sections_embeddings_api.parquet`

Think of these as a GPS map of meaning for your documentation.

## Phase 5 — Discover hidden relationships

### Script
`05_find_semantic_pairs.py`

### What this step does
It asks: “Which sections talk about similar things, even if no link exists?” and applies rules to keep only useful relationships:
- Concept ↔ concept
- API ↔ API
- Concept ↔ API

### Examples
- A “Security System Overview” section is closely related to a “PermissionPolicyRole API” page.
- Two Blazor‑specific explanations of filtering belong together.
- API pages in the same namespace naturally cluster.

### Why it matters
This reveals:
- Missing links
- Redundant content
- Hidden documentation gaps

### Output
`semantic_pairs.parquet`

This is the “possible connections humans forgot to add.”

**Key Statistics:**
- 93,905 semantic pairs discovered
- 8.5 average connections per section
- 19.8% cross-corpus links (API ↔ Conceptual)
- Quality gates: concept overlap, platform overlap, namespace overlap

---

## Pipeline 2: Quality Analysis & Improvement

### Goal
Measure documentation quality, identify gaps, and track improvements with quantifiable metrics.

### Phases

## Phase 6 — Establish Baseline Metrics

### Script
`tools/save_baseline_metrics.py`

### What this step does
Captures comprehensive baseline statistics:
- Overall connectivity metrics
- Per-concept statistics (all 133 concepts)
- Cross-corpus gap analysis
- Isolated section identification
- Under-connected concept detection

### Why it matters
You can't improve what you don't measure. This creates a quantitative foundation for:
- Tracking improvements over time
- Making data-driven decisions
- Proving ROI of documentation work
- Identifying high-priority issues

### Output
- `outputs/baseline_metrics.json` - Machine-readable metrics
- `BASELINE_METRICS.md` - Human-readable report

**Key Findings (Current Baseline):**
- 11,082 sections analyzed
- 603 isolated sections (5.4%)
- 6 concepts with zero cross-corpus links
- 16 under-connected concepts (<6 links/section)

## Phase 7 — Analyze Documentation Gaps

### Scripts
- `query_graph.py --mode gaps` - Overall gap analysis
- `tools/analyze_all_gaps.py` - Categorize gap types
- `tools/analyze_deployment_gap.py` - Concept-specific deep dive
- `tools/find_missing_deployment_apis.py` - Missing tagging identification
- `tools/list_all_deployment_apis.py` - API candidate generation

### What this step does
Identifies three types of documentation problems:

1. **Cross-Corpus Gaps** - Concepts with no API ↔ Conceptual links
   - 6 concepts affected (Deployment, Multi-Tenancy, etc.)
   - Root causes: missing API tags or semantic disconnections

2. **Isolated Sections** - Content with zero semantic connections
   - 603 sections (5.4% of total)
   - Causes: stub pages, missing tags, genuinely niche content

3. **Under-Connected Concepts** - Topics with weak connectivity
   - 16 concepts below 6 links/section threshold
   - Compare vs. well-connected benchmarks (Audit Trail: 14.1 links/section)

### Why it matters
Gaps represent:
- User navigation problems
- AI retrieval failures
- Knowledge silos
- Missing documentation

Each gap type requires different fixes:
- Missing tags → Update concept extraction
- Semantic gaps → Add cross-references, examples
- Isolated content → Review for relevance or connection opportunities

### Output
- `DOC_ANALYSIS_ACTION_PLAN.md` - Prioritized improvement roadmap
- `outputs/deployment_api_candidates.csv` - 263 APIs needing Deployment tags
- `outputs/deployment_api_candidates.json` - Same data in JSON format
- Gap categorization reports

**Example Finding:**
263 API documents contain deployment-related keywords (applicationbuilder, connectionstring, azure) but aren't tagged with "Deployment" concept. Fixing this one issue would create 50+ cross-corpus links.

## Phase 8 — Track Improvements

### Script
`tools/compare_to_baseline.py`

### What this step does
Compares current state against baseline and shows:
- ✅ Improvements (with green checkmarks)
- ⚠️ Regressions (with warnings)
- → No-change items
- Overall progress summary

### Why it matters
Makes improvement visible and measurable:
- Stakeholder reporting
- Before/after validation
- Iterative improvement tracking
- Success criteria verification

### Output
Console report showing:
```
📊 OVERALL METRICS
Total Semantic Pairs    | Baseline: 93905 | Current: 95123 | ✅ ▲ 1218 (+1.3%)
Isolated Sections       | Baseline: 603   | Current: 550   | ✅ ▼ 53 (-8.8%)
Concepts with Gaps      | Baseline: 6     | Current: 4     | ✅ ▼ 2 (-33.3%)
```

### Success Criteria
- All concepts have ≥10 cross-corpus links
- Isolated sections <3% (currently 5.4%)
- Under-connected concepts reduced by 50%
- Avg connections/section ≥9.0 (currently 8.5)

---

## Pipeline 3: Advanced Analysis & Enrichment

### Goal
Enhance documentation with AI-powered classification, metadata generation, and API mapping.

## Phase 5.5 — Filter High-Value Semantic Pairs

### Script
`scripts/05_5_filter_high_value_pairs.py`

### What this step does
Filters semantic pairs to focus on highest-value relationships for classification:
- High similarity scores (≥0.70 confidence)
- Cross-corpus links (tutorial ↔ API reference)
- Concepts with high support ticket volumes (customer pain points)
- Priority scoring with configurable boosts

### Why it matters
Classification with LLMs is expensive/slow. This ensures you:
- Focus on relationships that matter most
- Prioritize customer pain point areas
- Get maximum ROI from classification effort
- Keep processing time manageable

### Output
`outputs/semantic_pairs_high_value.parquet`

**Filtering Results:**
- Input: 93,905 semantic pairs
- Output: ~5,000 high-value pairs (configurable)
- Boost multipliers: 1.5x for cross-corpus, 2.0x for high-ticket concepts

## Phase 6 — Classify Relationship Types (Experimental)

### Script
`scripts/06_classify_relationships.py`

### What this step does
Uses LLM to classify semantic relationships into types:
- **explains** - Section A explains the concept in section B
- **requires** - Section A requires understanding section B
- **uses** - Section A uses/implements concepts from section B
- **extends** - Section A extends concepts from section B
- **applies_to** - Section A applies to scenarios in section B
- **contrasts_with** - Section A contrasts with section B
- **related_to** - General semantic similarity

### Why it matters
Enables intelligent features:
- Smart navigation ("Read this first")
- Learning path generation
- Prerequisites identification
- AI reasoning about documentation structure

### Output
`outputs/classified_pairs_checkpoint.parquet` (with checkpoint/resume support)

**Status:** ⚠️ Experimental - Requires LLM API configuration (OpenAI, Anthropic, or similar)

**Usage:**
```bash
# Test on 100 pairs
python scripts/06_classify_relationships.py --limit 100

# Resume from checkpoint
python scripts/06_classify_relationships.py --resume outputs/classified_pairs_checkpoint.parquet

# Filter by relationship type
python scripts/06_classify_relationships.py --types ca,ac --threshold 0.80
```

## Phase 7 — Generate AI-Friendly Metadata

### Script
`scripts/07_generate_metadata.py`

### What this step does
Generates metadata fields for each documentation section:
- **Tags** - Normalized concept/platform/API names
- **Description** - Auto-generated section summaries
- **Proficiency Level** - Beginner/Advanced/Expert classification
- **Semantic Connections** - Count of related sections

### Why it matters
Makes documentation more accessible to:
- AI chatbots and RAG systems
- Search engines and indexers
- Documentation portals
- Automated tooling

### Output
`outputs/metadata_suggestions.parquet`

**Strategy:**
- Tags from concepts, platforms, APIs (normalized format)
- Descriptions from section content and title
- Proficiency based on API reference vs. conceptual content
- Connection counts from semantic pairs

## Phase 8 — Export YAML Frontmatter

### Script
`scripts/08_export_yaml_metadata.py`

### What this step does
Exports metadata in YAML format for documentation frontmatter:
- Individual YAML files per document
- Bulk export for team review
- Diff reports showing proposed changes

### Why it matters
Enables integration with documentation systems:
- Add frontmatter to Markdown files
- Enrich documentation portals
- Improve SEO and discoverability
- Support documentation automation

### Output
- Individual YAML snippets
- Bulk export file
- Diff report

**Example Output:**
```yaml
---
description: "Learn how to implement authentication in XAF applications"
tags: [security-system, authentication, blazor-ui, aspnet-core]
proficiencyLevel: Advanced
---
```

## Phase 9 — Track Concept Quality Metrics

### Script
`scripts/09_concept_quality_metrics.py`

### What this step does
Monitors key quality indicators over time:
- Concept coverage and specificity
- Concept connectivity ratios
- Quality gate passage rates
- Co-occurrence patterns
- Isolated section tracking

### Why it matters
Validates that concept vocabulary improvements are working:
- Detect noise in concept definitions
- Track improvement after concept updates
- Identify concepts needing refinement
- Ensure changes improve quality

### Output
`outputs/concept_quality_metrics.json`

**Tracked Metrics:**
- Coverage: % of sections with concept tags
- Specificity: Sections per concept distribution
- Connectivity: Links per concept
- Gate quality: Semantic pair quality filters
- Isolation: Sections with zero connections

## Phase 10 — Roll Up Document Metadata

### Script
`scripts/10_rollup_document_metadata.py`

### What this step does
Aggregates section-level metadata to document level:
- Union of tags from all sections
- Best description (from most-connected section)
- Highest proficiency level
- Total semantic connection count

### Why it matters
Documentation is organized by documents, not sections:
- Provide document-level tags for portals
- Aggregate statistics for reporting
- Enable document-level search/filtering
- Support content management systems

### Output
`outputs/document_metadata.parquet`

**Aggregation Strategy:**
- Tags: Union with frequency weighting (top 12)
- Description: From section with most connections
- Proficiency: Maximum across sections
- Connections: Sum of all section connections

## Phase 11 — Extract API Entities

### Script
`scripts/11_extract_api_entities.py`

### What this step does
Structures API information from documentation:
- **API ID** - Full namespace path
- **API Name** - Short name (e.g., "SecurityStrategy")
- **API Type** - class, method, property, interface, etc.
- **Namespace** - DevExpress.ExpressApp.Security
- **Section Link** - Back-reference to documentation

### Why it matters
Creates structured API reference:
- Enable API-based queries
- Support API-concept mapping
- Build API documentation index
- Power intelligent search

### Output
- `outputs/api_entities.parquet` - 6,853 unique API definitions
- `outputs/documents_api.parquet` - Section → API relationships

**Key Statistics:**
- 6,853 API sections identified
- 5,767 API sections retained (84.2%)
- Structured namespace hierarchies
- Type classification (class, method, property, etc.)

## Phase 12 — Map APIs to Concepts

### Script
`scripts/12_map_apis_to_concepts.py`

### What this step does
Creates API → Concept implementation mappings using three strategies:
1. **Co-occurrence** - APIs and concepts appearing together in documentation
2. **Namespace rules** - DevExpress.ExpressApp.Security → Security System
3. **Confidence scoring** - Based on co-occurrence strength

### Why it matters
Bridges the critical gap between API reference and conceptual documentation:
- "Show me all Security System APIs"
- "What APIs implement Object Space?"
- "Find APIs for this concept"

### Output
`outputs/api_implements_concept.parquet`

**Mapping Results:**
- API entities mapped to concepts
- Confidence scores (high/medium/low)
- Multiple concepts per API supported
- Bidirectional navigation enabled

**Example Queries Enabled:**
```python
# Find all APIs implementing Security System
security_apis = api_concepts[api_concepts['concept'] == 'Security System']

# Find concepts implemented by an API
api_concepts = mappings[mappings['api_id'].str.contains('SecurityStrategy')]
```

### Phase 12 (Enhanced) — Ollama-Based API Classification

### Script
`12_map_apis_to_concepts_ollama.py` (experimental, in root directory)

### What this step does
Enhances Phase 12 with LLM-based classification:
- Same three strategies as above
- Adds Ollama/Llama 3.1 classification for unmapped APIs
- Fills gaps where rules don't apply
- Provides confidence scoring

### Why it matters
Automation achieves broader coverage:
- Rules-based: ~60% coverage (high precision)
- LLM-based: Fills remaining 40% (moderate precision)
- Combined: Near-complete API-concept mapping

### Status
⚠️ **Experimental** - See [docs/ollama_decision_log.md](ollama_decision_log.md) for evaluation

**Usage:**
```bash
# Test on 10 APIs
python 12_map_apis_to_concepts_ollama.py --sample 10 --use-ollama

# Run on unmapped APIs only
python 12_map_apis_to_concepts_ollama.py --use-ollama --unmapped-only

# Validate accuracy
python validate_ollama_accuracy.py --sample 50
```

---

## Project Capabilities

### Knowledge Graph Queries

**Script:** `query_graph.py`

Query the semantic knowledge graph with multiple modes:

```bash
# Get overall statistics
python query_graph.py --mode stats

# Identify documentation gaps
python query_graph.py --mode gaps

# Find related sections for a concept
python query_graph.py --mode query --concept "Deployment"

# Find related sections for a document
python query_graph.py --mode query --section "article/security-system/authentication"
```

### Gap Analysis Tools

**Purpose:** Identify specific documentation problems with actionable recommendations.

| Tool | Purpose | Output |
|------|---------|--------|
| `tools/analyze_all_gaps.py` | Categorizes all 6 cross-corpus gaps by type | Gap type classification |
| `tools/analyze_deployment_gap.py` | Deep dive on Deployment concept | Section breakdown, co-occurrence analysis |
| `tools/find_missing_deployment_apis.py` | Lists APIs needing Deployment tags | Top 20 candidates with rationale |
| `tools/list_all_deployment_apis.py` | Complete API candidate list | CSV + JSON (263 APIs) |

### Quality Metrics

**Purpose:** Measure documentation health with quantifiable data.

| Metric | Current State | Target |
|--------|--------------|--------|
| **Total Sections** | 11,082 | Stable |
| **Semantic Pairs** | 93,905 | 95,000+ |
| **Avg Connections/Section** | 8.5 | 9.0+ |
| **Isolated Sections** | 603 (5.4%) | <3% |
| **Cross-Corpus Links** | 18,613 (19.8%) | 21%+ |
| **Concepts with Gaps** | 6 | 0 |
| **Under-Connected Concepts** | 16 | <8 |

### Comparison & Tracking

**Script:** `compare_to_baseline.py`

Automatically compare any future state against baseline:
- Calculates improvements and regressions
- Shows percentage changes
- Highlights successful fixes
- Provides overall progress verdict

---

## Quick Start Guide

### 1. Build Knowledge Graph (Core Pipeline - Phases 1-5)

```bash
# Run core phases in sequence
python scripts/01_ingest_parse.py
python scripts/02_build_explicit_graph.py
python scripts/03_extract_concepts.py
python scripts/04_make_sections_embeddings.py --batch-size 32 --max-chars 4000
python scripts/05_find_semantic_pairs.py
```

### 2. Generate Enrichments (Phases 7-12)

```bash
# Generate metadata and API mappings
python scripts/07_generate_metadata.py
python scripts/08_export_yaml_metadata.py
python scripts/09_concept_quality_metrics.py
python scripts/10_rollup_document_metadata.py
python scripts/11_extract_api_entities.py
python scripts/12_map_apis_to_concepts.py
```

### 3. Establish Baseline

```bash
# Capture current state
python tools/save_baseline_metrics.py

# Review baseline
# Opens: outputs/baseline_metrics.json
# Opens: BASELINE_METRICS.md
```

### 4. Analyze Gaps

```bash
# Get overall picture
python query_graph.py --mode gaps

# Deep dive on specific issues
python tools/analyze_all_gaps.py
python tools/analyze_deployment_gap.py
python tools/find_missing_deployment_apis.py

# Generate cross-linking recommendations
python tools/generate_crosslink_filtered.py
```

### 5. Make Improvements

Based on gap analysis, make documentation changes:
- Update concept definitions in `config/concepts.yml`
- Re-run extraction: `python scripts/03_extract_concepts.py`
- Rebuild graph: Phases 4-5
- Add cross-references to isolated sections
- Create bridging content for semantic gaps

### 6. Measure Progress

```bash
# Compare against baseline
python tools/compare_to_baseline.py

# Get updated statistics
python query_graph.py --mode stats
python query_graph.py --mode gaps
```

### 7. (Optional) Experiment with LLM Classification

```bash
# Validate Ollama accuracy
python scripts/experimental/validate_ollama_accuracy.py --sample 100

# Test API-concept mapping with Ollama
python scripts/experimental/12_map_apis_to_concepts_ollama.py --sample 10 --use-ollama

# See decision log for evaluation criteria
# docs/ollama_decision_log.md
```

---

## What This Lets You Measure

### For Documentation Quality

**Questions Answered:**
- Which concepts have poor connectivity?
- Where are documentation islands (isolated content)?
- Which API docs lack conceptual bridging?
- What's the distribution of concept coverage?
- Are there navigation dead-ends?

**Actionable Insights:**
- 263 API documents need Deployment tagging
- 6 concepts have zero API ↔ Conceptual links
- 603 sections are completely isolated
- Template Kit concept needs 63% more connections

### For Content Strategy

**Questions Answered:**
- Which concepts are well-documented (benchmarks)?
- What patterns make content discoverable?
- Where should writers focus next?
- How does platform coverage compare?

**Best Practices Identified:**
- Audit Trail: 14.1 links/section (excellent)
- Conditional Appearance: 10.0 links/section (good)
- Target: All concepts above 7.0 links/section

### For AI/RAG Systems

**Questions Answered:**
- Can the system consistently retrieve the right section?
- Does every answer have a clear source?
- Are platform differences respected?
- Is the knowledge graph dense enough?

**Quality Gates:**
- Concept overlap: 73.1% of pairs
- Platform overlap: 33.0% of pairs
- Namespace overlap: 32.2% of pairs
- Average similarity: 0.759 (min: 0.600)

### For Users

**Questions Answered:**
- Do users land on the right page?
- Can they discover related topics?
- Are concepts duplicated or scattered?
- Is navigation intuitive?

**Improvements Enabled:**
- "Related Topics" based on semantic similarity
- Cross-platform navigation
- API ↔ Tutorial bridges
- Concept-based search and filtering

---

## Project Structure

```
xaf-doc-analysis/
├── scripts/                    # Core pipeline (Phases 1-5)
│   ├── 01_ingest_parse.py
│   ├── 02_build_explicit_graph.py
│   ├── 03_extract_concepts.py
│   ├── 04_make_sections_embeddings.py
│   ├── 05_find_semantic_pairs.py
│   └── 06-09_*.py            # Optional future phases
│
├── config/
│   ├── concepts.yml          # 45 XAF concept definitions
│   └── prompts/              # AI extraction prompts
│       ├── ai_action_prompts.md
│       └── relationship_classification.md
│
├── outputs/                   # All generated data
│   ├── topics_inventory.parquet          # Phase 1
│   ├── explicit_graph.parquet             # Phase 2
│   ├── doc_concepts.parquet               # Phase 3
│   ├── sections_embeddings_*.parquet      # Phase 4
│   ├── semantic_pairs.parquet             # Phase 5
│   ├── baseline_metrics.json              # Phase 6
│   └── deployment_api_candidates.csv      # Phase 7
│
├── docs/
│   ├── project-overview.md               # This file
│   ├── BASELINE_METRICS.md               # Current metrics report
│   ├── DOC_ANALYSIS_ACTION_PLAN.md       # Improvement roadmap
│   ├── METRICS_CAPTURED_NEXT_STEPS.md    # What to do next
│   ├── ai_action_prompts.md              # Gap analysis guide
│   ├── concept_quality_metrics_guide.md
│   └── prerequisites.md
│
├── tools/                     # Analysis & utility tools
│   ├── analyze_all_gaps.py               # Categorize gaps
│   ├── analyze_deployment_gap.py         # Concept deep dive
│   ├── find_missing_deployment_apis.py   # Missing tag finder
│   ├── list_all_deployment_apis.py       # Complete candidate list
│   ├── save_baseline_metrics.py          # Capture baseline
│   ├── compare_to_baseline.py            # Track improvements
│   ├── extractor_sanity_check.py         # Validate extraction
│   ├── graph-sanity-check.py             # Validate graph
│   ├── test_links.py                     # Link validation
│   └── unresolved-uids-check.py          # Check references
│
├── query_graph.py             # Main query tool (kept in root)
├── README.md                  # Quick start guide
└── requirements-lock.txt      # Python dependencies
```

---

## Key Files Reference

| File | Purpose | When to Use It |
|------|---------|---------------|
| `topics_inventory.parquet` | Full text of all sections | Reading actual content |
| `doc_concepts.parquet` | Section metadata & concept tags | Filtering by concept/platform |
| `semantic_pairs.parquet` | 93K relationship pairs | Analyzing connectivity |
| `sections_embeddings_*.parquet` | Vector embeddings | Similarity searches |
| `baseline_metrics.json` | Current quality snapshot | Comparison baseline |
| `deployment_api_candidates.csv` | APIs needing tags | Fixing Deployment gap |
| `config/concepts.yml` | Concept definitions | Understanding taxonomy |

---

## Next Steps

### Immediate Actions (Phase 1 Improvements)

**Goal:** Fix the 6 concepts with zero cross-corpus links

**Priority 1: Deployment Concept** (2-3 hours)
1. Review [deployment_api_candidates.csv](../outputs/deployment_api_candidates.csv)
2. Update concept extraction patterns in `config/concepts.yml`
3. Re-run: `python scripts/03_extract_concepts.py`
4. Rebuild: Phases 4-5
5. Verify: `python compare_to_baseline.py`

**Expected Impact:**
- Deployment: 0 → 50+ cross-corpus links
- Concepts with gaps: 6 → 5
- Overall cross-corpus: +200-500 pairs

**Priority 2: Multi-Tenancy Concept** (2-3 hours)
- Similar process to Deployment
- Likely ~20-30 APIs need tagging

### Strategic Actions (Phases 2-3)

**Goal:** Reduce isolated sections and strengthen under-connected concepts

- Analyze the 603 isolated sections
- Add cross-references to related content
- Create bridging tutorials for semantic gaps
- Study well-connected patterns (Audit Trail, Conditional Appearance)

### Measurement Cadence

**After Each Improvement Phase:**
```bash
python tools/compare_to_baseline.py          # Show progress
python query_graph.py --mode gaps            # Verify gap reduction
python query_graph.py --mode stats           # Updated metrics
```

**Save Checkpoints:**
```bash
python tools/save_baseline_metrics.py
mv outputs/baseline_metrics.json outputs/metrics_phase1_complete.json
```

---

## Success Metrics

### Phase 1 Complete When:
- [ ] All 6 gap concepts have ≥10 cross-corpus links
- [ ] Deployment concept has ≥50 cross-corpus links
- [ ] Overall cross-corpus % ≥20.5% (currently 19.8%)

### Project Success When:
- [ ] Isolated sections <3% (currently 5.4%)
- [ ] Under-connected concepts <8 (currently 16)
- [ ] Avg connections/section ≥9.0 (currently 8.5%)
- [ ] All concepts above 7.0 links/section threshold

---

## Technical Notes

### Data Pipeline
- **Storage:** Parquet format for efficient columnar storage
- **Embeddings:** SentenceTransformer 'all-MiniLM-L6-v2' (384 dimensions)
- **Similarity:** Cosine similarity with 0.60 minimum threshold
- **Quality Gates:** Concept, platform, namespace, API overlap filters

### Computational Requirements
- **Phase 4 (Embeddings):** GPU recommended, ~30 minutes for 11K sections
- **Phase 5 (Semantic Pairs):** CPU intensive, ~10-15 minutes
- **Analysis Tools:** Instant (<1 minute each)

### Reproducibility
All analysis is deterministic given the same inputs:
1. Baseline captured in `baseline_metrics.json`
2. All thresholds documented in scripts
3. Quality gates explicitly defined
4. Success criteria quantified