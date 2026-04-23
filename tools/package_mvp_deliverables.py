#!/usr/bin/env python3
"""
Package MVP Deliverables

Creates a curated set of outputs for tech writers and stakeholders:
- Gap analysis summary (JSON)
- Top priority actions (CSV)
- Metadata samples (YAML)
- Baseline snapshot (JSON)

Output: outputs/mvp_deliverables/ directory
"""

import json
import pandas as pd
from pathlib import Path
from datetime import datetime
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from config_loader import cfg

PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUTS_DIR = PROJECT_ROOT / "outputs"
MVP_DIR = OUTPUTS_DIR / "mvp_deliverables"


def load_data():
    """Load necessary data files"""
    return {
        'baseline': json.load(open(OUTPUTS_DIR / 'baseline_metrics.json')),
        'crosslinks': pd.read_csv(OUTPUTS_DIR / 'cross_linking_filtered_actionable.csv'),
        'metadata': pd.read_csv(OUTPUTS_DIR / 'metadata_review.csv'),
        'doc_metadata': pd.read_parquet(OUTPUTS_DIR / 'document_metadata.parquet'),
        'doc_concepts': pd.read_parquet(OUTPUTS_DIR / 'doc_concepts.parquet'),
        'semantic_pairs': pd.read_parquet(OUTPUTS_DIR / 'semantic_pairs.parquet'),
    }


def create_gap_analysis_summary(data):
    """Convert gap analysis to JSON format"""

    # Gap concepts loaded from config/product.yml (coverage.priority_gap_concepts)
    gap_concepts = cfg.priority_gap_concepts()
    
    doc_concepts = data['doc_concepts']
    pairs = data['semantic_pairs']
    kept = doc_concepts[doc_concepts["kept"] == True]
    
    gap_details = []
    
    for concept in gap_concepts:
        # Find sections
        concept_mask = kept["concepts"].apply(
            lambda cs: concept in (list(cs) if hasattr(cs, '__iter__') and not isinstance(cs, str) else [])
        )
        concept_sections = kept[concept_mask]
        
        conceptual = concept_sections[concept_sections["is_api"] == False]
        api_docs = concept_sections[concept_sections["is_api"] == True]
        
        # Check cross-links
        cross_pairs = pairs[pairs["neighbor_type"].isin(["ca", "ac"])]
        cross_with_concept = cross_pairs[
            cross_pairs["overlap_concepts"].apply(
                lambda cs: concept in (list(cs) if hasattr(cs, '__iter__') and not isinstance(cs, str) else [])
            )
        ]
        
        # Determine gap type and fix estimate
        if len(api_docs) == 0:
            gap_type = "missing_api_tagging"
            action = "Update concepts.yml and re-run extraction"
            effort_hours = "2-3 hours"
        elif len(conceptual) == 0:
            gap_type = "missing_conceptual_docs"
            action = "Write new tutorials/guides"
            effort_hours = "8-16 hours"
        else:
            gap_type = "semantic_gap"
            action = "Add cross-references, examples, code samples"
            effort_hours = "4-6 hours"
        
        gap_details.append({
            "concept": concept,
            "gap_type": gap_type,
            "conceptual_sections": len(conceptual),
            "api_sections": len(api_docs),
            "cross_links": len(cross_with_concept),
            "recommended_action": action,
            "estimated_effort": effort_hours
        })
    
    summary = {
        "generated_date": datetime.now().isoformat(),
        "total_concepts_analyzed": len(gap_concepts),
        "gaps_found": len(gap_details),
        "baseline_metrics": {
            "total_sections": len(kept),
            "isolated_sections": data['baseline'].get('overall_statistics', {}).get('isolated_sections', 0),
            "cross_corpus_links": data['baseline'].get('connectivity_by_type', {}).get('cross_corpus_total', 0),
        },
        "gap_details": gap_details,
        "next_steps": [
            "Review gap details and choose appropriate fix strategy",
            "Prioritize based on customer pain (see top_priorities.csv)",
            "Track improvements by re-running baseline comparison"
        ]
    }
    
    return summary


def create_top_priorities_csv(data):
    """Extract top 50 ticket-weighted recommendations"""
    
    crosslinks = data['crosslinks']
    
    # Sort by ticket weight and realistic score
    crosslinks = crosslinks.sort_values(
        ['ticket_weight', 'realistic_score'],
        ascending=[False, False]
    )
    
    # Take top 50
    top_50 = crosslinks.head(50)
    
    # Simplify columns for tech writers
    output = top_50[[
        'title',
        'article_type',
        'num_actual_useful_apis',
        'num_high_priority',
        'ticket_weight',
        'primary_ticket_category',
        'ticket_count',
        'word_count',
        'has_code_blocks',
        'path'
    ]].copy()
    
    # Shorten file paths for readability
    output['path'] = output['path'].apply(lambda p: str(Path(p).relative_to('data/raw_md/articles') if 'articles' in str(p) else Path(p).name))
    
    # Round ticket weight to 2 decimal places
    output['ticket_weight'] = output['ticket_weight'].round(2)
    
    output.columns = [
        'Title',
        'Type',
        'APIs to Link',
        'High Priority',
        'Pain Score',
        'Customer Pain Category',
        'Tickets',
        'Words',
        'Has Code',
        'File Path'
    ]
    
    return output


def create_metadata_samples(data):
    """Generate 20 sample YAML frontmatter examples"""
    
    metadata = data['doc_metadata']
    
    # Sample diverse examples
    # - Different proficiency levels
    # - Different platforms
    # - Different concepts
    
    samples = []
    
    # Get 5 from each proficiency level
    for proficiency in ['Beginner', 'Intermediate', 'Advanced', 'Expert']:
        level_docs = metadata[metadata['proficiency_level'] == proficiency]
        if len(level_docs) > 0:
            sample = level_docs.sample(min(5, len(level_docs)))
            samples.append(sample)
    
    if samples:
        combined = pd.concat(samples)
        
        yaml_examples = []
        for _, row in combined.iterrows():
            # Format tags list
            tags = row.get('tags', [])
            if tags is None or (isinstance(tags, float) and pd.isna(tags)):
                tags = []
            elif hasattr(tags, '__iter__') and not isinstance(tags, str):
                tags = list(tags)
            else:
                tags = []
            
            yaml = f"""# {row['doc_id']}
---
description: "{row.get('description', 'No description')[:100]}..."
tags: {tags[:8]}  # Limited to 8 tags for readability
proficiencyLevel: {row.get('proficiency_level', 'Unknown')}
---

""".strip()
            
            yaml_examples.append({
                'doc_id': row['doc_id'],
                'title': row.get('doc_id', ''),  # Use doc_id as title since title not in columns
                'yaml': yaml
            })
        
        return yaml_examples
    
    return []


def create_baseline_snapshot(data):
    """Create a simplified baseline snapshot"""
    
    baseline = data['baseline']
    overall = baseline.get('overall_statistics', {})
    connectivity = baseline.get('connectivity_by_type', {})
    
    snapshot = {
        "captured_date": baseline.get('metadata', {}).get('generated_date', 'Unknown'),
        "total_sections": overall.get('total_sections', 0),
        "kept_sections": overall.get('connected_sections', 0),  # Approximation
        "isolated_sections": {
            "count": overall.get('isolated_sections', 0),
            "percentage": overall.get('isolated_percentage', 0)
        },
        "cross_corpus_links": {
            "count": connectivity.get('cross_corpus_total', 0),
            "percentage": connectivity.get('cross_corpus_percentage', 0)
        },
        "concepts_with_gaps": 6,  # From gap analysis
        "targets": {
            "isolated_sections": "< 550 (< 5%)",
            "cross_corpus_links": "20,000+ (21%+)",
            "concepts_with_gaps": "≤ 4"
        },
        "interpretation": {
            "isolated_sections": "Sections with no semantic connections - may need better tagging or are truly standalone",
            "cross_corpus_links": "Bridges between tutorials and API docs - critical for discoverability",
            "concepts_with_gaps": "Core XAF concepts lacking proper documentation coverage"
        }
    }
    
    return snapshot


def main():
    """Package all MVP deliverables"""
    
    print("📦 Packaging MVP Deliverables\n")
    print("="*70)
    
    # Create output directory
    MVP_DIR.mkdir(exist_ok=True, parents=True)
    print(f"Output directory: {MVP_DIR}\n")
    
    # Load data
    print("Loading data...")
    data = load_data()
    print("✓ Data loaded\n")
    
    # 1. Gap Analysis Summary (JSON)
    print("1. Creating gap analysis summary...")
    gap_summary = create_gap_analysis_summary(data)
    output_file = MVP_DIR / "gap_analysis_summary.json"
    with open(output_file, 'w') as f:
        json.dump(gap_summary, f, indent=2)
    print(f"   ✓ Written to {output_file.name}")
    print(f"   Found {gap_summary['gaps_found']} concept gaps\n")
    
    # 2. Top Priorities (CSV)
    print("2. Creating top priorities list...")
    top_priorities = create_top_priorities_csv(data)
    output_file = MVP_DIR / "top_50_priorities.csv"
    top_priorities.to_csv(output_file, index=False)
    print(f"   ✓ Written to {output_file.name}")
    print(f"   Top priority: {top_priorities.iloc[0]['Title']}")
    print(f"   APIs to link: {top_priorities.iloc[0]['APIs to Link']}")
    print(f"   Pain score: {top_priorities.iloc[0]['Pain Score']:.2f}\n")
    
    # 3. Metadata Samples (YAML)
    print("3. Creating metadata samples...")
    samples = create_metadata_samples(data)
    output_file = MVP_DIR / "metadata_samples.yml"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Sample YAML Frontmatter for XAF Documentation\n")
        f.write(f"# Generated: {datetime.now().strftime('%Y-%m-%d')}\n")
        f.write("# Use these as templates for your documentation\n\n")
        f.write("="*70 + "\n\n")
        for sample in samples:
            f.write(sample['yaml'])
            f.write("\n\n" + "-"*70 + "\n\n")
    print(f"   ✓ Written to {output_file.name}")
    print(f"   Generated {len(samples)} sample YAML headers\n")
    
    # 4. Baseline Snapshot (JSON)
    print("4. Creating baseline snapshot...")
    snapshot = create_baseline_snapshot(data)
    output_file = MVP_DIR / "baseline_snapshot.json"
    with open(output_file, 'w') as f:
        json.dump(snapshot, f, indent=2)
    print(f"   ✓ Written to {output_file.name}")
    print(f"   Isolated sections: {snapshot['isolated_sections']['count']} ({snapshot['isolated_sections']['percentage']:.1f}%)\n")
    
    # 5. Create README
    print("5. Creating deliverables README...")
    readme = f"""# MVP Deliverables

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

This directory contains curated outputs from the XAF Documentation Analysis project,
packaged for tech writers and stakeholders.

## Files

### 1. gap_analysis_summary.json
**Purpose:** Identifies 6 XAF concepts with documentation gaps  
**Audience:** Tech writers, documentation leads  
**Action:** Review gap types and choose fix strategies

**Key Metrics:**
- Total sections analyzed: {gap_summary['baseline_metrics']['total_sections']:,}
- Gaps found: {gap_summary['gaps_found']}
- Isolated sections: {gap_summary['baseline_metrics']['isolated_sections']} ({gap_summary['baseline_metrics']['isolated_sections'] / gap_summary['baseline_metrics']['total_sections'] * 100:.1f}%)

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
- Isolated sections: {snapshot['isolated_sections']['count']} ({snapshot['isolated_sections']['percentage']:.1f}%)
- Cross-corpus links: {snapshot['cross_corpus_links']['count']:,} ({snapshot['cross_corpus_links']['percentage']:.1f}%)
- Concepts with gaps: {snapshot['concepts_with_gaps']}

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
"""
    
    output_file = MVP_DIR / "README.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(readme)
    print(f"   ✓ Written to {output_file.name}\n")
    
    # Summary
    print("="*70)
    print("✅ MVP Deliverables Package Complete!\n")
    print(f"📁 Location: {MVP_DIR}\n")
    print("Files created:")
    print("  ✓ gap_analysis_summary.json")
    print("  ✓ top_50_priorities.csv")
    print("  ✓ metadata_samples.yml")
    print("  ✓ baseline_snapshot.json")
    print("  ✓ README.md")
    print("\n📖 Next: Review README.md in the deliverables folder for usage instructions")


if __name__ == "__main__":
    main()
