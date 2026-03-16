#!/usr/bin/env python3
"""
Export metadata suggestions in YAML format for XAF documentation front matter

Takes metadata_suggestions.parquet and generates:
1. Individual YAML snippets per document
2. Bulk export for documentation team review
3. Diff report showing what would change
"""

import argparse
from pathlib import Path
import pandas as pd
import yaml


def safe_list(val):
    """Handle numpy arrays from parquet"""
    if val is None or (isinstance(val, float) and pd.isna(val)):
        return []
    if isinstance(val, (list, tuple)):
        return list(val)
    if hasattr(val, '__iter__') and not isinstance(val, str):
        return list(val)
    return []


def format_yaml_frontmatter(row):
    """
    Generate YAML front matter for a document
    
    Returns a dict ready for YAML serialization
    """
    tags = safe_list(row['suggested_tags'])
    description = row['suggested_description']
    proficiency = row['proficiency_level']
    
    # Build YAML structure
    frontmatter = {}
    
    # Add description if available
    if description and pd.notna(description):
        frontmatter['description'] = description
    
    # Add tags (required)
    if tags:
        frontmatter['tags'] = tags
    
    # Add proficiency level (default to Beginner if not specified)
    frontmatter['proficiencyLevel'] = proficiency or 'Beginner'
    
    return frontmatter


def export_individual_yamls(metadata_df, output_dir):
    """
    Export individual YAML files for each document
    
    Useful for automated integration or manual review
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    print(f"\nExporting individual YAML files to {output_dir}/...")
    
    for idx, row in metadata_df.iterrows():
        doc_id = row['doc_id']
        
        # Create safe filename from doc_id
        filename = doc_id.replace('/', '_').replace('\\', '_') + '.yml'
        filepath = output_path / filename
        
        # Generate YAML content
        frontmatter = format_yaml_frontmatter(row)
        
        # Add metadata comment
        yaml_content = f"# Suggested metadata for: {doc_id}\n"
        yaml_content += f"# Source: Phase 7 automated analysis\n"
        yaml_content += f"# Semantic connections: {row['num_semantic_connections']}\n"
        yaml_content += "---\n"
        yaml_content += yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True)
        yaml_content += "---\n"
        
        filepath.write_text(yaml_content, encoding='utf-8')
        
        if (idx + 1) % 500 == 0:
            print(f"  Exported {idx + 1}/{len(metadata_df)} files...")
    
    print(f"✅ Exported {len(metadata_df)} YAML files")


def export_bulk_review(metadata_df, output_file):
    """
    Export single CSV for documentation team review
    
    Includes original concepts/platforms and suggestions side-by-side
    """
    print(f"\nExporting bulk review CSV to {output_file}...")
    
    # Create review DataFrame
    review_df = metadata_df[[
        'doc_id',
        'is_api',
        'suggested_tags',
        'suggested_description',
        'proficiency_level',
        'num_semantic_connections',
        'original_concepts',
        'original_platforms'
    ]].copy()
    
    # Convert lists to comma-separated strings for CSV
    review_df['suggested_tags'] = review_df['suggested_tags'].apply(
        lambda tags: ', '.join(safe_list(tags))
    )
    review_df['original_concepts'] = review_df['original_concepts'].apply(
        lambda concepts: ', '.join(safe_list(concepts))
    )
    review_df['original_platforms'] = review_df['original_platforms'].apply(
        lambda platforms: ', '.join(safe_list(platforms))
    )
    
    # Save
    review_df.to_csv(output_file, index=False)
    print(f"✅ Exported review CSV with {len(review_df)} rows")


def generate_summary_report(metadata_df):
    """
    Generate a summary report of metadata coverage
    """
    print("\n" + "="*80)
    print("METADATA COVERAGE REPORT")
    print("="*80)
    
    total = len(metadata_df)
    
    # Description coverage
    with_desc = metadata_df['suggested_description'].notna().sum()
    print(f"\nDescription Coverage:")
    print(f"  With description: {with_desc}/{total} ({with_desc/total*100:.1f}%)")
    print(f"  Without description: {total - with_desc}/{total} ({(total-with_desc)/total*100:.1f}%)")
    
    # Tag coverage
    avg_tags = metadata_df['suggested_tags'].apply(lambda t: len(safe_list(t))).mean()
    min_tags = metadata_df['suggested_tags'].apply(lambda t: len(safe_list(t))).min()
    max_tags = metadata_df['suggested_tags'].apply(lambda t: len(safe_list(t))).max()
    
    print(f"\nTag Coverage:")
    print(f"  Average tags per doc: {avg_tags:.1f}")
    print(f"  Min tags: {min_tags}")
    print(f"  Max tags: {max_tags}")
    
    # Proficiency distribution
    print(f"\nProficiency Distribution:")
    proficiency_counts = metadata_df['proficiency_level'].value_counts()
    for level, count in proficiency_counts.items():
        print(f"  {level}: {count} ({count/total*100:.1f}%)")
    
    # Documents by connectivity
    print(f"\nConnectivity Distribution:")
    print(f"  Isolated (0 connections): {(metadata_df['num_semantic_connections'] == 0).sum()}")
    print(f"  Low (1-5): {((metadata_df['num_semantic_connections'] >= 1) & (metadata_df['num_semantic_connections'] <= 5)).sum()}")
    print(f"  Medium (6-10): {((metadata_df['num_semantic_connections'] >= 6) & (metadata_df['num_semantic_connections'] <= 10)).sum()}")
    print(f"  High (>10): {(metadata_df['num_semantic_connections'] > 10).sum()}")
    
    # Top tags
    all_tags = []
    for tag_list in metadata_df['suggested_tags']:
        all_tags.extend(safe_list(tag_list))
    
    tag_counts = pd.Series(all_tags).value_counts()
    print(f"\nTop 15 Tags:")
    for tag, count in tag_counts.head(15).items():
        print(f"  {tag}: {count} documents ({count/total*100:.1f}%)")


def main():
    parser = argparse.ArgumentParser(
        description='Export metadata suggestions in YAML format'
    )
    parser.add_argument(
        '--input',
        default='outputs/metadata_suggestions.parquet',
        help='Input metadata suggestions file'
    )
    parser.add_argument(
        '--export-yamls',
        action='store_true',
        help='Export individual YAML files (creates many files!)'
    )
    parser.add_argument(
        '--yaml-dir',
        default='outputs/metadata_yamls',
        help='Directory for individual YAML exports'
    )
    parser.add_argument(
        '--review-csv',
        default='outputs/metadata_review.csv',
        help='Bulk review CSV for documentation team'
    )
    parser.add_argument(
        '--save-report',
        action='store_true',
        help='Save validation report to JSON (for pipeline compatibility)'
    )
    
    args = parser.parse_args()
    
    # Load metadata
    print(f"Loading metadata from {args.input}...")
    metadata_df = pd.read_parquet(args.input)
    print(f"  Loaded {len(metadata_df)} documents")
    
    # Generate summary report
    generate_summary_report(metadata_df)
    
    # Export individual YAMLs if requested
    if args.export_yamls:
        export_individual_yamls(metadata_df, args.yaml_dir)
    else:
        print("\nℹ️  Skipping individual YAML export (use --export-yamls to enable)")
    
    # Always export bulk review CSV
    export_bulk_review(metadata_df, args.review_csv)
    
    # Show sample YAML
    print("\n" + "="*80)
    print("SAMPLE YAML OUTPUT (First Document)")
    print("="*80)
    sample_row = metadata_df.iloc[0]
    frontmatter = format_yaml_frontmatter(sample_row)
    
    print(f"\n# Document: {sample_row['doc_id']}")
    print("---")
    print(yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True))
    print("---")
    
    print(f"\n✅ Done!")
    print(f"   Review file: {args.review_csv}")
    if args.export_yamls:
        print(f"   YAML files: {args.yaml_dir}/")


if __name__ == '__main__':
    main()
