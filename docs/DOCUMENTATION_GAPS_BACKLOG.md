# Documentation Gaps Backlog

Generated: 2026-04-23 19:05

## Input Files
- config\xaf-taxonomy.json
- outputs\doc_concepts.parquet
- outputs\topics_inventory.parquet
- outputs\explicit_graph.parquet
- outputs\semantic_pairs.parquet
- outputs\classified_pairs.parquet
- outputs\api_entities.parquet
- outputs\api_implements_concept.parquet
- outputs\coverage_reports\high_priority_gaps.csv
- outputs\article_descriptions.parquet
- outputs\metadata_suggestions.parquet
- outputs\query_graph_gaps.txt

## Executive Summary
- Unused taxonomy concepts: 15 / 148
- Rare concepts (<5 kept sections): 31
- Underlinked docs (concept_count >= 10 and link_ratio < 0.20): 0
- Zero-link docs (same concept threshold): 0
- Missing descriptions: 1
- API mapping coverage: 2380/3243 (73.4%)
- Semantic fallback rate: 18170/75193 (24.2%)
- High-priority ticket-driven gaps: 23
- Cross-linking recommendations available: 0

## P0 - Immediate Priority

### Item P0.1 - Resolve Ticket-Driven Critical Gaps
- What: Close high-volume support concepts flagged as critical gaps.
- Why: These concepts have high ticket demand but insufficient documentation depth.
- Data evidence: 23 critical gaps from coverage matrix.
- Acceptance criteria:
  - Reduce critical gaps by at least 30% in the next refresh.
  - Each resolved concept has at least one overview page and one task-oriented page.
  - coverage_reports/high_priority_gaps.csv count is lower than the current baseline.
| concept_name | ticket_count | doc_score | coverage_class |
| --- | --- | --- | --- |
| Standard Property Editors | 765 | 0 | critical_gap |
| Performance Optimization | 394 | 0.6 | critical_gap |
| Layout Runtime Customization | 377 | 1.5 | critical_gap |
| Layout Generation | 329 | 0 | critical_gap |
| CRUD Controllers | 276 | 0 | critical_gap |
| Built-in Criteria Operators | 216 | 1.5 | critical_gap |
| Filtering UI | 194 | 0 | critical_gap |
| Model Extension | 191 | 0 | critical_gap |
| Inline Editing | 144 | 1.5 | critical_gap |
| Popup Windows | 144 | 2.5 | critical_gap |
| Legacy .NET Framework | 134 | 1.5 | critical_gap |
| Custom Criteria Functions | 130 | 1.5 | critical_gap |
| Multiple Databases | 95 | 0 | critical_gap |
| Dependency Injection | 84 | 2 | critical_gap |
| Memory Management | 73 | 0 | critical_gap |
| Diagnostic Tools | 61 | 2.5 | critical_gap |
| Programmatic Localization | 58 | 0 | critical_gap |
| Async Operations | 42 | 1.5 | critical_gap |
| Scaling Architecture | 39 | 0 | critical_gap |
| Recurring Events | 30 | 1.5 | critical_gap |

### Item P0.2 - Fix Underlinked High-Concept Documents
- What: Add internal links for concept-dense documents with very low link_ratio.
- Why: Discoverability and navigability are bottlenecked by sparse explicit linking.
- Data evidence: 0 underlinked docs, including 0 zero-link docs.
- Acceptance criteria:
  - Zero-link docs in this bucket reduced to 0.
  - Median link_ratio for this bucket reaches at least 0.5.
  - No doc with concept_count >= threshold remains below link_ratio 0.1.
No rows.

### Item P0.3 - Improve API-to-Concept Mapping
- What: Map unmapped APIs to taxonomy concepts, prioritizing heavy namespaces.
- Why: Unmapped APIs weaken semantic connections and concept-level coverage analytics.
- Data evidence: 863 unmapped APIs out of 3243 total (73.4% mapped).
- Acceptance criteria:
  - Raise API mapping coverage to at least 90%.
  - Top 5 unmapped namespace roots each reduced by at least 50%.
  - Regenerated api_implements_concept.parquet includes new mappings.
| namespace_root | unmapped_api_count |
| --- | --- |
| DevExpress | 863 |

## P1 - High Value Next

### Item P1.1 - Handle Unused Taxonomy Concepts
- What: Either add anchor documentation for unused concepts or deprecate/merge obsolete concepts.
- Why: Unused taxonomy nodes indicate vocabulary drift or missing content coverage.
- Data evidence: 15 concepts appear nowhere in kept doc concepts.
- Acceptance criteria:
  - For each retained concept, add 1-3 anchor sections with explicit concept tags.
  - Or remove/merge obsolete concepts in config/xaf-taxonomy.json with rationale.
- CRUD Controllers
- Dashboard View Items
- Detail View
- Error Styling
- Filtering UI
- Layout Generation
- List View Controllers
- Memory Management
- Model Extension
- Multiple Databases
- Programmatic Localization
- Runtime Language Switcher
- Scaling Architecture
- Standard Property Editors
- View Lifecycle

### Item P1.2 - Expand Rare Concepts
- What: Increase depth and cross-linking for concepts with sparse section coverage.
- Why: Low section counts reduce retrieval confidence and concept discoverability.
- Data evidence: 31 concepts have < 5 kept sections.
- Acceptance criteria:
  - No active concept remains below the rare threshold without an explicit exception.
  - Each rare concept gains at least one overview and one linked task/reference section.
| concept_name | section_count |
| --- | --- |
| Async Operations | 1 |
| Business Object Lifecycle | 1 |
| Generic View Controllers | 1 |
| Custom User Management | 1 |
| Layout Runtime Customization | 1 |
| Performance Optimization | 1 |
| Object View Controllers | 1 |
| Collection Property Editors | 2 |
| Custom Validation Rules | 2 |
| Charts | 2 |
| Built-in Criteria Operators | 2 |
| Direct SQL | 2 |
| Controller Lifecycle | 2 |
| Middle Tier | 2 |
| Controller Customization | 2 |
| Action Customization | 2 |
| Master-Detail Views | 2 |
| Popup Windows | 2 |
| Target Properties | 2 |
| Nested Views | 3 |

### Item P1.3 - Fill Missing Descriptions
- What: Add concise descriptions for docs missing metadata summaries.
- Why: Missing descriptions degrade search snippets, metadata quality, and triage UX.
- Data evidence: 1 docs missing descriptions.
- Acceptance criteria:
  - Missing description count reduced by at least 70%.
  - Remaining missing entries are intentional (redirect/index/special pages).
| doc_id | concept_count | path | title |
| --- | --- | --- | --- |
| data/raw_md/articles/data-manipulation-and-business-logic/ways-to-implement-business-logic | 0 | data\raw_md\articles\data-manipulation-and-business-logic\ways-to-implement-business-logic.md | ways-to-implement-business-logic |

## P2 - Optimization

### Item P2.1 - Reduce Semantic Fallback Dependence
- What: Increase concept/API overlap links so fewer pairs rely on high_similarity_fallback.
- Why: Fallback-heavy linkage is less explainable and can be lower precision.
- Data evidence: fallback appears in 18170/75193 pairs (24.2%).
- Acceptance criteria:
  - Reduce fallback rate by at least 20% relative.
  - Each neighbor_type bucket shows non-increasing fallback share.
| neighbor_type | total_pairs | fallback_pairs | fallback_pct |
| --- | --- | --- | --- |
| cc | 29984 | 15570 | 51.928 |
| aa | 21039 | 2217 | 10.538 |
| ac | 8858 | 208 | 2.348 |
| ca | 15312 | 175 | 1.143 |

### Item P2.2 - Execute Cross-Link Recommendation Queue
- What: Process top ticket-weighted actionable cross-link suggestions into explicit internal links.
- Why: Recommendations identify high-yield links that improve navigation and are weighted by customer pain.
- Data evidence: 0 recommendation rows available.
- Acceptance criteria:
  - Complete top 50 recommendations and regenerate explicit_graph.parquet.
  - Recomputed underlinked bucket shrinks by at least 25%.
No recent actionable cross-linking file detected (outputs/cross_linking_filtered_actionable.csv).

## How To Refresh
1. `$env:PYTHONUTF8=1; & .venv\Scripts\python.exe tools/coverage_matrix_xaf.py`
2. `$env:PYTHONUTF8=1; & .venv\Scripts\python.exe query_graph.py --mode gaps | Out-File outputs/query_graph_gaps.txt -Encoding utf8`
3. `$env:PYTHONUTF8=1; & .venv\Scripts\python.exe tools/generate_documentation_gaps_backlog.py`
