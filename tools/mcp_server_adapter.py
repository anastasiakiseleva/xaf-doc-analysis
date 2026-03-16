#!/usr/bin/env python3
"""
MCP Server Adapter for XAF Documentation Analysis

Provides clean function interfaces for integration with MCP servers.
All functions return JSON-serializable structures for easy transport.

Usage in MCP Server:
    from tools.mcp_server_adapter import XAFDocAnalysis
    
    analyzer = XAFDocAnalysis()
    gaps = analyzer.get_documentation_gaps(concept="Security System")
    recommendations = analyzer.get_crosslink_recommendations(limit=20)
"""

import sys
from pathlib import Path
from typing import Optional, List, Dict, Any
import pandas as pd
import json

# Setup paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))


def safe_list(val):
    """Safely convert to list, handling numpy arrays and None values"""
    if val is None or (isinstance(val, float) and pd.isna(val)):
        return []
    if isinstance(val, (list, tuple)):
        return list(val)
    if hasattr(val, '__iter__') and not isinstance(val, str):
        return list(val)
    return []


class XAFDocAnalysis:
    """
    Main adapter class for MCP server integration.
    Loads data once on initialization for fast subsequent queries.
    """
    
    def __init__(self, data_dir: Optional[Path] = None):
        """
        Initialize analyzer with data files.
        
        Args:
            data_dir: Path to outputs directory (defaults to PROJECT_ROOT/outputs)
        """
        self.data_dir = data_dir or PROJECT_ROOT / "outputs"
        self.data = None
        self._load_data()
    
    def _load_data(self):
        """Load all core data files"""
        print("📚 Loading analysis data...")
        
        self.data = {
            'topics': pd.read_parquet(self.data_dir / 'topics_inventory.parquet'),
            'doc_concepts': pd.read_parquet(self.data_dir / 'doc_concepts.parquet'),
            'semantic_pairs': pd.read_parquet(self.data_dir / 'semantic_pairs.parquet'),
            'baseline_metrics': self._load_json('baseline_metrics.json'),
            'document_metadata': pd.read_parquet(self.data_dir / 'document_metadata.parquet'),
            'api_entities': pd.read_parquet(self.data_dir / 'api_entities.parquet'),
            'api_implements': pd.read_parquet(self.data_dir / 'api_implements_concept.parquet'),
        }
        
        # Load cross-linking recommendations if available
        crosslink_file = self.data_dir / 'cross_linking_filtered_actionable.csv'
        if crosslink_file.exists():
            self.data['crosslinks'] = pd.read_csv(crosslink_file)
        else:
            self.data['crosslinks'] = None
        
        print(f"  ✓ Loaded {len(self.data['doc_concepts']):,} sections")
        print(f"  ✓ Loaded {len(self.data['semantic_pairs']):,} semantic connections")
    
    def _load_json(self, filename: str) -> Optional[Dict]:
        """Load JSON file safely"""
        filepath = self.data_dir / filename
        if filepath.exists():
            with open(filepath, 'r') as f:
                return json.load(f)
        return None
    
    def get_documentation_gaps(
        self, 
        concept: Optional[str] = None,
        platform: Optional[str] = None,
        min_sections: int = 5
    ) -> Dict[str, Any]:
        """
        Identify documentation gaps across the corpus.
        
        Args:
            concept: Filter by specific concept (e.g., "Security System")
            platform: Filter by platform (e.g., "Blazor UI")
            min_sections: Minimum sections needed to avoid gap classification
        
        Returns:
            {
                "total_concepts_analyzed": int,
                "gaps_found": int,
                "gap_details": [
                    {
                        "concept": str,
                        "gap_type": "missing_api_tagging" | "missing_conceptual" | "semantic_gap",
                        "conceptual_sections": int,
                        "api_sections": int,
                        "cross_links": int,
                        "priority": "high" | "medium" | "low",
                        "ticket_count": int
                    }
                ]
            }
        """
        doc_concepts = self.data['doc_concepts']
        pairs = self.data['semantic_pairs']
        kept = doc_concepts[doc_concepts["kept"] == True]
        
        # Gap concepts (from baseline analysis)
        gap_concepts = [
            "Performance Optimization",
            "Deployment",
            "Logging", 
            "Legacy .NET Framework",
            "Migration",
            "Multi-Tenancy"
        ]
        
        # Filter if specific concept requested
        if concept:
            gap_concepts = [c for c in gap_concepts if c == concept]
        
        gap_details = []
        
        for gap_concept in gap_concepts:
            # Find sections with this concept
            concept_mask = kept["concepts"].apply(
                lambda cs: gap_concept in safe_list(cs)
            )
            concept_sections = kept[concept_mask]
            
            # Apply platform filter if specified
            if platform:
                platform_mask = concept_sections["platforms"].apply(
                    lambda ps: platform in safe_list(ps)
                )
                concept_sections = concept_sections[platform_mask]
            
            conceptual = concept_sections[concept_sections["is_api"] == False]
            api_docs = concept_sections[concept_sections["is_api"] == True]
            
            # Check cross-corpus links
            cross_pairs = pairs[pairs["neighbor_type"].isin(["ca", "ac"])]
            cross_with_concept = cross_pairs[
                cross_pairs["overlap_concepts"].apply(
                    lambda cs: gap_concept in safe_list(cs)
                )
            ]
            
            # Determine gap type
            if len(api_docs) == 0:
                gap_type = "missing_api_tagging"
                priority = "medium"
            elif len(conceptual) == 0:
                gap_type = "missing_conceptual"
                priority = "high"
            elif len(cross_with_concept) == 0:
                gap_type = "semantic_gap"
                priority = "high"
            else:
                continue  # Not a gap
            
            gap_details.append({
                "concept": gap_concept,
                "gap_type": gap_type,
                "conceptual_sections": len(conceptual),
                "api_sections": len(api_docs),
                "cross_links": len(cross_with_concept),
                "priority": priority,
                "ticket_count": self._get_ticket_count(gap_concept)
            })
        
        return {
            "total_concepts_analyzed": len(gap_concepts),
            "gaps_found": len(gap_details),
            "gap_details": gap_details,
            "baseline_metrics": {
                "total_sections": len(kept),
                "isolated_sections": self.data['baseline_metrics'].get('isolated_section_count', 0) if self.data['baseline_metrics'] else 0,
            }
        }
    
    def get_crosslink_recommendations(
        self,
        article_path: Optional[str] = None,
        article_type: Optional[str] = None,
        min_apis: int = 1,
        min_ticket_weight: float = 1.0,
        limit: int = 50
    ) -> Dict[str, Any]:
        """
        Get ticket-weighted cross-linking recommendations.
        
        Returns documents that need cross-linking attention, prioritized by:
        - Number of useful APIs that could be linked
        - Support ticket volume (customer pain points)
        - Realistic opportunity score
        
        Args:
            article_path: Filter to specific article path substring
            article_type: Filter by article type ("how_to", "tutorial", etc.)
            min_apis: Minimum number of useful APIs (default: 1)
            min_ticket_weight: Minimum ticket weight multiplier (default: 1.0)
            limit: Maximum results to return
        
        Returns:
            {
                "total_recommendations": int,
                "recommendations": [
                    {
                        "uid": int,
                        "title": str,
                        "path": str,
                        "article_type": str,
                        "word_count": int,
                        "num_useful_apis": int,
                        "num_high_priority_apis": int,
                        "num_medium_priority_apis": int,
                        "has_code_blocks": bool,
                        "realistic_score": float,
                        "ticket_weight": float,
                        "ticket_category": str,
                        "ticket_count": int
                    }
                ]
            }
        """
        if self.data['crosslinks'] is None:
            return {
                "error": "Cross-linking recommendations not available. Run generate_crosslink_filtered.py first.",
                "total_recommendations": 0,
                "recommendations": []
            }
        
        df = self.data['crosslinks'].copy()
        
        # Apply filters
        if article_path:
            df = df[df['path'].str.contains(article_path, case=False, na=False)]
        
        if article_type:
            df = df[df['article_type'] == article_type]
        
        # Filter by minimum APIs
        if min_apis > 0:
            df = df[df['num_actual_useful_apis'] >= min_apis]
        
        # Filter by ticket weight
        if min_ticket_weight > 0:
            df = df[df['ticket_weight'] >= min_ticket_weight]
        
        # Sort by realistic score (already ticket-weighted)
        df = df.sort_values('realistic_score', ascending=False)
        
        # Limit results
        df = df.head(limit)
        
        recommendations = []
        for _, row in df.iterrows():
            recommendations.append({
                "uid": int(row.get('uid', 0)) if pd.notna(row.get('uid')) else None,
                "title": str(row.get('title', '')),
                "path": str(row.get('path', '')),
                "article_type": str(row.get('article_type', 'unknown')),
                "word_count": int(row.get('word_count', 0)),
                "num_useful_apis": int(row.get('num_actual_useful_apis', 0)),
                "num_high_priority_apis": int(row.get('num_high_priority', 0)),
                "num_medium_priority_apis": int(row.get('num_medium_priority', 0)),
                "has_code_blocks": bool(row.get('has_code_blocks', False)),
                "realistic_score": float(row.get('realistic_score', 0)),
                "ticket_weight": float(row.get('ticket_weight', 0)),
                "ticket_category": str(row.get('primary_ticket_category', '')),
                "ticket_count": int(row.get('ticket_count', 0))
            })
        
        return {
            "total_recommendations": len(recommendations),
            "recommendations": recommendations
        }
    
    def get_document_metadata(
        self,
        doc_path: Optional[str] = None,
        concept: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Get AI-optimized YAML metadata suggestions for documents.
        
        Args:
            doc_path: Specific document path (e.g., "article/security-system")
            concept: Filter to documents with this concept
        
        Returns:
            {
                "documents": [
                    {
                        "doc_id": str,
                        "url": str,
                        "title": str,
                        "description": str,
                        "tags": [str],
                        "proficiency_level": str,
                        "concepts": [str],
                        "platforms": [str],
                        "total_connections": int
                    }
                ]
            }
        """
        df = self.data['document_metadata'].copy()
        
        # Apply filters
        if doc_path:
            df = df[df['doc_id'].str.contains(doc_path, case=False, na=False)]
        
        if concept:
            df = df[df['concepts'].apply(lambda cs: concept in safe_list(cs))]
        
        documents = []
        for _, row in df.iterrows():
            documents.append({
                "doc_id": row['doc_id'],
                "url": row.get('url', ''),
                "title": row.get('title', ''),
                "description": row.get('description', ''),
                "tags": safe_list(row.get('tags', [])),
                "proficiency_level": row.get('proficiency', 'Unknown'),
                "concepts": safe_list(row.get('concepts', [])),
                "platforms": safe_list(row.get('platforms', [])),
                "total_connections": int(row.get('total_connections', 0))
            })
        
        return {
            "total_documents": len(documents),
            "documents": documents
        }
    
    def get_ticket_priorities(
        self,
        concept: Optional[str] = None,
        top_n: int = 20
    ) -> Dict[str, Any]:
        """
        Get concepts ranked by support ticket volume (customer pain points).
        
        Args:
            concept: Filter to specific concept
            top_n: Number of top concepts to return
        
        Returns:
            {
                "ticket_priorities": [
                    {
                        "concept": str,
                        "ticket_count": int,
                        "ticket_weight": float,
                        "priority_rank": int
                    }
                ]
            }
        """
        # Ticket mapping from generate_crosslink_filtered.py
        ticket_mapping = {
            'Views': 2772,
            'Property Editors': 1634,
            'Controllers': 761,
            'List Editors': 554,
            'Authorization': 449,
            'Performance Optimization': 394,
            'Non-Persistent Objects': 383,
            'Lookup View': 368,
            'Layout': 329,
            'Application Model': 488,
            'Business Objects': 492,
            'Entity Framework Core': 303,
            'Actions': 286,
            'Authentication': 244,
            'Criteria': 216,
        }
        
        # Calculate weights
        avg_tickets = sum(ticket_mapping.values()) / len(ticket_mapping)
        
        priorities = []
        for rank, (concept_name, count) in enumerate(
            sorted(ticket_mapping.items(), key=lambda x: x[1], reverse=True), 
            start=1
        ):
            if concept and concept_name != concept:
                continue
            
            priorities.append({
                "concept": concept_name,
                "ticket_count": count,
                "ticket_weight": round(count / avg_tickets, 2),
                "priority_rank": rank
            })
            
            if len(priorities) >= top_n:
                break
        
        return {
            "total_concepts": len(priorities),
            "average_ticket_count": int(avg_tickets),
            "ticket_priorities": priorities
        }
    
    def query_concept_coverage(
        self,
        concept_name: str,
        include_isolated: bool = False
    ) -> Dict[str, Any]:
        """
        Analyze coverage and connectivity for a specific concept.
        
        Args:
            concept_name: Concept to analyze
            include_isolated: Include sections with no connections
        
        Returns:
            {
                "concept": str,
                "total_sections": int,
                "conceptual_sections": int,
                "api_sections": int,
                "platforms": [str],
                "avg_connections_per_section": float,
                "isolated_sections": int,
                "sample_sections": [
                    {
                        "doc_id": str,
                        "section_id": str,
                        "title": str,
                        "is_api": bool,
                        "connection_count": int
                    }
                ]
            }
        """
        doc_concepts = self.data['doc_concepts']
        pairs = self.data['semantic_pairs']
        kept = doc_concepts[doc_concepts["kept"] == True]
        
        # Find sections with this concept
        concept_mask = kept["concepts"].apply(
            lambda cs: concept_name in safe_list(cs)
        )
        concept_sections = kept[concept_mask]
        
        if len(concept_sections) == 0:
            return {
                "error": f"No sections found for concept '{concept_name}'",
                "concept": concept_name,
                "total_sections": 0
            }
        
        # Analyze
        conceptual = concept_sections[concept_sections["is_api"] == False]
        api_sections = concept_sections[concept_sections["is_api"] == True]
        
        # Get all platforms
        all_platforms = set()
        for platforms in concept_sections['platforms']:
            all_platforms.update(safe_list(platforms))
        
        # Calculate connectivity
        section_ids = set(zip(concept_sections["doc_id"], concept_sections["section_id"]))
        connection_counts = {}
        
        for _, row in pairs.iterrows():
            src = (row["source_doc"], row["source_section"])
            tgt = (row["target_doc"], row["target_section"])
            
            if src in section_ids:
                connection_counts[src] = connection_counts.get(src, 0) + 1
            if tgt in section_ids:
                connection_counts[tgt] = connection_counts.get(tgt, 0) + 1
        
        isolated = len([c for c in connection_counts.values() if c == 0])
        avg_connections = sum(connection_counts.values()) / len(section_ids) if section_ids else 0
        
        # Sample sections
        sample = concept_sections.head(10)
        sample_sections = []
        
        for _, row in sample.iterrows():
            section_key = (row["doc_id"], row["section_id"])
            sample_sections.append({
                "doc_id": row["doc_id"],
                "section_id": row["section_id"],
                "title": row.get("title", ""),
                "is_api": bool(row["is_api"]),
                "connection_count": connection_counts.get(section_key, 0)
            })
        
        return {
            "concept": concept_name,
            "total_sections": len(concept_sections),
            "conceptual_sections": len(conceptual),
            "api_sections": len(api_sections),
            "platforms": sorted(list(all_platforms)),
            "avg_connections_per_section": round(avg_connections, 2),
            "isolated_sections": isolated,
            "sample_sections": sample_sections
        }
    
    def _get_ticket_count(self, concept: str) -> int:
        """Get ticket count for a concept"""
        ticket_mapping = {
            'Views': 2772,
            'Property Editors': 1634,
            'Controllers': 761,
            'Performance Optimization': 394,
            'Deployment': 150,  # Estimated
            'Logging': 100,     # Estimated
            'Legacy .NET Framework': 50,  # Estimated
            'Migration': 80,    # Estimated
            'Multi-Tenancy': 200,  # Estimated
        }
        return ticket_mapping.get(concept, 0)


def main():
    """CLI interface for testing"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Test MCP adapter functions")
    parser.add_argument('--function', required=True, 
                       choices=['gaps', 'crosslinks', 'metadata', 'tickets', 'coverage'])
    parser.add_argument('--concept', help="Filter by concept")
    parser.add_argument('--platform', help="Filter by platform")
    parser.add_argument('--article', help="Filter by article path")
    parser.add_argument('--limit', type=int, default=20, help="Result limit")
    
    args = parser.parse_args()
    
    analyzer = XAFDocAnalysis()
    
    if args.function == 'gaps':
        result = analyzer.get_documentation_gaps(concept=args.concept, platform=args.platform)
    elif args.function == 'crosslinks':
        result = analyzer.get_crosslink_recommendations(
            article_path=args.article,
            concept=args.concept,
            platform=args.platform,
            limit=args.limit
        )
    elif args.function == 'metadata':
        result = analyzer.get_document_metadata(doc_path=args.article, concept=args.concept)
    elif args.function == 'tickets':
        result = analyzer.get_ticket_priorities(concept=args.concept, top_n=args.limit)
    elif args.function == 'coverage':
        if not args.concept:
            print("ERROR: --concept required for coverage query")
            return
        result = analyzer.query_concept_coverage(args.concept)
    
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
