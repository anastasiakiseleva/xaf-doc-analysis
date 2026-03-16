#!/usr/bin/env python3
"""
Knowledge Graph Pipeline Runner (with validation)

Why this exists
---------------
The existing runner (scripts/run_pipeline_with_validation.py) targets the metadata/YAML
export deliverables. This runner targets the *knowledge graph* as the primary artifact
without removing or breaking the API mapping + metadata pipeline.

Pipeline phases (default order)
------------------------------
1  - Ingest & Parse                   -> outputs/topics_inventory.parquet
2  - Build Explicit Graph             -> outputs/explicit_graph*.parquet
3  - Extract Concepts/APIs/Platforms  -> outputs/doc_concepts.parquet
4  - Make Embeddings                  -> outputs/sections_embeddings_*.parquet
5  - Find Semantic Pairs              -> outputs/semantic_pairs.parquet
11 - Extract API Entities             -> outputs/api_entities.parquet, outputs/documents_api.parquet
12 - Map APIs to Concepts             -> outputs/api_implements_concept.parquet
13 - Build Knowledge Graph            -> outputs/knowledge_graph.json

Optional:
6  - Classify Relationships (LLM)     -> outputs/classified_pairs*.parquet
     (Only run if you have provider configured; graph builder will use it if present.)

Usage
-----
python scripts/run_kg_pipeline_with_validation.py --level quick
python scripts/run_kg_pipeline_with_validation.py --level full
python scripts/run_kg_pipeline_with_validation.py --phases 1,2,3,11,12,13
"""

import sys
import subprocess
import argparse
import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any


class PipelineRunner:
    KG_PHASES = [
        {"number": 1, "name": "Ingest & Parse", "script": "scripts/01_ingest_parse.py", "required": True},
        {"number": 2, "name": "Build Explicit Graph", "script": "scripts/02_build_explicit_graph.py", "required": True},
        {"number": 3, "name": "Extract Concepts", "script": "scripts/03_extract_concepts.py", "required": True},
        {"number": 4, "name": "Make Embeddings", "script": "scripts/04_make_sections_embeddings.py", "required": True},
        {"number": 5, "name": "Find Semantic Pairs", "script": "scripts/05_find_semantic_pairs.py", "required": True},
        {"number": 11, "name": "Extract API Entities", "script": "scripts/11_extract_api_entities.py", "required": True},
        {"number": 12, "name": "Map APIs to Concepts", "script": "scripts/12_map_apis_to_concepts.py", "required": True},
        {"number": 13, "name": "Build Knowledge Graph", "script": "scripts/13_build_knowledge_graph.py", "required": True},
    ]

    def __init__(self, project_root: Path, validation_level: str = "quick"):
        self.project_root = project_root
        self.validation_level = validation_level
        self.phase_results: List[Dict[str, Any]] = []
        self.start_time = None
        self.end_time = None

    def run_phase(self, phase: Dict[str, Any]) -> Dict[str, Any]:
        phase_num = phase["number"]
        phase_name = phase["name"]
        script_path = self.project_root / phase["script"]

        print(f"\n{'='*70}")
        print(f"Running Phase {phase_num}: {phase_name}")
        print(f"{'='*70}")
        print(f"Script: {script_path}")

        if not script_path.exists():
            return {"phase": phase_num, "name": phase_name, "success": False, "error": f"Script not found: {script_path}", "duration_seconds": 0}

        cmd = [sys.executable, str(script_path)]

        # Validation flags convention
        if self.validation_level == "full":
            cmd.append("--validate-quality")
        elif self.validation_level == "skip":
            cmd.append("--skip-validation")

        # Most scripts accept --save-report; embeddings/pairs may not, but tolerate unknown?
        # So only pass --save-report to scripts known to support it.
        if phase_num in {1, 2, 3, 13}:
            cmd.append("--save-report")

        print(f"\n🚀 Executing: {' '.join(cmd)}")
        phase_start = datetime.now()

        try:
            subprocess.run(cmd, cwd=self.project_root, text=True, check=True)
            phase_end = datetime.now()
            duration = (phase_end - phase_start).total_seconds()
            print(f"\n✅ Phase {phase_num} completed in {duration:.1f} seconds")
            return {"phase": phase_num, "name": phase_name, "success": True, "error": None, "duration_seconds": duration}
        except subprocess.CalledProcessError as e:
            phase_end = datetime.now()
            duration = (phase_end - phase_start).total_seconds()
            error_msg = f"Phase {phase_num} failed with exit code {e.returncode}"
            print(f"\n❌ {error_msg}")
            return {"phase": phase_num, "name": phase_name, "success": False, "error": error_msg, "duration_seconds": duration}

    def run_pipeline(self, phase_filter: List[int] | None = None) -> bool:
        self.start_time = datetime.now()
        print(f"\n{'#'*70}")
        print("Knowledge Graph Pipeline Execution")
        print(f"{'#'*70}")
        print(f"Start time: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Validation level: {self.validation_level}")
        print(f"Project root: {self.project_root}")

        phases_to_run = self.KG_PHASES
        if phase_filter:
            phases_to_run = [p for p in self.KG_PHASES if p["number"] in phase_filter]
            print(f"Running phases: {', '.join(str(p['number']) for p in phases_to_run)}")

        all_succeeded = True
        for phase in phases_to_run:
            result = self.run_phase(phase)
            self.phase_results.append(result)
            if not result["success"] and phase["required"]:
                all_succeeded = False
                break

        self.end_time = datetime.now()
        total_duration = (self.end_time - self.start_time).total_seconds()

        self.print_summary(total_duration)
        self.save_report(total_duration)

        return all_succeeded

    def print_summary(self, total_duration: float) -> None:
        print(f"\n{'#'*70}")
        print("KG Pipeline Summary")
        print(f"{'#'*70}")
        print(f"Total duration: {total_duration/60:.1f} minutes")
        for result in self.phase_results:
            status = "✅" if result["success"] else "❌"
            print(f"{status} Phase {result['phase']}: {result['name']:<28} ({result['duration_seconds']:.1f}s)")
            if result.get("error"):
                print(f"   └─ {result['error']}")

    def save_report(self, total_duration: float) -> None:
        outputs_dir = self.project_root / "outputs"
        outputs_dir.mkdir(exist_ok=True)
        report_path = outputs_dir / "kg_pipeline_validation_report.json"
        report = {
            "pipeline": "knowledge-graph",
            "start_time": self.start_time.isoformat() if self.start_time else None,
            "end_time": self.end_time.isoformat() if self.end_time else None,
            "total_duration_seconds": total_duration,
            "validation_level": self.validation_level,
            "phase_results": self.phase_results,
            "overall_success": all(r["success"] for r in self.phase_results),
        }
        report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(f"\n📄 KG pipeline report saved to: {report_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run knowledge graph pipeline with validation")
    parser.add_argument("--level", choices=["quick", "full", "skip"], default="quick")
    parser.add_argument("--phases", type=str, help="Comma-separated phase numbers")
    parser.add_argument("--project-root", type=Path, default=Path(__file__).parent.parent)

    args = parser.parse_args()

    phase_filter = None
    if args.phases:
        phase_filter = [int(p.strip()) for p in args.phases.split(",") if p.strip()]

    runner = PipelineRunner(args.project_root, args.level)
    success = runner.run_pipeline(phase_filter)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
