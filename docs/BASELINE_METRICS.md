# Baseline Documentation Metrics
**Generated:** February 10, 2026  
**Purpose:** Pre-improvement baseline for comparison  
**Project:** XAF Documentation Analysis

---

## 📊 Overall Statistics

| Metric | Value |
|--------|-------|
| **Total Documents** | 8,555 |
| **Total Sections (Kept)** | 11,082 |
| **Semantic Pairs** | 93,905 |
| **Avg Connections/Section** | 8.5 |
| **Isolated Sections** | 603 (5.4%) |
| **Connected Sections** | 10,479 (94.6%) |

---

## 🔗 Connectivity by Type

| Relationship Type | Count | Percentage |
|-------------------|-------|------------|
| Conceptual → Conceptual | 55,390 | 59.0% |
| API → API | 19,902 | 21.2% |
| API → Conceptual | 10,395 | 11.1% |
| Conceptual → API | 8,218 | 8.7% |
| **Total Cross-Corpus (API ↔ Conceptual)** | **18,613** | **19.8%** |

---

## 📈 Similarity Scores

| Metric | Score |
|--------|-------|
| **Average** | 0.759 |
| **Median** | 0.738 |
| **Minimum** | 0.600 |
| **Maximum** | 1.000 |

---

## 🚪 Quality Gates Performance

| Gate | Pairs Passed | Coverage |
|------|-------------|----------|
| **concept_overlap** | 68,606 | 73.1% |
| **platform_overlap** | 30,937 | 33.0% |
| **namespace_overlap** | 30,206 | 32.2% |
| **api_overlap** | 4,451 | 4.7% |
| **high_similarity_fallback** | 1,965 | 2.1% |

---

## 🔴 Critical Issues - Cross-Corpus Gaps

### Concepts with ZERO Cross-Corpus Links (6 total)

| Concept | Total Sections | Conceptual | API | Gap Type |
|---------|---------------|------------|-----|----------|
| **Performance Optimization** | 21 | 10 | 11 | Semantic Gap |
| **Deployment** | 125 | 125 | 0 | Missing API Tags |
| **Logging** | 65 | 55 | 10 | Semantic Gap |
| **Legacy .NET Framework** | 226 | 215 | 11 | Semantic Gap |
| **Migration** | 66 | 62 | 4 | Semantic Gap |
| **Multi-Tenancy** | 24 | 24 | 0 | Missing API Tags |

**Total sections affected:** 527 sections with zero cross-corpus connectivity

---

## 🟡 Under-Connected Concepts (<6 links/section)

| Concept | Sections | Total Links | Links/Section | Gap from Avg (8.5) |
|---------|----------|-------------|---------------|-------------------|
| **Legacy .NET Framework** | 226 | 786 | 3.5 | -5.0 |
| **Template Kit** | 213 | 921 | 4.3 | -4.2 |
| **Application Model** | 1,494 | 7,150 | 4.8 | -3.7 |
| **Reference Property** | 213 | 1,058 | 5.0 | -3.5 |
| **Object Space** | 1,211 | 6,521 | 5.4 | -3.1 |
| **List Editors** | 434 | 2,350 | 5.4 | -3.1 |
| **XAF Application** | 396 | 2,187 | 5.5 | -3.0 |
| **Business Objects** | 1,150 | 6,372 | 5.5 | -3.0 |
| **XPO** | 989 | 5,600 | 5.7 | -2.8 |
| **Authorization** | 310 | 1,874 | 6.0 | -2.5 |

**Total sections in under-connected concepts:** 6,636 sections

---

## 🟢 Well-Connected Concepts (Reference Benchmarks)

| Concept | Sections | Total Links | Links/Section |
|---------|----------|-------------|---------------|
| **Audit Trail** | 252 | 3,562 | 14.1 ✨ |
| **Conditional Appearance** | 283 | 2,821 | 10.0 |
| **Blazor UI** | 2,098 | 20,341 | 9.7 |
| **Reports** | 379 | 3,595 | 9.5 |
| **Authentication** | 470 | 4,408 | 9.4 |
| **.NET Runtime** | 1,553 | 14,118 | 9.1 |
| **WinForms** | 1,840 | 15,780 | 8.6 |
| **Dashboards** | 359 | 2,887 | 8.0 |
| **Entity Framework Core** | 672 | 4,945 | 7.4 |
| **Modules** | 516 | 3,639 | 7.1 |

---

## 🎯 Improvement Targets

### Phase 1: Cross-Corpus Gaps (HIGH PRIORITY)

| Metric | Baseline | Target | Success Criteria |
|--------|----------|--------|------------------|
| Concepts with 0 cross-links | 6 | 0 | All concepts have ≥10 cross-links |
| Deployment cross-links | 0 | 50+ | API docs properly tagged |
| Multi-Tenancy cross-links | 0 | 10+ | API docs properly tagged |

### Phase 2: Isolated Sections

| Metric | Baseline | Target | Success Criteria |
|--------|----------|--------|------------------|
| Isolated sections | 603 (5.4%) | <332 (<3%) | Reduce by ~50% |
| Isolated rate | 5.4% | 3.0% | Better concept tagging |

### Phase 3: Under-Connected Concepts

| Metric | Baseline | Target | Success Criteria |
|--------|----------|--------|------------------|
| Concepts with <6 links/section | 10 | 5 | 50% reduction |
| Template Kit links/section | 4.3 | 7.0+ | +63% improvement |
| Application Model links/section | 4.8 | 7.0+ | +46% improvement |

### Phase 4: Overall Connectivity

| Metric | Baseline | Target | Success Criteria |
|--------|----------|--------|------------------|
| Avg connections/section | 8.5 | 9.0+ | +6% improvement |
| Cross-corpus percentage | 19.8% | 22.0%+ | +11% improvement |
| Concept overlap gate | 73.1% | 75.0%+ | Better tagging |

---

## 📋 Specific Findings

### Deployment Concept Analysis
- **263 API documents** found with deployment keywords (connectionstring, applicationbuilder, azure, etc.)
- **0 currently tagged** with Deployment concept
- **Quick win:** Tag these APIs and re-run extraction

### Multi-Tenancy Analysis
- **24 conceptual sections** exist
- **0 API sections** tagged
- Likely similar to Deployment - missing API tagging

### Isolated Sections - Examples
```
data/raw_md/apidoc/DevExpress.ExpressApp/CreateCustomCollectionSourceEventArgs/ListViewID
data/raw_md/apidoc/DevExpress.ExpressApp/View/ScrollPosition
data/raw_md/articles/dialogs-and-notifications/ways-to-show-a-confirmation-dialog
data/raw_md/apidoc/DevExpress.ExpressApp.Actions/ChoiceActionItem/BeginGroup
data/raw_md/apidoc/DevExpress.ExpressApp.Win.Editors/WinColumnsListEditor/ReadOnlyEditors
```

**Analysis needed:** Categorize by cause (stub pages, niche content, missing tags, etc.)

---

## 🔬 Methodology Notes

### Data Sources
- `outputs/semantic_pairs.parquet` - All semantic relationships
- `outputs/doc_concepts.parquet` - Section metadata and concept tags
- `outputs/topics_inventory.parquet` - Full document text
- `config/concepts.yml` - Concept definitions (40 concepts)

### Semantic Pairing Criteria
- Minimum similarity threshold: 0.60
- Quality gates: concept overlap, platform overlap, namespace overlap, API overlap
- Fallback: high similarity (even without gate pass)

### Measurement Commands
```bash
# Full statistics
python query_graph.py --mode stats

# Gap analysis
python query_graph.py --mode gaps

# Concept-specific query
python query_graph.py --mode query --concept "Deployment"
```

---

## 📅 Timeline for Re-Measurement

**Recommended check-in points:**

1. **After Phase 1 (Quick Wins)** - Expected: +2 weeks
   - Deployment concept fixed
   - Multi-Tenancy concept fixed
   - Re-measure cross-corpus gaps

2. **After Phase 2 (Semantic Gaps)** - Expected: +4 weeks
   - Performance Optimization bridged
   - Logging bridged
   - Re-measure cross-corpus and isolated sections

3. **After Phase 3 (Under-Connected)** - Expected: +6 weeks
   - Template Kit connectivity improved
   - Application Model connectivity improved
   - Re-measure overall connectivity

4. **Final Review** - Expected: +8 weeks
   - All phases complete
   - Full comparison against baseline
   - Document lessons learned

---

## 🎓 Success Factors from Well-Connected Concepts

**Audit Trail (14.1 links/section) characteristics:**
- Strong concept co-occurrence patterns
- Well-balanced cc/aa/ca/ac link distribution
- High concept overlap gate pass rate
- Clear API ↔ Tutorial bridges

**Study these patterns and apply to under-connected concepts.**

---

## 📊 Baseline Snapshot Saved

This document serves as the official baseline. All future measurements should reference these values to demonstrate improvement.

**Next Steps:**
1. ✅ Baseline captured
2. ⏳ Implement Phase 1 fixes
3. ⏳ Re-measure and compare
4. ⏳ Document improvements
5. ⏳ Repeat for remaining phases

**Comparison Script:**
```bash
# After improvements, generate new metrics and compare
python query_graph.py --mode stats > outputs/metrics_after_phase1.txt
python query_graph.py --mode gaps > outputs/gaps_after_phase1.txt
diff BASELINE_METRICS.md outputs/metrics_after_phase1.txt
```

---

*Baseline established: February 10, 2026*  
*Ready for improvement tracking! 🚀*
