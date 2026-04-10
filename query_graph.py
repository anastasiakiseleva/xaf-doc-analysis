#!/usr/bin/env python
"""
Enhanced query graph with classified relationship support

# Analyze documentation gaps
python query_graph.py --mode gaps

# Show statistics
python query_graph.py --mode stats

# Find related sections by concept
python query_graph.py --mode query --concept "Dialog Controller"
python query_graph.py --mode query --concept "Collection Property"

# Find related sections for a specific document
python query_graph.py --mode query --section "article/security-system/authentication"

# ENHANCED: Filter by relationship type
python query_graph.py --mode query --concept "Dialog Controller" --relationship explains
python query_graph.py --mode query --concept "XAF Application" --relationship uses

# ENHANCED: Find learning paths (prerequisites)
python query_graph.py --mode prereqs --concept "Security System"

# ENHANCED: Show relationship type statistics
python query_graph.py --mode relationships
"""

import argparse
from pathlib import Path
import pandas as pd
from collections import Counter, defaultdict


PROJECT_ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = PROJECT_ROOT / "outputs"

F_SEMANTIC_PAIRS = OUTPUT_DIR / "semantic_pairs.parquet"
F_CLASSIFIED_PAIRS = OUTPUT_DIR / "classified_pairs_corrected.parquet"
F_DOC_CONCEPTS = OUTPUT_DIR / "doc_concepts.parquet"
F_TOPICS_INV = OUTPUT_DIR / "topics_inventory.parquet"


def safe_list(val):
    """Safely convert to list, handling numpy arrays"""
    if val is None or (isinstance(val, float) and pd.isna(val)):
        return []
    if isinstance(val, (list, tuple)):
        return list(val)
    if hasattr(val, '__iter__') and not isinstance(val, str):
        return list(val)
    return []


def load_data():
    """Load all necessary data files including classified relationships"""
    print("📚 Loading data...")
    pairs = pd.read_parquet(F_SEMANTIC_PAIRS, engine="pyarrow")
    concepts = pd.read_parquet(F_DOC_CONCEPTS, engine="pyarrow")
    inventory = pd.read_parquet(F_TOPICS_INV, engine="pyarrow")
    
    # Load classified relationships if available
    classified = None
    if F_CLASSIFIED_PAIRS.exists():
        classified = pd.read_parquet(F_CLASSIFIED_PAIRS, engine="pyarrow")
        print(f"  Semantic pairs: {len(pairs):,}")
        print(f"  Classified pairs: {len(classified):,} ✨")
        print(f"  Sections: {len(concepts):,}")
        print(f"  Documents: {len(inventory):,}")
    else:
        print(f"  Semantic pairs: {len(pairs):,}")
        print(f"  Sections: {len(concepts):,}")
        print(f"  Documents: {len(inventory):,}")
        print("  ⚠️  No classified relationships found (run classification first)")
    
    return pairs, classified, concepts, inventory


def query_by_concept(pairs: pd.DataFrame, classified: pd.DataFrame, concepts: pd.DataFrame, 
                     concept_name: str, relationship_filter: str = None, top_n: int = 20):
    """Find sections related to a specific concept, optionally filtered by relationship type"""
    filter_msg = f" with '{relationship_filter}' relationships" if relationship_filter else ""
    print(f"\n🔍 Searching for sections related to '{concept_name}'{filter_msg}...\n")
    
    # Find sections with this concept
    kept = concepts[concepts["kept"] == True].copy()
    mask = kept["concepts"].apply(lambda cs: concept_name in safe_list(cs))
    concept_sections = kept[mask]
    
    if len(concept_sections) == 0:
        print(f"❌ No sections found with concept '{concept_name}'")
        return
    
    print(f"📊 Found {len(concept_sections)} sections tagged with '{concept_name}'\n")
    
    # Use classified relationships if available, otherwise fall back to semantic pairs
    if classified is not None and len(classified) > 0:
        related = _find_related_classified(concept_sections, classified, relationship_filter)
        source = "classified relationships"
    else:
        related = _find_related_semantic(concept_sections, pairs)
        source = "semantic similarities"
        print("  💡 Using similarity scores (run classification for relationship types)\n")
    
    if len(related) == 0:
        print(f"⚠️  No connections found for '{concept_name}' sections")
        return
    
    df_related = pd.DataFrame(related)
    
    # Sort by confidence if available, else similarity
    sort_col = "confidence" if "confidence" in df_related.columns else "similarity"
    df_related = df_related.sort_values(sort_col, ascending=False).head(top_n)
    
    print(f"🔗 Top {len(df_related)} related sections (from {source}):\n")
    for i, (_, row) in enumerate(df_related.iterrows(), 1):
        print(f"{i}. {row['to_doc'][:80]}")
        
        # Show relationship type and confidence if available
        if "relationship" in row and pd.notna(row["relationship"]):
            print(f"   📌 Relationship: {row['relationship']} (confidence: {row['confidence']:.3f})")
        else:
            print(f"   Similarity: {row.get('similarity', 0):.3f} | Type: {row.get('type', 'N/A')}")
        
        # Show shared concepts
        overlap = safe_list(row.get('overlap_concepts', []))
        if overlap:
            print(f"   Shared concepts: {', '.join(overlap[:3])}")
        
        # Show bidirectional indicator if available
        if "bidirectional" in row and row["bidirectional"]:
            print(f"   ↔️  Bidirectional relationship")
        
        print()


def _find_related_classified(concept_sections, classified: pd.DataFrame, relationship_filter: str = None):
    """Find related sections using classified relationships"""
    section_ids = set(zip(concept_sections["doc_id"], concept_sections["section_id"]))
    
    related = []
    for _, row in classified.iterrows():
        src = (row["source_doc"], row["source_section"])
        tgt = (row["target_doc"], row["target_section"])
        
        # Filter by relationship type if specified
        if relationship_filter and row["relationship_type"] != relationship_filter:
            continue
        
        if src in section_ids:
            related.append({
                "from_doc": row["source_doc"],
                "to_doc": row["target_doc"],
                "to_section": row["target_section"],
                "type": row.get("neighbor_type", "N/A"),
                "relationship": row["relationship_type"],
                "confidence": row["relationship_confidence"],
                "bidirectional": row.get("relationship_bidirectional", False),
                "overlap_concepts": row.get("overlap_concepts", []),
                "similarity": row.get("sim_score", 0)
            })
        elif tgt in section_ids:
            # Reverse the relationship if searching from target
            related.append({
                "from_doc": row["target_doc"],
                "to_doc": row["source_doc"],
                "to_section": row["source_section"],
                "type": row.get("neighbor_type", "N/A"),
                "relationship": row["relationship_type"],
                "confidence": row["relationship_confidence"],
                "bidirectional": row.get("relationship_bidirectional", False),
                "overlap_concepts": row.get("overlap_concepts", []),
                "similarity": row.get("sim_score", 0)
            })
    
    return related


def _find_related_semantic(concept_sections, pairs: pd.DataFrame):
    """Find related sections using semantic similarity (fallback)"""
    section_ids = set(zip(concept_sections["doc_id"], concept_sections["section_id"]))
    
    related = []
    for _, row in pairs.iterrows():
        src = (row["source_doc"], row["source_section"])
        tgt = (row["target_doc"], row["target_section"])
        
        if src in section_ids:
            related.append({
                "from_doc": row["source_doc"],
                "to_doc": row["target_doc"], 
                "to_section": row["target_section"],
                "type": row["neighbor_type"],
                "similarity": row["sim_score"],
                "overlap_concepts": row["overlap_concepts"],
                "gates": row["gates_passed"]
            })
        elif tgt in section_ids:
            related.append({
                "from_doc": row["target_doc"],
                "to_doc": row["source_doc"],
                "to_section": row["source_section"],
                "type": row["neighbor_type"],
                "similarity": row["sim_score"],
                "overlap_concepts": row["overlap_concepts"],
                "gates": row["gates_passed"]
            })
    
    return related


def query_by_section(pairs: pd.DataFrame, classified: pd.DataFrame, concepts: pd.DataFrame, doc_id: str, top_n: int = 15):
    """Find sections semantically similar to a specific document section"""
    print(f"\n🔍 Finding sections related to '{doc_id}'...\n")
    
    # Use classified if available
    if classified is not None and len(classified) > 0:
        mask_src = classified["source_doc"] == doc_id
        mask_tgt = classified["target_doc"] == doc_id
        
        src_df = classified[mask_src][["target_doc", "target_section", "relationship_type", "relationship_confidence", "relationship_bidirectional", "overlap_concepts"]]
        tgt_df = classified[mask_tgt][["source_doc", "source_section", "relationship_type", "relationship_confidence", "relationship_bidirectional", "overlap_concepts"]]
        
        src_df = src_df.rename(columns={"target_doc": "doc", "target_section": "section", "relationship_confidence": "score"})
        tgt_df = tgt_df.rename(columns={"source_doc": "doc", "source_section": "section", "relationship_confidence": "score"})
        
        related = pd.concat([src_df, tgt_df]).sort_values("score", ascending=False).head(top_n)
        has_relationships = True
    else:
        # Fallback to semantic pairs
        mask_src = pairs["source_doc"] == doc_id
        mask_tgt = pairs["target_doc"] == doc_id
        
        related = pd.concat([
            pairs[mask_src][["target_doc", "target_section", "sim_score", "neighbor_type", "overlap_concepts"]].rename(columns={"target_doc": "doc", "target_section": "section", "sim_score": "score"}),
            pairs[mask_tgt][["source_doc", "source_section", "sim_score", "neighbor_type", "overlap_concepts"]].rename(columns={"source_doc": "doc", "source_section": "section", "sim_score": "score"})
        ]).sort_values("score", ascending=False).head(top_n)
        has_relationships = False
    
    if len(related) == 0:
        print(f"❌ No connections found for '{doc_id}'")
        return
    
    print(f"🔗 Top {len(related)} related sections:\n")
    for i, (_, row) in enumerate(related.iterrows(), 1):
        print(f"{i}. {row['doc'][:80]}")
        if has_relationships:
            print(f"   📌 Relationship: {row['relationship_type']} (confidence: {row['score']:.3f})")
            if row.get('relationship_bidirectional', False):
                print(f"   ↔️  Bidirectional")
        else:
            print(f"   Similarity: {row['score']:.3f} | Type: {row.get('neighbor_type', 'N/A')}")
        overlap = safe_list(row.get('overlap_concepts', []))
        if overlap:
            print(f"   Shared concepts: {', '.join(overlap[:3])}")
        print()


def analyze_gaps(pairs: pd.DataFrame, classified: pd.DataFrame, concepts: pd.DataFrame):
    """Analyze documentation gaps and under-connected concepts"""
    print("\n📊 Analyzing Documentation Gaps...\n")
    
    kept = concepts[concepts["kept"] == True].copy()
    
    # 1. Count connections per concept
    print("=" * 70)
    print("1. CONCEPT CONNECTIVITY ANALYSIS")
    print("=" * 70)
    
    concept_connections = {}
    for _, row in pairs.iterrows():
        for c in safe_list(row["overlap_concepts"]):
            concept_connections[c] = concept_connections.get(c, 0) + 1
    
    # Get concept frequencies
    all_concepts = kept["concepts"].explode().value_counts()
    
    connectivity_data = []
    for concept, freq in all_concepts.head(30).items():
        connections = concept_connections.get(concept, 0)
        connectivity_ratio = connections / freq if freq > 0 else 0
        connectivity_data.append({
            "concept": concept,
            "sections": freq,
            "semantic_connections": connections,
            "connections_per_section": connectivity_ratio
        })
    
    df_conn = pd.DataFrame(connectivity_data).sort_values("connections_per_section")
    
    print("\n🔴 UNDER-CONNECTED CONCEPTS (Low semantic links relative to frequency):\n")
    for _, row in df_conn.head(10).iterrows():
        print(f"  {row['concept']:30} | {row['sections']:4} sections | {row['semantic_connections']:5} links | {row['connections_per_section']:.1f} per section")
    
    print("\n🟢 WELL-CONNECTED CONCEPTS (High semantic links relative to frequency):\n")
    for _, row in df_conn.tail(10).iterrows():
        print(f"  {row['concept']:30} | {row['sections']:4} sections | {row['semantic_connections']:5} links | {row['connections_per_section']:.1f} per section")
    
    # 2. Cross-corpus connectivity (Conceptual ↔ API)
    print("\n" + "=" * 70)
    print("2. CROSS-CORPUS CONNECTIVITY (Conceptual ↔ API)")
    print("=" * 70)
    
    cross_pairs = pairs[pairs["neighbor_type"].isin(["ca", "ac"])]
    cross_concepts = {}
    for _, row in cross_pairs.iterrows():
        for c in safe_list(row["overlap_concepts"]):
            cross_concepts[c] = cross_concepts.get(c, 0) + 1
    
    print(f"\nTotal cross-corpus pairs: {len(cross_pairs):,}")
    print(f"Concepts with cross-links: {len(cross_concepts)}\n")
    
    print("🔗 Top concepts bridging conceptual ↔ API docs:\n")
    sorted_cross = sorted(cross_concepts.items(), key=lambda x: x[1], reverse=True)[:15]
    for concept, count in sorted_cross:
        sections = all_concepts.get(concept, 0)
        print(f"  {concept:30} | {count:4} cross-links | {sections:4} total sections")
    
    # Find concepts with NO cross-links
    concepts_with_sections = set(all_concepts.index)
    concepts_without_cross = concepts_with_sections - set(cross_concepts.keys())
    
    print(f"\n⚠️  Concepts with NO cross-corpus links: {len(concepts_without_cross)}")
    if len(concepts_without_cross) > 0:
        print("\nTop concepts missing conceptual ↔ API bridges:\n")
        for concept in list(concepts_without_cross)[:10]:
            freq = all_concepts.get(concept, 0)
            if freq >= 10:  # Only show significant concepts
                print(f"  {concept:30} | {freq:4} sections")
    
    # 3. Isolated sections
    print("\n" + "=" * 70)
    print("3. ISOLATED SECTIONS")
    print("=" * 70)
    
    connected_sections = set()
    for _, row in pairs.iterrows():
        connected_sections.add((row["source_doc"], row["source_section"]))
        connected_sections.add((row["target_doc"], row["target_section"]))
    
    all_sections = set(zip(kept["doc_id"], kept["section_id"]))
    isolated = all_sections - connected_sections
    
    print(f"\nTotal kept sections: {len(all_sections):,}")
    print(f"Connected sections: {len(connected_sections):,}")
    print(f"Isolated sections: {len(isolated):,} ({len(isolated)/len(all_sections)*100:.1f}%)")
    
    # Show some isolated sections
    if len(isolated) > 0:
        print("\nExample isolated sections (no semantic connections):\n")
        isolated_docs = [doc_id for doc_id, _ in list(isolated)[:10]]
        for doc_id in isolated_docs:
            section_row = kept[(kept["doc_id"] == doc_id)]
            if len(section_row) > 0:
                concepts_list = safe_list(section_row.iloc[0]["concepts"])
                print(f"  {doc_id}")
                if concepts_list:
                    print(f"    Concepts: {', '.join(concepts_list[:3])}")


def show_stats(pairs: pd.DataFrame, classified: pd.DataFrame, concepts: pd.DataFrame):
    """Show overall knowledge graph statistics"""
    print("\n📊 KNOWLEDGE GRAPH STATISTICS\n")
    print("=" * 70)
    
    kept = concepts[concepts["kept"] == True]
    
    print(f"Total semantic pairs: {len(pairs):,}")
    if classified is not None and len(classified) > 0:
        print(f"Classified relationships: {len(classified):,} ✨")
    print(f"Total sections: {len(kept):,}")
    print(f"Avg connections per section: {len(pairs) / len(kept):.1f}")
    
    print("\n📈 Breakdown by pair type:")
    type_counts = pairs["neighbor_type"].value_counts()
    for ntype, count in type_counts.items():
        type_map = {"cc": "Conceptual → Conceptual", "aa": "API → API", 
                    "ca": "Conceptual → API", "ac": "API → Conceptual"}
        print(f"  {type_map.get(ntype, ntype):25} | {count:6,} pairs")
    
    print("\n📊 Similarity score distribution:")
    print(f"  Average: {pairs['sim_score'].mean():.3f}")
    print(f"  Median:  {pairs['sim_score'].median():.3f}")
    print(f"  Min:     {pairs['sim_score'].min():.3f}")
    print(f"  Max:     {pairs['sim_score'].max():.3f}")
    
    print("\n🚪 Quality gates passed:")
    all_gates = []
    for gates_list in pairs["gates_passed"]:
        all_gates.extend(safe_list(gates_list))
    gate_counts = pd.Series(all_gates).value_counts()
    for gate, count in gate_counts.items():
        print(f"  {gate:30} | {count:6,} pairs")


def find_prerequisites(classified: pd.DataFrame, concepts: pd.DataFrame, inventory: pd.DataFrame, concept_name: str):
    """Find prerequisite documents using 'requires' relationships"""
    if classified is None or len(classified) == 0:
        print("\n❌ Classified relationships required for prerequisite analysis")
        print("   Run: python scripts/06_classify_relationships.py\n")
        return
    
    print(f"\n📚 Finding prerequisites for '{concept_name}'...\n")
    
    # Find sections with this concept
    kept = concepts[concepts["kept"] == True].copy()
    mask = kept["concepts"].apply(lambda cs: concept_name in safe_list(cs))
    concept_sections = kept[mask]
    
    if len(concept_sections) == 0:
        print(f"❌ No sections found with concept '{concept_name}'")
        return
    
    section_ids = set(zip(concept_sections["doc_id"], concept_sections["section_id"]))
    
    # Build doc_id → title lookup from inventory
    title_lookup = dict(zip(inventory["doc_id"], inventory["title"]))
    
    # Find 'requires' relationships where concept sections are the SOURCE.
    # "source requires target" means target is foundational to source —
    # so targets are the prerequisites of this concept.
    # Filters applied:
    #   - exclude API reference pages (not conceptual learning material)
    #   - exclude how-to articles (task-focused; assume prior knowledge of the concept)
    #   - exclude targets that already cover this concept (circular)
    prereqs = []
    for _, row in classified.iterrows():
        src = (row["source_doc"], row["source_section"])
        if src not in section_ids or row["relationship_type"] != "requires":
            continue
        # skip API reference pages
        if row.get("target_is_api", False):
            continue
        # skip how-to articles and tutorials — they are task/walkthrough guides that assume
        # prior knowledge of the concept, not foundational reading
        target_path = str(row["target_doc"]).lower()
        if "/how-to" in target_path or "tutorial" in target_path or "getting-started" in target_path or "get-started" in target_path:
            continue
        # skip docs that already cover the queried concept (circular)
        if concept_name in safe_list(row.get("target_concepts", [])):
            continue
        prereqs.append({
            "doc_id": row["target_doc"],
            "confidence": row["relationship_confidence"],
            "concepts": safe_list(row.get("target_concepts", [])),
        })
    
    if len(prereqs) == 0:
        print(f"✅ No prerequisites found for '{concept_name}'")
        print("   This concept does not require other knowledge first\n")
        return
    
    # Aggregate to doc level: max confidence, union of concepts
    df = pd.DataFrame(prereqs)
    def agg_doc(g):
        all_concepts = [c for cs in g["concepts"] for c in cs]
        top_concepts = [c for c, _ in Counter(all_concepts).most_common(5)]
        return pd.Series({
            "confidence": g["confidence"].max(),
            "key_concepts": top_concepts,
            "section_count": len(g),
        })
    df_prereqs = (
        df.groupby("doc_id", sort=False)
        .apply(agg_doc)
        .reset_index()
        .sort_values("confidence", ascending=False)
    )
    
    print(f"⚠️  {len(df_prereqs)} prerequisite document(s) found:\n")
    print(f"You should understand these topics BEFORE learning about '{concept_name}':\n")
    
    for i, (_, row) in enumerate(df_prereqs.iterrows(), 1):
        title = title_lookup.get(row["doc_id"], row["doc_id"])
        sections = int(row["section_count"])
        sec_label = "section" if sections == 1 else "sections"
        print(f"{i}. {title}")
        print(f"   Path:       {row['doc_id']}")
        print(f"   Confidence: {row['confidence']:.3f}  ({sections} matching {sec_label})")
        if row["key_concepts"]:
            print(f"   Key topics: {', '.join(row['key_concepts'])}")
        print()


def show_relationship_stats(classified: pd.DataFrame):
    """Show detailed statistics about classified relationships"""
    if classified is None or len(classified) == 0:
        print("\\n❌ No classified relationships found")
        print("   Run: python scripts/06_classify_relationships.py\\n")
        return
    
    print("\\n📊 CLASSIFIED RELATIONSHIP STATISTICS\\n")
    print("=" * 70)
    
    print(f"\\nTotal classified relationships: {len(classified):,}")
    
    # Relationship type distribution
    print("\\n🔗 Relationship Type Distribution:")
    rel_counts = classified["relationship_type"].value_counts()
    for rel_type, count in rel_counts.items():
        pct = 100 * count / len(classified)
        print(f"  {rel_type:20} {count:6,} ({pct:5.1f}%)")
    
    # Confidence statistics
    print("\\n📈 Confidence Scores:")
    print(f"  Average: {classified['relationship_confidence'].mean():.3f}")
    print(f"  Median:  {classified['relationship_confidence'].median():.3f}")
    print(f"  Min:     {classified['relationship_confidence'].min():.3f}")
    print(f"  Max:     {classified['relationship_confidence'].max():.3f}")
    
    # Bidirectional relationships
    if "relationship_bidirectional" in classified.columns:
        bidir_count = classified["relationship_bidirectional"].sum()
        print(f"\\n↔️  Bidirectional: {bidir_count:,} ({100*bidir_count/len(classified):.1f}%)")
        
        print("\\n   By relationship type:")
        for rel_type in rel_counts.index:
            subset = classified[classified["relationship_type"] == rel_type]
            bidir = subset["relationship_bidirectional"].sum()
            pct = 100 * bidir / len(subset)
            print(f"     {rel_type:20} {bidir:4,} / {len(subset):,} ({pct:5.1f}%)")
    
    # Pair type distribution
    if "neighbor_type" in classified.columns:
        print("\\n📝 By Pair Type:")
        type_counts = classified["neighbor_type"].value_counts()
        for ntype, count in type_counts.items():
            type_map = {"cc": "Concept↔Concept", "aa": "API↔API", 
                        "ca": "Concept→API", "ac": "API→Concept"}
            pct = 100 * count / len(classified)
            print(f"  {type_map.get(ntype, ntype):20} {count:6,} ({pct:5.1f}%)")
    
    # Top relationship patterns
    print("\\n🎯 Top Relationship Patterns:")
    pattern_counts = classified.groupby(["neighbor_type", "relationship_type"]).size().sort_values(ascending=False).head(10)
    for (ntype, rel_type), count in pattern_counts.items():
        type_map = {"cc": "C→C", "aa": "A→A", "ca": "C→A", "ac": "A→C"}
        print(f"  {type_map.get(ntype, ntype):6} + {rel_type:15} {count:5,} pairs")


def main():
    parser = argparse.ArgumentParser(description="Query the XAF knowledge graph with relationship intelligence")
    parser.add_argument("--mode", choices=["query", "gaps", "stats", "prereqs", "relationships"], required=True,
                        help="Operation mode")
    parser.add_argument("--concept", type=str, help="Concept name to query")
    parser.add_argument("--section", type=str, help="Document ID to query")
    parser.add_argument("--relationship", type=str, 
                        choices=["uses", "explains", "requires", "extends", "applies_to", "contrasts_with", "related_to"],
                        help="Filter by relationship type (requires classified data)")
    parser.add_argument("--top", type=int, default=20, help="Number of results to show")
    
    args = parser.parse_args()
    
    # Load data
    pairs, classified, concepts, inventory = load_data()
    
    if args.mode == "query":
        if args.concept:
            query_by_concept(pairs, classified, concepts, args.concept, args.relationship, args.top)
        elif args.section:
            query_by_section(pairs, classified, concepts, args.section, args.top)
        else:
            print("❌ Please specify --concept or --section for query mode")
    
    elif args.mode == "gaps":
        analyze_gaps(pairs, classified, concepts)
    
    elif args.mode == "stats":
        show_stats(pairs, classified, concepts)
    
    elif args.mode == "prereqs":
        if args.concept:
            find_prerequisites(classified, concepts, inventory, args.concept)
        else:
            print("❌ Please specify --concept for prereqs mode")
    
    elif args.mode == "relationships":
        show_relationship_stats(classified)


if __name__ == "__main__":
    main()
