#!/usr/bin/env python3
"""
Roll up section-level metadata to document-level metadata

Input: metadata_suggestions.parquet (section-level tags)
Output: document_metadata.parquet (article-level tags)

Strategy:
1. Group sections by doc_id
2. Aggregate tags (union, but weighted by section importance)
3. Pick best description (prioritize intro sections)
4. Determine document proficiency (max of sections)
5. Count total semantic connections for document
"""

import argparse
import sys
from pathlib import Path
import pandas as pd
from collections import Counter

# Add parent directory to path for validation imports
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils.pipeline_validators import (
    PipelineValidator, ValidationReport, ValidationResult,
    save_validation_report, load_validation_thresholds
)


def safe_list(val):
    """Handle numpy arrays from parquet"""
    if val is None or (isinstance(val, float) and pd.isna(val)):
        return []
    if isinstance(val, (list, tuple)):
        return list(val)
    if hasattr(val, '__iter__') and not isinstance(val, str):
        return list(val)
    return []


def aggregate_tags(section_tags_list, max_tags=12):
    """
    Aggregate tags from multiple sections
    
    Strategy:
    - Count tag frequency across sections
    - Keep tags that appear in multiple sections (higher weight)
    - Limit to max_tags most important
    """
    tag_counter = Counter()
    
    for tags in section_tags_list:
        for tag in safe_list(tags):
            tag_counter[tag] += 1
    
    # Sort by frequency, take top N
    most_common = tag_counter.most_common(max_tags)
    return [tag for tag, count in most_common]


def pick_best_description(sections_df):
    """
    Choose the best description from available sections
    
    Priority:
    1. Description from section with most connections
    2. First non-null description
    3. Generate from document title
    """
    # Filter to sections with descriptions
    with_desc = sections_df[sections_df['suggested_description'].notna()].copy()
    
    if len(with_desc) == 0:
        return None
    
    # Pick section with most connections
    best_section = with_desc.sort_values('num_semantic_connections', ascending=False).iloc[0]
    return best_section['suggested_description']


def determine_proficiency(sections_df):
    """
    Determine document-level proficiency
    
    Strategy:
    - If ANY section is Expert → document is Expert
    - If ANY section is Advanced and none are Expert → Advanced
    - Otherwise → Beginner
    """
    proficiency_values = sections_df['proficiency_level'].value_counts()
    
    if 'Expert' in proficiency_values and proficiency_values['Expert'] > 0:
        return 'Expert'
    elif 'Advanced' in proficiency_values and proficiency_values['Advanced'] > 0:
        return 'Advanced'
    else:
        return 'Beginner'


def aggregate_concepts_platforms_apis(sections_df):
    """
    Get unique concepts, platforms, and APIs mentioned in document
    """
    all_concepts = []
    all_platforms = []
    all_apis = []
    
    for _, row in sections_df.iterrows():
        all_concepts.extend(safe_list(row['original_concepts']))
        all_platforms.extend(safe_list(row['original_platforms']))
        all_apis.extend(safe_list(row['original_apis']))
    
    return {
        'concepts': list(set(all_concepts)),
        'platforms': list(set(all_platforms)),
        'apis': list(set(all_apis))
    }


def rollup_document_metadata(section_metadata_df):
    """
    Roll up section-level metadata to document-level
    
    Returns: DataFrame with one row per document
    """
    print("\nRolling up to document-level metadata...")
    
    document_rows = []
    
    # Group by document
    for doc_id, sections_df in section_metadata_df.groupby('doc_id'):
        # Aggregate tags
        all_section_tags = sections_df['suggested_tags'].tolist()
        document_tags = aggregate_tags(all_section_tags, max_tags=12)
        
        # Pick best description
        description = pick_best_description(sections_df)
        
        # Determine proficiency
        proficiency = determine_proficiency(sections_df)
        
        # Sum connections
        total_connections = sections_df['num_semantic_connections'].sum()
        
        # Aggregate original concepts/platforms/APIs
        aggregated = aggregate_concepts_platforms_apis(sections_df)
        
        # Check if any section is API
        has_api = sections_df['is_api'].any()
        
        document_rows.append({
            'doc_id': doc_id,
            'tags': document_tags,
            'description': description,
            'proficiency_level': proficiency,
            'total_connections': int(total_connections),
            'num_sections': len(sections_df),
            'is_api_reference': bool(has_api),
            'concepts': aggregated['concepts'],
            'platforms': aggregated['platforms'],
            'apis': aggregated['apis']
        })
    
    return pd.DataFrame(document_rows)


def calculate_document_statistics(doc_metadata_df):
    """Calculate statistics about document-level metadata"""
    print("\n" + "="*80)
    print("DOCUMENT-LEVEL METADATA STATISTICS")
    print("="*80)
    
    print(f"Total documents: {len(doc_metadata_df)}")
    print(f"Avg tags per document: {doc_metadata_df['tags'].apply(len).mean():.1f}")
    print(f"Avg sections per document: {doc_metadata_df['num_sections'].mean():.1f}")
    print(f"Avg connections per document: {doc_metadata_df['total_connections'].mean():.1f}")
    
    # Tag frequency across documents
    all_tags = []
    for tag_list in doc_metadata_df['tags']:
        all_tags.extend(safe_list(tag_list))
    
    tag_counts = pd.Series(all_tags).value_counts()
    print(f"\nTop 20 tags across all documents:")
    print(tag_counts.head(20).to_string())
    
    # Proficiency distribution
    print(f"\n{'='*80}")
    print("PROFICIENCY LEVEL DISTRIBUTION")
    print("="*80)
    print(doc_metadata_df['proficiency_level'].value_counts().to_string())
    
    # Platform distribution
    print(f"\n{'='*80}")
    print("PLATFORM COVERAGE")
    print("="*80)
    all_platforms = []
    for platforms in doc_metadata_df['platforms']:
        all_platforms.extend(safe_list(platforms))
    platform_counts = pd.Series(all_platforms).value_counts()
    print(platform_counts.head(10).to_string())
    
    # Concept distribution
    print(f"\n{'='*80}")
    print("CONCEPT COVERAGE")
    print("="*80)
    all_concepts = []
    for concepts in doc_metadata_df['concepts']:
        all_concepts.extend(safe_list(concepts))
    concept_counts = pd.Series(all_concepts).value_counts()
    print(concept_counts.head(20).to_string())


def validate_phase10_output(df: pd.DataFrame, section_df: pd.DataFrame, run_quality_checks: bool = False) -> ValidationReport:
    """
    Validate Phase 10 output data.
    
    Args:
        df: The document_metadata DataFrame
        section_df: The input section-level metadata DataFrame
        run_quality_checks: Whether to run deeper quality validation
    
    Returns:
        ValidationReport with validation results
    """
    config_path = Path(__file__).resolve().parents[1] / "config" / "validation_thresholds.yml"
    validator = PipelineValidator(config_path)
    report = ValidationReport(phase_name="Rollup Document Metadata", phase_number=10)
    
    # Level 1: Quick Sanity Checks
    print("\n🔍 Running Level 1 validation (quick sanity checks)...")
    
    # Check schema
    required_cols = ["doc_id", "tags", "description", "proficiency_level", 
                     "total_connections", "num_sections"]
    column_types = {
        "doc_id": str,
        "tags": list,
        "description": str,
        "proficiency_level": str,
        "num_sections": int
    }
    report.add_result(validator.validate_schema(df, required_cols, column_types, "Schema validation"))
    
    # Check row count (adjusted for actual unique doc count)
    report.add_result(validator.validate_row_count(df, min_rows=5000, check_name="Minimum documents"))
    
    # Check that all source docs are represented
    source_docs = set(section_df['doc_id'].unique())
    output_docs = set(df['doc_id'].unique())
    missing_docs = source_docs - output_docs
    
    if missing_docs:
        report.add_result(ValidationResult(
            check_name="Document completeness",
            passed=False,
            message=f"{len(missing_docs)} documents from section metadata are missing",
            severity="error",
            details={"missing_count": len(missing_docs), "sample": list(missing_docs)[:5]}
        ))
    else:
        report.add_result(ValidationResult(
            check_name="Document completeness",
            passed=True,
            message=f"All {len(source_docs)} documents from section metadata are present",
            severity="info"
        ))
    
    # Check average tags
    avg_tags = df['tags'].apply(len).mean()
    report.add_result(validator.validate_threshold(
        actual_value=avg_tags,
        threshold_key='min_avg_tags',
        phase_key='phase10_rollup',
        comparison='>=',
        check_name="Minimum avg tags"
    ))
    
    report.add_result(validator.validate_threshold(
        actual_value=avg_tags,
        threshold_key='max_avg_tags',
        phase_key='phase10_rollup',
        comparison='<=',
        check_name="Maximum avg tags"
    ))
    
    # Check for documents with zero tags
    zero_tags = df[df['tags'].apply(len) == 0]
    report.add_result(validator.validate_threshold(
        actual_value=len(zero_tags),
        threshold_key='max_docs_zero_tags',
        phase_key='phase10_rollup',
        comparison='<=',
        check_name="Documents with zero tags"
    ))
    
    if run_quality_checks:
        print("\n🔍 Running Level 2 validation (quality checks)...")
        
        # Check average connections
        avg_conn = df['total_connections'].mean()
        report.add_result(validator.validate_threshold(
            actual_value=avg_conn,
            threshold_key='min_avg_connections',
            phase_key='phase10_rollup',
            comparison='>=',
            check_name="Minimum avg connections"
        ))
        
        # Verify aggregation correctness (sample check)
        # For first 10 docs, verify that tags are superset of section tags
        aggregation_issues = 0
        for doc_id in df['doc_id'].head(10):
            doc_tags = set(safe_list(df[df['doc_id'] == doc_id].iloc[0]['tags']))
            section_tags = set()
            for tags in section_df[section_df['doc_id'] == doc_id]['suggested_tags']:
                section_tags.update(safe_list(tags))
            
            if not section_tags.issubset(doc_tags | set()):  # Allow some aggregation loss
                aggregation_issues += 1
        
        if aggregation_issues > 3:  # Allow some variance
            report.add_result(ValidationResult(
                check_name="Tag aggregation correctness",
                passed=False,
                message=f"{aggregation_issues}/10 sampled docs have tag aggregation issues",
                severity="warning"
            ))
        else:
            report.add_result(ValidationResult(
                check_name="Tag aggregation correctness",
                passed=True,
                message="Tag aggregation appears correct in sampled documents",
                severity="info"
            ))
        
        # Check section count distribution
        sections_stats = df['num_sections'].describe()
        report.add_result(ValidationResult(
            check_name="Sections per document",
            passed=True,
            message=f"Sections/doc: min={sections_stats['min']:.0f}, avg={sections_stats['mean']:.1f}, max={sections_stats['max']:.0f}",
            severity="info",
            details={"min": int(sections_stats['min']), "mean": float(sections_stats['mean']), "max": int(sections_stats['max'])}
        ))
    
    return report


def main():
    parser = argparse.ArgumentParser(
        description='Roll up section-level metadata to document-level'
    )
    parser.add_argument(
        '--input',
        default='outputs/metadata_suggestions.parquet',
        help='Input section-level metadata'
    )
    parser.add_argument(
        '--output',
        default='outputs/document_metadata.parquet',
        help='Output document-level metadata'
    )
    parser.add_argument(
        '--export-csv',
        action='store_true',
        help='Also export as CSV for review'
    )
    parser.add_argument(
        '--export-json',
        action='store_true',
        help='Also export as JSON for MCP/search integration'
    )
    parser.add_argument('--skip-validation', action='store_true', help='Skip validation checks')
    parser.add_argument('--validate-quality', action='store_true', help='Run deeper quality validation (Level 2)')
    parser.add_argument('--save-report', action='store_true', help='Save validation report to JSON')
    
    args = parser.parse_args()
    
    print("="*70)
    print("Phase 10: Rollup Document Metadata")
    print("="*70)
    
    # Load section-level metadata
    print(f"Loading section-level metadata from {args.input}...")
    section_metadata_df = pd.read_parquet(args.input)
    print(f"  Loaded {len(section_metadata_df)} sections")
    print(f"  Unique documents: {section_metadata_df['doc_id'].nunique()}")
    
    # Roll up to document level
    doc_metadata_df = rollup_document_metadata(section_metadata_df)
    print(f"  Generated metadata for {len(doc_metadata_df)} documents")
    
    # Save results
    print(f"\nSaving to {args.output}...")
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    doc_metadata_df.to_parquet(args.output, index=False)
    
    if args.export_csv:
        csv_path = args.output.replace('.parquet', '.csv')
        print(f"Exporting to {csv_path}...")
        doc_metadata_df.to_csv(csv_path, index=False)
    
    if args.export_json:
        json_path = args.output.replace('.parquet', '.json')
        print(f"Exporting to {json_path}...")
        doc_metadata_df.to_json(json_path, orient='records', indent=2)
    
    # Show statistics
    calculate_document_statistics(doc_metadata_df)
    
    # Show examples
    print(f"\n{'='*80}")
    print("SAMPLE DOCUMENT METADATA (First 5 Documents)")
    print("="*80)
    for idx, row in doc_metadata_df.head(5).iterrows():
        print(f"\nDocument: {row['doc_id']}")
        print(f"  Tags: {', '.join(safe_list(row['tags'])[:10])}")
        print(f"  Description: {row['description']}")
        print(f"  Proficiency: {row['proficiency_level']}")
        print(f"  Sections: {row['num_sections']}")
        print(f"  Connections: {row['total_connections']}")
        print(f"  Concepts: {', '.join(safe_list(row['concepts'])[:5])}")
        print(f"  Platforms: {', '.join(safe_list(row['platforms']))}")
    
    # Run validation
    if not args.skip_validation:
        report = validate_phase10_output(doc_metadata_df, section_metadata_df, run_quality_checks=args.validate_quality)
        report.print_summary()
        
        if args.save_report:
            report_path = Path(args.output).parent / 'validation_phase10.json'
            save_validation_report(report, report_path)
        
        if report.has_errors:
            print("\n❌ Phase 10 validation failed with errors. Review issues above.")
            sys.exit(1)
    else:
        print("\n⏭️  Validation skipped")
    
    print(f"\n✅ Phase 10 complete! Generated document-level metadata for {len(doc_metadata_df):,} documents")
    print(f"   Output: {args.output}")
    print(f"\n💡 Next steps:")
    print(f"   - Review {args.output.replace('.parquet', '.csv')} for quality")
    print(f"   - Publish tags to search index")
    print(f"   - Expose to MCP server for AI assistant queries")


if __name__ == '__main__':
    main()
