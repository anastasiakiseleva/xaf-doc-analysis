"""
Filter semantic pairs to high-value subset for relationship classification.

Focus on:
1. High similarity scores (confident relationships)
2. Cross-corpus links (tutorial ↔ API reference)
3. Concepts with high support ticket volumes (customer pain points)
"""

import json
import pandas as pd
from pathlib import Path

# Configuration
OUTPUT_DIR = Path("outputs")
MIN_SIMILARITY = 0.70  # High-confidence pairs only
MAX_PAIRS = 5000  # Target output size
CROSS_CORPUS_BOOST = 1.5  # Boost score for tutorial ↔ API links
HIGH_TICKET_BOOST = 2.0  # Boost score for high-ticket concepts

# Load support ticket mapping
TICKET_DATA_PATH = Path("xaf_support_tickets_by_feature.json")
with open(TICKET_DATA_PATH, encoding='utf-8') as f:
    ticket_data = json.load(f)

# Map concepts to ticket counts (from your previous work)
CONCEPT_TO_TICKET_MAPPING = {
    'Views': 2772,
    'Property Editors': 1634,
    'Controllers': 1144,
    'List Editors': 850,
    'Authorization': 757,
    'Actions': 717,
    'Performance Optimization': 676,
    'Non-Persistent Objects': 649,
    'Lookup View': 555,
    'Layout': 515,
    'Application Model': 484,
    'Business Objects': 473,
    'Entity Framework Core': 470,
    'Detail View': 467,
    'List View': 438,
    'Dashboards': 435,
    'Reports': 435,
    'Testing': 414,
    'Validation': 396,
    'Blazor UI': 365,
    'Security System': 364,
    'WinForms': 347,
    'ASP.NET Core': 341,
    'XPO': 324,
    'Localization': 268,
    'Conditional Appearance': 256,
    'Audit Trail': 252,
    'Clone Object': 239,
    'Filtering UI': 209,
    'Popup Windows': 209
}

def safe_list(val):
    """Convert various formats to list."""
    if val is None:
        return []
    if hasattr(val, 'tolist'):
        return val.tolist()
    if isinstance(val, float) and pd.isna(val):
        return []
    return list(val) if val else []

def get_max_ticket_count(concepts):
    """Get highest ticket count from list of concepts."""
    if not concepts:
        return 0
    counts = [CONCEPT_TO_TICKET_MAPPING.get(c, 0) for c in concepts]
    return max(counts) if counts else 0

def main():
    print("="*70)
    print("High-Value Semantic Pairs Filter")
    print("="*70)
    
    # Load semantic pairs
    pairs_path = OUTPUT_DIR / "semantic_pairs.parquet"
    print(f"\nLoading semantic pairs from {pairs_path}...")
    pairs_df = pd.read_parquet(pairs_path)
    print(f"  Total pairs: {len(pairs_df):,}")
    
    # Rename similarity column if needed
    if 'similarity' not in pairs_df.columns and 'sim_score' in pairs_df.columns:
        pairs_df = pairs_df.rename(columns={'sim_score': 'similarity'})
    
    # Filter by minimum similarity
    print(f"\nApplying similarity filter (>= {MIN_SIMILARITY})...")
    high_sim = pairs_df[pairs_df['similarity'] >= MIN_SIMILARITY].copy()
    print(f"  Remaining: {len(high_sim):,} pairs ({len(high_sim)/len(pairs_df)*100:.1f}%)")
    
    # Calculate priority scores
    print("\nCalculating priority scores...")
    
    # Convert concepts to lists
    high_sim['source_concepts_list'] = high_sim['source_concepts'].apply(safe_list)
    high_sim['target_concepts_list'] = high_sim['target_concepts'].apply(safe_list)
    
    # Get max ticket counts
    high_sim['source_tickets'] = high_sim['source_concepts_list'].apply(get_max_ticket_count)
    high_sim['target_tickets'] = high_sim['target_concepts_list'].apply(get_max_ticket_count)
    high_sim['max_tickets'] = high_sim[['source_tickets', 'target_tickets']].max(axis=1)
    
    # Check if cross-corpus (tutorial ↔ API)
    high_sim['is_cross_corpus'] = high_sim['source_is_api'] != high_sim['target_is_api']
    
    # Calculate priority score
    high_sim['priority_score'] = high_sim['similarity']
    
    # Boost for cross-corpus links
    cross_corpus_mask = high_sim['is_cross_corpus']
    high_sim.loc[cross_corpus_mask, 'priority_score'] *= CROSS_CORPUS_BOOST
    
    # Boost for high-ticket concepts (400+ tickets)
    high_ticket_mask = high_sim['max_tickets'] >= 400
    high_sim.loc[high_ticket_mask, 'priority_score'] *= HIGH_TICKET_BOOST
    
    # Sort by priority
    high_sim = high_sim.sort_values('priority_score', ascending=False)
    
    # Take top N
    filtered = high_sim.head(MAX_PAIRS)
    
    # Print summary statistics
    print("\n" + "="*70)
    print("FILTERED RESULTS SUMMARY")
    print("="*70)
    print(f"Total filtered pairs: {len(filtered):,}")
    print(f"\nSimilarity range: {filtered['similarity'].min():.3f} - {filtered['similarity'].max():.3f}")
    print(f"  Mean: {filtered['similarity'].mean():.3f}")
    print(f"  Median: {filtered['similarity'].median():.3f}")
    
    cross_corpus_count = filtered['is_cross_corpus'].sum()
    print(f"\nCross-corpus links (tutorial ↔ API): {cross_corpus_count:,} ({cross_corpus_count/len(filtered)*100:.1f}%)")
    
    high_ticket_count = (filtered['max_tickets'] >= 400).sum()
    print(f"High-ticket concept pairs (400+ tickets): {high_ticket_count:,} ({high_ticket_count/len(filtered)*100:.1f}%)")
    
    # Top concepts by frequency
    all_concepts = []
    for concepts in filtered['source_concepts_list']:
        all_concepts.extend(concepts)
    for concepts in filtered['target_concepts_list']:
        all_concepts.extend(concepts)
    
    concept_counts = pd.Series(all_concepts).value_counts()
    print(f"\nTop 10 concepts in filtered pairs:")
    for concept, count in concept_counts.head(10).items():
        tickets = CONCEPT_TO_TICKET_MAPPING.get(concept, 0)
        print(f"  {concept}: {count:,} pairs | {tickets:,} tickets")
    
    # Save filtered pairs
    output_path = OUTPUT_DIR / "semantic_pairs_high_value.parquet"
    print(f"\nSaving filtered pairs to {output_path}...")
    
    # Keep only essential columns for classification
    essential_cols = [
        'source_doc', 'source_section', 'source_is_api', 'source_concepts',
        'target_doc', 'target_section', 'target_is_api', 'target_concepts',
        'similarity', 'priority_score', 'is_cross_corpus', 'max_tickets'
    ]
    
    filtered[essential_cols].to_parquet(output_path, index=False)
    
    # Also save as CSV for easy inspection
    csv_path = OUTPUT_DIR / "semantic_pairs_high_value.csv"
    print(f"Saving CSV preview to {csv_path}...")
    filtered[essential_cols].head(100).to_csv(csv_path, index=False)
    
    print("\n" + "="*70)
    print("✅ FILTERING COMPLETE")
    print("="*70)
    print(f"\nNext step: Run relationship classification on {output_path.name}")
    print(f"  Command: python scripts/06_classify_relationships.py --input {output_path.name}")
    print(f"\nEstimated classification time:")
    print(f"  With local model (Ollama): ~2-3 hours")
    print(f"  With cloud API (GPT-4/Claude): ~30-60 minutes")
    print(f"  Estimated cost (cloud): ~${len(filtered) * 0.005:.2f} - ${len(filtered) * 0.01:.2f}")

if __name__ == "__main__":
    main()
