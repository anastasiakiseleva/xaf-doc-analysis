# Reporting Concepts — Full Analysis Summary
**Date:** 2026-04-23  
**Concepts analyzed:** `xaf.ui.views.report-parameters`, `xaf.ui.views.reports`, `xaf.ui.views.reports-v2`

---

## 1. Concept Overview

| Attribute | Report Parameters | Reports | Reports V2 |
|---|---|---|---|
| `artifact_kind` | module | module | module |
| `stability` | stable | **deprecated** | evolving |
| `platforms` | winforms, blazor | winforms, blazor | winforms, blazor |
| `audiences` | intermediate | intermediate | intermediate |
| `doc_intents` | concept, how_to | concept, how_to, configuration | concept, how_to, configuration |
| `tags` | reporting, parameters | reporting | reporting |
| `ownership.module` | reports | reports | reports |
| Key relation | `part_of: reports` | `related_to: views` | `replaces: reports` |

### Taxonomy gaps identified

- **Reports V2 synonyms are thin** — only 2 synonyms (`"Reports V2 Module"`, `"Modern Reports"`) vs 10 for Reports. Likely misses real doc terms like `"ReportsV2"`, `"XafReportDataV2"`, `"IReportDataSourceHelper"`, `"SetupBeforePrint"`, `"ReportDataSourceHelper"`.
- **report-parameters has no `related_to` Reports V2** — it is `part_of` the deprecated `reports` concept only. Given that `ReportParametersObjectBase` and `IReportDataV2.ParametersObjectType` are V2 APIs, this relation should also point to `reports-v2`.
- **`xaf.ui.views.views` still references the deprecated `reports`** in its `related_to` — should be updated to `reports-v2` or both.
- **No `keywords` on any of the 3 concepts** — could improve tagging recall.

---

## 2. Section & Connectivity Analysis

| Metric | Report Parameters | Reports | Reports V2 |
|---|---|---|---|
| Tagged sections (kept) | 36 | 141 | 21 |
| API sections | 18 | 78 | 11 |
| Conceptual sections | 18 | 63 | 10 |
| Avg connections/section | 21.83 | 21.99 | 27.24 |
| Median connections | 18.5 | 21.0 | 24.0 |
| Isolated sections (0 connections) | **0** | **0** | **0** |
| Cross-corpus pairs (ca/ac) | 101 | 528 | 45 |
| Unique APIs mapped | 7 | 108 | 7 |

### Key observations

- **All three concepts have zero isolated sections** — strong connectivity across the board.
- **Reports V2 has the highest avg connectivity (27.24)** despite having the fewest sections (21). This suggests high conceptual density, not sparse coverage.
- **Reports has the widest cross-corpus reach (528 pairs)** — expected for a large, well-established module with broad API surface.
- **Reports V2 cross-corpus pairs (45) are low relative to its size** — the smaller section count limits pair opportunities. Not a coverage gap, but confirms the concept is focused rather than sprawling.
- **API mapping parity**: Reports V2 maps only 7 APIs vs Reports' 108. This is a significant disparity. Many APIs in `reports-v2.api_surface.related_types` (e.g., `ReportsModuleV2`, `IReportDataV2`, `ReportDataV2`) overlap with the deprecated `reports` concept — possible tagging leakage.

---

## 3. Most / Least Connected Sections

### Report Parameters — top hits
- `articles/filtering/in-reports/data-filtering-in-reports` (57, 49 connections in multiple sections)
- `articles/shape-export-print-data/reports/task-based-help/how-to-access-the-report-parameters-object-in-report-scripts` (40, 34, 26, 22)
- `apidoc/DevExpress.ExpressApp.ReportsV2/ReportParametersObjectBase/ReportParametersObjectBase` (36, 25)

### Report Parameters — weakest links
- `apidoc/DataSourceBase/UpdateCriteriaWithReportParameters` (1 connection) — likely orphaned API doc
- `apidoc/PreviewReportDialogController` (7 connections) — underlinked controller page
- `articles/validation/validate-report-parameters` (9, 15 connections) — validation article underconnected

### Reports — notable weakest links
- `apidoc/DataSourceBase/UpdateCriteriaWithReportParameters` (1) — same orphan as above
- `apidoc/PredefinedReportsUpdater/#ctor` (2) — constructor doc orphan
- `apidoc/ReportsModuleV2/AddGeneratorUpdaters` (3)

### Reports V2 — notable weakest links
- `apidoc/ReportsModuleV2/AddGeneratorUpdaters` (3) — same orphan
- `apidoc/IModelNavigationItemsForReports` (4)
- `apidoc/ReportsBlazorModuleV2` (9) — Blazor module constructor underlinked

---

## 4. Graph Relationships (query_graph)

### Report Parameters — top classified relationships
- Primary pattern: **uses** (other sections call/use report parameter APIs)
- Secondary: **extends** (sections that extend `ReportParametersObjectBase`)
- 1 bidirectional **related_to**: `ReportServiceController/SetupBeforePrint`

### Reports — top classified relationships
- Primary pattern: **uses** and **extends** at 0.95 confidence
- 3 bidirectional **related_to** edges (`DataTypeName`, `IsPredefined`, `SetupBeforePrint`)
- WinReportServiceController docs strongly `uses`-linked

### Reports V2 — top classified relationships
- Pattern mix: **extends** (customization docs), **uses** (API callers), **explains** (overview articles), **requires** (setup guides), **contrasts_with** (migration content)
- `contrasts_with` edge on `add-reports-module-to-an-existing-xaf-application` — signals migration/deprecation comparison content

---

## 5. Prerequisites (Learning Paths)

| Concept | Prerequisites |
|---|---|
| Report Parameters | **Reports V2 Module overview** (1 prereq, confidence 0.85) |
| Reports | None |
| Reports V2 | None |

**Insight:** Report Parameters requires understanding Reports V2 first, but its taxonomy relation only points to the deprecated `reports`, not `reports-v2`. This is a taxonomy inconsistency.

---

## 6. Coverage Matrix Results

| Concept | Ticket Count | Doc Depth Score | Unique APIs in Coverage | Status |
|---|---|---|---|---|
| Reports | 388 | 55.8 | 74 | `well_covered` |
| Report Parameters | 98 | 32.5 | 13 | `well_covered` |
| Reports V2 | 52 | 24.5 | 14 | `well_covered` |

All three report as `well_covered` by support ticket mapping. Reports has the highest ticket volume (388) by a wide margin, consistent with its status as the major reporting feature.

---

## 7. Keyword Search — Untagged Reporting Content

**135 hits** across 200-section cap for keywords:  
`XtraReport, ReportDesigner, CollectionDataSource, ViewDataSource, IInplaceReport, PredefinedReportsUpdater, ReportPrintTool, ReportStorageBase, ReportsStorage, IReportDataV2`

Documents with 3+ hits not already in reporting concepts:
- `articles/filtering/in-reports/data-filtering-in-reports` — 3 hits (already tagged but confirms high relevance)
- `articles/debugging-testing-and-error-handling/performance/orm-performance` — 2 hits (performance article mentions `CollectionDataSource`/`ViewDataSource`) — **potential cross-tagging candidate**
- `articles/security-considerations/general-security-considerations` — 1 hit (mentions reporting in security context)

Full results in `keyword_hits_reporting.csv`.

---

## 8. Issues & Recommendations

### Critical
1. **`report-parameters` taxonomy relation gap**: Add `related_to: [xaf.ui.views.reports-v2]` — the learning path analysis confirms Reports V2 is a prerequisite, but the taxonomy only links to the deprecated parent.
2. **`xaf.ui.views.views` references deprecated `reports`**: Update `related_to` to include `reports-v2` or swap the deprecated reference.

### Important
3. **Reports V2 synonym enrichment**: Add synonyms based on actual doc terminology — `"ReportsV2"`, `"IReportDataSourceHelper"`, `"XafReportDataV2"`, `"SetupBeforePrint"`, `"Report Data Source Helper"`.
4. **API mapping leakage**: `ReportsModuleV2`, `IReportDataV2`, `ReportDataV2` appear in both `reports` and `reports-v2` API surfaces. Clarify ownership — these are V2 APIs and should primarily map to `reports-v2`.
5. **Underlinked API docs**:
   - `apidoc/DataSourceBase/UpdateCriteriaWithReportParameters` (1 connection) — needs crosslinks
   - `apidoc/PreviewReportDialogController` (7 connections) — needs crosslinks
   - `apidoc/ReportsModuleV2/AddGeneratorUpdaters` (3 connections) — needs crosslinks

### Nice to Have
6. **Add `keywords` to all 3 concepts** to improve tagging recall (currently empty).
7. **Report Parameters `doc_intents` missing `configuration`** — the concept covers how to configure report parameters (object type, custom editors), which warrants adding it.
8. **`orm-performance` article** mentions `CollectionDataSource`/`ViewDataSource` — consider adding `xaf.ui.views.reports` or `xaf.ui.views.reports-v2` as supplemental tags.
