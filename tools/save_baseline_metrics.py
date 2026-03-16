#!/usr/bin/env python
"""
Generate detailed baseline metrics in JSON format for programmatic comparison
"""
import pandas as pd
import json
from datetime import datetime
from pathlib import Path

# Load data
print("📚 Loading data...")
pairs = pd.read_parquet('outputs/semantic_pairs.parquet')
concepts_df = pd.read_parquet('outputs/doc_concepts.parquet')
inventory = pd.read_parquet('outputs/topics_inventory.parquet')
kept = concepts_df[concepts_df["kept"] == True]

print(f"✅ Loaded {len(pairs):,} pairs, {len(kept):,} sections\n")

# Helper function
def has_concept(concepts_val, target):
    if concepts_val is None or (isinstance(concepts_val, float) and pd.isna(concepts_val)):
        return False
    concepts_list = list(concepts_val) if hasattr(concepts_val, '__iter__') and not isinstance(concepts_val, str) else []
    return target in concepts_list

# Overall statistics
print("📊 Computing overall statistics...")
connected = set()
for row in pairs.itertuples():
    connected.add((row.source_doc, row.source_section))
    connected.add((row.target_doc, row.target_section))

all_sections = set(zip(kept["doc_id"], kept["section_id"]))
isolated = all_sections - connected

overall_stats = {
    "total_documents": len(inventory),
    "total_sections": len(kept),
    "total_pairs": len(pairs),
    "avg_connections_per_section": round(len(pairs) * 2 / len(kept), 2),
    "isolated_sections": len(isolated),
    "isolated_percentage": round(len(isolated) / len(kept) * 100, 2),
    "connected_sections": len(connected),
    "connected_percentage": round(len(connected) / len(kept) * 100, 2)
}

# Connectivity by type
print("🔗 Computing connectivity by type...")
type_counts = pairs["neighbor_type"].value_counts().to_dict()
connectivity_by_type = {
    "cc": int(type_counts.get("cc", 0)),
    "aa": int(type_counts.get("aa", 0)),
    "ac": int(type_counts.get("ac", 0)),
    "ca": int(type_counts.get("ca", 0)),
    "cross_corpus_total": int(type_counts.get("ac", 0) + type_counts.get("ca", 0)),
    "cross_corpus_percentage": round((type_counts.get("ac", 0) + type_counts.get("ca", 0)) / len(pairs) * 100, 2)
}

# Similarity scores
print("📈 Computing similarity statistics...")
similarity_stats = {
    "average": round(pairs["sim_score"].mean(), 3),
    "median": round(pairs["sim_score"].median(), 3),
    "min": round(pairs["sim_score"].min(), 3),
    "max": round(pairs["sim_score"].max(), 3),
    "std": round(pairs["sim_score"].std(), 3)
}

# Quality gates
print("🚪 Computing quality gate statistics...")
all_gates = []
for gates in pairs["gates_passed"]:
    if gates is not None and hasattr(gates, '__iter__'):
        all_gates.extend(list(gates))

gate_counts = pd.Series(all_gates).value_counts()
quality_gates = {
    gate: int(count) for gate, count in gate_counts.items()
}

# Per-concept statistics
print("📌 Computing per-concept statistics...\n")
# Get all unique concepts
all_concepts = set()
for concepts_list in kept["concepts"]:
    if concepts_list is not None and hasattr(concepts_list, '__iter__'):
        all_concepts.update(list(concepts_list))

concept_stats = {}
for concept in sorted(all_concepts):
    # Get sections with this concept
    concept_sections = kept[kept["concepts"].apply(lambda cs: has_concept(cs, concept))]
    
    if len(concept_sections) == 0:
        continue
    
    # Separate by type
    conceptual = concept_sections[concept_sections["is_api"] == False]
    api_docs = concept_sections[concept_sections["is_api"] == True]
    
    # Count links for this concept
    concept_section_ids = set(zip(concept_sections["doc_id"], concept_sections["section_id"]))
    concept_links = 0
    for row in pairs.itertuples():
        src = (row.source_doc, row.source_section)
        tgt = (row.target_doc, row.target_section)
        if src in concept_section_ids or tgt in concept_section_ids:
            # Check if this pair involves the concept
            overlap = row.overlap_concepts
            if overlap is not None and hasattr(overlap, '__iter__'):
                if concept in list(overlap):
                    concept_links += 1
    
    # Cross-corpus links
    cross_pairs = pairs[pairs["neighbor_type"].isin(["ca", "ac"])]
    cross_with_concept = cross_pairs[
        cross_pairs["overlap_concepts"].apply(lambda cs: has_concept(cs, concept))
    ]
    
    links_per_section = round(concept_links / len(concept_sections), 2) if len(concept_sections) > 0 else 0
    
    concept_stats[concept] = {
        "total_sections": len(concept_sections),
        "conceptual_sections": len(conceptual),
        "api_sections": len(api_docs),
        "total_links": concept_links,
        "links_per_section": links_per_section,
        "cross_corpus_links": len(cross_with_concept),
        "has_cross_corpus_gap": len(cross_with_concept) == 0,
        "under_connected": links_per_section < 6.0
    }
    
    print(f"  {concept:40} | {len(concept_sections):4} sections | {links_per_section:5.1f} links/sec | {len(cross_with_concept):4} cross-links")

# Identify critical issues
print("\n🔴 Identifying critical issues...")
gap_concepts = [c for c, stats in concept_stats.items() if stats["has_cross_corpus_gap"]]
under_connected = [c for c, stats in concept_stats.items() if stats["under_connected"]]

critical_issues = {
    "concepts_with_zero_cross_links": gap_concepts,
    "concepts_under_connected": under_connected,
    "isolated_section_examples": [f"{doc_id}/{section_id}" for doc_id, section_id in list(isolated)[:20]]
}

# Build final report
baseline_report = {
    "metadata": {
        "generated_date": datetime.now().isoformat(),
        "purpose": "Baseline metrics for documentation improvement tracking",
        "project": "XAF Documentation Analysis"
    },
    "overall_statistics": overall_stats,
    "connectivity_by_type": connectivity_by_type,
    "similarity_statistics": similarity_stats,
    "quality_gates": quality_gates,
    "concept_statistics": concept_stats,
    "critical_issues": critical_issues
}

# Save to JSON
output_file = Path("outputs/baseline_metrics.json")
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(baseline_report, f, indent=2, ensure_ascii=False)

print(f"\n✅ Baseline metrics saved to: {output_file}")
print(f"\n📊 Summary:")
print(f"   • {overall_stats['total_sections']:,} sections analyzed")
print(f"   • {overall_stats['total_pairs']:,} semantic pairs")
print(f"   • {len(gap_concepts)} concepts with cross-corpus gaps")
print(f"   • {len(under_connected)} under-connected concepts")
print(f"   • {overall_stats['isolated_sections']} isolated sections ({overall_stats['isolated_percentage']}%)")
print(f"\n🎯 Ready for improvement tracking!")
