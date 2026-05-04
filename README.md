# Documentation Analysis Pipeline

## Table of Contents

- [Overview](#overview)
- [Setup & Installation](#setup--installation)
- [Pipeline 1: Knowledge Graph Construction](#pipeline-1-knowledge-graph-construction)
  - [Phase 1 — Read the documentation like a human would](#phase-1--read-the-documentation-like-a-human-would)
  - [Phase 2 — Capture how authors intended docs to connect](#phase-2--capture-how-authors-intended-docs-to-connect)
  - [Phase 3 — Teach the system product language](#phase-3--teach-the-system-product-language)
  - [Phase 3.5 — Measure documentation readiness before AI](#phase-35--measure-documentation-readiness-before-ai)
  - [Phase 4 — Turn text into "meaning coordinates"](#phase-4--turn-text-into-meaning-coordinates)
  - [Phase 5 — Discover hidden relationships](#phase-5--discover-hidden-relationships)
  - [Phase 11 — Extract API Entities](#phase-11--extract-api-entities)
  - [Phase 12 — Map APIs to Concepts](#phase-12--map-apis-to-concepts)
  - [Phase 13 — Build Unified Knowledge Graph](#phase-13--build-unified-knowledge-graph)
- [Pipeline 2: Enrichment & Classification](#pipeline-2-enrichment--classification)
  - [Phase 5.5 — Filter High-Value Semantic Pairs](#phase-55--filter-high-value-semantic-pairs)
  - [Phase 6 — Classify Relationship Types (Experimental)](#phase-6--classify-relationship-types-experimental)
  - [Phase 7 — Generate AI-Friendly Metadata](#phase-7--generate-ai-friendly-metadata)
  - [Phase 8 — Export YAML Frontmatter](#phase-8--export-yaml-frontmatter)
  - [Phase 9 — Track Concept Quality Metrics](#phase-9--track-concept-quality-metrics)
  - [Phase 10 — Roll Up Document Metadata](#phase-10--roll-up-document-metadata)
- [Pipeline 3: Quality Analysis & Tooling](#pipeline-3-quality-analysis--tooling)
  - [Baseline & Gap Analysis](#baseline--gap-analysis)
  - [Concept Analysis Tools](#concept-analysis-tools)
  - [Section & Keyword Tools](#section--keyword-tools)
  - [Validation & Sanity Checks](#validation--sanity-checks)
  - [MCP Server Integration](#mcp-server-integration)
  - [MVP Deliverables](#mvp-deliverables)
  - [Ticket Discoverability](#ticket-discoverability)
  - [Doc Issue Analysis](#doc-issue-analysis)
- [Quick Start Guide](#quick-start-guide)
- [What This Lets You Measure](#what-this-lets-you-measure)
- [Project Structure](#project-structure)
- [Key Files Reference](#key-files-reference)
- [Next Steps](#next-steps)
- [Success Metrics](#success-metrics)
- [Technical Notes](#technical-notes)

---

## Overview

A product-agnostic pipeline for analyzing structured documentation sets. Originally built for DevExpress XAF; all product-specific values (taxonomy, support ticket paths, namespace mappings) are now in `config/product.yml` and `config/patterns.yml` — no Python changes needed to adapt for another product.

The pipeline:
1. **Builds a unified knowledge graph** of all documentation sections
2. **Identifies documentation gaps** (missing links, isolated content, under-connected concepts)
3. **Measures documentation quality** with quantifiable metrics
4. **Tracks improvements** over time with baseline comparison tools
5. **Guides documentation improvements** with actionable recommendations
6. **Generates AI-friendly metadata** for enhanced discoverability
7. **Maps APIs to concepts** for better navigation and understanding
8. **Bridges support-ticket language** to documentation concepts for discoverability

The project consists of three main pipelines:
- **Knowledge Graph Pipeline** (Phases 1–5, 11–13): Build semantic understanding and a unified graph
- **Enrichment Pipeline** (Phases 5.5–10): Metadata generation, API mapping, and LLM classification
- **Quality & Analysis Tools**: Baseline metrics, gap analysis, concept reports, ticket discoverability

---

## Setup & Installation

### Requirements

- Python **3.10 or 3.11**
- Git

### 1. Create a virtual environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install --upgrade pip setuptools wheel
pip install -r docs/requirements.txt
```

| Package | Used for |
|---------|---------|
| `pandas`, `numpy`, `pyarrow` | Data processing and Parquet I/O |
| `markdown-it-py`, `beautifulsoup4` | Markdown parsing (Phase 1) |
| `sentence-transformers` | Vector embeddings (Phase 4) |
| `scikit-learn` | Nearest-neighbor search (Phase 5) |
| `PyYAML` | Config and metadata export |
| `tqdm`, `regex` | Progress display and text matching |

**Optional extras:**

```bash
pip install openai anthropic   # Phase 6: LLM classification
pip install pyvis               # tools/visualize_graph.py
```

### 3. Configure product settings

Edit `config/product.yml` to point to your taxonomy, support tickets, and support concept map:

```yaml
product:
  name: "MyProduct"
  taxonomy_file: "config/my-taxonomy.json"
  support_tickets_file: "my_tickets.json"
  support_concept_map: "support_concept_map.yml"
```

Edit `config/patterns.yml` to set your namespace→concept mappings and external URL rules.

Create a `.env` file for runtime paths:

```env
PROJECT_ROOT=.
DATA_DIR=data
OUTPUT_DIR=outputs
```

For Phase 6, add an API key:

```env
OPENAI_API_KEY=sk-...
# or
ANTHROPIC_API_KEY=...
```

### 4. Add documentation source files

Copy Markdown files into `data/raw_md/`, preserving folder structure:

```
data/raw_md/
├── apidoc/      # API reference namespaces
└── articles/    # Conceptual articles
```

### 5. Validate

```bash
python -c "import pandas, numpy, sklearn; print('Core OK')"
python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2'); print('Embeddings OK')"
python -c "import yaml; print('YAML OK')"
```

The embeddings check downloads the model (~80 MB) on first run.

```powershell
.\tools\env_check.ps1
```

> Full setup details: [docs/prerequisites.md](docs/prerequisites.md)

---

## Pipeline 1: Knowledge Graph Construction

### Goal
Transform raw documentation into a unified knowledge graph that AI and humans can query, navigate, and reason about.

### Phases

## Phase 1 — Read the documentation like a human would

### Script
`scripts/01_ingest_parse.py`

### What this step does
It reads every Markdown file and breaks it into:
- Documents
- Section titles
- Sections of text
- Code blocks
- Explicit links between pages

### Why it matters
Before AI can understand documentation, it has to be structured. Humans understand that:
_"Object Space > Create, Read, Update and Delete Data"_ is more specific than _"Data Manipulation"_.
This step preserves document structure, instead of flattening text.

### Output
`topics_inventory.parquet`

This is your source of truth:
- "Which sections exist?"
- "Where do they live?"
- "How long are they?"

Think of it as an indexed table of contents for the entire documentation set.

## Phase 2 — Capture how authors intended docs to connect

### Script
`scripts/02_build_explicit_graph.py`

### What this step does
It looks at:
- "See also"
- Cross‑references
- Internal links

And builds a graph like: Page A → Page B → Page C

### Why it matters
Links are human intent. If an author linked two pages, that relationship matters—even if the text doesn't look similar.

### Output
`explicit_graph.parquet`

This answers questions like:
- Which pages are popular hubs?
- Which pages are never linked?
- Where navigation might be broken?

This is the "hallway map" of the documentation.

## Phase 3 — Teach the system product language

### Script
`scripts/03_extract_concepts.py`

### What this step does
It identifies:
- Product concepts (defined in your taxonomy)
- Platforms and target environments
- API names and namespace references

It does this section by section, using the concept definitions in the taxonomy file configured in `config/product.yml` (`product.taxonomy_file`).

### Why it matters
AI doesn't automatically know what matters for your product. You explicitly teach it: "This section is about Object Space and applies to Blazor."

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

This phase turns "AI experimentation" into a **controlled, auditable process**.

### Key outputs
- A **metrics snapshot** answering:
  - "Is the corpus clean enough to embed?"
  - "Are API docs filtered to the right signal level?"
  - "Are concepts explicit and well‑distributed?"
- Recommended **initial thresholds** for:
  - Embedding inclusion
  - Semantic similarity gates
  - API vs. conceptual balance

Only after this step do we proceed to embeddings.

## Phase 4 — Turn text into "meaning coordinates"

### Script
`scripts/04_make_sections_embeddings.py`

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
- Automatic "related topics"

Instead of keyword matching "save" ≠ "save" we get: "persist data", "commit changes", "save object" → same idea

### Output
`sections_embeddings_conceptual.parquet`
`sections_embeddings_api.parquet`

Think of these as a GPS map of meaning for your documentation.

## Phase 5 — Discover hidden relationships

### Script
`scripts/05_find_semantic_pairs.py`

### What this step does
It asks: "Which sections talk about similar things, even if no link exists?" and applies rules to keep only useful relationships:
- Concept ↔ concept
- API ↔ API
- Concept ↔ API

### Examples
- A "Security System Overview" section is closely related to a "PermissionPolicyRole API" page.
- Two Blazor‑specific explanations of filtering belong together.
- API pages in the same namespace naturally cluster.

### Why it matters
This reveals:
- Missing links
- Redundant content
- Hidden documentation gaps

### Output
`semantic_pairs.parquet`

This is the "possible connections humans forgot to add."

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
- `outputs/api_entities.parquet` - Unique API definitions
- `outputs/documents_api.parquet` - Section → API relationships

## Phase 12 — Map APIs to Concepts

### Script
`scripts/12_map_apis_to_concepts.py`

### What this step does
Creates API → Concept implementation mappings using three strategies:
1. **Co-occurrence** - APIs and concepts appearing together in documentation
2. **Namespace rules** - loaded from `config/patterns.yml` (`namespace_concept_map`)
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

## Phase 13 — Build Unified Knowledge Graph

### Script
`scripts/13_build_knowledge_graph.py`

### What this step does
Creates a single, explainable knowledge graph artifact by merging outputs from multiple phases:
- Document/section structure (Phase 1)
- Explicit cross-links (Phase 2)
- Concept/API/platform tagging (Phase 3)
- Semantic similarity edges (Phase 5)
- Typed relationships (Phase 6, if present)
- API entity inventory (Phase 11)
- API→Concept mappings (Phase 12)

### Why it matters
This is the **primary deliverable** of the pipeline — a unified graph designed for downstream tooling:
- MCP server adapters
- Dashboards and visualizations
- AI-powered navigation
- Cross-reference recommendations

The graph does NOT embed raw section text; it stores structure, relationships, and metadata.

### Output
`outputs/knowledge_graph.json`

A JSON file containing nodes (documents, sections, concepts, APIs) and edges (explicit links, semantic pairs, API-concept mappings, typed relationships).

### Pipeline Runner

The full knowledge graph pipeline can be run end-to-end with validation:

```bash
python scripts/run_kg_pipeline_with_validation.py
```

This executes Phases 1 → 2 → 3 → 4 → 5 → 11 → 12 → 13 in sequence, with Phase 6 (classification) included if an LLM provider is configured. Each phase is validated against thresholds defined in `config/validation_thresholds.yml`.

---

## Pipeline 2: Enrichment & Classification

### Goal
Enhance documentation with AI-powered classification, metadata generation, and quality tracking.

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

## Phase 6 — Classify Relationship Types (Expensive)

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

### Post-processing
`scripts/07_postprocess_classifications.py` corrects over-aggressive bidirectional marking:
- "uses" relationships: Only bidirectional if similarity ≥ 0.90 AND confidence ≥ 0.85
- Other types: Keep existing (conservative rules already applied)

### Why it matters
Enables intelligent features:
- Smart navigation ("Read this first")
- Learning path generation
- Prerequisites identification
- AI reasoning about documentation structure

### Output
- `outputs/classified_pairs.parquet` - Classified relationship pairs
- `outputs/classified_pairs_corrected.parquet` - Post-processed (false positive reduction)
- Checkpoint files for resume support (`classified_pairs_checkpoint_pid_*.parquet`)

**Status:** ⚠️ Expensive - Requires LLM API configuration (OpenAI or Anthropic)

**Usage:**
```bash
# Test on 100 pairs
python scripts/06_classify_relationships.py --limit 100

# Resume from checkpoint
python scripts/06_classify_relationships.py --resume outputs/classified_pairs_checkpoint.parquet

# Post-process to reduce false positives
python scripts/07_postprocess_classifications.py
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

---

## Pipeline 3: Quality Analysis & Tooling

### Goal
Measure documentation quality, identify gaps, track improvements, and provide actionable analysis tools.

## Baseline & Gap Analysis

### Establishing Baseline

**Script:** `tools/save_baseline_metrics.py`

Captures comprehensive baseline statistics:
- Overall connectivity metrics
- Per-concept statistics
- Cross-corpus gap analysis
- Isolated section identification
- Under-connected concept detection

**Output:**
- `outputs/baseline_metrics.json` - Machine-readable metrics
- `docs/BASELINE_METRICS.md` - Human-readable report

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

### Concept Analysis Tools

| Tool | Purpose | Output |
|------|---------|--------|
| `tools/concept_drilldown.py` | Deep-dive on a single concept: API/conceptual split, platform distribution, connectivity stats, top/least connected sections | `outputs/concept_<name>_sections.csv` |
| `tools/concept_report.py` | Aggregated concept metrics: sections, connections, cross-corpus pairs, mapped APIs per concept | `outputs/concept_report.csv`, `outputs/concept_report.json` |
| `tools/suggest_isolated_links.py` | Finds isolated sections for a concept and recommends link targets via embedding nearest neighbors | `outputs/isolated_<concept>_link_suggestions.csv/.md` |
| `tools/coverage_matrix.py` | Coverage matrix with ticket counts, code sample presence, feature-to-concept mapping; paths loaded from `config/product.yml` | `outputs/coverage_reports/` |

### Section & Keyword Tools

| Tool | Purpose | Output |
|------|---------|--------|
| `tools/keyword_section_query.py` | Search section text for keywords not in the concept taxonomy | `outputs/keyword_hits.csv` |
| `tools/section_relationships.py` | Build induced subgraph over selected sections from semantic pairs and classified pairs | Relationship edges/nodes CSVs |

### Validation & Sanity Checks

| Tool | Purpose |
|------|---------|
| `tools/extractor_sanity_check.py` | Validate concept extraction results |
| `tools/graph-sanity-check.py` | Validate graph structure and integrity |

### MCP Server Integration (Experimental)

**Script:** `tools/mcp_server_adapter.py`

Provides clean function interfaces for MCP server integration. The `XAFDocAnalysis` class exposes methods like:
- `get_documentation_gaps(concept="Security System")`
- `get_crosslink_recommendations(limit=20)`

All functions return JSON-serializable structures for downstream consumption.

### MVP Deliverables

**Script:** `tools/package_mvp_deliverables.py`

Creates a curated output set for tech writers and stakeholders:
- Gap analysis summary (JSON)
- Top priority actions (CSV)
- Metadata samples (YAML)
- Baseline snapshot (JSON)

**Output:** `outputs/mvp_deliverables/`

### Ticket Discoverability

**Directory:** `tools/ticket_discoverability/`

Tools for analyzing the language gap between support tickets (problem-based) and documentation (architecture-based).

| Tool | Purpose |
|------|---------|
| `analyze_real_tickets.py` | Maps ticket feature categories to concepts, identifies high-volume gaps, prioritizes ontology implementation |
| `validate_ticket_mapping.py` | Compares baseline vs current ticket-to-concept mappings |
| `check_confidence_stats.py` | Checks confidence statistics for ticket mappings |


### Doc Issue Analysis

**Config:** `config/docissues.json` — Support ticket issues database (ticket IDs, titles, types, statuses, feedback)

**Output:** `outputs/docissue_analysis/` — Enriched analysis including concept-issue mapping, category breakdowns, and priority assignments.

---

---

## Quick Start Guide

### 1. Build Knowledge Graph (Full Pipeline)

```bash
# Run the full KG pipeline with validation
python scripts/run_kg_pipeline_with_validation.py

# Or run core phases individually
python scripts/01_ingest_parse.py
python scripts/02_build_explicit_graph.py
python scripts/03_extract_concepts.py
python scripts/04_make_sections_embeddings.py --batch-size 32 --max-chars 4000
python scripts/05_find_semantic_pairs.py
python scripts/11_extract_api_entities.py
python scripts/12_map_apis_to_concepts.py
python scripts/13_build_knowledge_graph.py
```

### 2. Generate Enrichments (Phases 7-10)

```bash
python scripts/07_generate_metadata.py
python scripts/08_export_yaml_metadata.py
python scripts/09_concept_quality_metrics.py
python scripts/10_rollup_document_metadata.py
```

### 3. Establish Baseline

```bash
python tools/save_baseline_metrics.py

# Review:
#   outputs/baseline_metrics.json
#   docs/BASELINE_METRICS.md
```

### 4. Analyze Gaps & Quality

```bash
# Overall picture
python query_graph.py --mode gaps

# Concept deep-dives
python tools/concept_drilldown.py --concept "Deployment"
python tools/concept_report.py

# Find link opportunities for isolated sections
python tools/suggest_isolated_links.py --concept "Deployment"

# Coverage matrix
python tools/coverage_matrix.py
```

### 5. Make Improvements

Based on gap analysis, make documentation changes:
- Update concept definitions in your taxonomy file (set in `config/product.yml`)
- Re-run extraction: `python scripts/03_extract_concepts.py`
- Rebuild graph: Phases 4-5, then 13
- Add cross-references to isolated sections
- Create bridging content for semantic gaps

### 6. Measure Progress

```bash
python query_graph.py --mode stats
python query_graph.py --mode gaps
python tools/concept_report.py
```

### 7. (Optional) LLM Classification

```bash
# Classify relationship types (requires LLM API)
python scripts/06_classify_relationships.py --limit 100

# Post-process to reduce false positives
python scripts/07_postprocess_classifications.py

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


### For Content Strategy

**Questions Answered:**
- Which concepts are well-documented (benchmarks)?
- What patterns make content discoverable?
- Where should writers focus next?
- How does platform coverage compare?


### For AI/RAG Systems

**Questions Answered:**
- Can the system consistently retrieve the right section?
- Does every answer have a clear source?
- Are platform differences respected?
- Is the knowledge graph dense enough?

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
├── scripts/                    # Core pipeline scripts
│   ├── config_loader.py                  # ★ Central config accessor (cfg, patterns) (NEW)
│   ├── 01_ingest_parse.py                # Phase 1: Parse markdown → structured data
│   ├── 02_build_explicit_graph.py        # Phase 2: Extract/resolve internal links
│   ├── 03_extract_concepts.py            # Phase 3: Tag sections with concepts
│   ├── 04_make_sections_embeddings.py    # Phase 4: Generate vector embeddings
│   ├── 05_find_semantic_pairs.py         # Phase 5: Discover semantic relationships
│   ├── 05_5_filter_high_value_pairs.py   # Phase 5.5: Filter for LLM classification
│   ├── 06_classify_relationships.py      # Phase 6: LLM relationship classification
│   ├── 07_generate_metadata.py           # Phase 7: AI-friendly metadata
│   ├── 07_postprocess_classifications.py # Phase 6 post-processing (false positive reduction)
│   ├── 08_export_yaml_metadata.py        # Phase 8: YAML frontmatter export
│   ├── 09_concept_quality_metrics.py     # Phase 9: Concept quality tracking
│   ├── 09b_generate_descriptions.py      # Phase 9b: LLM-generated section descriptions
│   ├── 10_rollup_document_metadata.py    # Phase 10: Document-level metadata
│   ├── 11_extract_api_entities.py        # Phase 11: API entity extraction
│   ├── 12_map_apis_to_concepts.py        # Phase 12: API→Concept mapping
│   ├── 13_build_knowledge_graph.py       # Phase 13: Unified knowledge graph
│   ├── run_kg_pipeline_with_validation.py    # Full KG pipeline runner
│   ├── run_pipeline_with_validation.py       # MVP pipeline runner
│   └── test_semantic_extraction.py           # Concept extraction tests
│
├── config/
│   ├── product.yml                     # ★ Product identity & per-product settings (NEW)
│   ├── patterns.yml                    # ★ URL rules & namespace→concept map (NEW)
│   ├── xaf-taxonomy.json               # XAF concept definitions (name, type, synonyms, keywords)
│   ├── xaf-taxonomy.schema.json        # JSON schema for taxonomy validation
│   ├── xaf-domain-registry.yml         # Domain registry for taxonomy governance
│   ├── xaf-taxonomy-contribution-guide.md  # Guide for extending the taxonomy
│   ├── xaf-taxonomy-schema-contract.md     # Formal schema contract
│   ├── ticket_language_map.yml         # Ticket category → concept mapping
│   ├── validation_thresholds.yml       # Quality thresholds for all 13 pipeline phases
│   └── prompts/                        # AI extraction prompts
│       ├── metadata_description.md
│       └── relationship_classification.md
│
├── outputs/                   # All generated data
│   ├── topics_inventory.parquet              # Phase 1
│   ├── explicit_graph.parquet                # Phase 2
│   ├── doc_concepts.parquet                  # Phase 3
│   ├── sections_embeddings_conceptual.parquet # Phase 4
│   ├── sections_embeddings_api.parquet       # Phase 4
│   ├── semantic_pairs.parquet                # Phase 5
│   ├── semantic_pairs_high_value.parquet     # Phase 5.5
│   ├── classified_pairs.parquet              # Phase 6
│   ├── classified_pairs_corrected.parquet    # Phase 6 (post-processed)
│   ├── metadata_suggestions.parquet          # Phase 7
│   ├── document_metadata.parquet             # Phase 10
│   ├── api_entities.parquet                  # Phase 11
│   ├── documents_api.parquet                 # Phase 11
│   ├── api_implements_concept.parquet        # Phase 12
│   ├── knowledge_graph.json                  # Phase 13
│   ├── baseline_metrics.json                 # Quality baseline
│   ├── concept_quality_metrics.json          # Phase 9
│   ├── concept_report.csv / .json            # Concept-level metrics
│   ├── coverage_reports/                     # Coverage matrix outputs
│   ├── mvp_deliverables/                     # Packaged MVP outputs
│   ├── ticket_discoverability/               # Ticket analysis outputs
│   └── .emb_cache/                           # Embedding cache
│
├── docs/
│   ├── index.html                        # Project landing page
│   ├── knowledge_graph_explorer.html     # Interactive knowledge graph viewer
│   ├── metadata_reviewer.html            # Interactive metadata review tool
│   ├── project-overview.md               # Project documentation
│   ├── BASELINE_METRICS.md               # Baseline metrics report (Feb 2026)
│   ├── BASELINE_METRICS_2026-04-23.md    # Latest metrics snapshot
│   ├── DOCUMENTATION_GAPS_BACKLOG.md     # Gap analysis backlog
│   ├── WHATS_NEW.md                      # Changelog
│   ├── taxonomy_review_2026-04-16.md     # Taxonomy review notes
│   ├── prerequisites.md                  # Setup requirements
│   ├── requirements.txt                  # Python dependencies
│   └── xaf-doc-analysis_Architecture.docx # Architecture document
│
├── tools/                     # Analysis & utility tools
│   ├── build_metadata_reviewer.py        # Generate docs/metadata_reviewer.html
│   ├── visualize_graph.py                # Generate docs/knowledge_graph_explorer.html
│   ├── concept_drilldown.py              # Single-concept deep dive
│   ├── concept_report.py                 # Concept-level metrics report
│   ├── coverage_matrix.py                # Coverage matrix (product paths from config/product.yml)
│   ├── extractor_sanity_check.py         # Validate extraction
│   ├── graph-sanity-check.py             # Validate graph
│   ├── generate_documentation_gaps_backlog.py  # Generate gap analysis backlog
│   ├── keyword_section_query.py          # Keyword-based section search
│   ├── mcp_server_adapter.py             # MCP server integration
│   ├── package_mvp_deliverables.py       # Package MVP outputs
│   ├── save_baseline_metrics.py          # Capture quality baseline
│   ├── section_relationships.py          # Section subgraph extraction
│   ├── suggest_isolated_links.py         # Link suggestions for isolated sections
│   ├── env_check.ps1                     # Environment validation
│   ├── archive/                          # Superseded scripts (.bak)
│   │   └── README.md
│   └── ticket_discoverability/           # Support ticket analysis
│       ├── analyze_real_tickets.py
│       ├── validate_ticket_mapping.py
│       ├── check_confidence_stats.py
│       └── README.md
│
├── utils/                     # Shared utilities
│   ├── taxonomy_loader.py                # Taxonomy loading and concept lookup
│   └── pipeline_validators.py            # Reusable validation (ValidationResult)
│
├── tests/                     # Test suite
│   ├── test_pipeline_integration.py      # Pipeline phase dependency tests
│   ├── test_mcp_comparison.py            # MCP adapter vs production comparison
│   ├── test_classify_relationships.py    # Relationship classification tests
│   ├── test_extract_concepts.py          # Concept extraction tests
│   ├── test_make_sections_embeddings.py  # Embeddings pipeline tests
│   └── test_taxonomy_loader.py           # Taxonomy loader tests
│
├── data/
│   ├── raw_md/                           # Source documentation
│   │   ├── apidoc/                       # 100+ DevExpress API namespace dirs
│   │   └── articles/                     # 40+ article dirs/files
│   └── interim/                          # Intermediate processing
│
├── query_graph.py             # Main query tool (root)
├── README.md                  # Quick start guide
└── requirements-lock.txt      # Python dependencies
```

---

## Key Files Reference

| File | Purpose | When to Use It |
|------|---------|---------------|
| `topics_inventory.parquet` | Full text of all sections | Reading actual content |
| `doc_concepts.parquet` | Section metadata & concept tags | Filtering by concept/platform |
| `semantic_pairs.parquet` | Semantic relationship pairs | Analyzing connectivity |
| `sections_embeddings_*.parquet` | Vector embeddings | Similarity searches |
| `knowledge_graph.json` | Unified knowledge graph | Downstream tooling, MCP, dashboards |
| `classified_pairs_corrected.parquet` | Typed relationships (post-processed) | Learning paths, prerequisites |
| `baseline_metrics.json` | Current quality snapshot | Comparison baseline |
| `concept_quality_metrics.json` | Per-concept quality tracking | Concept refinement |
| `deployment_api_candidates.csv` | APIs needing tags | Fixing Deployment gap |
| `config/product.yml` | Product name, taxonomy/ticket/support-map paths, noise concepts, gap concepts | Adapting to a new product |
| `config/patterns.yml` | External URL rules, namespace→concept mappings | Namespace classification |
| `config/xaf-taxonomy.json` | XAF concept definitions | Understanding taxonomy |
| `config/validation_thresholds.yml` | Quality thresholds for all phases | Pipeline validation tuning |
| `config/ticket_language_map.yml` | Ticket→concept mapping | Ticket discoverability |

---

### Strategic Actions

**Goal:** Reduce isolated sections and strengthen under-connected concepts

- Run `tools/suggest_isolated_links.py` for under-connected concepts
- Run `tools/concept_drilldown.py` to identify specific weak areas
- Add cross-references to related content
- Create bridging tutorials for semantic gaps
- Study well-connected patterns 

### Measurement Cadence

**After Each Improvement Phase:**
```bash
python query_graph.py --mode gaps            # Verify gap reduction
python query_graph.py --mode stats           # Updated metrics
python tools/concept_report.py               # Per-concept metrics
```

**Save Checkpoints:**
```bash
python tools/save_baseline_metrics.py
```

---

## Success Metrics

### Phase 1 Complete When:
- [ ] All gap concepts have cross-corpus links
- [ ] Deployment concept is well-connected
- [ ] Overall cross-corpus % is improving

### Project Success When:
- [ ] Isolated sections <5%
- [ ] Under-connected concepts minimized
- [ ] Avg connections/section meets target
- [ ] All concepts above minimum links/section threshold

---

## Technical Notes

### Data Pipeline
- **Storage:** Parquet format for efficient columnar storage
- **Embeddings:** SentenceTransformer 'all-MiniLM-L6-v2' (384 dimensions)
- **Similarity:** Cosine similarity with 0.60 minimum threshold
- **Quality Gates:** Concept, platform, namespace, API overlap filters
- **Validation:** All phases validated against `config/validation_thresholds.yml`

### Computational Requirements
- **Phase 4 (Embeddings):** GPU recommended, ~30 minutes for 11K sections
- **Phase 5 (Semantic Pairs):** CPU intensive, ~10-15 minutes
- **Phase 13 (Knowledge Graph):** Fast (<1 minute), merges existing outputs
- **Analysis Tools:** Instant (<1 minute each)

### Infrastructure
- **`scripts/config_loader.py`** — Central config accessor; exposes `cfg` (product.yml) and `patterns` (patterns.yml) singletons used by all pipeline scripts
- **`utils/taxonomy_loader.py`** — Taxonomy loading, concept lookup, and context string generation
- **`utils/pipeline_validators.py`** — Reusable validation (`ValidationResult` data class) for schema, foreign key, and threshold checks
- **`tests/test_pipeline_integration.py`** — Integration tests for phase dependencies (`--phase N`)
- **`tests/test_mcp_comparison.py`** — Compares local MCP adapter against production dxdocs MCP

### Reproducibility
All analysis is deterministic given the same inputs:
1. Baseline captured in `baseline_metrics.json`
2. All thresholds documented in `config/validation_thresholds.yml`
3. Quality gates explicitly defined
4. Success criteria quantified
