"""
config_loader.py — Central loader for product-specific configuration.

All pipeline scripts import from here instead of hardcoding file paths,
concept names, or namespace patterns.

Usage:
    from scripts.config_loader import cfg, patterns

    taxonomy_path = cfg.taxonomy_path()
    noise = cfg.noise_concepts()
    ns_map = patterns.namespace_concept_map()
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

_ROOT = Path(__file__).resolve().parents[1]
_PRODUCT_YML = _ROOT / "config" / "product.yml"
_PATTERNS_YML = _ROOT / "config" / "patterns.yml"


@lru_cache(maxsize=1)
def _load_product() -> dict[str, Any]:
    with open(_PRODUCT_YML, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


@lru_cache(maxsize=1)
def _load_patterns() -> dict[str, Any]:
    if not _PATTERNS_YML.exists():
        return {}
    with open(_PATTERNS_YML, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


# ---------------------------------------------------------------------------
# Product config accessors
# ---------------------------------------------------------------------------

class _Cfg:
    """Typed accessors for config/product.yml."""

    def taxonomy_path(self) -> Path:
        """Absolute path to the taxonomy JSON file."""
        return _ROOT / _load_product()["product"]["taxonomy_file"]

    def support_tickets_path(self) -> Path:
        """Absolute path to the aggregated support tickets JSON."""
        return _ROOT / _load_product()["product"]["support_tickets_file"]

    def support_concept_map_path(self) -> Path:
        """Absolute path to the support-to-concept mapping YAML."""
        return _ROOT / _load_product()["product"]["support_concept_map"]

    def raw_docs_root(self) -> str:
        """Root directory for raw markdown source files (relative to project root)."""
        return _load_product()["paths"]["raw_docs_root"]

    def api_path_marker(self) -> str:
        """Directory name segment that identifies API reference docs in doc_id paths."""
        return _load_product().get("parsing", {}).get("api_path_marker", "apidoc")

    def noise_concepts(self) -> frozenset[str]:
        """Concept names too generic to produce meaningful semantic relationships."""
        return frozenset(_load_product().get("filtering", {}).get("noise_concepts", []))

    def priority_gap_concepts(self) -> list[str]:
        """Concepts flagged as priority gaps for coverage reports."""
        return _load_product().get("coverage", {}).get("priority_gap_concepts", [])


class _Patterns:
    """Typed accessors for config/patterns.yml."""

    def external_url_rules(self) -> list[dict[str, Any]]:
        """URL classification rules for unresolved external UIDs."""
        return _load_patterns().get("external_url_rules", [])

    def namespace_concept_map(self) -> dict[str, str]:
        """Mapping from namespace segment to canonical taxonomy concept name."""
        return _load_patterns().get("namespace_concept_map", {})


cfg = _Cfg()
patterns = _Patterns()
