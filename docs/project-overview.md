# XAF Documentation Analysis Project

## Table of Contents

- [Overview](#overview)
- [Pipeline 1: Knowledge Graph Construction](#pipeline-1-knowledge-graph-construction)
  - [Phase 1 — Read the documentation like a human would](#phase-1--read-the-documentation-like-a-human-would)
  - [Phase 2 — Capture how authors intended docs to connect](#phase-2--capture-how-authors-intended-docs-to-connect)
  - [Phase 3 — Teach the system XAF language](#phase-3--teach-the-system-xaf-language)
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
  - [Experimental: Ollama-Based API Classification](#experimental-ollama-based-api-classification)
- [Quality Metrics](#quality-metrics)
- [Quick Start Guide](#quick-start-guide)
- [What This Lets You Measure](#what-this-lets-you-measure)
- [Project Structure](#project-structure)
- [Key Files Reference](#key-files-reference)
- [Next Steps](#next-steps)
- [Success Metrics](#success-metrics)
- [Technical Notes](#technical-notes)

---

## Overview

This project analyzes DevExpress XAF (eXpressApp Framework) documentation to:
1. **Build a unified knowledge graph** of 11,000+ documentation sections
2. **Identify documentation gaps** (missing links, isolated content, under-connected concepts)
3. **Measure documentation quality** with quantifiable metrics
4. **Track improvements** over time with baseline comparison tools
5. **Guide documentation improvements** with actionable recommendations
6. **Generate AI-friendly metadata** for enhanced discoverability
7. **Map APIs to concepts** for better navigation and understanding
8. **Bridge support-ticket language** to documentation concepts for discoverability

The project consists of three main pipelines:
- **Knowledge Graph Pipeline** (Phases 1–5, 11–13): Build semantic understanding and a unified graph
- **Enrichment Pipeline** (Phases 5.5–10): Metadata generation, API mapping, and LLM classification
- **Quality & Analysis Tools**: Baseline metrics, gap analysis, concept reports, ticket discoverability

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

## Phase 3 — Teach the system XAF language

### Script
`scripts/03_extract_concepts.py`

### What this step does
It identifies:
- XAF concepts (Object Space, Validation, Security System…)
- Platforms (Blazor, WinForms, Web API)
- API names (DevExpress.ExpressApp.ObjectSpace, etc.)

It does this section by section, using the 148 concept definitions in `config/concepts.yml`.

### Why it matters
AI doesn't automatically know what matters in XAF. You explicitly teach it: "This section is about Object Space and applies to Blazor."

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
- Notebook: `notebooks/phase_3_5_metrics_snapshot.ipynb`

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

**Key Statistics:**
- 93,905 semantic pairs discovered
- 8.5 average connections per section
- 19.8% cross-corpus links (API ↔ Conceptual)
- Quality gates: concept overlap, platform overlap, namespace overlap

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

**Status:** ⚠️ Experimental - Requires LLM API configuration (OpenAI, Anthropic, or Ollama)

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
- Per-concept statistics (all 148 concepts)
- Cross-corpus gap analysis
- Isolated section identification
- Under-connected concept detection

**Output:**
- `outputs/baseline_metrics.json` - Machine-readable metrics
- `docs/BASELINE_METRICS.md` - Human-readable report

**Key Findings (Current Baseline):**
- 11,082 sections analyzed
- 603 isolated sections (5.4%)
- 6 concepts with zero cross-corpus links
- 16 under-connected concepts (<6 links/section)

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
| `tools/coverage_matrix_xaf.py` | XAF-specific coverage matrix with ticket counts, code sample presence, feature-to-concept mapping | `outputs/coverage_reports/` |

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

### MCP Server Integration

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

**Current Baseline (Feb 2026):**
- 14,860 total tickets analyzed
- 159 feature categories → 74 mapped concepts
- 7,975 API search tickets (53.7%) — biggest opportunity
- Top concept: View Items (1,634 tickets, 11.0%)

### Doc Issue Analysis

**Config:** `config/docissues.json` — Support ticket issues database (ticket IDs, titles, types, statuses, feedback)

**Output:** `outputs/docissue_analysis/` — Enriched analysis including concept-issue mapping, category breakdowns, and priority assignments.

### Experimental: Ollama-Based API Classification

**Scripts:** `scripts/experimental/`

| Script | Purpose |
|--------|---------|
| `12_map_apis_to_concepts_ollama.py` | Enhances Phase 12 with Ollama/Llama 3.1 classification for unmapped APIs |
| `validate_ollama_accuracy.py` | Validates LLM classification accuracy against ground truth |

⚠️ **Experimental** — See [ollama_decision_log.md](ollama_decision_log.md) for evaluation

**Usage:**
```bash
python scripts/experimental/12_map_apis_to_concepts_ollama.py --sample 10 --use-ollama
python scripts/experimental/validate_ollama_accuracy.py --sample 50
```

---

## Quality Metrics

### Current State

| Metric | Current State | Target |
|--------|--------------|--------|
| **Total Sections** | 11,082 | Stable |
| **Semantic Pairs** | 93,905 | 95,000+ |
| **Avg Connections/Section** | 8.5 | 9.0+ |
| **Isolated Sections** | 603 (5.4%) | <3% |
| **Cross-Corpus Links** | 18,613 (19.8%) | 21%+ |
| **Concepts with Gaps** | 6 | 0 |
| **Under-Connected Concepts** | 16 | <8 |

### Quality Gates (Semantic Pairs)

- Concept overlap: 73.1% of pairs
- Platform overlap: 33.0% of pairs
- Namespace overlap: 32.2% of pairs
- Average similarity: 0.759 (min: 0.600)

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
python tools/coverage_matrix_xaf.py
```

### 5. Make Improvements

Based on gap analysis, make documentation changes:
- Update concept definitions in `config/concepts.yml`
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

# Ollama-based API mapping
python scripts/experimental/12_map_apis_to_concepts_ollama.py --sample 10 --use-ollama
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
│   ├── 10_rollup_document_metadata.py    # Phase 10: Document-level metadata
│   ├── 11_extract_api_entities.py        # Phase 11: API entity extraction
│   ├── 12_map_apis_to_concepts.py        # Phase 12: API→Concept mapping
│   ├── 13_build_knowledge_graph.py       # Phase 13: Unified knowledge graph
│   ├── run_kg_pipeline_with_validation.py    # Full KG pipeline runner
│   ├── run_pipeline_with_validation.py       # MVP pipeline runner
│   ├── test_semantic_extraction.py           # Concept extraction tests
│   └── experimental/
│       ├── 12_map_apis_to_concepts_ollama.py # Ollama-based API classification
│       ├── validate_ollama_accuracy.py       # LLM accuracy validation
│       └── README.md
│
├── config/
│   ├── concepts.yml                # 148 XAF concept definitions (name, type, synonyms, keywords)
│   ├── docissues.json              # Support ticket issues database
│   ├── ticket_language_map.yml     # Ticket category → concept mapping (top 20 categories)
│   ├── validation_thresholds.yml   # Quality thresholds for all 13 pipeline phases
│   └── prompts/                    # AI extraction prompts
│       ├── ai_action_prompts.md
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
│   ├── deployment_api_candidates.csv / .json # Gap analysis
│   ├── coverage_reports/                     # Coverage matrix outputs
│   ├── docissue_analysis/                    # Doc issue breakdowns
│   ├── mvp_deliverables/                     # Packaged MVP outputs
│   ├── ticket_discoverability/               # Ticket analysis outputs
│   └── .emb_cache/                           # Embedding cache
│
├── docs/
│   ├── project-overview.md               # This file
│   ├── BASELINE_METRICS.md               # Current metrics report
│   ├── DOC_ANALYSIS_ACTION_PLAN.md       # Improvement roadmap
│   ├── prerequisites.md                  # Setup requirements
│   ├── ollama_decision_log.md            # Ollama evaluation log
│   ├── setup_ollama_classification.md    # Ollama setup guide
│   ├── XAF_Main_Concepts_for_LLM_Training.md  # LLM training concepts
│   ├── xaf concepts plan.md             # Concepts planning
│   └── xaf-doc-analysis_Architecture.docx # Architecture document
│
├── tools/                     # Analysis & utility tools
│   ├── concept_drilldown.py              # Single-concept deep dive
│   ├── concept_report.py                 # Concept-level metrics report
│   ├── coverage_matrix_xaf.py            # XAF coverage matrix
│   ├── extractor_sanity_check.py         # Validate extraction
│   ├── graph-sanity-check.py             # Validate graph
│   ├── keyword_section_query.py          # Keyword-based section search
│   ├── mcp_server_adapter.py             # MCP server integration
│   ├── package_mvp_deliverables.py       # Package MVP outputs
│   ├── save_baseline_metrics.py          # Capture quality baseline
│   ├── section_relationships.py          # Section subgraph extraction
│   ├── suggest_isolated_links.py         # Link suggestions for isolated sections
│   ├── env_check.ps1                     # Environment validation
│   ├── archive/                          # Superseded scripts (.bak)
│   │   ├── find_missing_deployment_apis.py.bak
│   │   ├── generate_crosslink_report.py.bak
│   │   ├── list_all_deployment_apis.py.bak
│   │   └── README.md
│   └── ticket_discoverability/           # Support ticket analysis
│       ├── analyze_real_tickets.py
│       ├── validate_ticket_mapping.py
│       ├── check_confidence_stats.py
│       └── README.md
│
├── utils/                     # Shared utilities
│   ├── __init__.py
│   ├── helpers.py                        # Data manipulation, concept checking
│   └── pipeline_validators.py            # Reusable validation (ValidationResult)
│
├── tests/                     # Test suite
│   ├── test_pipeline_integration.py      # Pipeline phase dependency tests
│   └── test_mcp_comparison.py            # MCP adapter vs production comparison
│
├── notebooks/
│   └── phase_3_5_metrics_snapshot.ipynb   # Phase 3.5 metrics notebook
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
| `semantic_pairs.parquet` | 93K relationship pairs | Analyzing connectivity |
| `sections_embeddings_*.parquet` | Vector embeddings | Similarity searches |
| `knowledge_graph.json` | Unified knowledge graph | Downstream tooling, MCP, dashboards |
| `classified_pairs_corrected.parquet` | Typed relationships (post-processed) | Learning paths, prerequisites |
| `baseline_metrics.json` | Current quality snapshot | Comparison baseline |
| `concept_quality_metrics.json` | Per-concept quality tracking | Concept refinement |
| `deployment_api_candidates.csv` | APIs needing tags | Fixing Deployment gap |
| `config/concepts.yml` | 148 concept definitions | Understanding taxonomy |
| `config/validation_thresholds.yml` | Quality thresholds for all phases | Pipeline validation tuning |
| `config/ticket_language_map.yml` | Ticket→concept mapping | Ticket discoverability |

---

## Next Steps

### Immediate Actions (Phase 1 Improvements)

**Goal:** Fix the 6 concepts with zero cross-corpus links

**Priority 1: Deployment Concept**
1. Review [deployment_api_candidates.csv](../outputs/deployment_api_candidates.csv)
2. Update concept extraction patterns in `config/concepts.yml`
3. Re-run: `python scripts/03_extract_concepts.py`
4. Rebuild: Phases 4-5, then 13
5. Verify: `python query_graph.py --mode gaps`

**Expected Impact:**
- Deployment: 0 → 50+ cross-corpus links
- Concepts with gaps: 6 → 5
- Overall cross-corpus: +200-500 pairs

**Priority 2: Multi-Tenancy Concept**
- Similar process to Deployment
- Likely ~20-30 APIs need tagging

### Strategic Actions

**Goal:** Reduce isolated sections and strengthen under-connected concepts

- Run `tools/suggest_isolated_links.py` for under-connected concepts
- Run `tools/concept_drilldown.py` to identify specific weak areas
- Add cross-references to related content
- Create bridging tutorials for semantic gaps
- Study well-connected patterns (Audit Trail, Conditional Appearance)

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
- [ ] All 6 gap concepts have ≥10 cross-corpus links
- [ ] Deployment concept has ≥50 cross-corpus links
- [ ] Overall cross-corpus % ≥20.5% (currently 19.8%)

### Project Success When:
- [ ] Isolated sections <3% (currently 5.4%)
- [ ] Under-connected concepts <8 (currently 16)
- [ ] Avg connections/section ≥9.0 (currently 8.5)
- [ ] All concepts above 7.0 links/section threshold

---

## Technical Notes

### Known Limitation: API Stub Pages Not Indexed

The corpus on disk contains **8,217 `.md` files** but only **5,517 appear in the pipeline**. This is expected — the 2,700 difference is fully accounted for by three legitimate exclusions:

| Reason | Count | Details |
|---|---|---|
| Field/enum/constant members | **651** | Excluded by Phase 1 by design (`--include-enum-fields` flag re-enables) |
| Zero-content API stubs | **1,509** | Pages for Properties (962), Methods (149), Constructors (165), Events (113), Namespaces (98) that have **0 words of body text** — just a type-signature header. Phase 1 parses them correctly but produces an empty `sections: []` list, so Phase 3 never creates concept rows for them. Most are from narrow testing namespaces like `DevExpress.EasyTest.Framework`. |
| All sections boilerplate | **539** | Pages that Phase 3 did process but where every section was too short or matched boilerplate skip patterns (e.g. "Parameters", "Returns"), leaving zero `kept=True` sections. |

**Verdict:** No ingestion bug. The pipeline handles all 8,217 files; it simply produces no output for pages that contain no meaningful prose.

---

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
- **`utils/helpers.py`** — Shared data manipulation, concept checking, metrics helpers
- **`utils/pipeline_validators.py`** — Reusable validation (`ValidationResult` data class) for schema, foreign key, and threshold checks
- **`tests/test_pipeline_integration.py`** — Integration tests for phase dependencies (`--phase N`)
- **`tests/test_mcp_comparison.py`** — Compares local MCP adapter against production dxdocs MCP

### Reproducibility
All analysis is deterministic given the same inputs:
1. Baseline captured in `baseline_metrics.json`
2. All thresholds documented in `config/validation_thresholds.yml`
3. Quality gates explicitly defined
4. Success criteria quantified
