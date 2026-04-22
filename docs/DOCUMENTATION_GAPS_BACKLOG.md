# Documentation Gaps Backlog

Generated: 2026-04-22 10:31

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
- outputs\cross_linking_filtered_actionable.csv
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
- Cross-linking recommendations available: 553

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
- Data evidence: 553 recommendation rows available.
- Acceptance criteria:
  - Complete top 50 recommendations and regenerate explicit_graph.parquet.
  - Recomputed underlinked bucket shrinks by at least 25%.
| uid | title | realistic_score | ticket_weight | ticket_count | num_actual_useful_apis | path |
| --- | --- | --- | --- | --- | --- | --- |
| 118451 | How to: Show Various Notifications to Multiple Users | 198.747 | 2.008 | 869 | 14 | data\raw_md\articles\event-planning-and-notifications\how-to-show-various-notifications-for-multiple-users.md |
| 402155 | Add a Parametrized Action | 190.717 | 2.008 | 869 | 10 | data\raw_md\articles\getting-started\in-depth-tutorial-blazor\add-actions-menu-commands\add-a-parametrized-action.md |
| 113161 | How to: Access Nested List View or Master Detail View Environment (ASP.NET Core Blazor and Windows Forms) | 188.709 | 2.008 | 869 | 9 | data\raw_md\articles\ui-construction\ways-to-access-ui-elements-and-their-controls\how-to-access-master-detail-view-and-nested-list-view-environment.md |
| 116516 | Non-Persistent Objects | 184.694 | 2.008 | 869 | 12 | data\raw_md\articles\business-model-design-orm\non-persistent-objects.md |
| 113653 | How to Add an Unbound Control (Button) to the Form Layout in an XAF View (with a Fully Custom ViewItem) | 178.672 | 2.008 | 869 | 9 | data\raw_md\articles\ui-construction\view-items-and-property-editors\add-a-button-to-a-detail-view-using-custom-view-item.md |
| 113143 | How to: Enable Database Storage for User-Defined Criteria that Filter a List View | 178.496 | 1.767 | 765 | 11 | data\raw_md\articles\ui-construction\view-items-and-property-editors\property-editors\use-criteria-property-editors.md |
| 112818 | Determine Why an Action, Controller or Editor is Inactive | 174.657 | 2.008 | 869 | 12 | data\raw_md\articles\ui-construction\controllers-and-actions\determine-why-an-action-controller-or-editor-is-inactive.md |
| 118760 | How to: Create and Show a Detail View of the Selected Object in a Popup Window (ASP.NET Core Blazor) | 172.649 | 2.008 | 869 | 11 | data\raw_md\articles\ui-construction\views\ways-to-show-a-view\how-to-create-and-show-a-detail-view-of-the-selected-object-in-a-popup-window.md |
| 113471 | How to: Display a Non-Persistent Object's Detail View | 164.619 | 2.008 | 869 | 12 | data\raw_md\articles\business-model-design-orm\non-persistent-objects\how-to-display-a-non-persistent-objects-detail-view-from-the-navigation.md |
| 113103 | Define the Scope of Controllers and Actions | 160.604 | 2.008 | 869 | 10 | data\raw_md\articles\ui-construction\controllers-and-actions\define-the-scope-of-controllers-and-actions.md |
| 403452 | How To: Create a Custom Blazor Application Template | 152.574 | 2.008 | 869 | 11 | data\raw_md\articles\ui-construction\templates\in-blazor\custom-blazor-application-template.md |
| 113707 | Ways to Access an Object Space (the Database Context for CRUD Operations) | 151.987 | 1.767 | 765 | 16 | data\raw_md\articles\data-manipulation-and-business-logic\object-space.md |
| 113287 | How to: Customize the Export Action Behavior | 150.219 | 1.767 | 765 | 10 | data\raw_md\articles\shape-export-print-data\printing-exporting-in-list-view\how-to-customize-the-export-action-behavior.md |
| 112681 | How to: Implement Cascading Filtering for Lookup List Views | 148.558 | 2.008 | 869 | 9 | data\raw_md\articles\filtering\in-list-view\how-to-implement-cascading-filtering-for-lookup-list-views.md |
| 113452 | Implement a Custom Security System User Based on an Existing Business Class | 148.558 | 2.008 | 869 | 9 | data\raw_md\articles\data-security-and-safety\security-system\security-object-model\implement-custom-security-objects\implement-a-custom-security-system-user-based-on-an-existing-business-class.md |
| 402956 | Localize an XAF Application (.NET) | 146.685 | 1.767 | 765 | 13 | data\raw_md\articles\localization\localize-an-xaf-application.md |
| 404256 | Extend the Data Model | 138.521 | 2.008 | 869 | 9 | data\raw_md\articles\getting-started\in-depth-tutorial-blazor\define-data-model-and-set-initial-data\define-data-model-and-set-initial-data-with-ef-core\extend-the-data-model.md |
| 404559 | How to: Add a Grid Column with an Action (ASP.NET Core Blazor) | 138.521 | 2.008 | 869 | 9 | data\raw_md\articles\ui-construction\controllers-and-actions\actions\how-to-add-a-grid-column-with-an-action.md |
| 112805 | Dialog Controller | 138.521 | 2.008 | 869 | 9 | data\raw_md\articles\ui-construction\controllers-and-actions\dialog-controller.md |
| 404204 | Use the Security System | 136.513 | 2.008 | 869 | 8 | data\raw_md\articles\getting-started\in-depth-tutorial-blazor\enable-additional-modules\use-the-security-system.md |

## How To Refresh
1. `$env:PYTHONUTF8=1; & .venv\Scripts\python.exe tools/coverage_matrix_xaf.py`
2. `$env:PYTHONUTF8=1; & .venv\Scripts\python.exe query_graph.py --mode gaps | Out-File outputs/query_graph_gaps.txt -Encoding utf8`
3. `$env:PYTHONUTF8=1; & .venv\Scripts\python.exe tools/generate_documentation_gaps_backlog.py`
