# Documentation Metrics Snapshot
**Generated:** April 23, 2026
**Purpose:** Current-state snapshot for progress tracking against Feb 10, 2026 baseline
**Project:** XAF Documentation Analysis
**Data sources:** `outputs/semantic_pairs.parquet`, `outputs/doc_concepts.parquet`, `outputs/topics_inventory.parquet` (all last updated April 20, 2026)

---

## 📊 Overall Statistics

| Metric | Baseline (Feb 10) | This Snapshot (Apr 23) | Delta |
|--------|-------------------|------------------------|-------|
| **Total Documents** | 8,555 | 7,566 | -989 (.NET Framework docs removed) |
| **Total Sections (Kept)** | 11,082 | 11,584 | +502 |
| **Semantic Pairs** | 93,905 | 75,193 | -18,712 |
| **Avg Connections/Section** | 8.5 | 6.5 | -2.0 |
| **Isolated Sections** | 603 (5.4%) | 1,201 (10.4%) | **+598 ⚠️** |
| **Connected Sections** | 10,479 (94.6%) | 10,383 (89.6%) | -96 |

> **Note on document count drop:** The corpus shrank from 8,555 → 7,566 documents (-989) because all .NET Framework documentation was intentionally removed. XAF dropped .NET Framework support, and the corresponding docs were deleted from the corpus as part of the normal documentation lifecycle. This is the root cause of most connectivity regressions in this snapshot — the removed docs were well-connected and their removal reduced total pairs and average connectivity.

---

## 🔗 Connectivity by Type

| Relationship Type | Baseline (Feb 10) | Current (Apr 23) | Delta |
|-------------------|-------------------|------------------|-------|
| Conceptual → Conceptual (CC) | 55,390 (59.0%) | 29,984 (39.9%) | -25,406 |
| API → API (AA) | 19,902 (21.2%) | 21,039 (28.0%) | +1,137 |
| Concept → API (CA) | 8,218 (8.7%) | 15,312 (20.4%) | **+7,094 ✅** |
| API → Conceptual (AC) | 10,395 (11.1%) | 8,858 (11.8%) | -1,537 |
| **Total Cross-Corpus (CA + AC)** | **18,613 (19.8%)** | **24,170 (32.1%)** | **+5,557 ✅** |

> **Positive signal:** Cross-corpus pairs increased by 30% (+5,557), and concept→API links more than doubled (+7,094). The cross-corpus percentage rose from 19.8% to 32.1%, exceeding the original 22% target. This reflects improved API tagging and concept mapping in the pipeline.

---

## 📈 Similarity Scores

| Metric | Baseline (Feb 10) | Current (Apr 23) | Delta |
|--------|-------------------|------------------|-------|
| **Average** | 0.759 | 0.762 | +0.003 |
| **Median** | 0.738 | 0.765 | **+0.027** |
| **Minimum** | 0.600 | 0.600 | 0 |
| **Maximum** | 1.000 | 1.000 | 0 |

---

## 🚪 Quality Gates Performance

| Gate | Baseline (Feb 10) | Current (Apr 23) | Delta |
|------|-------------------|------------------|-------|
| **concept_overlap** | 68,606 (73.1%) | 73,870 (98.2%) | +5,264 ✅ |
| **platform_overlap** | 30,937 (33.0%) | 30,937 (41.1%) | 0 |
| **namespace_overlap** | 30,206 (32.2%) | 30,206 (40.2%) | 0 |
| **api_overlap** | 4,451 (4.7%) | 4,451 (5.9%) | 0 |
| **high_similarity_fallback** | 1,965 (2.1%) | 1,256 (1.7%) | -709 |

---

## 🔴 Critical Issues — Concepts with Zero Cross-Corpus Links

### Baseline (Feb 10): 4 concepts

| Concept | Status in Apr 23 snapshot |
|---------|--------------------------|
| Performance Optimization | ✅ Fixed — now has cross-corpus links |
| Deployment | ⚠️ Still zero |
| Logging | ⚠️ Still zero |
| Migration | ⚠️ Still zero |

### New in Apr 23 snapshot: 15 additional concepts with zero cross-corpus links

These are **newly added taxonomy concepts** not yet reflected in the corpus tagging. They represent taxonomy expansion debt, not regressions in existing coverage.

| Concept |
|---------|
| Accordion Control |
| Assembly References |
| Async Operations |
| Auto-Increment Fields |
| Custom User Management |
| Demo Applications |
| Diagnostic Tools |
| Memory Management |
| Multiple Databases |
| Package Management |
| Programmatic Localization |
| Project Wizards |
| Recurring Events |
| Scaling Architecture |
| Theming |

**Total with zero cross-corpus links: 18** (vs. 4 at baseline)

---

## 🟡 Under-Connected Concepts (<6 links/section)

**Baseline:** 33 concepts under-connected  
**Current:** 57 concepts under-connected (+24)

Concepts fixed since baseline: none  
Newly under-connected (includes new taxonomy concepts): 24 additional concepts, including Context Menus, Custom Validation Rules, Database Update, Domain Components, Error Styling, Inline Editing, Report Parameters, SVG Graphics, Spreadsheet Control, Tabbed MDI Interface, Threading Issues, and others added to the taxonomy since Feb 10.

---

## 📋 What Changed Since Feb 10 Baseline

### Pipeline changes (from WHATSNEW.md, April 20)
- **Phase 5 xref gate added** — direct xref pairs now get a dedicated pass; this changes pair counts and composition
- **Phase 10 taxonomy-only tags** — sections tagged with taxonomy-only concepts no longer propagate non-taxonomy tags; this affects concept overlap gate counts

### Corpus changes
- **-989 documents** removed intentionally — all .NET Framework documentation was deleted from the corpus following the end of .NET Framework support in XAF. This is expected and permanent.
- **+502 sections** — new sections added or previously filtered sections now kept (net corpus growth on the remaining content)

### Taxonomy changes
- **15+ new concepts** added to the taxonomy since Feb 10 — these appear as zero-link gaps because the corpus has not yet been re-tagged to cover them

---

## 🎯 Revised Improvement Targets

| Metric | Feb 10 Baseline | Apr 23 Snapshot | Original Target | Status |
|--------|-----------------|-----------------|-----------------|--------|
| Isolated sections | 603 (5.4%) | 1,201 (10.4%) | <332 (<3%) | ⚠️ Regressed |
| Avg connections/section | 8.5 | 6.5 | 9.0+ | ⚠️ Regressed |
| Cross-corpus % | 19.8% | 32.1% | 22.0%+ | ✅ Exceeded |
| Concepts with 0 cross-links | 4 | 18 | 0 | ⚠️ Increased (taxonomy expansion) |
| Concept overlap gate % | 73.1% | 98.2% | 75.0%+ | ✅ Exceeded |

---

## 🔬 Methodology Notes

### Data Sources
- `outputs/semantic_pairs.parquet` — All semantic relationships (last updated April 20, 2026)
- `outputs/doc_concepts.parquet` — Section metadata and concept tags (last updated April 20, 2026)
- `outputs/topics_inventory.parquet` — Full document inventory (last updated April 20, 2026)

### Semantic Pairing Criteria (unchanged)
- Minimum similarity threshold: 0.60
- Quality gates: concept overlap, platform overlap, namespace overlap, API overlap
- Fallback: high similarity (even without gate pass)
- **New in Phase 5 (April 20):** xref direct-pairs pass added

### Priority Investigation Items
1. **Isolated sections doubled** — determine how many are caused by .NET Framework doc removal vs. Phase 5 xref gate change. Some formerly-connected sections may have lost their partners when the .NET Framework docs were removed.
2. **Legacy .NET Framework concept** \u2014 keep in taxonomy; migration guides explaining how to move from .NET Framework to .NET still exist in the corpus and depend on this concept for tagging and cross-linking.
3. **15 new taxonomy concepts** need corpus re-tagging (Phase 3 re-run after taxonomy update).
