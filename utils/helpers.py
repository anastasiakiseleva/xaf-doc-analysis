"""
XAF Documentation Analysis Utilities

Shared helper functions for data manipulation, concept checking, and metrics calculation.
"""

import pandas as pd
import re
from typing import Any, List


def safe_list(val):
    """
    Safely convert to list, handling numpy arrays and None values.
    
    Handles various input types common when working with pandas/numpy:
    - None or NaN values
    - Lists and tuples
    - Numpy arrays
    - Other iterables
    
    Returns:
        list: Empty list if val is None/NaN, otherwise converted to list
    """
    if val is None or (isinstance(val, float) and pd.isna(val)):
        return []
    if isinstance(val, (list, tuple)):
        return list(val)
    if hasattr(val, '__iter__') and not isinstance(val, str):
        return list(val)
    return []


def has_concept(concepts_val, target):
    """
    Check if a target concept exists in a concepts list/array.
    
    Handles various data types from parquet files including pandas Series,
    numpy arrays, and None values.
    
    Args:
        concepts_val: Value from 'concepts' column (list, array, or None)
        target: Concept string to search for
    
    Returns:
        bool: True if target concept found, False otherwise
    """
    if concepts_val is None or (isinstance(concepts_val, float) and pd.isna(concepts_val)):
        return False
    concepts_list = list(concepts_val) if hasattr(concepts_val, '__iter__') and not isinstance(concepts_val, str) else []
    return target in concepts_list


def normalize_tag(text):
    """
    Convert concept/platform/API name to XAF tag format.
    
    Rules:
    - lowercase
    - no spaces (replace with hyphens)
    - no dots (remove)
    - no special characters except hyphens
    - collapse multiple hyphens
    
    Examples:
        "Blazor UI" -> "blazor-ui"
        "ASP.NET Core" -> "asp-net-core"
        "SecurityStrategy" -> "securitystrategy"
        "DevExpress.ExpressApp" -> "devexpressexpressapp"
    
    Args:
        text: Raw concept/API name
    
    Returns:
        str: Normalized tag string
    """
    tag = text.lower()
    tag = tag.replace('.', '')  # Remove dots
    tag = tag.replace(' ', '-')  # Spaces to hyphens
    tag = re.sub(r'[^a-z0-9-]', '', tag)  # Remove other special chars
    tag = re.sub(r'-+', '-', tag)  # Collapse multiple hyphens
    tag = tag.strip('-')  # Remove leading/trailing hyphens
    return tag


def format_percentage(value: float, decimals: int = 1) -> str:
    """Format a percentage value for display."""
    return f"{value:.{decimals}f}%"


def format_count(value: int) -> str:
    """Format a count with thousand separators."""
    return f"{value:,}"


# Stub implementations for planned but not yet implemented functions
# These are imported by some existing code but functionality is inline

def load_core_data():
    """
    Load common data files (stub - to be implemented).
    Currently each script has its own load_data() function.
    """
    raise NotImplementedError("load_core_data() not yet implemented - use script-specific load_data()")


def get_kept_sections(df):
    """Get sections marked as kept (stub - use inline filtering instead)."""
    return df[df.get("kept", True) == True] if "kept" in df.columns else df


def calculate_connectivity_stats():
    """Calculate connectivity statistics (stub - to be implemented)."""
    raise NotImplementedError("calculate_connectivity_stats() not yet implemented")


def get_connectivity_by_type():
    """Get connectivity breakdown by type (stub - to be implemented)."""
    raise NotImplementedError("get_connectivity_by_type() not yet implemented")


def get_concept_stats():
    """Get per-concept statistics (stub - to be implemented)."""
    raise NotImplementedError("get_concept_stats() not yet implemented")


def get_all_concepts(df):
    """
    Extract unique concepts from a dataframe (basic implementation).
    
    Args:
        df: DataFrame with 'concepts' column
    
    Returns:
        set: Unique concepts
    """
    all_concepts = set()
    if "concepts" not in df.columns:
        return all_concepts
    
    for concepts_list in df["concepts"]:
        if concepts_list is not None and hasattr(concepts_list, '__iter__') and not isinstance(concepts_list, str):
            all_concepts.update(list(concepts_list))
    
    return all_concepts


def calculate_cross_corpus_links_for_concept():
    """Calculate cross-corpus links for a concept (stub - to be implemented)."""
    raise NotImplementedError("calculate_cross_corpus_links_for_concept() not yet implemented")


def get_isolated_sections():
    """Find disconnected sections (stub - to be implemented)."""
    raise NotImplementedError("get_isolated_sections() not yet implemented")

