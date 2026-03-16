#!/usr/bin/env python3
"""
Integration Tests for MVP Pipeline

Tests that validate data consistency and foreign key relationships
between pipeline phases.

Usage:
    python tests/test_pipeline_integration.py
    python tests/test_pipeline_integration.py --phase 3  # Test specific phase
"""

import sys
from pathlib import Path
import pandas as pd
import argparse

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))
from utils.pipeline_validators import PipelineValidator, ValidationReport, ValidationResult


class PipelineIntegrationTester:
    """Integration tests for pipeline phase dependencies."""
    
    def __init__(self, outputs_dir: Path):
        self.outputs_dir = outputs_dir
        self.validator = PipelineValidator()
        self.results = []
    
    def load_parquet_safe(self, filename: str) -> pd.DataFrame:
        """Safely load a parquet file, returning empty DataFrame if not found."""
        filepath = self.outputs_dir / filename
        if not filepath.exists():
            print(f"⚠️  File not found: {filename}")
            return pd.DataFrame()
        return pd.read_parquet(filepath)
    
    def test_phase1_to_phase3_consistency(self) -> ValidationResult:
        """
        Test that all section_ids in Phase 3 output exist in Phase 1 output.
        """
        print("\n🔍 Testing Phase 1 → Phase 3 consistency...")
        
        topics_df = self.load_parquet_safe("topics_inventory.parquet")
        concepts_df = self.load_parquet_safe("doc_concepts.parquet")
        
        if topics_df.empty or concepts_df.empty:
            return ValidationResult(
                check_name="Phase 1→3 consistency",
                passed=False,
                message="Required input files missing",
                severity="error"
            )
        
        # Extract all section_ids from Phase 1
        phase1_sections = set()
        for _, row in topics_df.iterrows():
            sections = row.get('sections', [])
            if isinstance(sections, list):
                for section in sections:
                    if isinstance(section, dict):
                        section_id = section.get('section_id')
                        doc_id = row['doc_id']
                        if section_id:
                            phase1_sections.add((doc_id, section_id))
        
        # Extract all section_ids from Phase 3
        phase3_sections = set(zip(concepts_df['doc_id'], concepts_df['section_id']))
        
        # Find orphaned sections (in Phase 3 but not in Phase 1)
        orphaned = phase3_sections - phase1_sections
        
        if orphaned:
            sample = list(orphaned)[:5]
            return ValidationResult(
                check_name="Phase 1→3 consistency",
                passed=False,
                message=f"{len(orphaned)} section_ids in Phase 3 don't exist in Phase 1",
                severity="error",
                details={"orphaned_count": len(orphaned), "sample": [f"{d}::{s}" for d, s in sample]}
            )
        
        return ValidationResult(
            check_name="Phase 1→3 consistency",
            passed=True,
            message=f"All {len(phase3_sections):,} section IDs in Phase 3 reference valid Phase 1 sections",
            severity="info",
            details={"validated_sections": len(phase3_sections)}
        )
    
    def test_phase3_to_phase7_consistency(self) -> ValidationResult:
        """
        Test that all section_ids in Phase 7 output exist in Phase 3 output.
        """
        print("\n🔍 Testing Phase 3 → Phase 7 consistency...")
        
        concepts_df = self.load_parquet_safe("doc_concepts.parquet")
        metadata_df = self.load_parquet_safe("metadata_suggestions.parquet")
        
        if concepts_df.empty or metadata_df.empty:
            return ValidationResult(
                check_name="Phase 3→7 consistency",
                passed=False,
                message="Required input files missing",
                severity="error"
            )
        
        # Extract section_ids from Phase 3 (only kept sections)
        phase3_kept = concepts_df[concepts_df['kept'] == True] if 'kept' in concepts_df.columns else concepts_df
        phase3_sections = set(zip(phase3_kept['doc_id'], phase3_kept['section_id']))
        
        # Extract section_ids from Phase 7
        phase7_sections = set(zip(metadata_df['doc_id'], metadata_df['section_id']))
        
        # Find orphaned sections
        orphaned = phase7_sections - phase3_sections
        
        if orphaned:
            sample = list(orphaned)[:5]
            return ValidationResult(
                check_name="Phase 3→7 consistency",
                passed=False,
                message=f"{len(orphaned)} section_ids in Phase 7 don't exist in Phase 3 (kept sections)",
                severity="error",
                details={"orphaned_count": len(orphaned), "sample": [f"{d}::{s}" for d, s in sample]}
            )
        
        return ValidationResult(
            check_name="Phase 3→7 consistency",
            passed=True,
            message=f"All {len(phase7_sections):,} section IDs in Phase 7 reference valid Phase 3 sections",
            severity="info",
            details={"validated_sections": len(phase7_sections)}
        )
    
    def test_phase7_to_phase10_rollup(self) -> ValidationResult:
        """
        Test that Phase 10 document tags are proper supersets of Phase 7 section tags.
        """
        print("\n🔍 Testing Phase 7 → Phase 10 rollup consistency...")
        
        metadata_df = self.load_parquet_safe("metadata_suggestions.parquet")
        doc_metadata_df = self.load_parquet_safe("document_metadata.parquet")
        
        if metadata_df.empty or doc_metadata_df.empty:
            return ValidationResult(
                check_name="Phase 7→10 rollup",
                passed=False,
                message="Required input files missing",
                severity="error"
            )
        
        # Sample 20 documents for testing
        sample_docs = doc_metadata_df['doc_id'].head(20).tolist()
        
        rollup_issues = []
        for doc_id in sample_docs:
            # Get document-level tags
            doc_row = doc_metadata_df[doc_metadata_df['doc_id'] == doc_id]
            if doc_row.empty:
                continue
            
            doc_tags = set(doc_row.iloc[0]['tags']) if isinstance(doc_row.iloc[0]['tags'], list) else set()
            
            # Get all section-level tags for this document
            section_rows = metadata_df[metadata_df['doc_id'] == doc_id]
            section_tags = set()
            for _, row in section_rows.iterrows():
                tags = row.get('suggested_tags', [])
                if isinstance(tags, list):
                    section_tags.update(tags)
            
            # Check if most section tags are in document tags (allow some loss due to aggregation limits)
            if section_tags:
                overlap = len(section_tags & doc_tags) / len(section_tags)
                if overlap < 0.80:  # At least 80% of section tags should be in doc tags
                    rollup_issues.append({
                        "doc_id": doc_id,
                        "overlap": f"{overlap:.1%}",
                        "section_tags": len(section_tags),
                        "doc_tags": len(doc_tags)
                    })
        
        if rollup_issues:
            return ValidationResult(
                check_name="Phase 7→10 rollup",
                passed=False,
                message=f"{len(rollup_issues)}/{len(sample_docs)} sampled docs have tag aggregation issues (<80% overlap)",
                severity="warning",
                details={"issues": rollup_issues[:3]}
            )
        
        return ValidationResult(
            check_name="Phase 7→10 rollup",
            passed=True,
            message=f"Tag aggregation looks good for all {len(sample_docs)} sampled documents",
            severity="info"
        )
    
    def test_semantic_pairs_references(self) -> ValidationResult:
        """
        Test that all source/target sections in semantic pairs exist in doc_concepts.
        """
        print("\n🔍 Testing semantic pairs references...")
        
        concepts_df = self.load_parquet_safe("doc_concepts.parquet")
        pairs_df = self.load_parquet_safe("semantic_pairs.parquet")
        
        if concepts_df.empty:
            return ValidationResult(
                check_name="Semantic pairs references",
                passed=False,
                message="doc_concepts.parquet not found",
                severity="error"
            )
        
        if pairs_df.empty:
            return ValidationResult(
                check_name="Semantic pairs references",
                passed=True,
                message="semantic_pairs.parquet not found (optional feature)",
                severity="info"
            )
        
        # Build set of valid section identifiers
        valid_sections = set(zip(concepts_df['doc_id'], concepts_df['section_id']))
        
        # Check source and target sections
        source_sections = set(zip(pairs_df['source_doc'], pairs_df['source_section']))
        target_sections = set(zip(pairs_df['target_doc'], pairs_df['target_section']))
        
        invalid_sources = source_sections - valid_sections
        invalid_targets = target_sections - valid_sections
        
        if invalid_sources or invalid_targets:
            return ValidationResult(
                check_name="Semantic pairs references",
                passed=False,
                message=f"Invalid references: {len(invalid_sources)} sources, {len(invalid_targets)} targets",
                severity="error",
                details={
                    "invalid_sources": len(invalid_sources),
                    "invalid_targets": len(invalid_targets),
                    "sample_invalid": list(invalid_sources | invalid_targets)[:5]
                }
            )
        
        return ValidationResult(
            check_name="Semantic pairs references",
            passed=True,
            message=f"All {len(pairs_df):,} semantic pairs reference valid sections",
            severity="info"
        )
    
    def test_api_entities_references(self) -> ValidationResult:
        """
        Test that all section_ids in documents_api exist in doc_concepts.
        """
        print("\n🔍 Testing API entities references...")

        concepts_df = self.load_parquet_safe("doc_concepts.parquet")
        docs_api_df = self.load_parquet_safe("documents_api.parquet")
        
        if concepts_df.empty:
            return ValidationResult(
                check_name="API entities references",
                passed=False,
                message="doc_concepts.parquet not found",
                severity="error"
            )
        
        if docs_api_df.empty:
            return ValidationResult(
                check_name="API entities references",
                passed=True,
                message="documents_api.parquet not found (optional feature)",
                severity="info"
            )
        
        # Build set of valid sections
        valid_sections = set(zip(concepts_df['doc_id'], concepts_df['section_id']))
        
        # Check documents_api references
        api_sections = set(zip(docs_api_df['doc_id'], docs_api_df['section_id']))
        
        invalid = api_sections - valid_sections
        
        if invalid:
            sample = list(invalid)[:5]
            return ValidationResult(
                check_name="API entities references",
                passed=False,
                message=f"{len(invalid)} section_ids in documents_api don't exist in doc_concepts",
                severity="error",
                details={"invalid_count": len(invalid), "sample": [f"{d}::{s}" for d, s in sample]}
            )
        
        return ValidationResult(
            check_name="API entities references",
            passed=True,
            message=f"All {len(api_sections):,} API section references are valid",
            severity="info"
        )

    def test_knowledge_graph_artifact(self) -> ValidationResult:
        """Validate that outputs/knowledge_graph.json is present and well-formed (if generated)."""
        print("\n🔍 Testing knowledge graph artifact...")

        kg_path = self.outputs_dir / "knowledge_graph.json"
        if not kg_path.exists():
            return ValidationResult(
                check_name="Knowledge graph artifact",
                passed=True,
                message="knowledge_graph.json not found (optional feature)",
                severity="info",
            )

        try:
            import json
            kg = json.loads(kg_path.read_text(encoding="utf-8"))
        except Exception as e:
            return ValidationResult(
                check_name="Knowledge graph artifact",
                passed=False,
                message=f"knowledge_graph.json could not be parsed: {e}",
                severity="error",
            )

        if not isinstance(kg, dict):
            return ValidationResult(
                check_name="Knowledge graph artifact",
                passed=False,
                message="knowledge_graph.json is not a JSON object",
                severity="error",
            )

        for key in ("metadata", "nodes", "edges"):
            if key not in kg:
                return ValidationResult(
                    check_name="Knowledge graph artifact",
                    passed=False,
                    message=f"Missing top-level key: {key}",
                    severity="error",
                )

        nodes = kg.get("nodes") or []
        edges = kg.get("edges") or []

        if not isinstance(nodes, list) or not isinstance(edges, list):
            return ValidationResult(
                check_name="Knowledge graph artifact",
                passed=False,
                message="nodes/edges must be JSON arrays",
                severity="error",
            )

        # Light endpoint validation on a sample (avoid reading huge graphs fully)
        node_ids = set()
        for n in nodes[:50000]:
            if isinstance(n, dict) and n.get("id"):
                node_ids.add(n.get("id"))

        missing_endpoints = 0
        for e in edges[:20000]:
            if not isinstance(e, dict):
                continue
            if e.get("source") not in node_ids or e.get("target") not in node_ids:
                missing_endpoints += 1

        severity = "warning" if missing_endpoints > 0 else "info"
        passed = missing_endpoints == 0

        return ValidationResult(
            check_name="Knowledge graph artifact",
            passed=passed,
            message=f"knowledge_graph.json loaded: {len(nodes):,} nodes, {len(edges):,} edges; missing_endpoints(sample)={missing_endpoints}",
            severity=severity,
        )
    
    def test_explicit_graph_references(self) -> ValidationResult:
        """
        Test that all doc_ids in explicit graph exist in topics_inventory.
        Phase 2 is required in MVP pipeline.
        """
        print("\n🔍 Testing explicit graph references...")
        
        topics_df = self.load_parquet_safe("topics_inventory.parquet")
        graph_df = self.load_parquet_safe("explicit_graph.parquet")
        
        if topics_df.empty:
            return ValidationResult(
                check_name="Explicit graph references",
                passed=False,
                message="topics_inventory.parquet not found",
                severity="error"
            )
        
        if graph_df.empty:
            return ValidationResult(
                check_name="Explicit graph references",
                passed=False,
                message="explicit_graph.parquet not found (Phase 2 is required in MVP)",
                severity="error"
            )
        
        valid_docs = set(topics_df['doc_id'])
        
        # Check source and target docs
        source_docs = set(graph_df['source_doc'])
        target_docs = set(graph_df['target_doc'])
        
        invalid_sources = source_docs - valid_docs
        invalid_targets = target_docs - valid_docs
        
        if invalid_sources or invalid_targets:
            return ValidationResult(
                check_name="Explicit graph references",
                passed=False,
                message=f"Invalid doc_ids: {len(invalid_sources)} sources, {len(invalid_targets)} targets",
                severity="error",
                details={
                    "invalid_sources": len(invalid_sources),
                    "invalid_targets": len(invalid_targets)
                }
            )
        
        return ValidationResult(
            check_name="Explicit graph references",
            passed=True,
            message=f"All {len(graph_df):,} graph edges reference valid documents",
            severity="info"
        )
    
    def run_all_tests(self, phase_filter: int = None) -> ValidationReport:
        """Run all integration tests."""
        report = ValidationReport(phase_name="Pipeline Integration Tests", phase_number=0)
        
        tests = [
            (1, self.test_phase1_to_phase3_consistency),
            (3, self.test_phase3_to_phase7_consistency),
            (7, self.test_phase7_to_phase10_rollup),
            (5, self.test_semantic_pairs_references),
            (11, self.test_api_entities_references),
            (2, self.test_explicit_graph_references),
            (13, self.test_knowledge_graph_artifact),
        ]
        
        for phase_num, test_func in tests:
            if phase_filter is not None and phase_num != phase_filter:
                continue
            
            try:
                result = test_func()
                report.add_result(result)
            except Exception as e:
                report.add_result(ValidationResult(
                    check_name=test_func.__name__,
                    passed=False,
                    message=f"Test failed with exception: {str(e)}",
                    severity="error"
                ))
        
        return report


def main():
    parser = argparse.ArgumentParser(description="Run pipeline integration tests")
    parser.add_argument('--phase', type=int, help='Test only specific phase (e.g., 3 for Phase 3)')
    parser.add_argument('--outputs-dir', default='outputs', help='Path to outputs directory')
    parser.add_argument('--save-report', action='store_true', help='Save validation report to JSON')
    
    args = parser.parse_args()
    
    print("="*70)
    print("Pipeline Integration Tests")
    print("="*70)
    print(f"\nOutputs directory: {args.outputs_dir}")
    
    outputs_dir = Path(args.outputs_dir)
    if not outputs_dir.exists():
        print(f"\n❌ Outputs directory not found: {outputs_dir}")
        print("   Run the pipeline first to generate output files.")
        sys.exit(1)
    
    tester = PipelineIntegrationTester(outputs_dir)
    report = tester.run_all_tests(phase_filter=args.phase)
    
    report.print_summary()
    
    if args.save_report:
        from utils.pipeline_validators import save_validation_report
        report_path = outputs_dir / 'validation_integration_tests.json'
        save_validation_report(report, report_path)
    
    # Exit with error code if tests failed
    sys.exit(0 if report.passed else 1)


if __name__ == '__main__':
    main()
