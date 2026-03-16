# Ticket-to-Documentation Discoverability Tools

This folder contains tools for analyzing the language gap between support ticket terminology and documentation concepts.

## Overview

Support tickets use problem-based, feature-oriented language while documentation is organized around architectural concepts and API entities. These tools help bridge that discoverability gap.

## Tools

### `analyze_real_tickets.py`

Analyzes support tickets to prioritize documentation improvements and ontology implementation.

**Purpose:**
1. Maps ticket feature categories to concepts.yml concepts
2. Identifies high-volume areas needing improved documentation/discoverability
3. Prioritizes which ontology features to implement first
4. Generates actionable recommendations for implementation phases

**Usage:**
```bash
python tools/ticket_discoverability/analyze_real_tickets.py
```

**Requirements:**
- `xaf_support_tickets_by_feature.json` in project root
- `config/concepts.yml` with concept definitions
- Python packages: polars, pyyaml

**Outputs:**
All outputs are saved to `outputs/ticket_discoverability/`:
- `ticket_volumes_by_concept.csv` - Ticket counts rolled up by concept
- `ticket_feature_to_concept_mapping.csv` - Individual category-to-concept mappings with confidence scores
- `ontology_implementation_priorities.json` - Implementation phases with ROI data
- `ticket_analysis_actions.csv` - Top 20 concepts ranked by ticket volume

## Outputs

See `outputs/ticket_discoverability/` folder for generated analysis files.

### Key Metrics

**Current Baseline (as of Feb 13, 2026):**
- Total tickets analyzed: 14,860
- Feature categories: 159
- Mapped concepts: 74
- Unmapped categories: 4 (447 tickets)
- API search tickets: 7,975 (53.7%) - biggest opportunity
- Top concept: View Items (1,634 tickets, 11.0%)

### Priority Areas

1. **Phase 1: Metadata Tagging** - 8,129 tickets impact (54.7%)
2. **Phase 2: API Entities** - 7,975 tickets impact (53.7%)

## Related Documentation

- `PlanTicketToDocumentationDiscoverabilityBridge.md` - Full implementation roadmap
- `config/concepts.yml` - Concept taxonomy with synonyms
- `xaf_ontology_schema.yml` - Ontology structure

## Future Tools (Planned)

As outlined in the roadmap:
- `validate_ticket_mapping.py` - Compare baseline vs current mapping scores
- `extract_ticket_phrases.py` - Process full ticket text when available
- `generate_synonym_suggestions.py` - LLM-powered synonym discovery
