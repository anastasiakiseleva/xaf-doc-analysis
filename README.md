# XAF Documentation Analysis

A Python-based tool for analyzing XAF (eXpressApp Framework) documentation through semantic relationships and knowledge graph construction.

## Overview

This project builds a knowledge graph from XAF documentation to identify relationships between documentation sections, analyze documentation gaps, and provide insights into support ticket patterns by feature.

## Key Features

- **Semantic Relationship Analysis**: Identifies semantic connections between documentation sections
- **Classified Relationship Types**: Categorizes relationships (uses, explains, requires, extends, applies_to, contrasts_with, related_to)
- **Documentation Gap Detection**: Finds under-connected concepts and isolated sections
- **Cross-Corpus Connectivity**: Analyzes links between conceptual and API documentation
- **Prerequisite Mapping**: Discovers learning paths through "requires" relationships
- **Support Ticket Analytics**: Maps support tickets to XAF features

## Project Structure

```
├── config/               # Configuration files
├── data/                 # Input data
├── docs/                 # Documentation
├── notebooks/            # Jupyter notebooks for exploration
├── outputs/              # Generated parquet files with analysis results
├── scripts/              # Processing scripts
├── tests/                # Test files
├── tools/                # Utility tools
├── utils/                # Helper utilities
├── query_graph.py        # Main query interface
└── requirements-lock.txt # Python dependencies
```

## Usage

### Query Documentation Relationships

```bash
# Find related sections by concept
python query_graph.py --mode query --concept "Dialog Controller"

# Filter by relationship type
python query_graph.py --mode query --concept "Dialog Controller" --relationship explains

# Find related sections for a specific document
python query_graph.py --mode query --section "article/security-system/authentication"
```

### Analyze Documentation Gaps

```bash
python query_graph.py --mode gaps
```

### View Statistics

```bash
# Show knowledge graph statistics
python query_graph.py --mode stats

# Show relationship type statistics
python query_graph.py --mode relationships
```

### Find Learning Prerequisites

```bash
python query_graph.py --mode prereqs --concept "Security System"
```

## Support Ticket Analysis

The repository includes support ticket data categorized by XAF features, helping to identify which features generate the most support requests and documentation needs.

## Dependencies

See `requirements-lock.txt` for complete dependency list. Key dependencies include:

## Installation

```bash
pip install -r requirements-lock.txt
```
