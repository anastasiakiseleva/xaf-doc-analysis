#!/usr/bin/env python3
"""
Shared validation utilities for XAF Documentation Analysis Pipeline.

Provides reusable validation functions for checking data quality, schemas,
foreign key relationships, and threshold compliance across all pipeline phases.
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import Dict, List, Any, Optional, Callable, Union
from dataclasses import dataclass, field
from datetime import datetime
import yaml
import json


@dataclass
class ValidationResult:
    """Result of a single validation check."""
    check_name: str
    passed: bool
    message: str
    severity: str = "error"  # error, warning, info
    details: Optional[Dict[str, Any]] = None
    
    def __str__(self):
        symbol = "✅" if self.passed else ("⚠️" if self.severity == "warning" else "❌")
        return f"{symbol} {self.check_name}: {self.message}"


@dataclass
class ValidationReport:
    """Comprehensive validation report for a pipeline phase."""
    phase_name: str
    phase_number: int
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    results: List[ValidationResult] = field(default_factory=list)
    
    def add_result(self, result: ValidationResult):
        """Add a validation result to the report."""
        self.results.append(result)
    
    @property
    def passed(self) -> bool:
        """Check if all critical validations passed."""
        return all(r.passed or r.severity == "warning" for r in self.results)
    
    @property
    def has_warnings(self) -> bool:
        """Check if there are any warnings."""
        return any(not r.passed and r.severity == "warning" for r in self.results)
    
    @property
    def has_errors(self) -> bool:
        """Check if there are any errors."""
        return any(not r.passed and r.severity == "error" for r in self.results)
    
    def print_summary(self):
        """Print a formatted summary of the validation report."""
        print(f"\n{'='*70}")
        print(f"Validation Report: Phase {self.phase_number} - {self.phase_name}")
        print(f"{'='*70}")
        
        for result in self.results:
            print(result)
            if result.details:
                for key, value in result.details.items():
                    print(f"  └─ {key}: {value}")
        
        print(f"\n{'─'*70}")
        errors = sum(1 for r in self.results if not r.passed and r.severity == "error")
        warnings = sum(1 for r in self.results if not r.passed and r.severity == "warning")
        passed = sum(1 for r in self.results if r.passed)
        
        print(f"Summary: {passed} passed, {warnings} warnings, {errors} errors")
        
        if self.passed:
            if self.has_warnings:
                print("⚠️  PASSED WITH WARNINGS")
            else:
                print("✅ ALL VALIDATIONS PASSED")
        else:
            print("❌ VALIDATION FAILED")
        print(f"{'='*70}\n")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert report to dictionary for JSON serialization."""
        return {
            "phase_name": self.phase_name,
            "phase_number": self.phase_number,
            "timestamp": self.timestamp,
            "passed": self.passed,
            "has_warnings": self.has_warnings,
            "has_errors": self.has_errors,
            "results": [
                {
                    "check_name": r.check_name,
                    "passed": r.passed,
                    "message": r.message,
                    "severity": r.severity,
                    "details": r.details
                }
                for r in self.results
            ]
        }


class PipelineValidator:
    """Main validator class with reusable validation methods."""
    
    def __init__(self, thresholds_path: Optional[Path] = None):
        """
        Initialize validator with optional thresholds config.
        
        Args:
            thresholds_path: Path to validation_thresholds.yml file
        """
        self.thresholds = {}
        if thresholds_path and thresholds_path.exists():
            with open(thresholds_path, 'r') as f:
                self.thresholds = yaml.safe_load(f) or {}
    
    def validate_schema(
        self,
        df: pd.DataFrame,
        required_columns: List[str],
        column_types: Optional[Dict[str, type]] = None,
        check_name: str = "Schema validation"
    ) -> ValidationResult:
        """
        Validate DataFrame schema (required columns and types).
        
        Args:
            df: DataFrame to validate
            required_columns: List of required column names
            column_types: Optional dict mapping column names to expected types
            check_name: Name for this validation check
        
        Returns:
            ValidationResult indicating success or failure
        """
        missing_cols = [col for col in required_columns if col not in df.columns]
        
        if missing_cols:
            return ValidationResult(
                check_name=check_name,
                passed=False,
                message=f"Missing required columns: {missing_cols}",
                severity="error",
                details={"missing_columns": missing_cols, "found_columns": list(df.columns)}
            )
        
        # Check types if provided
        if column_types:
            type_mismatches = []
            for col, expected_type in column_types.items():
                if col in df.columns:
                    if expected_type == list:
                        # Check if column contains list-like objects
                        sample = df[col].iloc[0] if len(df) > 0 else None
                        if sample is not None and not isinstance(sample, (list, np.ndarray)):
                            type_mismatches.append(f"{col} (expected list, got {type(sample).__name__})")
                    elif expected_type == str:
                        if df[col].dtype not in ['object', 'string']:
                            type_mismatches.append(f"{col} (expected str, got {df[col].dtype})")
                    elif expected_type in [int, float]:
                        if not pd.api.types.is_numeric_dtype(df[col]):
                            type_mismatches.append(f"{col} (expected numeric, got {df[col].dtype})")
            
            if type_mismatches:
                return ValidationResult(
                    check_name=check_name,
                    passed=False,
                    message=f"Type mismatches found: {len(type_mismatches)}",
                    severity="error",
                    details={"type_mismatches": type_mismatches}
                )
        
        return ValidationResult(
            check_name=check_name,
            passed=True,
            message=f"All {len(required_columns)} required columns present with correct types",
            severity="info"
        )
    
    def validate_row_count(
        self,
        df: pd.DataFrame,
        min_rows: Optional[int] = None,
        max_rows: Optional[int] = None,
        check_name: str = "Row count validation"
    ) -> ValidationResult:
        """
        Validate DataFrame has acceptable number of rows.
        
        Args:
            df: DataFrame to validate
            min_rows: Minimum acceptable row count
            max_rows: Maximum acceptable row count
            check_name: Name for this validation check
        
        Returns:
            ValidationResult indicating success or failure
        """
        row_count = len(df)
        
        if min_rows is not None and row_count < min_rows:
            return ValidationResult(
                check_name=check_name,
                passed=False,
                message=f"Row count {row_count:,} below minimum {min_rows:,}",
                severity="error",
                details={"row_count": row_count, "min_rows": min_rows}
            )
        
        if max_rows is not None and row_count > max_rows:
            return ValidationResult(
                check_name=check_name,
                passed=False,
                message=f"Row count {row_count:,} exceeds maximum {max_rows:,}",
                severity="warning",
                details={"row_count": row_count, "max_rows": max_rows}
            )
        
        return ValidationResult(
            check_name=check_name,
            passed=True,
            message=f"Row count {row_count:,} is within acceptable range",
            severity="info",
            details={"row_count": row_count}
        )
    
    def validate_range(
        self,
        df: pd.DataFrame,
        column: str,
        min_value: Optional[float] = None,
        max_value: Optional[float] = None,
        allow_null: bool = False,
        check_name: Optional[str] = None
    ) -> ValidationResult:
        """
        Validate numeric column values are within expected range.
        
        Args:
            df: DataFrame to validate
            column: Column name to check
            min_value: Minimum acceptable value
            max_value: Maximum acceptable value
            allow_null: Whether null values are acceptable
            check_name: Name for this validation check
        
        Returns:
            ValidationResult indicating success or failure
        """
        if check_name is None:
            check_name = f"Range validation for {column}"
        
        if column not in df.columns:
            return ValidationResult(
                check_name=check_name,
                passed=False,
                message=f"Column {column} not found",
                severity="error"
            )
        
        series = df[column]
        
        # Check for nulls
        null_count = series.isnull().sum()
        if null_count > 0 and not allow_null:
            return ValidationResult(
                check_name=check_name,
                passed=False,
                message=f"Found {null_count} null values in {column}",
                severity="error",
                details={"null_count": int(null_count), "total_rows": len(df)}
            )
        
        # Filter out nulls for range checking
        valid_series = series.dropna()
        
        if len(valid_series) == 0:
            return ValidationResult(
                check_name=check_name,
                passed=True,
                message=f"No non-null values to validate in {column}",
                severity="info"
            )
        
        # Check range
        actual_min = valid_series.min()
        actual_max = valid_series.max()
        
        if min_value is not None and actual_min < min_value:
            return ValidationResult(
                check_name=check_name,
                passed=False,
                message=f"{column} minimum {actual_min:.4f} below threshold {min_value}",
                severity="error",
                details={"actual_min": float(actual_min), "threshold_min": min_value}
            )
        
        if max_value is not None and actual_max > max_value:
            return ValidationResult(
                check_name=check_name,
                passed=False,
                message=f"{column} maximum {actual_max:.4f} exceeds threshold {max_value}",
                severity="error",
                details={"actual_max": float(actual_max), "threshold_max": max_value}
            )
        
        return ValidationResult(
            check_name=check_name,
            passed=True,
            message=f"{column} values in range [{actual_min:.4f}, {actual_max:.4f}]",
            severity="info",
            details={"min": float(actual_min), "max": float(actual_max)}
        )
    
    def validate_foreign_key(
        self,
        df: pd.DataFrame,
        column: str,
        reference_df: pd.DataFrame,
        reference_column: str,
        check_name: Optional[str] = None,
        sample_size: int = 5
    ) -> ValidationResult:
        """
        Validate foreign key relationship between DataFrames.
        
        Args:
            df: DataFrame with foreign key column
            column: Foreign key column name
            reference_df: Reference DataFrame
            reference_column: Reference column name
            check_name: Name for this validation check
            sample_size: Number of invalid keys to include in details
        
        Returns:
            ValidationResult indicating success or failure
        """
        if check_name is None:
            check_name = f"Foreign key validation: {column} -> {reference_column}"
        
        if column not in df.columns:
            return ValidationResult(
                check_name=check_name,
                passed=False,
                message=f"Column {column} not found in source DataFrame",
                severity="error"
            )
        
        if reference_column not in reference_df.columns:
            return ValidationResult(
                check_name=check_name,
                passed=False,
                message=f"Column {reference_column} not found in reference DataFrame",
                severity="error"
            )
        
        # Get unique values
        fk_values = set(df[column].dropna().unique())
        ref_values = set(reference_df[reference_column].dropna().unique())
        
        # Find invalid foreign keys
        invalid_keys = fk_values - ref_values
        
        if invalid_keys:
            invalid_count = len(invalid_keys)
            sample_invalid = list(invalid_keys)[:sample_size]
            
            return ValidationResult(
                check_name=check_name,
                passed=False,
                message=f"Found {invalid_count} invalid foreign key values",
                severity="error",
                details={
                    "invalid_count": invalid_count,
                    "total_fk_values": len(fk_values),
                    "sample_invalid": sample_invalid
                }
            )
        
        return ValidationResult(
            check_name=check_name,
            passed=True,
            message=f"All {len(fk_values)} foreign key values are valid",
            severity="info",
            details={"validated_values": len(fk_values)}
        )
    
    def validate_no_duplicates(
        self,
        df: pd.DataFrame,
        subset: Optional[List[str]] = None,
        check_name: str = "Duplicate detection"
    ) -> ValidationResult:
        """
        Validate DataFrame has no duplicate rows.
        
        Args:
            df: DataFrame to validate
            subset: Optional list of columns to check for duplicates
            check_name: Name for this validation check
        
        Returns:
            ValidationResult indicating success or failure
        """
        duplicates = df.duplicated(subset=subset, keep=False)
        dup_count = duplicates.sum()
        
        if dup_count > 0:
            dup_rows = df[duplicates]
            sample_size = min(3, len(dup_rows))
            
            return ValidationResult(
                check_name=check_name,
                passed=False,
                message=f"Found {dup_count} duplicate rows",
                severity="error",
                details={
                    "duplicate_count": int(dup_count),
                    "total_rows": len(df),
                    "checked_columns": subset or "all columns"
                }
            )
        
        return ValidationResult(
            check_name=check_name,
            passed=True,
            message="No duplicates found",
            severity="info",
            details={"checked_columns": subset or "all columns"}
        )
    
    def validate_threshold(
        self,
        actual_value: float,
        threshold_key: str,
        phase_key: str,
        comparison: str = ">=",
        check_name: Optional[str] = None
    ) -> ValidationResult:
        """
        Validate a metric against a configured threshold.
        
        Args:
            actual_value: The actual metric value
            threshold_key: Key in thresholds config (e.g., 'min_kept_percentage')
            phase_key: Phase key in thresholds config (e.g., 'phase3_concepts')
            comparison: Comparison operator (>=, <=, ==)
            check_name: Name for this validation check
        
        Returns:
            ValidationResult indicating success or failure
        """
        if check_name is None:
            check_name = f"Threshold check: {threshold_key}"
        
        # Get threshold from config
        phase_thresholds = self.thresholds.get(phase_key, {})
        threshold_value = phase_thresholds.get(threshold_key)
        
        if threshold_value is None:
            return ValidationResult(
                check_name=check_name,
                passed=True,
                message=f"No threshold configured for {phase_key}.{threshold_key}",
                severity="info",
                details={"actual_value": actual_value}
            )
        
        # Perform comparison
        passed = False
        if comparison == ">=":
            passed = actual_value >= threshold_value
        elif comparison == "<=":
            passed = actual_value <= threshold_value
        elif comparison == "==":
            passed = actual_value == threshold_value
        elif comparison == ">":
            passed = actual_value > threshold_value
        elif comparison == "<":
            passed = actual_value < threshold_value
        
        if not passed:
            return ValidationResult(
                check_name=check_name,
                passed=False,
                message=f"Value {actual_value:.2f} fails threshold {comparison} {threshold_value}",
                severity="warning",
                details={
                    "actual_value": actual_value,
                    "threshold_value": threshold_value,
                    "comparison": comparison
                }
            )
        
        return ValidationResult(
            check_name=check_name,
            passed=True,
            message=f"Value {actual_value:.2f} meets threshold {comparison} {threshold_value}",
            severity="info",
            details={
                "actual_value": actual_value,
                "threshold_value": threshold_value
            }
        )
    
    def validate_vocabulary(
        self,
        df: pd.DataFrame,
        column: str,
        allowed_values: Union[List[str], set],
        check_name: Optional[str] = None,
        sample_size: int = 5
    ) -> ValidationResult:
        """
        Validate that values in a column match an allowed vocabulary.
        
        Args:
            df: DataFrame to validate
            column: Column name to check
            allowed_values: Set or list of allowed values
            check_name: Name for this validation check
            sample_size: Number of invalid values to include in details
        
        Returns:
            ValidationResult indicating success or failure
        """
        if check_name is None:
            check_name = f"Vocabulary validation for {column}"
        
        if column not in df.columns:
            return ValidationResult(
                check_name=check_name,
                passed=False,
                message=f"Column {column} not found",
                severity="error"
            )
        
        allowed_set = set(allowed_values)
        
        # For list columns, explode first
        if df[column].apply(lambda x: isinstance(x, (list, np.ndarray))).any():
            actual_values = set()
            for val_list in df[column].dropna():
                if isinstance(val_list, (list, np.ndarray)):
                    actual_values.update(val_list)
                else:
                    actual_values.add(val_list)
        else:
            actual_values = set(df[column].dropna().unique())
        
        invalid_values = actual_values - allowed_set
        
        if invalid_values:
            sample_invalid = list(invalid_values)[:sample_size]
            return ValidationResult(
                check_name=check_name,
                passed=False,
                message=f"Found {len(invalid_values)} values not in vocabulary",
                severity="error",
                details={
                    "invalid_count": len(invalid_values),
                    "sample_invalid": sample_invalid,
                    "vocabulary_size": len(allowed_set)
                }
            )
        
        return ValidationResult(
            check_name=check_name,
            passed=True,
            message=f"All {len(actual_values)} unique values match vocabulary",
            severity="info",
            details={"unique_values": len(actual_values), "vocabulary_size": len(allowed_set)}
        )


def save_validation_report(report: ValidationReport, output_path: Path):
    """
    Save validation report to JSON file.
    
    Args:
        report: ValidationReport to save
        output_path: Path to output JSON file
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(report.to_dict(), f, indent=2)
    print(f"📄 Validation report saved to: {output_path}")


def load_validation_thresholds(config_path: Optional[Path] = None) -> Dict[str, Any]:
    """
    Load validation thresholds from YAML config file.
    
    Args:
        config_path: Path to validation_thresholds.yml, or None for default
    
    Returns:
        Dictionary of thresholds by phase
    """
    if config_path is None:
        config_path = Path(__file__).parent.parent / "config" / "validation_thresholds.yml"
    
    if not config_path.exists():
        print(f"⚠️  Threshold config not found: {config_path}")
        return {}
    
    with open(config_path, 'r') as f:
        return yaml.safe_load(f) or {}
