#!/usr/bin/env python3
""" MCP Server Capability Comparison Test

Compare capabilities between:
1. DevExpress public dxdocs MCP server (production)
2. Local XAF documentation analysis MCP adapter (your project)

This test helps validate whether your enhanced local analysis provides
value beyond what's available in the production MCP server.
"""

import sys
from pathlib import Path
import json

# Setup paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from tools.mcp_server_adapter import XAFDocAnalysis


def test_local_capabilities():
    """Test what the local MCP adapter can do."""
    
    print("=" * 80)
    print("TESTING LOCAL MCP ADAPTER CAPABILITIES")
    print("=" * 80)
    
    analyzer = XAFDocAnalysis()
    
    test_results = {}
    
    # Test 1: Concept Coverage Analysis
    print("\n📊 Test 1: Concept Coverage Analysis")
    print("-" * 80)
    try:
        result = analyzer.query_concept_coverage('Security System')
        test_results['concept_coverage'] = {
            'success': True,
            'total_sections': result['total_sections'],
            'conceptual_sections': result['conceptual_sections'],
            'api_sections': result['api_sections'],
            'platforms': result['platforms'],
            'avg_connections': result['avg_connections_per_section'],
            'isolated': result['isolated_sections']
        }
        print(f"✅ SUCCESS: Found {result['total_sections']} sections")
        print(f"   - Conceptual: {result['conceptual_sections']}")
        print(f"   - API: {result['api_sections']}")
        print(f"   - Platforms: {', '.join(result['platforms'])}")
        print(f"   - Avg connections: {result['avg_connections_per_section']:.1f}")
    except Exception as e:
        test_results['concept_coverage'] = {'success': False, 'error': str(e)}
        print(f"❌ FAILED: {e}")
    
    # Test 2: Documentation Gaps
    print("\n🔍 Test 2: Documentation Gap Detection")
    print("-" * 80)
    try:
        result = analyzer.get_documentation_gaps()
        test_results['gap_detection'] = {
            'success': True,
            'total_analyzed': result['total_concepts_analyzed'],
            'gaps_found': result['gaps_found'],
            'gap_types': [g['gap_type'] for g in result['gap_details']]
        }
        print(f"✅ SUCCESS: Analyzed {result['total_concepts_analyzed']} concepts")
        print(f"   - Gaps found: {result['gaps_found']}")
        if result['gap_details']:
            for gap in result['gap_details'][:3]:
                print(f"   - {gap['concept']}: {gap['gap_type']} (priority: {gap['priority']})")
    except Exception as e:
        test_results['gap_detection'] = {'success': False, 'error': str(e)}
        print(f"❌ FAILED: {e}")
    
    # Test 3: Ticket Priorities
    print("\n🎫 Test 3: Ticket-Based Priority Analysis")
    print("-" * 80)
    try:
        result = analyzer.get_ticket_priorities(top_n=5)
        test_results['ticket_priorities'] = {
            'success': True,
            'total_concepts': result['total_concepts'],
            'avg_ticket_count': result['average_ticket_count']
        }
        print(f"✅ SUCCESS: {result['total_concepts']} prioritized concepts")
        print(f"   - Avg ticket count: {result['average_ticket_count']}")
        for priority in result['ticket_priorities']:
            print(f"   - {priority['concept']}: {priority['ticket_count']} tickets (rank #{priority['priority_rank']})")
    except Exception as e:
        test_results['ticket_priorities'] = {'success': False, 'error': str(e)}
        print(f"❌ FAILED: {e}")
    
    # Test 4: Cross-Linking Recommendations
    print("\n🔗 Test 4: Cross-Linking Recommendations")
    print("-" * 80)
    try:
        result = analyzer.get_crosslink_recommendations(limit=5)
        if 'error' in result:
            test_results['cross_linking'] = {'success': False, 'error': result['error']}
            print(f"⚠️  WARNING: {result['error']}")
        else:
            test_results['cross_linking'] = {
                'success': True,
                'total_recommendations': result['total_recommendations']
            }
            print(f"✅ SUCCESS: {result['total_recommendations']} recommendations")
            for rec in result['recommendations'][:3]:
                apis_desc = f"{rec.get('num_useful_apis', 0)} APIs ({rec.get('num_high_priority_apis', 0)} high priority)"
                print(f"   - {rec.get('title', 'N/A')}: {apis_desc}")
                print(f"      Score: {rec.get('realistic_score', 0):.1f}, Ticket weight: {rec.get('ticket_weight', 0):.2f}x")
    except Exception as e:
        test_results['cross_linking'] = {'success': False, 'error': str(e)}
        print(f"❌ FAILED: {e}")
    
    # Test 5: API-to-Concept Mappings
    print("\n🔌 Test 5: API-to-Concept Mappings (Custom Data)")
    print("-" * 80)
    try:
        # This data doesn't exist in dxdocs
        import pandas as pd
        apis = pd.read_parquet(PROJECT_ROOT / 'outputs' / 'api_implements_concept.parquet')
        test_results['api_concept_mapping'] = {
            'success': True,
            'total_mappings': len(apis),
            'unique_apis': apis['api_id'].nunique(),
            'unique_concepts': apis['concept_name'].nunique()
        }
        print(f"✅ SUCCESS: Custom API-concept analysis available")
        print(f"   - Total mappings: {len(apis):,}")
        print(f"   - Unique APIs: {apis['api_id'].nunique():,}")
        print(f"   - Unique concepts: {apis['concept_name'].nunique()}")
        
        # Show some high-confidence mappings
        high_conf = apis[apis['confidence'] > 0.8].sort_values('count', ascending=False).head(3)
        print(f"   - High-confidence examples:")
        for _, row in high_conf.iterrows():
            print(f"      • {row['api_id']} → {row['concept_name']} (conf: {row['confidence']:.2f}, count: {row['count']})")
    except Exception as e:
        test_results['api_concept_mapping'] = {'success': False, 'error': str(e)}
        print(f"❌ FAILED: {e}")
    
    # Test 6: Semantic Connections
    print("\n🕸️  Test 6: Semantic Connection Graph")
    print("-" * 80)
    try:
        pairs = analyzer.data['semantic_pairs']
        test_results['semantic_graph'] = {
            'success': True,
            'total_connections': len(pairs),
            'unique_sources': len(pairs['source_id'].unique()) if 'source_id' in pairs.columns else 'N/A'
        }
        print(f"✅ SUCCESS: Semantic graph available")
        print(f"   - Total connections: {len(pairs):,}")
        if 'neighbor_type' in pairs.columns:
            type_dist = pairs['neighbor_type'].value_counts().head(5)
            print(f"   - Connection types:")
            for conn_type, count in type_dist.items():
                print(f"      • {conn_type}: {count:,}")
    except Exception as e:
        test_results['semantic_graph'] = {'success': False, 'error': str(e)}
        print(f"❌ FAILED: {e}")
    
    return test_results


def print_comparison_summary(test_results):
    """Print comparison between local capabilities and dxdocs."""
    
    print("\n" + "=" * 80)
    print("CAPABILITY COMPARISON: Local MCP vs dxdocs MCP")
    print("=" * 80)
    
    capabilities = [
        {
            'name': 'Concept Coverage Analysis',
            'local': test_results.get('concept_coverage', {}).get('success', False),
            'dxdocs': True,  # dxdocs can search by concept
            'local_advantage': 'Quantitative metrics (connections, sections, platforms)',
            'dxdocs_advantage': 'Full document content, better for reading'
        },
        {
            'name': 'Gap Detection',
            'local': test_results.get('gap_detection', {}).get('success', False),
            'dxdocs': False,  # dxdocs cannot identify gaps
            'local_advantage': 'Identifies missing/disconnected docs proactively',
            'dxdocs_advantage': 'N/A'
        },
        {
            'name': 'Ticket-Based Priorities',
            'local': test_results.get('ticket_priorities', {}).get('success', False),
            'dxdocs': False,  # dxdocs has no ticket data
            'local_advantage': 'Customer pain point prioritization',
            'dxdocs_advantage': 'N/A'
        },
        {
            'name': 'Cross-Linking Recommendations',
            'local': test_results.get('cross_linking', {}).get('success', False),
            'dxdocs': False,  # dxdocs cannot recommend links
            'local_advantage': 'Actionable doc improvement tasks with ticket priorities',
            'dxdocs_advantage': 'N/A'
        },
        {
            'name': 'API-to-Concept Mappings',
            'local': test_results.get('api_concept_mapping', {}).get('success', False),
            'dxdocs': False,  # dxdocs has APIs and concepts but no explicit mapping
            'local_advantage': 'Structured API→Concept relationships',
            'dxdocs_advantage': 'N/A'
        },
        {
            'name': 'Semantic Connection Graph',
            'local': test_results.get('semantic_graph', {}).get('success', False),
            'dxdocs': False,  # dxdocs uses vector search but doesn't expose graph
            'local_advantage': 'Document relationship analysis',
            'dxdocs_advantage': 'N/A'
        },
        {
            'name': 'Full Document Content',
            'local': False,  # Local has sections/concepts but not full markdown
            'dxdocs': True,
            'local_advantage': 'N/A',
            'dxdocs_advantage': 'Can read full articles, format preserved'
        },
        {
            'name': 'Natural Language Search',
            'local': False,  # Local has structured queries only
            'dxdocs': True,
            'local_advantage': 'N/A',
            'dxdocs_advantage': 'Semantic vector search, conversational'
        },
        {
            'name': 'Code Examples',
            'local': True,  # Local has code_blocks field
            'dxdocs': True,
            'local_advantage': 'Structured analysis of code presence',
            'dxdocs_advantage': 'Formatted code with syntax highlighting'
        }
    ]
    
    print("\n| Capability | Local | dxdocs | Winner |")
    print("|------------|-------|--------|--------|")
    
    for cap in capabilities:
        local_status = "✅" if cap['local'] else "❌"
        dxdocs_status = "✅" if cap['dxdocs'] else "❌"
        
        if cap['local'] and not cap['dxdocs']:
            winner = "**LOCAL**"
        elif cap['dxdocs'] and not cap['local']:
            winner = "**DXDOCS**"
        elif cap['local'] and cap['dxdocs']:
            winner = "Both"
        else:
            winner = "Neither"
        
        print(f"| {cap['name']} | {local_status} | {dxdocs_status} | {winner} |")
    
    print("\n" + "=" * 80)
    print("LOCAL MCP UNIQUE VALUE PROPOSITIONS")
    print("=" * 80)
    
    unique_capabilities = [cap for cap in capabilities if cap['local'] and not cap['dxdocs']]
    
    for i, cap in enumerate(unique_capabilities, 1):
        print(f"\n{i}. **{cap['name']}**")
        print(f"   Advantage: {cap['local_advantage']}")
    
    print("\n" + "=" * 80)
    print("DXDOCS MCP ADVANTAGES")
    print("=" * 80)
    
    dxdocs_capabilities = [cap for cap in capabilities if cap['dxdocs'] and not cap['local']]
    
    for i, cap in enumerate(dxdocs_capabilities, 1):
        print(f"\n{i}. **{cap['name']}**")
        print(f"   Advantage: {cap['dxdocs_advantage']}")
    
    print("\n" + "=" * 80)
    print("RECOMMENDATION: IS YOUR PROJECT VIABLE?")
    print("=" * 80)
    
    local_unique = len([c for c in capabilities if c['local'] and not c['dxdocs']])
    total_tested = len([t for t in test_results.values() if t.get('success')])
    
    print(f"\n✅ Local MCP has {local_unique} unique capabilities")
    print(f"✅ {total_tested}/{len(test_results)} tests passed")
    
    if local_unique >= 3:
        print("\n🎯 **VERDICT: YES, YOUR PROJECT IS VIABLE**")
        print("\nReasons:")
        print("1. Provides analytical capabilities dxdocs cannot offer")
        print("2. Enables proactive documentation improvement (gap detection)")
        print("3. Prioritizes work based on customer pain (ticket analysis)")
        print("4. Actionable recommendations for doc team (cross-linking)")
        print("5. Structured API-concept mapping for ontology building")
        print("\n💡 **USE CASE SEPARATION**:")
        print("   - dxdocs MCP: For developers CONSUMING documentation")
        print("   - Your MCP: For doc team IMPROVING documentation")
    else:
        print("\n⚠️  **VERDICT: PROJECT NEEDS MORE DIFFERENTIATION**")
        print("\nTo be viable, add more unique capabilities")
    
    return local_unique >= 3


if __name__ == '__main__':
    print("\n🧪 XAF Documentation MCP Capability Comparison Test")
    print("=" * 80)
    
    # Test local capabilities
    test_results = test_local_capabilities()
    
    # Print comparison
    is_viable = print_comparison_summary(test_results)
    
    # Save results
    output_file = PROJECT_ROOT / 'outputs' / 'mcp_comparison_test_results.json'
    with open(output_file, 'w') as f:
        json.dump({
            'test_results': test_results,
            'is_viable': is_viable,
            'unique_capabilities_count': len([c for c in test_results.values() if c.get('success')])
        }, f, indent=2, default=str)
    
    print(f"\n📄 Results saved to: {output_file}")
    print("\n" + "=" * 80)
    print("✅ Comparison test complete!")
    print("=" * 80)
    
    sys.exit(0 if is_viable else 1)
