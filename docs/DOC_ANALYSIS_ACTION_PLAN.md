# Documentation Analysis Results & Action Plan
**Generated:** February 10, 2026  
**Project:** XAF Documentation Analysis  
**Based on:** config/prompts/ai_action_prompts.md

---

## 📊 Executive Summary

Your documentation corpus has **11,082 sections** with **93,905 semantic connections**.

### Critical Issues Identified:
1. ✅ **6 concepts** have ZERO cross-corpus links (conceptual ↔ API)
2. ✅ **603 isolated sections** (5.4%) with no semantic connections
3. ✅ **10 under-connected concepts** with <6 links per section (avg: 8.5)

---

## 🔴 Priority 1: Fix Cross-Corpus Gaps

### Gap Type Breakdown:

| Concept | Conceptual | API | Gap Type | Priority | Effort |
|---------|-----------|-----|----------|----------|--------|
| **Deployment** | 125 | 0 | Missing API tags | HIGH | 2-3h |
| **Multi-Tenancy** | 24 | 0 | Missing API tags | HIGH | 2-3h |
| **Performance Optimization** | 10 | 11 | Semantic gap | MEDIUM | 4-6h |
| **Logging** | 55 | 10 | Semantic gap | MEDIUM | 4-6h |
| **Legacy .NET Framework** | 215 | 11 | Semantic gap | MEDIUM | 4-6h |
| **Migration** | 62 | 4 | Semantic gap | MEDIUM | 4-6h |

### 🎯 Quick Wins (Missing API Tags):

**Deployment** - Found 263 API docs that should be tagged:
- ApplicationBuilder classes
- ConnectionString properties
- Azure authentication setup
- Hosting/configuration APIs

**Multi-Tenancy** - Likely similar pattern:
- Tenant-related APIs not tagged
- Multi-database configuration classes

**Action:**
```bash
# 1. Review and update concept definitions
code config/concepts.yml

# 2. Update extraction prompts if needed
code config/prompts/

# 3. Re-run concept extraction
python scripts/03_extract_concepts.py

# 4. Rebuild semantic pairs
python scripts/04_make_sections_embeddings.py --batch-size 32 --max-chars 4000
python scripts/05_find_semantic_pairs.py

# 5. Verify improvements
python query_graph.py --mode gaps
```

---

## 🟡 Priority 2: Fix Under-Connected Concepts

### Top 4 Under-Connected Concepts:

| Concept | Sections | Links | Per Section | Target | Gap |
|---------|----------|-------|-------------|--------|-----|
| **Legacy .NET Framework** | 226 | 786 | 3.5 | 8.5 | -5.0 |
| **Template Kit** | 213 | 921 | 4.3 | 8.5 | -4.2 |
| **Application Model** | 1494 | 7150 | 4.8 | 8.5 | -3.7 |
| **Reference Property** | 213 | 1058 | 5.0 | 8.5 | -3.5 |

**Action:**
```bash
# Analyze isolated sections for a specific concept
python -c "
import pandas as pd
from collections import Counter

pairs = pd.read_parquet('outputs/semantic_pairs.parquet')
concepts = pd.read_parquet('outputs/doc_concepts.parquet')
kept = concepts[concepts['kept'] == True]

target_concept = 'Template Kit'

# Get sections with concept
def has_concept(cs, target):
    if cs is None or (isinstance(cs, float) and pd.isna(cs)): return False
    return target in (list(cs) if hasattr(cs, '__iter__') else [])

concept_sections = kept[kept['concepts'].apply(lambda cs: has_concept(cs, target_concept))].copy()

# Count connections
section_connections = Counter()
for row in pairs.itertuples():
    section_connections[(row.source_doc, row.source_section)] += 1
    section_connections[(row.target_doc, row.target_section)] += 1

# Find isolated
concept_sections['num_connections'] = concept_sections.apply(
    lambda r: section_connections.get((r['doc_id'], r['section_id']), 0), axis=1
)

isolated = concept_sections[concept_sections['num_connections'] <= 2]
print(f'Isolated {target_concept} sections: {len(isolated)}/{len(concept_sections)}')
print('\\nTop 10 most isolated:')
for _, row in isolated.head(10).iterrows():
    print(f'  {row[\"doc_id\"]} - {row[\"num_connections\"]} connections')
"
```

---

## 🔵 Priority 3: Connect Isolated Sections

**603 sections (5.4%)** have no semantic connections.

### Sample Isolated Sections:
- `DevExpress.ExpressApp/CreateCustomCollectionSourceEventArgs/ListViewID`
- `DevExpress.ExpressApp/View/ScrollPosition`
- `articles/dialogs-and-notifications/ways-to-show-a-confirmation-dialog`

**Possible Causes:**
1. Stub pages with minimal content
2. Very niche/specific functionality
3. Missing concept tags
4. Content below similarity threshold

**Action:**
```bash
# Analyze isolated sections
python -c "
import pandas as pd
import random

pairs = pd.read_parquet('outputs/semantic_pairs.parquet')
concepts = pd.read_parquet('outputs/doc_concepts.parquet')
kept = concepts[concepts['kept'] == True]

# Find isolated
connected = set()
for row in pairs.itertuples():
    connected.add((row.source_doc, row.source_section))
    connected.add((row.target_doc, row.target_section))

all_sections = set(zip(kept['doc_id'], kept['section_id']))
isolated = list(all_sections - connected)

print(f'Total isolated: {len(isolated)}')

# Sample 20 for review
sample = random.sample(isolated, min(20, len(isolated)))
for doc_id, section_id in sample:
    row = kept[(kept['doc_id'] == doc_id) & (kept['section_id'] == section_id)]
    if not row.empty:
        concepts_list = list(row.iloc[0]['concepts']) if hasattr(row.iloc[0]['concepts'], '__iter__') else []
        print(f'{doc_id}')
        print(f'  Concepts: {concepts_list}')
        print()
"
```

---

## 📈 Success Metrics

After implementing fixes, run:
```bash
python query_graph.py --mode gaps
python query_graph.py --mode stats
```

**Target Goals:**
- [ ] All concepts have ≥10 cross-corpus links
- [ ] Isolated sections <3% (currently 5.4%)
- [ ] Under-connected concepts >7 links/section
- [ ] Deployment concept: ≥50 cross-links
- [ ] Multi-Tenancy concept: ≥10 cross-links

---

## 🚀 Recommended Execution Order

### Week 1: Quick Wins (High ROI)
1. **Day 1-2:** Fix Deployment API tagging (263 docs)
2. **Day 3:** Fix Multi-Tenancy API tagging
3. **Day 4:** Validate and measure improvements
4. **Day 5:** Document changes and review

### Week 2: Semantic Gaps
5. **Day 1-2:** Analyze Performance Optimization semantic gap
6. **Day 3-4:** Analyze Logging semantic gap
7. **Day 5:** Add cross-references and examples

### Week 3: Under-Connected Concepts
8. **Day 1-2:** Fix Template Kit connectivity
9. **Day 3-4:** Fix Legacy .NET Framework connectivity
10. **Day 5:** Review and validate

### Week 4: Isolated Sections
11. **Day 1-3:** Categorize 603 isolated sections
12. **Day 4-5:** Fix/tag/accept as appropriate

---

## 📁 Analysis Scripts Created

I've created these helper scripts for you:

1. **`analyze_deployment_gap.py`** - Deep dive into Deployment gap
2. **`find_missing_deployment_apis.py`** - Find 263 API docs to tag
3. **`analyze_all_gaps.py`** - Categorize all 6 gap types

These follow the patterns from `ai_action_prompts.md` and are ready to run!

---

## 🎓 Learning from Well-Connected Concepts

Reference these as models:
- **Audit Trail:** 14.1 links/section
- **Conditional Appearance:** 10.0 links/section  
- **Blazor UI:** 9.7 links/section
- **Reports:** 9.5 links/section

Study their patterns:
```bash
python query_graph.py --mode query --concept "Audit Trail"
```

---

## 📞 Next Steps

**Choose your starting point:**

**Option A - Quick Win (Recommended):**
```bash
# Fix Deployment tagging first (2-3 hours)
python find_missing_deployment_apis.py  # Review the 263 API docs
# Then update concepts.yml and re-run extraction
```

**Option B - Deep Analysis:**
```bash
# Analyze all gaps in detail
python analyze_all_gaps.py
python analyze_deployment_gap.py
# Then create a comprehensive fix plan
```

**Option C - Measure First:**
```bash
# Get detailed statistics
python query_graph.py --mode stats
python query_graph.py --mode query --concept "Template Kit"
```

Ready to start? Let me know which option you'd like to pursue! 🚀
