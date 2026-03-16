#!/usr/bin/env python3
"""
Phase 9: Track Concept Quality Metrics Over Time

Monitors key indicators to detect noise and validate concept vocabulary quality.
Run this after each concepts.yml update to track improvements.

Metrics tracked:
1. Concept coverage and specificity
2. Concept connectivity ratios
3. Gate passage quality
4. Co-occurrence patterns
5. Isolated sections
"""

import argparse
from pathlib import Path
import pandas as pd
import numpy as np
from datetime import datetime


def safe_list(val):
    """Handle numpy arrays from parquet"""
    if val is None or (isinstance(val, float) and pd.isna(val)):
        return []
    if isinstance(val, (list, tuple)):
        return list(val)
    if hasattr(val, '__iter__') and not isinstance(val, str):
        return list(val)
    return []


def load_data():
    """Load all analysis outputs"""
    concepts = pd.read_parquet('outputs/doc_concepts.parquet')
    concepts = concepts[concepts['kept'] == True].copy()
    
    pairs = pd.read_parquet('outputs/semantic_pairs.parquet')
    
    return concepts, pairs


def metric_1_concept_coverage(concepts_df):
    """
    Measure concept coverage and specificity
    
    Returns dict with:
    - total_sections
    - tagged_sections
    - coverage_percent
    - concepts_used
    - sections_per_concept (distribution)
    """
    total = len(concepts_df)
    
    # Count sections with at least one concept
    has_concepts = concepts_df['concepts'].apply(lambda c: len(safe_list(c)) > 0)
    tagged = has_concepts.sum()
    
    # Count sections per concept
    all_concepts = []
    for concept_list in concepts_df['concepts']:
        all_concepts.extend(safe_list(concept_list))
    
    concept_counts = pd.Series(all_concepts).value_counts()
    
    return {
        'total_sections': total,
        'tagged_sections': int(tagged),
        'coverage_percent': round(tagged / total * 100, 1),
        'unique_concepts_used': len(concept_counts),
        'avg_sections_per_concept': round(concept_counts.mean(), 1),
        'median_sections_per_concept': int(concept_counts.median()),
        'min_sections': int(concept_counts.min()),
        'max_sections': int(concept_counts.max()),
        'concepts_under_20': int((concept_counts < 20).sum()),
        'concepts_over_500': int((concept_counts > 500).sum()),
        'concept_distribution': concept_counts.to_dict()
    }


def metric_2_concept_connectivity(concepts_df, pairs_df):
    """
    Calculate average semantic links per section, grouped by concept
    
    Returns dict mapping concept -> connectivity_ratio
    """
    # Build connections dict
    connections = {}
    for _, row in pairs_df.iterrows():
        src = (row['source_doc'], row['source_section'])
        tgt = (row['target_doc'], row['target_section'])
        connections[src] = connections.get(src, 0) + 1
        connections[tgt] = connections.get(tgt, 0) + 1
    
    # Count by concept
    concept_stats = {}
    
    all_concepts = set()
    for concept_list in concepts_df['concepts']:
        all_concepts.update(safe_list(concept_list))
    
    for concept in all_concepts:
        # Get sections with this concept
        mask = concepts_df['concepts'].apply(lambda c: concept in safe_list(c))
        sections_with_concept = concepts_df[mask]
        
        # Count their connections
        total_connections = 0
        for _, row in sections_with_concept.iterrows():
            key = (row['doc_id'], row['section_id'])
            total_connections += connections.get(key, 0)
        
        num_sections = len(sections_with_concept)
        avg_connections = total_connections / num_sections if num_sections > 0 else 0
        
        concept_stats[concept] = {
            'num_sections': num_sections,
            'total_connections': total_connections,
            'avg_connections_per_section': round(avg_connections, 1)
        }
    
    return concept_stats


def metric_3_gate_quality(pairs_df):
    """
    Analyze gate passage rates and similarity scores
    
    Detects if gates are becoming too loose or too strict
    """
    total_pairs = len(pairs_df)
    
    # Count gate passages
    all_gates = []
    for gates in pairs_df['gates_passed']:
        all_gates.extend(safe_list(gates))
    
    gate_counts = pd.Series(all_gates).value_counts()
    
    # Similarity scores by gate type
    gate_similarity = {}
    for gate_name in gate_counts.index:
        mask = pairs_df['gates_passed'].apply(lambda g: gate_name in safe_list(g))
        avg_sim = pairs_df[mask]['sim_score'].mean()
        gate_similarity[gate_name] = round(avg_sim, 3)
    
    # Overall similarity stats
    similarity_stats = {
        'mean': round(pairs_df['sim_score'].mean(), 3),
        'median': round(pairs_df['sim_score'].median(), 3),
        'std': round(pairs_df['sim_score'].std(), 3),
        'min': round(pairs_df['sim_score'].min(), 3),
        'max': round(pairs_df['sim_score'].max(), 3)
    }
    
    # Calculate fallback percentage (red flag if high)
    fallback_count = gate_counts.get('high_similarity_fallback', 0)
    fallback_pct = fallback_count / total_pairs * 100 if total_pairs > 0 else 0
    
    return {
        'total_pairs': total_pairs,
        'gate_passages': gate_counts.to_dict(),
        'gate_percentages': {k: round(v/total_pairs*100, 1) for k, v in gate_counts.items()},
        'avg_similarity_by_gate': gate_similarity,
        'overall_similarity': similarity_stats,
        'fallback_percentage': round(fallback_pct, 1),
        'quality_flag': '🔴 HIGH FALLBACK' if fallback_pct > 5 else '🟢 HEALTHY' if fallback_pct < 2 else '🟡 WATCH'
    }


def metric_4_concept_cooccurrence(concepts_df, top_n=10):
    """
    Identify which concepts frequently appear together
    
    Helps validate concept relationships and detect noise
    """
    # Build co-occurrence matrix
    cooccurrence = {}
    
    for _, row in concepts_df.iterrows():
        concepts = safe_list(row['concepts'])
        
        # Count pairs
        for i, concept1 in enumerate(concepts):
            for concept2 in concepts[i+1:]:
                pair = tuple(sorted([concept1, concept2]))
                cooccurrence[pair] = cooccurrence.get(pair, 0) + 1
    
    # Sort by frequency
    sorted_pairs = sorted(cooccurrence.items(), key=lambda x: x[1], reverse=True)
    
    return {
        'top_cooccurrences': [
            {'concepts': list(pair), 'count': count}
            for pair, count in sorted_pairs[:top_n]
        ],
        'total_unique_pairs': len(cooccurrence)
    }


def metric_5_isolated_content(concepts_df, pairs_df):
    """
    Identify isolated sections and concepts with poor connectivity
    """
    # Find connected sections
    connected = set()
    for _, row in pairs_df.iterrows():
        connected.add((row['source_doc'], row['source_section']))
        connected.add((row['target_doc'], row['target_section']))
    
    # Count isolated
    all_sections = set(zip(concepts_df['doc_id'], concepts_df['section_id']))
    isolated = all_sections - connected
    
    isolated_pct = len(isolated) / len(all_sections) * 100 if all_sections else 0
    
    # Which concepts appear in isolated sections most?
    isolated_concepts = []
    for doc_id, section_id in isolated:
        row = concepts_df[(concepts_df['doc_id'] == doc_id) & 
                          (concepts_df['section_id'] == section_id)]
        if not row.empty:
            isolated_concepts.extend(safe_list(row.iloc[0]['concepts']))
    
    isolated_concept_counts = pd.Series(isolated_concepts).value_counts()
    
    return {
        'total_sections': len(all_sections),
        'isolated_sections': len(isolated),
        'isolated_percentage': round(isolated_pct, 1),
        'quality_flag': '🔴 HIGH ISOLATION' if isolated_pct > 10 else '🟢 HEALTHY' if isolated_pct < 5 else '🟡 WATCH',
        'concepts_in_isolated_sections': isolated_concept_counts.head(10).to_dict()
    }


def generate_report(metrics, output_file=None):
    """Generate comprehensive quality report"""
    
    report = []
    report.append("="*80)
    report.append("CONCEPT QUALITY METRICS REPORT")
    report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("="*80)
    
    # Metric 1: Coverage
    report.append("\n📊 METRIC 1: CONCEPT COVERAGE & SPECIFICITY")
    report.append("-"*80)
    cov = metrics['coverage']
    report.append(f"Total sections: {cov['total_sections']}")
    report.append(f"Tagged sections: {cov['tagged_sections']} ({cov['coverage_percent']}%)")
    report.append(f"Unique concepts used: {cov['unique_concepts_used']}")
    report.append(f"Avg sections per concept: {cov['avg_sections_per_concept']}")
    report.append(f"Median sections per concept: {cov['median_sections_per_concept']}")
    report.append(f"Range: {cov['min_sections']} - {cov['max_sections']}")
    
    # Quality flags
    if cov['concepts_under_20'] > 0:
        report.append(f"⚠️  {cov['concepts_under_20']} concepts have <20 sections (too specific?)")
    if cov['concepts_over_500'] > 0:
        report.append(f"⚠️  {cov['concepts_over_500']} concepts have >500 sections (too generic?)")
    
    # Top/bottom concepts
    dist = cov['concept_distribution']
    report.append(f"\nTop 10 most common concepts:")
    for concept, count in sorted(dist.items(), key=lambda x: x[1], reverse=True)[:10]:
        report.append(f"  {concept:40} {count:>4} sections")
    
    report.append(f"\nBottom 10 least common concepts:")
    for concept, count in sorted(dist.items(), key=lambda x: x[1])[:10]:
        report.append(f"  {concept:40} {count:>4} sections")
    
    # Metric 2: Connectivity
    report.append("\n\n🔗 METRIC 2: CONCEPT CONNECTIVITY RATIOS")
    report.append("-"*80)
    conn = metrics['connectivity']
    
    # Sort by connectivity
    sorted_conn = sorted(conn.items(), key=lambda x: x[1]['avg_connections_per_section'])
    
    report.append("LOWEST CONNECTIVITY (Potential noise or gaps):")
    for concept, stats in sorted_conn[:10]:
        avg_conn = stats['avg_connections_per_section']
        flag = "🔴" if avg_conn < 5 else "🟡" if avg_conn < 8 else "🟢"
        report.append(f"  {flag} {concept:40} {avg_conn:>5.1f} links/section ({stats['num_sections']} sections)")
    
    report.append("\nHIGHEST CONNECTIVITY (Reference models):")
    for concept, stats in sorted_conn[-10:]:
        avg_conn = stats['avg_connections_per_section']
        flag = "🔵" if avg_conn > 12 else "🟢"
        report.append(f"  {flag} {concept:40} {avg_conn:>5.1f} links/section ({stats['num_sections']} sections)")
    
    # Metric 3: Gate Quality
    report.append("\n\n🚪 METRIC 3: SEMANTIC GATE QUALITY")
    report.append("-"*80)
    gate = metrics['gate_quality']
    report.append(f"Total semantic pairs: {gate['total_pairs']}")
    report.append(f"Overall quality: {gate['quality_flag']}")
    report.append(f"Fallback usage: {gate['fallback_percentage']}%")
    
    report.append("\nGate passage rates:")
    for gate_name, pct in sorted(gate['gate_percentages'].items(), key=lambda x: x[1], reverse=True):
        count = gate['gate_passages'][gate_name]
        avg_sim = gate['avg_similarity_by_gate'].get(gate_name, 0)
        report.append(f"  {gate_name:30} {pct:>5.1f}% ({count:>6} pairs, avg sim: {avg_sim:.3f})")
    
    sim = gate['overall_similarity']
    report.append(f"\nOverall similarity distribution:")
    report.append(f"  Mean: {sim['mean']:.3f}  Median: {sim['median']:.3f}  Std: {sim['std']:.3f}")
    report.append(f"  Range: {sim['min']:.3f} - {sim['max']:.3f}")
    
    # Metric 4: Co-occurrence
    report.append("\n\n🔀 METRIC 4: CONCEPT CO-OCCURRENCE PATTERNS")
    report.append("-"*80)
    cooc = metrics['cooccurrence']
    report.append(f"Total unique concept pairs: {cooc['total_unique_pairs']}")
    report.append("\nTop 10 co-occurring concept pairs:")
    for pair_info in cooc['top_cooccurrences']:
        concepts = pair_info['concepts']
        count = pair_info['count']
        report.append(f"  {concepts[0]:30} + {concepts[1]:30} {count:>4}x")
    
    # Metric 5: Isolation
    report.append("\n\n🏝️  METRIC 5: ISOLATED CONTENT ANALYSIS")
    report.append("-"*80)
    iso = metrics['isolation']
    report.append(f"Total sections: {iso['total_sections']}")
    report.append(f"Isolated sections: {iso['isolated_sections']} ({iso['isolated_percentage']}%)")
    report.append(f"Quality flag: {iso['quality_flag']}")
    
    if iso['concepts_in_isolated_sections']:
        report.append("\nConcepts frequently appearing in isolated sections:")
        for concept, count in iso['concepts_in_isolated_sections'].items():
            report.append(f"  {concept:40} {count:>4} isolated sections")
    
    # Overall assessment
    report.append("\n\n" + "="*80)
    report.append("📈 OVERALL QUALITY ASSESSMENT")
    report.append("="*80)
    
    flags = []
    if cov['coverage_percent'] < 70:
        flags.append("🔴 Low concept coverage - add more concepts")
    if cov['concepts_over_500'] > 3:
        flags.append("🔴 Too many generic concepts - split into sub-concepts")
    if gate['fallback_percentage'] > 5:
        flags.append("🔴 High fallback usage - gates too strict OR concepts too sparse")
    if iso['isolated_percentage'] > 10:
        flags.append("🔴 High isolation - documentation gaps or poor concept coverage")
    
    if not flags:
        report.append("✅ Overall quality is GOOD - no major red flags")
    else:
        report.append("⚠️  Action items:")
        for flag in flags:
            report.append(f"  {flag}")
    
    report_text = "\n".join(report)
    
    # Print to console
    print(report_text)
    
    # Save to file if requested
    if output_file:
        Path(output_file).write_text(report_text, encoding='utf-8')
        print(f"\n✅ Report saved to: {output_file}")
    
    return report_text


def main():
    parser = argparse.ArgumentParser(
        description='Track concept quality metrics over time'
    )
    parser.add_argument(
        '--output',
        default='outputs/concept_quality_report.txt',
        help='Output report file'
    )
    parser.add_argument(
        '--json',
        default='outputs/concept_quality_metrics.json',
        help='JSON metrics file for tracking over time'
    )
    
    args = parser.parse_args()
    
    print("Loading data...")
    concepts_df, pairs_df = load_data()
    
    print("Calculating metrics...")
    metrics = {
        'timestamp': datetime.now().isoformat(),
        'coverage': metric_1_concept_coverage(concepts_df),
        'connectivity': metric_2_concept_connectivity(concepts_df, pairs_df),
        'gate_quality': metric_3_gate_quality(pairs_df),
        'cooccurrence': metric_4_concept_cooccurrence(concepts_df),
        'isolation': metric_5_isolated_content(concepts_df, pairs_df)
    }
    
    # Generate report
    generate_report(metrics, output_file=args.output)
    
    # Save JSON for tracking
    import json
    Path(args.json).write_text(json.dumps(metrics, indent=2), encoding='utf-8')
    print(f"✅ Metrics saved to: {args.json}")


if __name__ == '__main__':
    main()
