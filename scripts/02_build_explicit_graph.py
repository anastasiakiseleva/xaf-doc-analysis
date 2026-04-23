# scripts/02_build_explicit_graph.py
# Builds the explicit link graph from Phase 1 inventory.
# - Internal edges: resolved (uid -> doc_id)
# - External edges: unresolved UIDs kept with bucket + optional target_url
#
# Outputs (Parquet):
#   outputs/explicit_graph.parquet                 (internal-only)
#   outputs/explicit_unresolved_uid_edges.parquet  (external-only, with bucket/URL)
#   outputs/explicit_graph_all.parquet             (combined)
#
# Customize external URL mapping via config/patterns.yml (optional).

from __future__ import annotations

import re
import sys
import argparse
import pathlib
from collections.abc import Iterable
from typing import Any, List, Optional, Tuple, TypedDict, Literal

import pandas as pd

# Add parent directory to path for validation imports
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from utils.pipeline_validators import (
    PipelineValidator, ValidationReport, ValidationResult,
    save_validation_report, load_validation_thresholds
)

try:
    import yaml  # Optional; if missing, defaults are used
except Exception:  # pragma: no cover
    yaml = None

INV_PATH = "outputs/topics_inventory.parquet"
OUT_INTERNAL = "outputs/explicit_graph.parquet"
OUT_UNRESOLVED = "outputs/explicit_unresolved_uid_edges.parquet"
OUT_COMBINED = "outputs/explicit_graph_all.parquet"
ENGINE = "pyarrow"  # or "fastparquet"

CONFIG_PATH = pathlib.Path("config/patterns.yml")


# -----------------------------
# Typed config structures
# -----------------------------
class UrlRule(TypedDict, total=False):
    match: Literal["regex", "prefix", "substring"]
    value: str
    bucket: str
    url_fmt: Optional[str]


# -----------------------------
# Helpers
# -----------------------------
def as_list(x: Any) -> List[Any]:
    """Return a real Python list for any iterable that isn't a scalar or dict."""
    if x is None:
        return []
    # Handle pandas NaN and other floats
    if isinstance(x, float):
        try:
            import math
            return [] if math.isnan(x) else []
        except Exception:
            return []
    if isinstance(x, (str, bytes, dict)):
        s = x.strip() if isinstance(x, str) else None
        return [s] if s else []
    if isinstance(x, Iterable):
        try:
            return list(x)
        except TypeError:
            return []
    try:
        return list(x)
    except Exception:
        return []


def normalize_uid_series(s: pd.Series) -> pd.Series:
    return s.astype(str).str.replace(r"\s+", " ", regex=True).str.strip()


def load_inventory() -> pd.DataFrame:
    inv = pd.read_parquet(INV_PATH, engine=ENGINE).copy()

    # Ensure list columns are real lists
    if "internal_links" in inv.columns:
        inv["internal_links"] = inv["internal_links"].apply(as_list)
    else:
        inv["internal_links"] = [[] for _ in range(len(inv))]

    if "internal_doc_links" in inv.columns:
        inv["internal_doc_links"] = inv["internal_doc_links"].apply(as_list)

    # Normalize identifiers
    inv["uid_norm"] = normalize_uid_series(inv.get("uid", pd.Series([None] * len(inv))))
    inv["doc_id"] = inv["doc_id"].astype(str)

    # Diagnostics
    has_links = inv["internal_links"].apply(lambda v: len(v) > 0)
    print(f"Inventory rows: {len(inv)} | rows with non-empty internal_links: {int(has_links.sum())}")

    return inv


def build_uid_to_doc(inv: pd.DataFrame) -> pd.Series:
    uid_map = (
        inv.loc[inv["uid_norm"].str.len() > 0, ["uid_norm", "doc_id"]]
           .drop_duplicates("uid_norm")
           .set_index("uid_norm")["doc_id"]
    )
    print(f"UIDs in inventory (unique, non-empty): {len(uid_map)}")
    return uid_map


# -----------------------------
# External URL mapping / classification
# -----------------------------
def load_external_url_rules() -> List[UrlRule]:
    """
    Try to load URL mapping/classification rules from config/patterns.yml.

    Schema (per rule):
      - match: "regex" | "prefix" | "substring"
      - value: pattern/prefix/text
      - bucket: string (e.g., ".net_bcl", "kb_numeric", "xpo")
      - url_fmt: string with '{uid}' placeholder (optional)
    """
    if yaml is None or not CONFIG_PATH.exists():
        return []

    try:
        data = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8")) or {}
        raw_rules = data.get("external_url_rules", []) or []
        rules: List[UrlRule] = []
        for r in raw_rules:
            match = str(r.get("match", "")).strip().lower()
            value = str(r.get("value", "")).strip()
            bucket = str(r.get("bucket", "unknown")).strip() or "unknown"
            url_fmt = r.get("url_fmt", None)
            if match in {"regex", "prefix", "substring"} and value:
                rule: UrlRule = {"match": match, "value": value, "bucket": bucket}  # type: ignore
                # only set url_fmt if provided
                if isinstance(url_fmt, str) and url_fmt:
                    rule["url_fmt"] = url_fmt
                rules.append(rule)
        if rules:
            print(f"Loaded {len(rules)} external URL rule(s) from {CONFIG_PATH}")
        return rules
    except Exception as e:  # pragma: no cover
        print(f"Warning: could not read {CONFIG_PATH}: {e}")
        return []


# Built-in defaults — generic rules only; product-specific rules belong in config/patterns.yml
DEFAULT_URL_RULES: List[UrlRule] = [
    {"match": "prefix", "value": "System.", "bucket": ".net_bcl", "url_fmt": "https://learn.microsoft.com/dotnet/api/{uid}"},
    # Leave these without url_fmt by default—define in config/patterns.yml for your canonical hosts.
    {"match": "regex", "value": r"^\d+$", "bucket": "kb_numeric"},
]


def classify_and_url_for_uid(uid: str, rules: List[UrlRule]) -> Tuple[str, Optional[str]]:
    """Return (bucket, target_url) for an unresolved UID using provided rules."""
    u = str(uid).strip()

    # Try config rules first
    for r in rules:
        mtype = r.get("match", "")
        val = r.get("value", "")
        bucket = r.get("bucket", "unknown") or "unknown"
        fmt = r.get("url_fmt")

        matched = False
        if mtype == "regex":
            try:
                if re.fullmatch(val, u):
                    matched = True
            except re.error:
                pass
        elif mtype == "prefix":
            matched = u.startswith(val)
        elif mtype == "substring":
            matched = val in u

        if matched:
            target_url = (fmt.format(uid=u) if isinstance(fmt, str) and fmt else None)
            return bucket, target_url

    # Fallback to defaults
    for r in DEFAULT_URL_RULES:
        mtype = r.get("match", "")
        val = r.get("value", "")
        bucket = r.get("bucket", "unknown") or "unknown"
        fmt = r.get("url_fmt")

        matched = False
        if mtype == "regex":
            try:
                if re.fullmatch(val, u):
                    matched = True
            except re.error:
                pass
        elif mtype == "prefix":
            matched = u.startswith(val)
        elif mtype == "substring":
            matched = val in u

        if matched:
            target_url = (fmt.format(uid=u) if isinstance(fmt, str) and fmt else None)
            return bucket, target_url

    return "unknown", None


# -----------------------------
# Edge building
# -----------------------------
def build_edges(inv: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Returns:
      edges_df: internal (resolved) edges with counts
      unresolved_df: unresolved targets (with bucket + target_url)
    """
    if inv.empty:
        cols_int = ["source_doc", "target_doc", "count"]
        cols_ext = ["source_doc", "target_uid", "count", "bucket", "target_url"]
        return pd.DataFrame(columns=cols_int), pd.DataFrame(columns=cols_ext)

    uid_to_doc = build_uid_to_doc(inv)

    # Explode UID links
    links = inv.explode("internal_links", ignore_index=True)
    links = links[links["internal_links"].notna() & (links["internal_links"] != "")]
    if links.empty:
        print("No explodable UID links after normalization; nothing to resolve.")
        cols_int = ["source_doc", "target_doc", "count"]
        cols_ext = ["source_doc", "target_uid", "count", "bucket", "target_url"]
        return pd.DataFrame(columns=cols_int), pd.DataFrame(columns=cols_ext)

    # Normalize, map
    links["source_doc"] = links["doc_id"]
    links["target_uid"] = normalize_uid_series(links["internal_links"])
    links["target_doc"] = links["target_uid"].map(uid_to_doc)

    total = len(links)
    resolved = links["target_doc"].notna().sum()
    print(f"Explicit links (UID-based): {total} | resolved: {resolved} ({resolved/total:.1%})")

    # Internal edges (drop self-loops)
    edges = (
        links.dropna(subset=["target_doc"])
             .loc[lambda df: df["source_doc"] != df["target_doc"], :]
             .groupby(["source_doc", "target_doc"], as_index=False)
             .size()
    )
    # Rename 'size' column to 'count' for consistency
    if 'size' in edges.columns:
        edges = edges.rename(columns={'size': 'count'})

    # External edges (unresolved UIDs)
    config_rules = load_external_url_rules()
    unresolved = links[links["target_doc"].isna()].copy()
    
    if not unresolved.empty:
        unresolved[["bucket", "target_url"]] = unresolved["target_uid"].apply(
            lambda uid: pd.Series(classify_and_url_for_uid(uid, config_rules))
        )
        unresolved_grouped = (
            unresolved.groupby(["source_doc", "target_uid", "bucket", "target_url"], as_index=False)
                      .size()
        )
        # Rename 'size' column to 'count' for consistency
        if 'size' in unresolved_grouped.columns:
            unresolved_grouped = unresolved_grouped.rename(columns={'size': 'count'})
    else:
        unresolved_grouped = pd.DataFrame(columns=["source_doc", "target_uid", "count", "bucket", "target_url"])

    print(f"Internal edges (resolved): {len(edges)} | External edges (unresolved): {len(unresolved_grouped)}")
    
    return edges, unresolved_grouped


def validate_phase2_output(
    edges_df: pd.DataFrame,
    unresolved_df: pd.DataFrame,
    combined_df: pd.DataFrame,
    inv_df: pd.DataFrame,
    run_quality_checks: bool = False
) -> ValidationReport:
    """
    Validate Phase 2 output data.
    
    Args:
        edges_df: Internal (resolved) edges DataFrame
        unresolved_df: External (unresolved) edges DataFrame
        combined_df: Combined edges DataFrame
        inv_df: Input inventory DataFrame
        run_quality_checks: Whether to run deeper quality validation
    
    Returns:
        ValidationReport with validation results
    """
    config_path = pathlib.Path(__file__).resolve().parents[1] / "config" / "validation_thresholds.yml"
    validator = PipelineValidator(config_path)
    report = ValidationReport(phase_name="Build Explicit Graph", phase_number=2)
    
    # Level 1: Quick Sanity Checks
    print("\n🔍 Running Level 1 validation (quick sanity checks)...")
    
    # Check internal edges schema
    required_cols_internal = ["source_doc", "target_doc", "count"]
    column_types_internal = {
        "source_doc": str,
        "target_doc": str,
        "count": int
    }
    report.add_result(validator.validate_schema(
        edges_df, required_cols_internal, column_types_internal, "Internal edges schema"
    ))
    
    # Check unresolved edges schema
    required_cols_unresolved = ["source_doc", "target_uid", "count", "bucket", "target_url"]
    column_types_unresolved = {
        "source_doc": str,
        "target_uid": str,
        "count": int,
        "bucket": str
    }
    report.add_result(validator.validate_schema(
        unresolved_df, required_cols_unresolved, column_types_unresolved, "Unresolved edges schema"
    ))
    
    # Check row counts
    thresholds = load_validation_thresholds(config_path)
    
    total_edges = len(edges_df) + len(unresolved_df)
    if total_edges > 0:
        resolution_rate = (len(edges_df) / total_edges * 100) if total_edges > 0 else 0
        
        report.add_result(validator.validate_threshold(
            actual_value=resolution_rate,
            threshold_key='min_resolution_rate',
            phase_key='phase2_graph',
            comparison='>=',
            check_name="Link resolution rate"
        ))
    else:
        report.add_result(ValidationResult(
            check_name="Link resolution rate",
            passed=False,
            message="No links found in input data",
            severity="error"
        ))
    
    # Check for self-loops
    if len(edges_df) > 0:
        # Should already be filtered, but verify
        self_loops = edges_df[edges_df['source_doc'] == edges_df['target_doc']]
        if len(self_loops) > 0:
            report.add_result(ValidationResult(
                check_name="Self-loop check",
                passed=False,
                message=f"Found {len(self_loops)} self-loops (should be filtered)",
                severity="error",
                details={"self_loop_count": len(self_loops)}
            ))
        else:
            report.add_result(ValidationResult(
                check_name="Self-loop check",
                passed=True,
                message="No self-loops found (correctly filtered)",
                severity="info"
            ))
    
    # Check connected documents
    if len(edges_df) > 0:
        connected_docs = set(edges_df['source_doc'].unique()) | set(edges_df['target_doc'].unique())
        report.add_result(validator.validate_threshold(
            actual_value=len(connected_docs),
            threshold_key='min_connected_docs',
            phase_key='phase2_graph',
            comparison='>=',
            check_name="Minimum connected documents"
        ))
    
    if run_quality_checks:
        print("\n🔍 Running Level 2 validation (quality checks)...")
        
        # Validate that all source/target docs exist in inventory
        inv_docs = set(inv_df['doc_id'].unique())
        
        if len(edges_df) > 0:
            invalid_sources = set(edges_df['source_doc'].unique()) - inv_docs
            invalid_targets = set(edges_df['target_doc'].unique()) - inv_docs
            
            if invalid_sources or invalid_targets:
                report.add_result(ValidationResult(
                    check_name="Document references validation",
                    passed=False,
                    message=f"Found invalid doc_ids: {len(invalid_sources)} sources, {len(invalid_targets)} targets",
                    severity="error",
                    details={
                        "invalid_sources": len(invalid_sources),
                        "invalid_targets": len(invalid_targets),
                        "sample": list((invalid_sources | invalid_targets))[:5]
                    }
                ))
            else:
                report.add_result(ValidationResult(
                    check_name="Document references validation",
                    passed=True,
                    message=f"All {len(set(edges_df['source_doc'].unique()) | set(edges_df['target_doc'].unique()))} referenced documents exist in inventory",
                    severity="info"
                ))
        
        # Check for duplicate edges
        if len(edges_df) > 0:
            duplicates = edges_df.duplicated(subset=['source_doc', 'target_doc'], keep=False)
            dup_count = duplicates.sum()
            
            if dup_count > 0:
                report.add_result(ValidationResult(
                    check_name="Duplicate edge detection",
                    passed=False,
                    message=f"Found {dup_count} duplicate edges",
                    severity="error"
                ))
            else:
                report.add_result(ValidationResult(
                    check_name="Duplicate edge detection",
                    passed=True,
                    message="No duplicate edges found",
                    severity="info"
                ))
        
        # Check unresolved UID buckets distribution
        if len(unresolved_df) > 0:
            bucket_dist = unresolved_df['bucket'].value_counts().to_dict()
            report.add_result(ValidationResult(
                check_name="Unresolved UID bucket distribution",
                passed=True,
                message=f"Unresolved UIDs categorized into {len(bucket_dist)} buckets",
                severity="info",
                details=bucket_dist
            ))
        
        # Validate combined DataFrame completeness
        expected_total = len(edges_df) + len(unresolved_df)
        actual_total = len(combined_df)
        
        if expected_total != actual_total:
            report.add_result(ValidationResult(
                check_name="Combined edges completeness",
                passed=False,
                message=f"Combined edges count {actual_total} doesn't match sum {expected_total}",
                severity="error",
                details={"expected": expected_total, "actual": actual_total}
            ))
        else:
            report.add_result(ValidationResult(
                check_name="Combined edges completeness",
                passed=True,
                message=f"Combined edges complete: {actual_total:,} total edges",
                severity="info"
            ))
    
    return report


def main():
    parser = argparse.ArgumentParser(description="Phase 2: Build explicit link graph")
    parser.add_argument('--skip-validation', action='store_true', help='Skip validation checks')
    parser.add_argument('--validate-quality', action='store_true', help='Run deeper quality validation (Level 2)')
    parser.add_argument('--save-report', action='store_true', help='Save validation report to JSON')
    args = parser.parse_args()
    
    print("="*70)
    print("Phase 2: Build Explicit Graph")
    print("="*70)
    
    # Load inventory
    print("\n📚 Loading topics inventory...")
    inv = load_inventory()
    
    if inv.empty:
        print("❌ Empty inventory. Run Phase 1 first.")
        sys.exit(1)
    
    # Build edges
    print("\n🔗 Building explicit link graph...")
    edges, unresolved = build_edges(inv)
    
    # Combine for "all" view
    print("\n📦 Combining internal and external edges...")
    edges_for_combined = edges.copy()
    edges_for_combined["edge_type"] = "internal"
    edges_for_combined["target_uid"] = None
    edges_for_combined["bucket"] = None
    edges_for_combined["target_url"] = None
    
    unresolved_for_combined = unresolved.copy()
    unresolved_for_combined["edge_type"] = "external"
    unresolved_for_combined["target_doc"] = None
    
    combined = pd.concat([edges_for_combined, unresolved_for_combined], ignore_index=True)
    
    # Save outputs
    print("\n💾 Saving outputs...")
    pathlib.Path("outputs").mkdir(parents=True, exist_ok=True)
    
    edges.to_parquet(OUT_INTERNAL, index=False, engine=ENGINE)
    print(f"   └─ Internal edges: {OUT_INTERNAL} ({len(edges):,} edges)")
    
    unresolved.to_parquet(OUT_UNRESOLVED, index=False, engine=ENGINE)
    print(f"   └─ Unresolved edges: {OUT_UNRESOLVED} ({len(unresolved):,} edges)")
    
    combined.to_parquet(OUT_COMBINED, index=False, engine=ENGINE)
    print(f"   └─ Combined edges: {OUT_COMBINED} ({len(combined):,} edges)")
    
    # Summary statistics
    print("\n📊 Summary Statistics:")
    total_links = len(edges) + len(unresolved)
    if total_links > 0:
        print(f"   └─ Total links: {total_links:,}")
        print(f"   └─ Resolved (internal): {len(edges):,} ({len(edges)/total_links*100:.1f}%)")
        print(f"   └─ Unresolved (external): {len(unresolved):,} ({len(unresolved)/total_links*100:.1f}%)")
        print(f"   └─ Unique source documents: {edges['source_doc'].nunique():,}" if len(edges) > 0 else "")
        print(f"   └─ Unique target documents: {edges['target_doc'].nunique():,}" if len(edges) > 0 else "")
    
    # Run validation
    if not args.skip_validation:
        report = validate_phase2_output(edges, unresolved, combined, inv, run_quality_checks=args.validate_quality)
        report.print_summary()
        
        if args.save_report:
            report_path = pathlib.Path('outputs/validation_phase2.json')
            save_validation_report(report, report_path)
        
        if report.has_errors:
            print("\n❌ Phase 2 validation failed with errors. Review issues above.")
            sys.exit(1)
    else:
        print("\n⏭️  Validation skipped")
    
    print("\n✅ Phase 2 complete!")


if __name__ == "__main__":
    main()
