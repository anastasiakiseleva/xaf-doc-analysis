"""
Validate Ticket-to-Concept Mapping Quality

This tool:
1. Compares current mapping results against ticket_language_map.yml
2. Validates API name associations
3. Identifies gaps between user language and concept synonyms
4. Generates recommendations for synonym additions

Usage:
    python tools/ticket_discoverability/validate_ticket_mapping.py
    python tools/ticket_discoverability/validate_ticket_mapping.py --baseline baseline.json
"""

import json
import yaml
from pathlib import Path
from typing import Dict, List, Tuple
import sys
from datetime import datetime

def load_translation_map(path: str = 'config/ticket_language_map.yml') -> Dict:
    """Load the ticket language translation map."""
    with open(path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        return data['translation_map']


def load_ticket_mapping(path: str = 'outputs/ticket_discoverability/ticket_feature_to_concept_mapping.csv') -> List[Dict]:
    """Load current ticket-to-concept mappings."""
    import csv
    mappings = []
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            mappings.append({
                'feature_category': row['feature_category'],
                'ticket_count': int(row['ticket_count']),
                'primary_concept': row['primary_concept'],
                'confidence': int(row['confidence'])
            })
    return mappings


def load_concepts(path: str = 'config/concepts.yml') -> Dict[str, Dict]:
    """Load concept definitions indexed by name."""
    with open(path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        concepts = {}
        for concept in data.get('concepts', []):
            concepts[concept['name']] = concept
        return concepts


def validate_mapping(translation_map: List[Dict], ticket_mappings: List[Dict], concepts: Dict) -> Dict:
    """
    Validate current mappings against the translation map.
    Returns validation report with recommendations.
    """
    validation_results = {
        'timestamp': datetime.now().isoformat(),
        'validated_mappings': [],
        'synonym_gaps': [],
        'confidence_issues': [],
        'summary': {}
    }
    
    # Index translation map by ticket category
    trans_map_index = {item['ticket_category']: item for item in translation_map}
    
    high_confidence_count = 0
    medium_confidence_count = 0
    low_confidence_count = 0
    
    for mapping in ticket_mappings:
        category = mapping['feature_category']
        concept = mapping['primary_concept']
        confidence = mapping['confidence']
        
        # Track confidence distribution
        if confidence >= 10:
            high_confidence_count += 1
        elif confidence >= 7:
            medium_confidence_count += 1
        else:
            low_confidence_count += 1
        
        # Check if this category is in translation map
        if category in trans_map_index:
            trans_entry = trans_map_index[category]
            expected_concepts = trans_entry['mapped_concepts']
            user_phrases = trans_entry['user_phrases']
            
            # Validate mapping matches translation map
            is_valid = concept in expected_concepts
            
            result = {
                'ticket_category': category,
                'ticket_count': mapping['ticket_count'],
                'current_concept': concept,
                'expected_concepts': expected_concepts,
                'confidence': confidence,
                'is_valid': is_valid,
                'user_phrases': user_phrases
            }
            
            # Check if user phrases are in concept synonyms
            if concept in concepts:
                concept_def = concepts[concept]
                synonyms = [s.lower() for s in concept_def.get('synonyms', [])]
                missing_phrases = []
                
                for phrase in user_phrases:
                    # Check if any word from phrase is in synonyms
                    phrase_lower = phrase.lower()
                    if not any(phrase_lower in syn or syn in phrase_lower for syn in synonyms):
                        missing_phrases.append(phrase)
                
                if missing_phrases:
                    validation_results['synonym_gaps'].append({
                        'concept': concept,
                        'ticket_category': category,
                        'ticket_count': mapping['ticket_count'],
                        'missing_phrases': missing_phrases,
                        'current_synonyms': concept_def.get('synonyms', []),
                        'recommendation': f"Add synonyms: {', '.join(missing_phrases[:3])}"
                    })
            
            validation_results['validated_mappings'].append(result)
        
        # Flag low confidence mappings for review
        if confidence < 7:
            validation_results['confidence_issues'].append({
                'ticket_category': category,
                'ticket_count': mapping['ticket_count'],
                'current_concept': concept,
                'confidence': confidence,
                'recommendation': 'Review mapping or add more synonyms'
            })
    
    # Calculate summary statistics
    total_categories = len(ticket_mappings)
    validation_results['summary'] = {
        'total_categories': total_categories,
        'high_confidence_10': high_confidence_count,
        'medium_confidence_7_9': medium_confidence_count,
        'low_confidence_below_7': low_confidence_count,
        'high_confidence_pct': f"{(high_confidence_count / total_categories) * 100:.1f}%",
        'synonym_gaps_found': len(validation_results['synonym_gaps']),
        'low_confidence_requiring_review': len(validation_results['confidence_issues']),
        'categories_in_translation_map': len([m for m in ticket_mappings if m['feature_category'] in trans_map_index])
    }
    
    return validation_results


def generate_html_report(validation_results: Dict, output_path: str):
    """Generate HTML validation report."""
    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Ticket Mapping Validation Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        h1 {{ color: #2c3e50; }}
        h2 {{ color: #34495e; margin-top: 30px; }}
        .summary {{ background: #ecf0f1; padding: 15px; border-radius: 5px; }}
        .metric {{ display: inline-block; margin: 10px 20px 10px 0; }}
        .metric-value {{ font-size: 24px; font-weight: bold; color: #3498db; }}
        .metric-label {{ font-size: 14px; color: #7f8c8d; }}
        table {{ border-collapse: collapse; width: 100%; margin-top: 15px; }}
        th {{ background: #3498db; color: white; padding: 10px; text-align: left; }}
        td {{ padding: 8px; border-bottom: 1px solid #ddd; }}
        tr:hover {{ background: #f5f5f5; }}
        .high-priority {{ background: #ffe5e5; }}
        .recommendation {{ color: #27ae60; font-weight: bold; }}
        .gap-list {{ color: #e74c3c; }}
    </style>
</head>
<body>
    <h1>Ticket-to-Concept Mapping Validation Report</h1>
    <p><strong>Generated:</strong> {validation_results['timestamp']}</p>
    
    <div class="summary">
        <h2>Summary Statistics</h2>
        <div class="metric">
            <div class="metric-value">{validation_results['summary']['total_categories']}</div>
            <div class="metric-label">Total Categories</div>
        </div>
        <div class="metric">
            <div class="metric-value">{validation_results['summary']['high_confidence_10']}</div>
            <div class="metric-label">High Confidence (10)</div>
        </div>
        <div class="metric">
            <div class="metric-value">{validation_results['summary']['medium_confidence_7_9']}</div>
            <div class="metric-label">Medium Confidence (7-9)</div>
        </div>
        <div class="metric">
            <div class="metric-value">{validation_results['summary']['low_confidence_below_7']}</div>
            <div class="metric-label">Low Confidence (<7)</div>
        </div>
        <div class="metric">
            <div class="metric-value">{validation_results['summary']['high_confidence_pct']}</div>
            <div class="metric-label">High Confidence %</div>
        </div>
    </div>
    
    <h2>Synonym Gaps ({len(validation_results['synonym_gaps'])} found)</h2>
    <p>User phrases from tickets that are missing from concept synonyms:</p>
    <table>
        <tr>
            <th>Concept</th>
            <th>Ticket Category</th>
            <th>Volume</th>
            <th>Missing Phrases</th>
            <th>Recommendation</th>
        </tr>
"""
    
    for gap in sorted(validation_results['synonym_gaps'], key=lambda x: x['ticket_count'], reverse=True):
        html += f"""
        <tr class="high-priority">
            <td><strong>{gap['concept']}</strong></td>
            <td>{gap['ticket_category']}</td>
            <td>{gap['ticket_count']}</td>
            <td class="gap-list">{', '.join(gap['missing_phrases'])}</td>
            <td class="recommendation">{gap['recommendation']}</td>
        </tr>
"""
    
    html += """
    </table>
    
    <h2>Low Confidence Mappings ({} requiring review)</h2>
    <p>Categories with confidence scores below 7 that need attention:</p>
    <table>
        <tr>
            <th>Ticket Category</th>
            <th>Volume</th>
            <th>Current Concept</th>
            <th>Confidence</th>
            <th>Recommendation</th>
        </tr>
""".format(len(validation_results['confidence_issues']))
    
    for issue in sorted(validation_results['confidence_issues'], key=lambda x: x['ticket_count'], reverse=True):
        html += f"""
        <tr>
            <td><strong>{issue['ticket_category']}</strong></td>
            <td>{issue['ticket_count']}</td>
            <td>{issue['current_concept']}</td>
            <td>{issue['confidence']}</td>
            <td class="recommendation">{issue['recommendation']}</td>
        </tr>
"""
    
    html += """
    </table>
</body>
</html>
"""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)


def main():
    print("=" * 80)
    print("TICKET MAPPING VALIDATION")
    print("=" * 80)
    print()
    
    # Load data
    print("📊 Loading data...")
    translation_map = load_translation_map()
    ticket_mappings = load_ticket_mapping()
    concepts = load_concepts()
    
    print(f"   ✓ Loaded {len(translation_map)} translation map entries")
    print(f"   ✓ Loaded {len(ticket_mappings)} ticket mappings")
    print(f"   ✓ Loaded {len(concepts)} concept definitions")
    print()
    
    # Validate
    print("🔍 Validating mappings...")
    results = validate_mapping(translation_map, ticket_mappings, concepts)
    print()
    
    # Display summary
    print("=" * 80)
    print("VALIDATION SUMMARY")
    print("=" * 80)
    print()
    print(f"Total Categories Analyzed: {results['summary']['total_categories']}")
    print(f"High Confidence (10): {results['summary']['high_confidence_10']} ({results['summary']['high_confidence_pct']})")
    print(f"Medium Confidence (7-9): {results['summary']['medium_confidence_7_9']}")
    print(f"Low Confidence (<7): {results['summary']['low_confidence_below_7']}")
    print()
    print(f"✅ Synonym Gaps Found: {results['summary']['synonym_gaps_found']}")
    print(f"⚠️  Low Confidence Requiring Review: {results['summary']['low_confidence_requiring_review']}")
    print()
    
    # Save outputs
    print("=" * 80)
    print("SAVING OUTPUTS")
    print("=" * 80)
    print()
    
    # Save JSON report
    json_path = 'outputs/ticket_discoverability/mapping_validation.json'
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    print(f"  ✓ {json_path}")
    
    # Save HTML report
    html_path = 'outputs/ticket_discoverability/mapping_validation.html'
    generate_html_report(results, html_path)
    print(f"  ✓ {html_path}")
    print()
    
    # Display top synonym gap recommendations
    if results['synonym_gaps']:
        print("=" * 80)
        print("TOP 5 SYNONYM GAP RECOMMENDATIONS")
        print("=" * 80)
        print()
        for gap in sorted(results['synonym_gaps'], key=lambda x: x['ticket_count'], reverse=True)[:5]:
            print(f"📌 {gap['concept']} ({gap['ticket_count']} tickets)")
            print(f"   Category: {gap['ticket_category']}")
            print(f"   Missing: {', '.join(gap['missing_phrases'][:3])}")
            print(f"   ➜ {gap['recommendation']}")
            print()
    
    print("✅ Validation complete! Open mapping_validation.html to view full report.")
    print()


if __name__ == '__main__':
    main()
