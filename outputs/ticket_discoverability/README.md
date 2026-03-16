# Ticket Discoverability Analysis Outputs

This folder contains outputs from ticket-to-documentation discoverability gap analysis.

## Files

### `ticket_volumes_by_concept.csv`

Ticket counts aggregated by concept, sorted by volume.

**Columns:**
- `primary_concept` - Concept name from concepts.yml
- `total_tickets` - Sum of tickets mapped to this concept
- `feature_count` - Number of ticket feature categories mapping to this concept

**Use Case:** Identify which concepts have highest support ticket volume and should be prioritized for synonym expansion and discoverability improvements.

### `ticket_feature_to_concept_mapping.csv`

Individual ticket feature category to concept mappings with confidence scores.

**Columns:**
- `feature_category` - Original ticket feature category name (user language)
- `ticket_count` - Number of tickets in this category
- `primary_concept` - Best matching concept from concepts.yml
- `confidence` - Mapping confidence score (0-10)
  - 10: Exact match
  - 7: Synonym match
  - 5: Partial word overlap
  - 0: UNMAPPED

**Use Case:** 
- Find low-confidence mappings (<7) that need synonym additions
- Identify UNMAPPED categories that need new concepts
- Understand how user language differs from documentation terminology

### `ontology_implementation_priorities.json`

Implementation roadmap phases with ticket impact analysis.

**Structure:**
```json
{
  "priorities": [
    {
      "phase": "Phase 1: Metadata Tagging",
      "time_estimate": "2-4 hours",
      "impact_tickets": 8129,
      "impact_pct": "54.7%",
      "recommendation": "...",
      "priority": "CRITICAL"
    }
  ],
  "total_tickets": 14860,
  "ticket_categories": {...},
  "top_10_concepts": [...]
}
```

**Use Case:** ROI analysis and phase prioritization for roadmap implementation.

### `ticket_analysis_actions.csv`

Top 20 concepts ranked by ticket volume - actionable summary.

**Columns:**
- `rank` - Priority ranking (1-20)
- `concept` - Concept name
- `tickets` - Total tickets
- `pct_of_total` - Percentage of all tickets
- `feature_categories` - Number of ticket categories mapping to this concept

**Use Case:** Quick reference for prioritizing which concepts to focus on first for synonym expansion and content improvements.

## Baseline Metrics (Feb 13, 2026)

- **Total Tickets:** 14,860
- **Mapped Concepts:** 74
- **Unmapped Categories:** 4 (447 tickets)
- **Average Confidence:** ~40% of categories have >7/10 confidence
- **Top Opportunity:** API search tickets (7,975 tickets, 53.7%)

## Analysis Insights

### High-Volume Concepts (Top 5)
1. View Items - 1,634 tickets (11.0%)
2. Views - 1,138 tickets (7.7%)
3. Object Space - 783 tickets (5.3%)
4. XAF Application - 651 tickets (4.4%)
5. List Editors - 554 tickets (3.7%)

### Ticket Type Distribution
- **API Search:** 53.7% - Users looking for specific APIs
- **Concepts:** 38.9% - Understanding core concepts
- **Performance:** 2.7%
- **Integration:** 1.9%
- **Setup:** 1.8%
- **Platform-specific:** 1.0%

### Unmapped Categories (Need Manual Review)
- Form Templates (207 tickets)
- Popups (144 tickets)
- Callbacks (66 tickets)
- TIME: 1-2h (30 tickets)

## Usage

These outputs serve as the baseline for measuring discoverability improvements. After implementing synonym expansions or concept refinements, re-run the analysis to compare:

```bash
python tools/ticket_discoverability/analyze_real_tickets.py
```

Then compare the new outputs against this baseline to track:
- Increase in mapping confidence scores
- Reduction in UNMAPPED categories
- Better distribution of tickets across specific (vs generic) concepts
