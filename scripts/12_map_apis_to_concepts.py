#!/usr/bin/env python3
"""
Phase 2b: Map APIs to Concepts (api_implements_concept relationships)

Creates the crucial bridge between API documentation and conceptual explanations.
This enables queries like:
- "Show me all APIs that implement Security System"
- "What APIs do I use for Object Space?"
- "Find implementing APIs for this concept"

Strategy:
1. Use existing API → Concept co-occurrence from doc_concepts
2. Add namespace-based mappings (DevExpress.ExpressApp.Security → Security System)
3. Calculate confidence scores based on co-occurrence strength

Output: outputs/api_implements_concept.parquet
"""

import argparse
from pathlib import Path
import pandas as pd
import sys
from collections import Counter
from typing import Optional

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils.taxonomy_loader import load_concepts


def load_concept_definitions():
    """Load concept metadata for matching"""
    return load_concepts().get('concepts', [])


def _build_canonical_concept_index(concept_defs):
    """Build fast lookup for taxonomy concept names (case-insensitive)."""
    canonical_names = {str(c.get('name')) for c in concept_defs if c.get('name')}
    lowercase_lookup = {name.lower(): name for name in canonical_names}
    return canonical_names, lowercase_lookup


def _normalize_concept_name(raw_name: str, canonical_names: set[str], lowercase_lookup: dict[str, str]) -> Optional[str]:
    """Normalize concept labels to taxonomy canonical names or return None if unsupported."""
    if raw_name is None or (isinstance(raw_name, float) and pd.isna(raw_name)):
        return None

    name = str(raw_name).strip()
    if not name:
        return None

    if name in canonical_names:
        return name

    # Known historical aliases/legacy labels -> taxonomy canonical names.
    alias_map = {
        'Business Objects': 'Business Object',
        'Controllers': 'Controllers and Actions',
        'System Module': 'Modules',
        'Templates': 'Template Kit',
        'Office Integration': 'Office Module',
        'Pivot Grid': 'PivotGrid',
        'Pivot Charts': 'Charts',
    }
    if name in alias_map:
        mapped = alias_map[name]
        return mapped if mapped in canonical_names else None

    # Terms that are platform/runtime facets, not concepts in taxonomy.
    non_concept_labels = {'WinForms', 'Blazor UI', 'Utilities'}
    if name in non_concept_labels:
        return None

    # Case-insensitive exact fallback.
    return lowercase_lookup.get(name.lower())


def build_namespace_concept_map():
    """
    Map namespace patterns to concepts.
    
    Based on XAF architecture:
    - DevExpress.ExpressApp.Security → Security System
    - DevExpress.ExpressApp.Validation → Validation
    - DevExpress.ExpressApp.ConditionalAppearance → Conditional Appearance
    """
    return {
        'Security': 'Security System',
        'Validation': 'Validation',
        'ConditionalAppearance': 'Conditional Appearance',
        'Chart': 'Charts',
        'PivotChart': 'Pivot Charts',
        'PivotGrid': 'Pivot Grid',
        'Reports': 'Reports',
        'AuditTrail': 'Audit Trail',
        'StateMachine': 'State Machine',
        'Scheduler': 'Scheduler',
        'FileAttachments': 'File Attachments',
        'Notifications': 'Notifications',
        'ReportsV2': 'Reports',
        'Xpo': 'XPO',
        'EFCore': 'Entity Framework Core',
        'Objects': 'Business Objects',
        'Editors': 'Property Editors',
        'Actions': 'Actions',
        'Controllers': 'Controllers',
        'SystemModule': 'System Module',
        'Model': 'Application Model',
        'ViewItems': 'View Items',
        'Templates': 'Templates',
        'Utils': 'Utilities',
        'Web': 'Web API Service',
        'Win': 'WinForms',
        'Blazor': 'Blazor UI',
        'Office': 'Office Integration'
    }


def extract_api_concept_mappings(doc_concepts_df, api_entities_df):
    """
    Extract API → Concept relationships from doc_concepts.
    
    Each row in doc_concepts has both 'apis' and 'concepts' -
    these represent co-occurrence in the same documentation section.
    """
    print("\nExtracting API → Concept relationships from co-occurrence...")
    
    # Filter to API sections with both APIs and concepts
    api_sections = doc_concepts_df[
        (doc_concepts_df['is_api'] == True) & 
        (doc_concepts_df['apis'].notna()) &
        (doc_concepts_df['concepts'].notna())
    ].copy()
    
    print(f"  Processing {len(api_sections)} API sections with concept tags")
    
    # Build relationship list
    relationships = []
    
    for idx, row in api_sections.iterrows():
        # Handle both list and numpy array
        apis_raw = row['apis']
        if apis_raw is None or (isinstance(apis_raw, float) and pd.isna(apis_raw)):
            apis = []
        elif isinstance(apis_raw, list):
            apis = apis_raw
        else:
            apis = list(apis_raw)
        
        concepts_raw = row['concepts']
        if concepts_raw is None or (isinstance(concepts_raw, float) and pd.isna(concepts_raw)):
            concepts = []
        elif isinstance(concepts_raw, list):
            concepts = concepts_raw
        else:
            concepts = list(concepts_raw)
        
        # Create all API × Concept pairs from this section
        for api_str in apis:
            # Clean API identifier (remove suffix)
            api_id = api_str
            for suffix in ['description', 'name', 'remarks', 'example', 'parameters', 'returns', 'exceptions']:
                if api_id.lower().endswith(suffix):
                    api_id = api_id[:-len(suffix)]
                    break
            
            for concept in concepts:
                relationships.append({
                    'api_id': api_id,
                    'concept_name': concept,
                    'source': 'co_documentation',
                    'section_id': row['section_id']
                })
    
    print(f"  Extracted {len(relationships)} API → Concept co-occurrences")
    
    return pd.DataFrame(relationships)


def add_namespace_mappings(api_entities_df):
    """
    Add namespace-based API → Concept inferences.
    
    Example: DevExpress.ExpressApp.Security.SecurityStrategy
             → Security System (from namespace 'Security')
    """
    print("\nAdding namespace-based concept mappings...")
    
    namespace_map = build_namespace_concept_map()
    relationships = []
    
    for idx, row in api_entities_df.iterrows():
        api_id = row['api_id']
        namespace = row['namespace']
        
        # Check each namespace component
        for ns_keyword, concept_name in namespace_map.items():
            if ns_keyword in namespace:
                relationships.append({
                    'api_id': api_id,
                    'concept_name': concept_name,
                    'source': 'namespace_inference',
                    'section_id': None
                })
    
    print(f"  Added {len(relationships)} namespace-based inferences")
    
    return pd.DataFrame(relationships)


def add_related_concepts_mappings(api_entities_df):
    """
    Extract API → Concept relationships from api_entities.related_concepts field.
    
    Phase 11 already extracted concepts that co-occur with each API across all its
    documentation sections. These are stored in the related_concepts field.
    This ensures APIs get mapped even if they don't appear in doc_concepts.apis field.
    """
    print("\nAdding relationships from api_entities.related_concepts...")
    
    relationships = []
    
    for idx, row in api_entities_df.iterrows():
        api_id = row['api_id']
        related_concepts = row.get('related_concepts', [])
        
        # Handle both list and numpy array
        if related_concepts is None or (isinstance(related_concepts, float) and pd.isna(related_concepts)):
            concepts = []
        elif isinstance(related_concepts, list):
            concepts = related_concepts
        else:
            # numpy array or other iterable
            concepts = list(related_concepts)
        
        # Create relationship for each concept
        for concept in concepts:
            relationships.append({
                'api_id': api_id,
                'concept_name': concept,
                'source': 'api_entity_concepts',
                'section_id': None
            })
    
    print(f"  Added {len(relationships)} relationships from related_concepts")
    
    return pd.DataFrame(relationships)


def calculate_confidence_scores(relationships_df):
    """
    Calculate confidence score for each API → Concept relationship.
    
    Scoring:
    - co_documentation: Higher score for more co-occurrences
    - api_entity_concepts: High score (0.85) - directly from Phase 11 extraction
    - namespace_inference: Fixed moderate score (0.7)
    
    Final confidence = normalized score 0.0-1.0
    """
    print("\nCalculating confidence scores...")
    
    # Count co-occurrences
    cooccurrence_counts = (
        relationships_df[relationships_df['source'] == 'co_documentation']
        .groupby(['api_id', 'concept_name'])
        .size()
        .reset_index(name='count')
    )
    
    # Calculate confidence based on count
    # 1 occurrence = 0.6, 2+ occurrences = 0.8, 5+ = 1.0
    def count_to_confidence(count):
        if count >= 5:
            return 1.0
        elif count >= 3:
            return 0.9
        elif count >= 2:
            return 0.8
        else:
            return 0.6
    
    cooccurrence_counts['confidence'] = cooccurrence_counts['count'].apply(count_to_confidence)
    cooccurrence_counts['source'] = 'co_documentation'
    
    # API entity concepts get high confidence (0.85) - already validated in Phase 11
    entity_rels = relationships_df[relationships_df['source'] == 'api_entity_concepts'].copy()
    entity_rels = entity_rels[['api_id', 'concept_name', 'source']].drop_duplicates()
    entity_rels['confidence'] = 0.85
    entity_rels['count'] = 1
    
    # Namespace inferences get fixed 0.7 confidence
    namespace_rels = relationships_df[relationships_df['source'] == 'namespace_inference'].copy()
    namespace_rels = namespace_rels[['api_id', 'concept_name', 'source']].drop_duplicates()
    namespace_rels['confidence'] = 0.7
    namespace_rels['count'] = 1
    
    # Combine
    final_rels = pd.concat([
        cooccurrence_counts[['api_id', 'concept_name', 'confidence', 'source', 'count']],
        entity_rels[['api_id', 'concept_name', 'confidence', 'source', 'count']],
        namespace_rels[['api_id', 'concept_name', 'confidence', 'source', 'count']]
    ], ignore_index=True)
    
    # If same API-Concept pair from multiple sources, keep highest confidence
    final_rels = (
        final_rels
        .sort_values('confidence', ascending=False)
        .drop_duplicates(subset=['api_id', 'concept_name'], keep='first')
    )
    
    return final_rels


def print_statistics(api_implements_df, api_entities_df):
    """Print mapping statistics"""
    print("\n" + "="*80)
    print("API → CONCEPT MAPPING STATISTICS")
    print("="*80)
    
    print(f"\nTotal API → Concept relationships: {len(api_implements_df)}")
    print(f"Unique APIs with concept mappings: {api_implements_df['api_id'].nunique()}")
    print(f"Unique concepts referenced: {api_implements_df['concept_name'].nunique()}")
    
    print(f"\nMapping source distribution:")
    print(api_implements_df['source'].value_counts().to_string())
    
    print(f"\nConfidence distribution:")
    print(api_implements_df['confidence'].describe().to_string())
    
    print(f"\nTop 15 concepts by API count:")
    concept_api_counts = api_implements_df.groupby('concept_name')['api_id'].nunique().sort_values(ascending=False)
    print(concept_api_counts.head(15).to_string())
    
    # Coverage analysis
    total_apis = len(api_entities_df)
    mapped_apis = api_implements_df['api_id'].nunique()
    coverage_pct = (mapped_apis / total_apis) * 100
    
    print(f"\nCoverage: {mapped_apis}/{total_apis} APIs mapped to concepts ({coverage_pct:.1f}%)")


def main():
    parser = argparse.ArgumentParser(
        description='Map APIs to Concepts (api_implements_concept relationships)'
    )
    parser.add_argument(
        '--doc-concepts',
        default='outputs/doc_concepts.parquet',
        help='Input doc_concepts file'
    )
    parser.add_argument(
        '--api-entities',
        default='outputs/api_entities.parquet',
        help='Input API entities file'
    )
    parser.add_argument(
        '--output',
        default='outputs/api_implements_concept.parquet',
        help='Output API-concept relationships file'
    )
    parser.add_argument(
        '--export-csv',
        action='store_true',
        help='Also export as CSV for review'
    )
    
    args = parser.parse_args()
    
    # Load data
    print(f"Loading {args.doc_concepts}...")
    doc_concepts_df = pd.read_parquet(args.doc_concepts)
    
    print(f"Loading {args.api_entities}...")
    api_entities_df = pd.read_parquet(args.api_entities)
    print(f"  {len(api_entities_df)} API entities")

    concept_defs = load_concept_definitions()
    canonical_concepts, lowercase_lookup = _build_canonical_concept_index(concept_defs)
    print(f"  Loaded {len(canonical_concepts)} canonical concepts from taxonomy")
    
    # Extract co-occurrence relationships
    cooccurrence_rels = extract_api_concept_mappings(doc_concepts_df, api_entities_df)
    
    # Add namespace-based inferences
    namespace_rels = add_namespace_mappings(api_entities_df)
    
    # Add relationships from api_entities.related_concepts field
    related_concepts_rels = add_related_concepts_mappings(api_entities_df)
    
    # Combine and calculate confidence
    all_relationships = pd.concat([
        cooccurrence_rels, 
        namespace_rels, 
        related_concepts_rels
    ], ignore_index=True)

    # Enforce taxonomy as source of truth for concept labels.
    all_relationships['concept_name_raw'] = all_relationships['concept_name']
    all_relationships['concept_name'] = all_relationships['concept_name'].apply(
        lambda x: _normalize_concept_name(x, canonical_concepts, lowercase_lookup)
    )
    dropped = all_relationships['concept_name'].isna().sum()
    if dropped:
        print(f"\nDropped {dropped} API→concept relationships with non-taxonomy concept names")
        dropped_by_label = (
            all_relationships[all_relationships['concept_name'].isna()]
            .groupby('concept_name_raw')
            .size()
            .sort_values(ascending=False)
            .head(10)
        )
        print("Top dropped labels:")
        print(dropped_by_label.to_string())

    all_relationships = all_relationships[all_relationships['concept_name'].notna()].copy()
    all_relationships = all_relationships.drop(columns=['concept_name_raw'])

    api_implements_df = calculate_confidence_scores(all_relationships)
    
    # Save results
    print(f"\nSaving to {args.output}...")
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    api_implements_df.to_parquet(args.output, index=False)
    
    if args.export_csv:
        csv_path = args.output.replace('.parquet', '.csv')
        print(f"Exporting to {csv_path}...")
        api_implements_df.to_csv(csv_path, index=False)
    
    # Show statistics
    print_statistics(api_implements_df, api_entities_df)
    
    # Show examples
    print(f"\n{'='*80}")
    print("SAMPLE API → CONCEPT MAPPINGS")
    print("="*80)
    
    # Show examples for a few concepts
    for concept in ['Security System', 'Actions', 'Object Space', 'Views']:
        apis = api_implements_df[api_implements_df['concept_name'] == concept].head(5)
        if len(apis) > 0:
            print(f"\n{concept} ({len(api_implements_df[api_implements_df['concept_name'] == concept])} APIs):")
            for _, row in apis.iterrows():
                api_name = row['api_id'].split('.')[-1]
                print(f"  • {api_name} (confidence: {row['confidence']:.2f}, source: {row['source']})")
    
    print(f"\n✅ Done!")
    print(f"   Created {len(api_implements_df)} API → Concept relationships")
    print(f"   Coverage: {api_implements_df['api_id'].nunique()} / {len(api_entities_df)} APIs mapped")
    print(f"\n💡 This enables queries like:")
    print(f"   - 'Show me all APIs for Security System'")
    print(f"   - 'What APIs implement Object Space?'")
    print(f"   - 'Find APIs related to Validation'")


if __name__ == '__main__':
    main()
