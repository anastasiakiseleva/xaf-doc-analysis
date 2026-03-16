#!/usr/bin/env python3
"""
MVP Pipeline Test Runner

Executes the MVP pipeline phases (1, 3, 7, 8, 10) with built-in validation
and generates a comprehensive validation report.

Usage:
    python scripts/run_pipeline_with_validation.py --level quick
    python scripts/run_pipeline_with_validation.py --level full
    python scripts/run_pipeline_with_validation.py --phases 1,3,7  # Run specific phases
"""

import sys
import subprocess
import argparse
import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any


class PipelineRunner:
    """Orchestrates MVP pipeline execution with validation."""
    
    # MVP phases in execution order
    MVP_PHASES = [
        {
            "number": 1,
            "name": "Ingest & Parse",
            "script": "scripts/01_ingest_parse.py",
            "required": True,
            "description": "Parse markdown documents into structured data"
        },
        {
            "number": 2,
            "name": "Build Explicit Graph",
            "script": "scripts/02_build_explicit_graph.py",
            "required": True,
            "description": "Extract and resolve internal document links"
        },
        {
            "number": 3,
            "name": "Extract Concepts",
            "script": "scripts/03_extract_concepts.py",
            "required": True,
            "description": "Tag sections with concepts, APIs, and platforms"
        },
        {
            "number": 7,
            "name": "Generate Metadata",
            "script": "scripts/07_generate_metadata.py",
            "required": True,
            "description": "Generate AI-friendly metadata suggestions"
        },
        {
            "number": 8,
            "name": "Export YAML",
            "script": "scripts/08_export_yaml_metadata.py",
            "required": True,
            "description": "Export YAML frontmatter for documents"
        },
        {
            "number": 10,
            "name": "Rollup Document Metadata",
            "script": "scripts/10_rollup_document_metadata.py",
            "required": True,
            "description": "Aggregate section metadata to document level"
        }
    ]
    
    def __init__(self, project_root: Path, validation_level: str = "quick"):
        self.project_root = project_root
        self.validation_level = validation_level
        self.phase_results = []
        self.start_time = None
        self.end_time = None
    
    def run_phase(self, phase: Dict[str, Any]) -> Dict[str, Any]:
        """
        Run a single pipeline phase with validation.
        
        Returns:
            Dict with phase execution results
        """
        phase_num = phase["number"]
        phase_name = phase["name"]
        script_path = self.project_root / phase["script"]
        
        print(f"\n{'='*70}")
        print(f"Running Phase {phase_num}: {phase_name}")
        print(f"{'='*70}")
        print(f"Script: {script_path}")
        print(f"Description: {phase['description']}")
        
        if not script_path.exists():
            print(f"❌ Script not found: {script_path}")
            return {
                "phase": phase_num,
                "name": phase_name,
                "success": False,
                "error": f"Script not found: {script_path}",
                "duration_seconds": 0
            }
        
        # Build command
        cmd = [sys.executable, str(script_path)]
        
        # Add validation arguments based on level
        if self.validation_level == "quick":
            # Default - validation runs automatically
            pass
        elif self.validation_level == "full":
            cmd.append("--validate-quality")
        elif self.validation_level == "skip":
            cmd.append("--skip-validation")
        
        # Always save reports for aggregation
        cmd.append("--save-report")
        
        # Execute phase
        print(f"\n🚀 Executing: {' '.join(cmd)}")
        phase_start = datetime.now()
        
        try:
            result = subprocess.run(
                cmd,
                cwd=self.project_root,
                capture_output=False,  # Show output in real-time
                text=True,
                check=True
            )
            
            phase_end = datetime.now()
            duration = (phase_end - phase_start).total_seconds()
            
            print(f"\n✅ Phase {phase_num} completed in {duration:.1f} seconds")
            
            return {
                "phase": phase_num,
                "name": phase_name,
                "success": True,
                "error": None,
                "duration_seconds": duration,
                "start_time": phase_start.isoformat(),
                "end_time": phase_end.isoformat()
            }
        
        except subprocess.CalledProcessError as e:
            phase_end = datetime.now()
            duration = (phase_end - phase_start).total_seconds()
            
            error_msg = f"Phase {phase_num} failed with exit code {e.returncode}"
            print(f"\n❌ {error_msg}")
            
            return {
                "phase": phase_num,
                "name": phase_name,
                "success": False,
                "error": error_msg,
                "duration_seconds": duration,
                "start_time": phase_start.isoformat(),
                "end_time": phase_end.isoformat()
            }
    
    def run_integration_tests(self) -> Dict[str, Any]:
        """Run integration tests after pipeline completes."""
        print(f"\n{'='*70}")
        print("Running Integration Tests")
        print(f"{'='*70}")
        
        test_script = self.project_root / "tests" / "test_pipeline_integration.py"
        
        if not test_script.exists():
            print(f"⚠️  Integration test script not found: {test_script}")
            return {
                "success": False,
                "error": "Test script not found",
                "duration_seconds": 0
            }
        
        cmd = [sys.executable, str(test_script), "--save-report"]
        
        print(f"🚀 Executing: {' '.join(cmd)}")
        test_start = datetime.now()
        
        try:
            result = subprocess.run(
                cmd,
                cwd=self.project_root,
                capture_output=False,
                text=True,
                check=True
            )
            
            test_end = datetime.now()
            duration = (test_end - test_start).total_seconds()
            
            print(f"\n✅ Integration tests passed in {duration:.1f} seconds")
            
            return {
                "success": True,
                "error": None,
                "duration_seconds": duration
            }
        
        except subprocess.CalledProcessError as e:
            test_end = datetime.now()
            duration = (test_end - test_start).total_seconds()
            
            error_msg = f"Integration tests failed with exit code {e.returncode}"
            print(f"\n⚠️  {error_msg}")
            
            return {
                "success": False,
                "error": error_msg,
                "duration_seconds": duration
            }
    
    def run_pipeline(self, phase_filter: List[int] = None) -> bool:
        """
        Run the complete MVP pipeline.
        
        Args:
            phase_filter: Optional list of phase numbers to run (e.g., [1, 3])
        
        Returns:
            True if all phases succeeded, False otherwise
        """
        self.start_time = datetime.now()
        print(f"\n{'#'*70}")
        print("MVP Pipeline Execution with Validation")
        print(f"{'#'*70}")
        print(f"Start time: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Validation level: {self.validation_level}")
        print(f"Project root: {self.project_root}")
        
        # Filter phases if requested
        phases_to_run = self.MVP_PHASES
        if phase_filter:
            phases_to_run = [p for p in self.MVP_PHASES if p["number"] in phase_filter]
            print(f"Running phases: {', '.join(str(p['number']) for p in phases_to_run)}")
        
        # Run each phase
        all_succeeded = True
        for phase in phases_to_run:
            result = self.run_phase(phase)
            self.phase_results.append(result)
            
            if not result["success"] and phase["required"]:
                print(f"\n❌ Required phase {phase['number']} failed. Stopping pipeline.")
                all_succeeded = False
                break
        
        # Run integration tests if all phases succeeded
        integration_result = None
        if all_succeeded and not phase_filter:  # Only run integration tests for full pipeline
            integration_result = self.run_integration_tests()
            if not integration_result["success"]:
                all_succeeded = False
        
        self.end_time = datetime.now()
        total_duration = (self.end_time - self.start_time).total_seconds()
        
        # Print summary
        self.print_summary(integration_result, total_duration)
        
        # Save comprehensive report
        self.save_comprehensive_report(integration_result, total_duration)
        
        return all_succeeded
    
    def print_summary(self, integration_result: Dict[str, Any], total_duration: float):
        """Print execution summary."""
        print(f"\n{'#'*70}")
        print("Pipeline Execution Summary")
        print(f"{'#'*70}")
        
        print(f"\nTotal duration: {total_duration / 60:.1f} minutes ({total_duration:.0f} seconds)")
        print(f"\nPhase Results:")
        print(f"{'─'*70}")
        
        for result in self.phase_results:
            status = "✅" if result["success"] else "❌"
            duration = result["duration_seconds"]
            print(f"{status} Phase {result['phase']}: {result['name']:<30} ({duration:.1f}s)")
            if result.get("error"):
                print(f"   └─ Error: {result['error']}")
        
        if integration_result:
            status = "✅" if integration_result["success"] else "⚠️"
            duration = integration_result["duration_seconds"]
            print(f"{status} Integration Tests{'':<35} ({duration:.1f}s)")
        
        print(f"{'─'*70}")
        
        succeeded = sum(1 for r in self.phase_results if r["success"])
        total = len(self.phase_results)
        
        print(f"\n📊 Statistics:")
        print(f"   Phases run: {total}")
        print(f"   Succeeded: {succeeded}")
        print(f"   Failed: {total - succeeded}")
        
        if succeeded == total and (integration_result is None or integration_result["success"]):
            print(f"\n✅ Pipeline completed successfully!")
        else:
            print(f"\n❌ Pipeline completed with errors.")
    
    def save_comprehensive_report(self, integration_result: Dict[str, Any], total_duration: float):
        """Save comprehensive validation report."""
        outputs_dir = self.project_root / "outputs"
        outputs_dir.mkdir(exist_ok=True)
        
        report_path = outputs_dir / "pipeline_validation_report.json"
        
        # Collect individual phase reports
        phase_reports = []
        for result in self.phase_results:
            phase_num = result["phase"]
            report_file = outputs_dir / f"validation_phase{phase_num}.json"
            
            if report_file.exists():
                with open(report_file, 'r') as f:
                    phase_reports.append(json.load(f))
        
        # Collect integration test report
        integration_report = None
        integration_report_file = outputs_dir / "validation_integration_tests.json"
        if integration_report_file.exists():
            with open(integration_report_file, 'r') as f:
                integration_report = json.load(f)
        
        # Build comprehensive report
        comprehensive_report = {
            "pipeline_execution": {
                "start_time": self.start_time.isoformat(),
                "end_time": self.end_time.isoformat(),
                "total_duration_seconds": total_duration,
                "validation_level": self.validation_level,
                "phases_run": len(self.phase_results),
                "phases_succeeded": sum(1 for r in self.phase_results if r["success"]),
                "overall_success": all(r["success"] for r in self.phase_results)
            },
            "phase_results": self.phase_results,
            "phase_validation_reports": phase_reports,
            "integration_tests": integration_result,
            "integration_test_report": integration_report
        }
        
        with open(report_path, 'w') as f:
            json.dump(comprehensive_report, f, indent=2)
        
        print(f"\n📄 Comprehensive validation report saved to: {report_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Run MVP pipeline with integrated validation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Run full MVP pipeline with quick validation (default)
    python scripts/run_pipeline_with_validation.py
    
    # Run with comprehensive quality checks
    python scripts/run_pipeline_with_validation.py --level full
    
    # Run specific phases only
    python scripts/run_pipeline_with_validation.py --phases 1,3,7
    
    # Skip validation (fast run)
    python scripts/run_pipeline_with_validation.py --level skip
        """
    )
    
    parser.add_argument(
        '--level',
        choices=['quick', 'full', 'skip'],
        default='quick',
        help='Validation level: quick (Level 1), full (Level 1+2), skip (no validation)'
    )
    
    parser.add_argument(
        '--phases',
        type=str,
        help='Comma-separated list of phase numbers to run (e.g., "1,3,7")'
    )
    
    parser.add_argument(
        '--project-root',
        type=Path,
        default=Path(__file__).parent.parent,
        help='Path to project root directory'
    )
    
    args = parser.parse_args()
    
    # Parse phase filter
    phase_filter = None
    if args.phases:
        try:
            phase_filter = [int(p.strip()) for p in args.phases.split(',')]
        except ValueError:
            print(f"❌ Invalid phase list: {args.phases}")
            print("   Expected comma-separated integers (e.g., '1,3,7')")
            sys.exit(1)
    
    # Run pipeline
    runner = PipelineRunner(args.project_root, args.level)
    success = runner.run_pipeline(phase_filter)
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
