# MVP Deliverables

**Generated:** 2026-02-14 20:58:31

This directory contains curated outputs from the XAF Documentation Analysis project,
packaged for tech writers and stakeholders.

## Files

### 1. gap_analysis_summary.json
**Purpose:** Identifies 6 XAF concepts with documentation gaps  
**Audience:** Tech writers, documentation leads  
**Action:** Review gap types and choose fix strategies

**Key Metrics:**
- Total sections analyzed: 10,994
- Gaps found: 6
- Isolated sections: 539 (4.9%)

**Gap Types:**
- `missing_api_tagging` - Update concept extraction (2-3 hours)
- `missing_conceptual_docs` - Write new tutorials (8-16 hours)
- `semantic_gap` - Improve connections (4-6 hours)

### 2. top_50_priorities.csv
**Purpose:** Top 50 API cross-linking recommendations, weighted by customer support tickets  
**Audience:** Tech writers  
**Action:** Add API links to high-priority articles

**Columns:**
- `Article` - Document path
- `API` - API class/member to link
- `Priority` - HIGH/MEDIUM/LOW based on code usage
- `Customer Pain` - Ticket weight (>2.0 = critical pain point)
- `Used in Code` - TRUE if API appears in code blocks (highest value)

**How to Use:**
1. Sort by "Customer Pain" descending
2. Focus on Priority = HIGH first
3. Add cross-references to API documentation
4. Track progress (aim for 20+ links/week)

### 3. metadata_samples.yml
**Purpose:** Sample YAML frontmatter for AI agent optimization  
**Audience:** Tech writers, documentation engineers  
**Action:** Use as templates when adding YAML headers

**Fields:**
- `description` - One sentence summary (for search results)
- `tags` - Normalized tags (concepts, platforms, content types)
- `proficiencyLevel` - Beginner/Intermediate/Advanced/Expert

**Guidelines:**
- Keep descriptions under 160 characters
- Use 3-8 tags per document
- Tags must be lowercase with hyphens (no spaces or dots)

### 4. baseline_snapshot.json
**Purpose:** Current state metrics for tracking improvements  
**Audience:** Project managers, documentation leads  
**Action:** Re-run analysis after fixes to measure progress

**Current State:**
- Isolated sections: 539 (4.9%)
- Cross-corpus links: 19,911 (20.4%)
- Concepts with gaps: 6

**Targets:**
- Isolated sections: < 550 (< 5%)
- Cross-corpus links: 20,000+ (21%+)
- Concepts with gaps: ≤ 4

## Next Steps

1. **Quick Wins (This Week)**
   - Review `top_50_priorities.csv`
   - Add 10-20 high-priority API links
   - Test metadata samples on 5-10 documents

2. **Gap Fixes (This Month)**
   - Review `gap_analysis_summary.json`
   - Fix "missing_api_tagging" gaps (2-3 hours each)
   - Start work on 1-2 "semantic_gap" concepts (4-6 hours each)

3. **Bulk Metadata Updates (This Quarter)**
   - Use `metadata_samples.yml` as templates
   - Add YAML frontmatter to top 100 most-viewed docs
   - Integrate with MCP server for AI agent queries

4. **Measure Progress**
   - Re-run full pipeline after fixes: `python scripts/run_mvp_pipeline.sh`
   - Compare new metrics to `baseline_snapshot.json`
   - Use `tools/compare_to_baseline.py` for detailed comparison

## Questions?

- **Technical:** See [MCP_INTEGRATION_GUIDE.md](../../docs/MCP_INTEGRATION_GUIDE.md)
- **Conceptual:** See [project-overview.md](../../docs/project-overview.md)
- **Queries:** Use [query_graph.py](../../query_graph.py) for interactive exploration

---

For more details on how this data was generated, see the main [README.md](../../README.md).
