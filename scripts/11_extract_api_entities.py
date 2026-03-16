#!/usr/bin/env python3
"""
Phase 2a: Extract API Entities from existing doc_concepts data

Your doc_concepts.parquet already has 'apis' extracted (6,853 API sections).
This script structures them into proper API entities with:
- api_id: Full namespace path
- api_name: Short name (e.g., "SecurityStrategy")
- api_type: class, method, property, interface, delegate, enum
- namespace: DevExpress.ExpressApp.Security
- section_id: Link back to documentation

Output: 
- outputs/api_entities.parquet (unique API definitions)
- outputs/documents_api.parquet (section → API relationships)
"""

import argparse
import re
from pathlib import Path
import pandas as pd
from collections import defaultdict


def parse_api_identifier(api_full_path: str) -> dict:
    """
    Parse API identifier from extracted format.
    
    Examples:
        "DevExpress.ExpressApp.Actions.SecurityStrategy" 
        → {name: "SecurityStrategy", namespace: "DevExpress.ExpressApp.Actions", type: "class"}
        
        "DevExpress.ExpressApp.Security.SecurityStrategyBasedescription"
        → {name: "SecurityStrategyBase", namespace: "...", type: "class", suffix: "description"}
        
        "DevExpress.ExpressApp.IObjectSpace.CreateObjectname"
        → {name: "CreateObject", namespace: "...", type: "method", suffix: "name"}
    """
    if not api_full_path or pd.isna(api_full_path):
        return None
    
    # Remove common suffixes that indicate documentation types
    suffix_pattern = r'(description|name|remarks|example|parameters?|returns?|exceptions?)$'
    suffix_match = re.search(suffix_pattern, api_full_path, re.IGNORECASE)
    suffix = suffix_match.group(1) if suffix_match else None
    
    # Clean the path
    clean_path = re.sub(suffix_pattern, '', api_full_path, flags=re.IGNORECASE)
    
    # Split into parts
    parts = clean_path.split('.')
    
    if len(parts) < 2:
        return None
    
    # Last part is the API name
    api_name = parts[-1]
    
    # Skip if name is empty
    if not api_name:
        return None
    
    # Everything before is namespace
    namespace = '.'.join(parts[:-1])
    
    # Determine type from name patterns and context
    api_type = 'unknown'
    
    # Interfaces start with I
    if api_name.startswith('I') and len(api_name) > 1 and api_name[1].isupper():
        api_type = 'interface'
    # EventHandlers/EventArgs are delegates
    elif 'EventHandler' in api_name or 'EventArgs' in api_name:
        api_type = 'delegate'
    # Methods typically lowercase first letter or have verb patterns
    elif api_name[0].islower() or re.search(r'^(Get|Set|Create|Delete|Update|Add|Remove|Find|Show|Hide|Execute)', api_name):
        api_type = 'method'
    # Properties are typically nouns
    elif suffix in ['name', 'description']:
        # These suffixes usually document properties
        api_type = 'property'
    # Enums often have 'Type', 'Mode', 'State' suffixes
    elif re.search(r'(Type|Mode|State|Status|Kind)$', api_name):
        api_type = 'enum'
    else:
        # Default to class
        api_type = 'class'
    
    return {
        'api_id': clean_path,
        'api_name': api_name,
        'namespace': namespace,
        'api_type': api_type,
        'suffix': suffix,
        'original': api_full_path
    }


def extract_api_entities(doc_concepts_df: pd.DataFrame, uid_map: dict[str, str] | None = None, fallback_to_uid: bool = True) -> tuple:
    """
    Extract unique API entities and document relationships.
    
    Returns: (api_entities_df, documents_api_df)
    """
    print("\nExtracting API entities from doc_concepts...")
    
    # Filter to API sections (do not require extracted APIs to be present)
    api_sections = doc_concepts_df[
        (doc_concepts_df['is_api'] == True)
    ].copy()
    
    print(f"  Found {len(api_sections)} API sections")
    
    # Track unique APIs and relationships
    api_entities = {}  # api_id → entity info
    documents_api = []  # section → API relationships
    
    # Process each API section
    for idx, row in api_sections.iterrows():
        doc_id = row['doc_id']
        section_id = row['section_id']
        
        # Handle both list and numpy array
        apis_raw = row['apis']
        if apis_raw is None or (isinstance(apis_raw, float) and pd.isna(apis_raw)):
            apis_list = []
        elif isinstance(apis_raw, list):
            apis_list = apis_raw
        else:
            # Assume it's array-like
            apis_list = list(apis_raw)
        
        concepts_raw = row['concepts']
        if concepts_raw is None or (isinstance(concepts_raw, float) and pd.isna(concepts_raw)):
            concepts = []
        elif isinstance(concepts_raw, list):
            concepts = concepts_raw
        else:
            concepts = list(concepts_raw)
        
        # Fallback: if API identifiers weren't extracted (common when patterns.yml is missing),
        # use the document UID as the API id.
        if fallback_to_uid and (not apis_list) and uid_map is not None:
            uid = uid_map.get(str(doc_id))
            if uid and isinstance(uid, str) and ('.' in uid):
                apis_list = [uid]

        # Parse each API mentioned in this section
        for api_str in apis_list:
            parsed = parse_api_identifier(api_str)
            
            if not parsed:
                continue
            
            api_id = parsed['api_id']
            
            # Add to unique entities (or update if already seen)
            if api_id not in api_entities:
                api_entities[api_id] = {
                    'api_id': api_id,
                    'api_name': parsed['api_name'],
                    'namespace': parsed['namespace'],
                    'api_type': parsed['api_type'],
                    'documented_in_sections': [],
                    'related_concepts': set()
                }
            
            # Track documentation locations
            api_entities[api_id]['documented_in_sections'].append(section_id)
            api_entities[api_id]['related_concepts'].update(concepts)
            
            # Create documents_api relationship
            documents_api.append({
                'section_id': section_id,
                'doc_id': doc_id,
                'api_id': api_id,
                'api_name': parsed['api_name'],
                'api_type': parsed['api_type'],
                'namespace': parsed['namespace']
            })
    
    # Convert to DataFrames
    api_entities_list = []
    for api_id, entity in api_entities.items():
        api_entities_list.append({
            'api_id': entity['api_id'],
            'api_name': entity['api_name'],
            'namespace': entity['namespace'],
            'api_type': entity['api_type'],
            'num_sections': len(entity['documented_in_sections']),
            'related_concepts': list(entity['related_concepts'])
        })
    
    api_entities_df = pd.DataFrame(api_entities_list)
    documents_api_df = pd.DataFrame(documents_api)

    # Ensure stable schemas even when empty
    if api_entities_df.empty:
        api_entities_df = pd.DataFrame(columns=[
            'api_id', 'api_name', 'namespace', 'api_type', 'num_sections', 'related_concepts'
        ])
    if documents_api_df.empty:
        documents_api_df = pd.DataFrame(columns=[
            'section_id', 'doc_id', 'api_id', 'api_name', 'api_type', 'namespace'
        ])
    
    return api_entities_df, documents_api_df


def print_statistics(api_entities_df, documents_api_df):
    """Print extraction statistics"""
    print("\n" + "="*80)
    print("API EXTRACTION STATISTICS")
    print("="*80)
    
    print(f"\nUnique API entities: {len(api_entities_df)}")
    print(f"Document → API relationships: {len(documents_api_df)}")
    
    if api_entities_df.empty:
        print("\n(no API entities extracted)")
        return

    print(f"\nAPI Type Distribution:")
    if 'api_type' in api_entities_df.columns:
        print(api_entities_df['api_type'].value_counts().to_string())
    
    print(f"\nTop 10 Namespaces:")
    if 'namespace' in api_entities_df.columns:
        namespace_counts = api_entities_df['namespace'].value_counts()
        print(namespace_counts.head(10).to_string())
    
    print(f"\nAPIs with most documentation sections:")
    if 'num_sections' in api_entities_df.columns:
        top_documented = api_entities_df.nlargest(10, 'num_sections')[['api_name', 'api_type', 'namespace', 'num_sections']]
        print(top_documented.to_string())


def main():
    parser = argparse.ArgumentParser(
        description='Extract API entities from doc_concepts'
    )
    parser.add_argument(
        '--input',
        default='outputs/doc_concepts.parquet',
        help='Input doc_concepts file'
    )
    parser.add_argument(
        '--output-entities',
        default='outputs/api_entities.parquet',
        help='Output API entities file'
    )
    parser.add_argument(
        '--output-relationships',
        default='outputs/documents_api.parquet',
        help='Output documents-API relationships file'
    )
    parser.add_argument(
        '--export-csv',
        action='store_true',
        help='Also export as CSV for review'
    )
    parser.add_argument(
        '--topics-inventory',
        default='outputs/topics_inventory.parquet',
        help='topics_inventory.parquet (used for UID fallback when APIs are not extracted)'
    )
    parser.add_argument(
        '--no-uid-fallback',
        action='store_true',
        help='Disable UID-based fallback API extraction'
    )
    
    args = parser.parse_args()
    
    # Load doc_concepts
    print(f"Loading {args.input}...")
    doc_concepts_df = pd.read_parquet(args.input)
    print(f"  Loaded {len(doc_concepts_df)} sections")

    # Load topics inventory for UID fallback
    uid_map = None
    topics_path = Path(args.topics_inventory)
    if topics_path.exists():
        topics_df = pd.read_parquet(topics_path)
        if 'doc_id' in topics_df.columns and 'uid' in topics_df.columns:
            uid_map = dict(zip(topics_df['doc_id'].astype(str), topics_df['uid'].astype(str)))
    
    # Extract API entities
    api_entities_df, documents_api_df = extract_api_entities(
        doc_concepts_df,
        uid_map=uid_map,
        fallback_to_uid=(not args.no_uid_fallback)
    )
    
    # Save results
    print(f"\nSaving API entities to {args.output_entities}...")
    Path(args.output_entities).parent.mkdir(parents=True, exist_ok=True)
    api_entities_df.to_parquet(args.output_entities, index=False)
    
    print(f"Saving documents-API relationships to {args.output_relationships}...")
    documents_api_df.to_parquet(args.output_relationships, index=False)
    
    if args.export_csv:
        entities_csv = args.output_entities.replace('.parquet', '.csv')
        relationships_csv = args.output_relationships.replace('.parquet', '.csv')
        
        print(f"Exporting to CSV...")
        api_entities_df.to_csv(entities_csv, index=False)
        documents_api_df.to_csv(relationships_csv, index=False)
    
    # Show statistics
    print_statistics(api_entities_df, documents_api_df)
    
    # Show examples
    print(f"\n{'='*80}")
    print("SAMPLE API ENTITIES")
    print("="*80)
    if api_entities_df.empty:
        print("(none)")
    else:
        for idx, row in api_entities_df.head(10).iterrows():
            print(f"\n{row['api_name']} ({row['api_type']})")
            print(f"  Namespace: {row['namespace']}")
            print(f"  Documented in: {row['num_sections']} sections")
            concepts = row.get('related_concepts', [])
            concepts = list(concepts) if isinstance(concepts, (list, tuple)) else []
            print(f"  Concepts: {', '.join(concepts[:3])}")
    
    print(f"\n✅ Done!")
    print(f"   API entities: {len(api_entities_df)}")
    print(f"   Relationships: {len(documents_api_df)}")
    print(f"\n💡 Next step: Run scripts/12_map_apis_to_concepts.py")


if __name__ == '__main__':
    main()
