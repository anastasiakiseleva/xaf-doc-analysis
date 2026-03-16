#!/usr/bin/env python3
"""
12_map_apis_to_concepts_ollama.py

Enhanced Phase 2b: API-to-Concept Classification with Ollama

Combines three strategies:
1. Co-occurrence from doc_concepts (existing - high confidence)
2. Namespace-based rules (existing - medium confidence)
3. Ollama/Llama 3.1 classification (new - fills gaps)

Usage:
    # Test on 10 APIs first
    python 12_map_apis_to_concepts_ollama.py --sample 10 --use-ollama
    
    # Run on unmapped APIs only
    python 12_map_apis_to_concepts_ollama.py --use-ollama --unmapped-only
    
    # Full run (overnight)
    python 12_map_apis_to_concepts_ollama.py --use-ollama
"""

import argparse
import json
import subprocess
import time
from pathlib import Path
from typing import Dict, List, Optional
import pandas as pd
import yaml


# ============================================================================
# Ollama Integration
# ============================================================================

SYSTEM_PROMPT = """You are an expert at analyzing DevExpress XAF (eXpressApp Framework) documentation. Your task is to classify which XAF concepts a given API entity implements or relates to.

XAF CONCEPTS (choose from these 45 concepts):

PLATFORMS: Blazor UI, WinForms, Web API Service, Template Kit, .NET Runtime

ARCHITECTURE: XAF Application, Modules, Application Model, Model Nodes, MVC Pattern, ApplicationBuilder, Dependency Injection, Middle Tier, Callback Pattern, Async Operations

DATA LAYER: Object Space, Object Space Provider, Database Connection, Entity Framework Core, XPO, Business Objects, Non-Persistent Objects, Collection Property, Reference Property, Calculated Property, Criteria, Multiple Databases, Direct SQL, Auto-Increment Fields, Tree Node Interface

UI - VIEWS: Views, List View, Detail View, Dashboard View, Lookup View

UI - EDITORS: List Editors, Inline Editing, Tree List, Property Editors, Layout

UI - CONTROLLERS & ACTIONS: Controllers, View Controller, Window Controller, Dialog Controller, Tabbed MDI Interface, Context Menus, Loading Indicators, Filtering UI, Spreadsheet Control, SVG Graphics, Accordion Control, Theming, Actions, Simple Action, Popup Window Show Action, Parametrized Action, Navigation

SECURITY: Security System, Security Strategy, Authentication, Authorization, Custom User Management, Permission Policies, Audit Trail

MODULES: Validation, Custom Validation Rules, Error Styling, Conditional Appearance, Reports, Report Parameters, Reports V2, Mail Merge, Dashboards, Scheduler, Event Scheduling Interfaces, Recurring Events, Notifications, State Machine, File Attachments, Charts, PivotGrid, Clone Object

MULTI-TENANCY: Multi-Tenancy, Tenant

OPERATIONS: Deployment, Testing, Logging, Diagnostic Tools, Threading Issues, Performance Optimization, Memory Management, Scaling Architecture

LEGACY/MIGRATION: Legacy .NET Framework, Migration, Database Update, Package Management, Assembly References, Project Wizards, Programmatic Localization, Domain Components, Demo Applications

CLASSIFICATION RULES:

1. Namespace signals:
   - DevExpress.ExpressApp.Security.* → Security System
   - DevExpress.ExpressApp.Validation.* → Validation
   - DevExpress.ExpressApp.Actions.* → Actions
   - DevExpress.Xpo.* → XPO
   - DevExpress.ExpressApp.EFCore.* → Entity Framework Core

2. Interface patterns:
   - IObjectSpace → Object Space
   - IModel* → Application Model
   - ITreeNode → Tree Node Interface

3. Base class patterns:
   - *ViewController → View Controller
   - *Controller → Controllers
   - XafApplication → XAF Application

4. Multi-concept APIs are common - an API can implement multiple concepts.

Return ONLY valid JSON with this structure (no additional text):
{
  "concepts": ["Concept Name 1", "Concept Name 2"],
  "confidence": 0.85,
  "primary_concept": "Concept Name 1",
  "reasoning": "Brief explanation",
  "namespace_signal": true
}"""


def call_ollama(api_name: str, namespace: str, api_type: str, 
                doc_context: str = "", timeout: int = 30) -> Dict:
    """
    Call Ollama to classify a single API.
    
    Returns:
        Dict with keys: concepts, confidence, primary_concept, reasoning, error (if failed)
    """
    
    user_prompt = f"""Classify this XAF API entity:

API Name: {api_name}
Full Identifier: {namespace}.{api_name}
Namespace: {namespace}
API Type: {api_type}
Documentation Context: {doc_context[:300]}

Analyze the API and return JSON classification."""

    try:
        # Call Ollama via subprocess
        result = subprocess.run(
            ['ollama', 'run', 'llama3.1:8b', '--'],
            input=f"{SYSTEM_PROMPT}\n\n{user_prompt}".encode('utf-8'),
            capture_output=True,
            timeout=timeout
        )
        
        output = result.stdout.decode('utf-8').strip()
        
        # Extract JSON (Ollama may wrap it in text)
        json_start = output.find('{')
        json_end = output.rfind('}') + 1
        
        if json_start >= 0 and json_end > json_start:
            json_str = output[json_start:json_end]
            classification = json.loads(json_str)
            
            # Validate required fields
            if 'concepts' not in classification:
                return {"error": "Missing 'concepts' field", "raw": output[:200]}
            
            # Ensure concepts is a list
            if not isinstance(classification['concepts'], list):
                classification['concepts'] = [classification['concepts']]
            
            # Set defaults for optional fields
            classification.setdefault('confidence', 0.7)
            classification.setdefault('primary_concept', 
                                     classification['concepts'][0] if classification['concepts'] else None)
            classification.setdefault('reasoning', '')
            classification.setdefault('namespace_signal', False)
            
            return classification
        else:
            return {"error": "No JSON in response", "raw": output[:200]}
            
    except subprocess.TimeoutExpired:
        return {"error": f"Timeout after {timeout}s"}
    except subprocess.CalledProcessError as e:
        return {"error": f"Ollama error: {e.stderr.decode('utf-8')[:200]}"}
    except json.JSONDecodeError as e:
        return {"error": f"JSON parse error: {str(e)}", "raw": output[:200] if 'output' in locals() else ""}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}


# ============================================================================
# Rule-Based Classification (from original script)
# ============================================================================

def build_namespace_concept_map():
    """Namespace pattern → Concept mappings"""
    return {
        'Security': 'Security System',
        'Validation': 'Validation',
        'ConditionalAppearance': 'Conditional Appearance',
        'Chart': 'Charts',
        'PivotChart': 'Charts',
        'PivotGrid': 'PivotGrid',
        'Reports': 'Reports',
        'AuditTrail': 'Audit Trail',
        'StateMachine': 'State Machine',
        'Scheduler': 'Scheduler',
        'FileAttachments': 'File Attachments',
        'Notifications': 'Notifications',
        'ReportsV2': 'Reports V2',
        'Xpo': 'XPO',
        'EFCore': 'Entity Framework Core',
        'Objects': 'Business Objects',
        'Editors': 'Property Editors',
        'Actions': 'Actions',
        'Controllers': 'Controllers',
        'SystemModule': 'Modules',
        'Model': 'Application Model',
        'ViewItems': 'Views',
        'Templates': 'Template Kit',
        'Web': 'Web API Service',
        'Win': 'WinForms',
        'Blazor': 'Blazor UI'
    }


def extract_cooccurrence_mappings(doc_concepts_df) -> pd.DataFrame:
    """Extract API → Concept from documentation co-occurrence"""
    
    api_sections = doc_concepts_df[
        (doc_concepts_df['is_api'] == True) & 
        (doc_concepts_df['apis'].notna()) &
        (doc_concepts_df['concepts'].notna())
    ].copy()
    
    relationships = []
    
    for _, row in api_sections.iterrows():
        # Safe list conversion
        apis = row['apis'] if isinstance(row['apis'], list) else []
        concepts = row['concepts'] if isinstance(row['concepts'], list) else []
        
        for api_str in apis:
            # Clean API identifier
            api_id = api_str
            for suffix in ['description', 'name', 'remarks', 'example']:
                if api_id.lower().endswith(suffix):
                    api_id = api_id[:-len(suffix)]
                    break
            
            for concept in concepts:
                relationships.append({
                    'api_id': api_id,
                    'concept_name': concept,
                    'source': 'co_documentation',
                    'confidence': 0.9,  # High - they're documented together
                    'section_id': row['section_id']
                })
    
    return pd.DataFrame(relationships)


def extract_namespace_mappings(api_entities_df) -> pd.DataFrame:
    """Extract API → Concept from namespace patterns"""
    
    namespace_map = build_namespace_concept_map()
    relationships = []
    
    for _, row in api_entities_df.iterrows():
        api_id = row['api_id']
        namespace = row['namespace']
        
        # Check each namespace component
        for ns_keyword, concept_name in namespace_map.items():
            if ns_keyword in namespace:
                relationships.append({
                    'api_id': api_id,
                    'concept_name': concept_name,
                    'source': 'namespace_inference',
                    'confidence': 0.75,
                    'section_id': None
                })
    
    return pd.DataFrame(relationships)


# ============================================================================
# Ollama Classification
# ============================================================================

def classify_with_ollama(api_entities_df, doc_concepts_df, 
                         api_ids_to_classify: List[str],
                         verbose: bool = False) -> pd.DataFrame:
    """
    Use Ollama to classify APIs that weren't handled by rules.
    
    Args:
        api_entities_df: DataFrame with API metadata
        doc_concepts_df: DataFrame with documentation
        api_ids_to_classify: List of API IDs to classify
        verbose: Print progress details
    
    Returns:
        DataFrame with columns: api_id, concept_name, source, confidence
    """
    
    print(f"\n🤖 Classifying {len(api_ids_to_classify)} APIs with Ollama...")
    print(f"   Model: Llama 3.1 8B")
    print(f"   Estimated time: {len(api_ids_to_classify) * 3 / 60:.1f} minutes")
    
    relationships = []
    success_count = 0
    error_count = 0
    
    for idx, api_id in enumerate(api_ids_to_classify):
        if (idx + 1) % 10 == 0:
            print(f"   Progress: {idx + 1}/{len(api_ids_to_classify)} "
                  f"(✓{success_count} ✗{error_count})")
        
        # Get API metadata
        api_row = api_entities_df[api_entities_df['api_id'] == api_id]
        if api_row.empty:
            continue
        api_row = api_row.iloc[0]
        
        # Get documentation context
        doc_context = ""
        doc_rows = doc_concepts_df[
            doc_concepts_df['apis'].apply(
                lambda x: api_id in x if isinstance(x, list) else False
            )
        ]
        if len(doc_rows) > 0:
            # Extract text content
            first_doc = doc_rows.iloc[0]
            doc_context = str(first_doc.get('h_path', '')) + " " + str(first_doc.get('text', ''))[:300]
        
        # Call Ollama
        classification = call_ollama(
            api_name=api_row['api_name'],
            namespace=api_row['namespace'],
            api_type=api_row['api_type'],
            doc_context=doc_context
        )
        
        # Handle result
        if 'error' in classification:
            error_count += 1
            if verbose:
                print(f"   ✗ {api_row['api_name']}: {classification['error'][:50]}")
            continue
        
        # Add relationships
        if classification.get('concepts'):
            success_count += 1
            for concept in classification['concepts']:
                relationships.append({
                    'api_id': api_id,
                    'concept_name': concept,
                    'source': 'ollama_classification',
                    'confidence': classification.get('confidence', 0.7),
                    'section_id': None,
                    'reasoning': classification.get('reasoning', '')[:200]
                })
            
            if verbose and (idx + 1) % 50 == 0:
                print(f"   ✓ {api_row['api_name']}: {', '.join(classification['concepts'][:2])}")
        
        # Rate limiting (be nice to your hardware)
        time.sleep(0.5)
    
    print(f"\n   Completed: {success_count} successful, {error_count} errors")
    
    return pd.DataFrame(relationships)


# ============================================================================
# Main Pipeline
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='Enhanced API-to-Concept mapping with Ollama'
    )
    parser.add_argument(
        '--use-ollama',
        action='store_true',
        help='Use Ollama for unmapped APIs'
    )
    parser.add_argument(
        '--unmapped-only',
        action='store_true',
        help='Only classify APIs not covered by rules'
    )
    parser.add_argument(
        '--sample',
        type=int,
        default=None,
        help='Process only N APIs (for testing)'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Show detailed progress'
    )
    parser.add_argument(
        '--min-confidence',
        type=float,
        default=0.6,
        help='Minimum confidence threshold for Ollama results'
    )
    
    args = parser.parse_args()
    
    # Load data
    print("📚 Loading data...")
    api_entities_df = pd.read_parquet('outputs/api_entities.parquet')
    doc_concepts_df = pd.read_parquet('outputs/doc_concepts.parquet')
    
    print(f"   {len(api_entities_df)} API entities")
    print(f"   {len(doc_concepts_df)} documentation sections")
    
    # Step 1: Co-occurrence mappings
    print("\n📊 Extracting co-occurrence mappings...")
    cooccurrence_df = extract_cooccurrence_mappings(doc_concepts_df)
    print(f"   Found {len(cooccurrence_df)} co-occurrence relationships")
    
    # Step 2: Namespace mappings
    print("\n🔗 Extracting namespace mappings...")
    namespace_df = extract_namespace_mappings(api_entities_df)
    print(f"   Found {len(namespace_df)} namespace relationships")
    
    # Combine rule-based mappings
    rule_based_df = pd.concat([cooccurrence_df, namespace_df], ignore_index=True)
    
    # Deduplicate (keep highest confidence)
    rule_based_df = (
        rule_based_df
        .sort_values('confidence', ascending=False)
        .drop_duplicates(subset=['api_id', 'concept_name'], keep='first')
    )
    
    print(f"\n📈 Rule-based mapping summary:")
    print(f"   Total relationships: {len(rule_based_df)}")
    print(f"   APIs covered: {rule_based_df['api_id'].nunique()}/{len(api_entities_df)}")
    print(f"   Coverage: {rule_based_df['api_id'].nunique() / len(api_entities_df) * 100:.1f}%")
    
    # Step 3: Ollama classification (optional)
    final_df = rule_based_df
    
    if args.use_ollama:
        # Identify unmapped APIs
        mapped_apis = set(rule_based_df['api_id'].unique())
        all_apis = set(api_entities_df['api_id'].unique())
        unmapped_apis = list(all_apis - mapped_apis)
        
        print(f"\n🎯 APIs needing Ollama classification: {len(unmapped_apis)}")
        
        # Sample if requested
        if args.sample:
            import random
            unmapped_apis = random.sample(unmapped_apis, min(args.sample, len(unmapped_apis)))
            print(f"   Processing sample: {len(unmapped_apis)} APIs")
        
        if unmapped_apis:
            # Classify with Ollama
            ollama_df = classify_with_ollama(
                api_entities_df,
                doc_concepts_df,
                unmapped_apis,
                verbose=args.verbose
            )
            
            # Filter by confidence
            ollama_df = ollama_df[ollama_df['confidence'] >= args.min_confidence]
            
            print(f"\n   Ollama results (confidence >= {args.min_confidence}):")
            print(f"   Added {len(ollama_df)} new relationships")
            print(f"   APIs classified: {ollama_df['api_id'].nunique()}")
            
            # Combine with rule-based
            final_df = pd.concat([rule_based_df, ollama_df], ignore_index=True)
    
    # Final statistics
    print(f"\n" + "="*70)
    print("FINAL MAPPING STATISTICS")
    print("="*70)
    print(f"Total relationships: {len(final_df)}")
    print(f"Unique APIs mapped: {final_df['api_id'].nunique()}/{len(api_entities_df)}")
    print(f"Coverage: {final_df['api_id'].nunique() / len(api_entities_df) * 100:.1f}%")
    print(f"Unique concepts: {final_df['concept_name'].nunique()}")
    
    print(f"\nSource breakdown:")
    print(final_df['source'].value_counts().to_string())
    
    print(f"\nTop 10 concepts by API count:")
    concept_counts = final_df.groupby('concept_name')['api_id'].nunique().sort_values(ascending=False)
    print(concept_counts.head(10).to_string())
    
    # Save results
    output_path = 'outputs/api_implements_concept.parquet'
    final_df.to_parquet(output_path, index=False)
    
    # Also save CSV for manual review
    csv_path = 'outputs/api_implements_concept.csv'
    final_df.to_csv(csv_path, index=False)
    
    print(f"\n✅ Results saved:")
    print(f"   {output_path}")
    print(f"   {csv_path}")
    
    print(f"\n💡 Next steps:")
    print(f"   1. Review {csv_path} for quality")
    print(f"   2. Run validation: python tools/validate_api_concepts.py")
    print(f"   3. Proceed to Phase 3: python scripts/03_cross_corpus_bridges.py")


if __name__ == '__main__':
    main()
