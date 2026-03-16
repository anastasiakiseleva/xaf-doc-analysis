#!/usr/bin/env python3
"""
validate_ollama_accuracy.py

Test Ollama classification accuracy against known API-concept mappings.

This helps you:
1. Measure precision/recall before full run
2. Iterate on prompts
3. Identify which concept categories need improvement

Usage:
    # Test on 50 random APIs with known concepts
    python validate_ollama_accuracy.py --sample 50
    
    # Test specific concepts
    python validate_ollama_accuracy.py --concepts "Security System,Actions,Views"
    
    # Detailed output
    python validate_ollama_accuracy.py --sample 100 --verbose
"""

import argparse
import sys
from pathlib import Path
from typing import Dict, List, Set
import pandas as pd
import numpy as np
from collections import defaultdict

# Import from classify_unmapped_with_ollama in root directory
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from classify_unmapped_with_ollama import call_ollama_classify


def load_ground_truth(doc_concepts_df) -> Dict[str, Set[str]]:
    """
    Extract ground truth API → Concept mappings from doc_concepts.
    
    These are APIs where concepts co-occur in documentation,
    giving us high-confidence known mappings.
    
    Returns:
        Dict mapping api_id → set of concept names
    """
    
    ground_truth = defaultdict(set)
    
    api_sections = doc_concepts_df[
        (doc_concepts_df['is_api'] == True) & 
        (doc_concepts_df['apis'].notna()) &
        (doc_concepts_df['concepts'].notna())
    ]
    
    for _, row in api_sections.iterrows():
        # Handle both lists and numpy arrays
        apis = row['apis'] if isinstance(row['apis'], (list, np.ndarray)) else []
        concepts = row['concepts'] if isinstance(row['concepts'], (list, np.ndarray)) else []
        
        for api_str in apis:
            # Clean API ID
            api_id = api_str
            for suffix in ['description', 'name', 'remarks', 'example']:
                if api_id.lower().endswith(suffix):
                    api_id = api_id[:-len(suffix)]
                    break
            
            for concept in concepts:
                ground_truth[api_id].add(concept)
    
    return ground_truth


def calculate_metrics(predicted: Set[str], actual: Set[str]) -> Dict[str, float]:
    """
    Calculate precision, recall, F1 for a single API.
    
    Args:
        predicted: Set of concepts predicted by Ollama
        actual: Set of true concepts from ground truth
    
    Returns:
        Dict with precision, recall, f1
    """
    
    if not predicted and not actual:
        return {'precision': 1.0, 'recall': 1.0, 'f1': 1.0, 'tp': 0, 'fp': 0, 'fn': 0}
    
    if not predicted:
        return {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'tp': 0, 'fp': 0, 'fn': len(actual)}
    
    if not actual:
        return {'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'tp': 0, 'fp': len(predicted), 'fn': 0}
    
    true_positives = len(predicted & actual)
    false_positives = len(predicted - actual)
    false_negatives = len(actual - predicted)
    
    precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0
    recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
    
    return {
        'precision': precision,
        'recall': recall,
        'f1': f1,
        'tp': true_positives,
        'fp': false_positives,
        'fn': false_negatives
    }


def validate_ollama(
    api_entities_df: pd.DataFrame,
    doc_concepts_df: pd.DataFrame,
    ground_truth: Dict[str, Set[str]],
    sample_size: int = 50,
    target_concepts: List[str] = None,
    verbose: bool = False
) -> Dict:
    """
    Test Ollama accuracy on APIs with known concept mappings.
    
    Returns:
        Dict with overall metrics and per-concept breakdown
    """
    
    # Filter to APIs with ground truth
    testable_apis = list(ground_truth.keys())
    
    # Filter by target concepts if specified
    if target_concepts:
        testable_apis = [
            api_id for api_id in testable_apis
            if any(concept in ground_truth[api_id] for concept in target_concepts)
        ]
    
    print(f"📊 Testable APIs: {len(testable_apis)}")
    
    # Sample
    import random
    if sample_size and len(testable_apis) > sample_size:
        test_apis = random.sample(testable_apis, sample_size)
    else:
        test_apis = testable_apis
    
    print(f"🧪 Testing on {len(test_apis)} APIs...")
    
    results = []
    per_concept_stats = defaultdict(lambda: {'tp': 0, 'fp': 0, 'fn': 0, 'count': 0})
    
    for idx, api_id in enumerate(test_apis):
        if (idx + 1) % 10 == 0:
            print(f"   Progress: {idx + 1}/{len(test_apis)}")
        
        # Get API metadata
        api_row = api_entities_df[api_entities_df['api_id'] == api_id]
        if api_row.empty:
            continue
        api_row = api_row.iloc[0]
        
        # Get documentation context
        doc_context = ""
        doc_rows = doc_concepts_df[
            doc_concepts_df['apis'].apply(
                lambda x: api_id in x if isinstance(x, (list, np.ndarray)) else False
            )
        ]
        if len(doc_rows) > 0:
            first_doc = doc_rows.iloc[0]
            doc_context = str(first_doc.get('h_path', '')) + " " + str(first_doc.get('text', ''))[:300]
        
        # Classify with Ollama
        classification = call_ollama_classify(
            api_id=api_id,
            api_name=api_row['api_name'],
            namespace=api_row['namespace'],
            api_type=api_row['api_type'],
            doc_context=doc_context,
            timeout=60
        )
        
        # Get predicted concepts
        if 'error' in classification:
            if verbose:
                print(f"   ✗ {api_row['api_name']}: {classification['error'][:50]}")
            continue
        
        predicted_concepts = set(classification.get('concepts', []))
        actual_concepts = ground_truth[api_id]
        
        # Calculate metrics
        metrics = calculate_metrics(predicted_concepts, actual_concepts)
        
        result = {
            'api_id': api_id,
            'api_name': api_row['api_name'],
            'namespace': api_row['namespace'],
            'predicted': list(predicted_concepts),
            'actual': list(actual_concepts),
            'confidence': classification.get('confidence', 0),
            **metrics
        }
        results.append(result)
        
        # Update per-concept stats
        for concept in actual_concepts:
            per_concept_stats[concept]['count'] += 1
            if concept in predicted_concepts:
                per_concept_stats[concept]['tp'] += 1
            else:
                per_concept_stats[concept]['fn'] += 1
        
        for concept in predicted_concepts:
            if concept not in actual_concepts:
                per_concept_stats[concept]['fp'] += 1
        
        if verbose:
            status = "✓" if metrics['f1'] > 0.7 else "⚠" if metrics['f1'] > 0.4 else "✗"
            print(f"   {status} {api_row['api_name']}: F1={metrics['f1']:.2f}")
            if metrics['f1'] < 0.7:
                print(f"      Predicted: {predicted_concepts}")
                print(f"      Actual: {actual_concepts}")
    
    # Calculate overall metrics
    results_df = pd.DataFrame(results)
    
    if len(results) == 0:
        print("⚠️  No APIs were successfully classified. Check that Ollama is running.")
        return {'sample_size': 0, 'per_concept': []}
    
    overall = {
        'sample_size': len(results),
        'avg_precision': results_df['precision'].mean(),
        'avg_recall': results_df['recall'].mean(),
        'avg_f1': results_df['f1'].mean(),
        'total_tp': results_df['tp'].sum(),
        'total_fp': results_df['fp'].sum(),
        'total_fn': results_df['fn'].sum(),
        'avg_confidence': results_df['confidence'].mean()
    }
    
    # Calculate per-concept metrics
    concept_metrics = []
    for concept, stats in per_concept_stats.items():
        if stats['count'] > 0:  # Only concepts that appeared in ground truth
            precision = stats['tp'] / (stats['tp'] + stats['fp']) if (stats['tp'] + stats['fp']) > 0 else 0
            recall = stats['tp'] / (stats['tp'] + stats['fn']) if (stats['tp'] + stats['fn']) > 0 else 0
            f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
            
            concept_metrics.append({
                'concept': concept,
                'count': stats['count'],
                'precision': precision,
                'recall': recall,
                'f1': f1
            })
    
    concept_metrics_df = pd.DataFrame(concept_metrics).sort_values('f1', ascending=False)
    
    return {
        'overall': overall,
        'per_concept': concept_metrics_df,
        'details': results_df
    }


def print_validation_report(validation_results: Dict):
    """Print formatted validation report"""
    
    overall = validation_results['overall']
    per_concept = validation_results['per_concept']
    
    print("\n" + "="*70)
    print("OLLAMA VALIDATION RESULTS")
    print("="*70)
    
    print(f"\n📊 Overall Performance (n={overall['sample_size']})")
    print(f"   Precision: {overall['avg_precision']:.1%}")
    print(f"   Recall:    {overall['avg_recall']:.1%}")
    print(f"   F1 Score:  {overall['avg_f1']:.1%}")
    print(f"   Avg Confidence: {overall['avg_confidence']:.2f}")
    
    print(f"\n   True Positives:  {overall['total_tp']}")
    print(f"   False Positives: {overall['total_fp']}")
    print(f"   False Negatives: {overall['total_fn']}")
    
    # Quality assessment
    f1 = overall['avg_f1']
    if f1 >= 0.80:
        quality = "🟢 EXCELLENT - Ready for production"
    elif f1 >= 0.70:
        quality = "🟡 GOOD - Acceptable with validation"
    elif f1 >= 0.60:
        quality = "🟠 FAIR - Needs prompt improvement"
    else:
        quality = "🔴 POOR - Not recommended"
    
    print(f"\n   Quality: {quality}")
    
    # Per-concept breakdown
    print(f"\n📈 Per-Concept Performance")
    print(f"\nTop 10 concepts (by F1):")
    print(per_concept.head(10).to_string(index=False))
    
    print(f"\nBottom 10 concepts (need improvement):")
    print(per_concept.tail(10).to_string(index=False))
    
    # Recommendations
    print(f"\n💡 Recommendations:")
    
    if overall['avg_precision'] < 0.70:
        print("   - HIGH FALSE POSITIVES: Add more examples to system prompt")
        print("   - Strengthen 'choose ONLY from this list' instruction")
    
    if overall['avg_recall'] < 0.70:
        print("   - MISSING CONCEPTS: Model is too conservative")
        print("   - Add more namespace mapping rules")
        print("   - Provide better documentation context")
    
    low_f1_concepts = per_concept[per_concept['f1'] < 0.60]
    if len(low_f1_concepts) > 0:
        print(f"   - {len(low_f1_concepts)} concepts with F1 < 0.60:")
        for _, row in low_f1_concepts.head(5).iterrows():
            print(f"     • {row['concept']}: {row['f1']:.2%}")
        print("   - Consider manual review or cloud API for these concepts")


def main():
    parser = argparse.ArgumentParser(
        description='Validate Ollama classification accuracy'
    )
    parser.add_argument(
        '--sample',
        type=int,
        default=50,
        help='Number of APIs to test'
    )
    parser.add_argument(
        '--concepts',
        type=str,
        default=None,
        help='Comma-separated list of concepts to test (e.g., "Security System,Actions")'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Show detailed per-API results'
    )
    parser.add_argument(
        '--save-details',
        action='store_true',
        help='Save detailed results to CSV'
    )
    
    args = parser.parse_args()
    
    # Load data
    print("📚 Loading data...")
    api_entities_df = pd.read_parquet('outputs/api_entities.parquet')
    doc_concepts_df = pd.read_parquet('outputs/doc_concepts.parquet')
    
    # Build ground truth
    print("🎯 Building ground truth from co-occurrence data...")
    ground_truth = load_ground_truth(doc_concepts_df)
    print(f"   Ground truth: {len(ground_truth)} APIs with known concepts")
    
    # Parse target concepts
    target_concepts = None
    if args.concepts:
        target_concepts = [c.strip() for c in args.concepts.split(',')]
        print(f"   Filtering to concepts: {target_concepts}")
    
    # Run validation
    results = validate_ollama(
        api_entities_df,
        doc_concepts_df,
        ground_truth,
        sample_size=args.sample,
        target_concepts=target_concepts,
        verbose=args.verbose
    )
    
    # Print report
    print_validation_report(results)
    
    # Save details if requested
    if args.save_details:
        details_path = 'outputs/ollama_validation_details.csv'
        results['details'].to_csv(details_path, index=False)
        print(f"\n💾 Detailed results saved to: {details_path}")


if __name__ == '__main__':
    main()
