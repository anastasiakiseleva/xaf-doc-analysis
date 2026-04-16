"""
Taxonomy loader – single adapter for reading xaf-taxonomy.json
and returning the flat concept dict shape that all pipeline scripts expect.

Replaces direct yaml.safe_load() calls against concepts.yml.
"""

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

_CONFIG_DIR = Path(__file__).resolve().parent.parent / "config"
_DEFAULT_TAXONOMY = _CONFIG_DIR / "xaf-taxonomy.json"

# ── reverse map: (artifact_kind, domain) → original concepts.yml `type` ──
# Built from generate_taxonomy.py's TYPE_TO_KIND plus domain heuristics.
# Order matters: first match wins when multiple (artifact_kind, domain) pairs
# could map to the same type.  Platform concepts are detected separately
# via _is_platform().

_KIND_DOMAIN_TO_TYPE: Dict[tuple, str] = {
    # modules
    ("module", "ui"):            "module",
    ("module", "quality"):       "validation",
    ("module", "data"):          "module",
    ("module", "ops"):           "module",
    # tools
    ("tool", "tooling"):         "tooling",
    ("tool", "quality"):         "diagnostics",
    ("tool", "ops"):             "ops",
    # patterns / api
    ("pattern", None):           "patterns",
    ("api", None):               "interfaces",
    ("feature", None):           "module",
    # conceptual – domain-specific
    ("conceptual", "security"):  "security",
    ("conceptual", "data"):      "data",
    ("conceptual", "ui"):        "ui",
    ("conceptual", "architecture"): "architecture",
    ("conceptual", "ops"):       "ops",
    ("conceptual", "quality"):   "quality",
    ("conceptual", "migration"): "migration",
    ("conceptual", "localization"): "localization",
    ("conceptual", "learning"):  "learning",
    ("conceptual", "tooling"):   "tooling",
}

# Concepts whose original type was "Data Access & Business Logic"
_DATA_ACCESS_NAMES = frozenset({
    "Entity Framework Core", "XPO", "Business Object",
})

# Concepts whose original type was "Platform" or "runtime".
# Only concepts that exist in xaf-taxonomy.json are listed here.
# (Blazor and WinForms were removed from the taxonomy as standalone concepts.)
_PLATFORM_NAMES = frozenset({"Web API Service"})


def _is_platform(concept: Dict[str, Any]) -> bool:
    """Return True if this concept should have type 'Platform'."""
    return concept.get("name", "") in _PLATFORM_NAMES


def _reverse_type(concept: Dict[str, Any]) -> str:
    """Map (artifact_kind, domain) back to the original concepts.yml `type`."""
    if _is_platform(concept):
        return "Platform"
    name = concept.get("name", "")
    if name in _DATA_ACCESS_NAMES:
        return "Data Access & Business Logic"
    kind = concept.get("artifact_kind", "conceptual")
    domain = concept.get("domain")
    # exact (kind, domain) first, then (kind, None) as fallback
    return (
        _KIND_DOMAIN_TO_TYPE.get((kind, domain))
        or _KIND_DOMAIN_TO_TYPE.get((kind, None))
        or domain
        or "conceptual"
    )


def _resolve_ids(ids: List[str], id_to_name: Dict[str, str]) -> List[str]:
    """Resolve a list of concept IDs to concept names."""
    return [id_to_name.get(cid, cid) for cid in ids]


def _build_inverse_maps(
    raw_concepts: List[Dict[str, Any]],
) -> tuple[Dict[str, List[str]], Dict[str, List[str]]]:
    """Build reverse-lookup maps for hierarchical relations.

    Returns
    -------
    id_to_has_part : dict
        Maps parent ID → sorted list of child IDs that declare ``part_of`` this parent.
    id_to_has_kind : dict
        Maps parent ID → sorted list of child IDs that declare ``is_a`` this parent.

    These are the SKOS ``narrower`` / inverse-``broader`` equivalents.
    Computed once at load time so the JSON stays a single source of truth.
    """
    id_to_has_part: Dict[str, List[str]] = {c["id"]: [] for c in raw_concepts if "id" in c}
    id_to_has_kind: Dict[str, List[str]] = {c["id"]: [] for c in raw_concepts if "id" in c}
    for c in raw_concepts:
        cid = c.get("id", "")
        relations = c.get("relations") or {}
        for parent_id in relations.get("part_of") or []:
            if parent_id in id_to_has_part:
                id_to_has_part[parent_id].append(cid)
        for parent_id in relations.get("is_a") or []:
            if parent_id in id_to_has_kind:
                id_to_has_kind[parent_id].append(cid)
    return id_to_has_part, id_to_has_kind


def _flatten_concept(
    raw: Dict[str, Any],
    id_to_name: Dict[str, str],
    id_to_has_part: Dict[str, List[str]],
    id_to_has_kind: Dict[str, List[str]],
) -> Dict[str, Any]:
    """Convert a single taxonomy concept into the flat dict shape scripts expect."""
    terminology = raw.get("terminology") or {}
    api_surface = raw.get("api_surface") or {}
    relations = raw.get("relations") or {}
    part_of_ids = relations.get("part_of") or []
    is_a_ids = relations.get("is_a") or []
    related_to_ids = relations.get("related_to") or []
    replaces_ids = relations.get("replaces") or []
    requires_ids = relations.get("requires") or []

    # Resolve relation IDs to names
    part_of_names = _resolve_ids(part_of_ids, id_to_name)
    is_a_names = _resolve_ids(is_a_ids, id_to_name)
    related_to_names = _resolve_ids(related_to_ids, id_to_name)
    replaces_names = _resolve_ids(replaces_ids, id_to_name)
    requires_names = _resolve_ids(requires_ids, id_to_name)

    # Parent: prefer part_of, fall back to is_a
    parent_list = part_of_names or is_a_names
    parent = parent_list[0] if parent_list else None

    # Merge api_surface into keywords (primary first, then related)
    keywords: List[str] = list(api_surface.get("primary_types") or [])
    keywords.extend(api_surface.get("related_types") or [])
    # Also include terminology.keywords if present
    keywords.extend(terminology.get("keywords") or [])

    # Computed inverse (narrower) relations — SKOS narrower / Z39.19 reciprocal
    cid = raw.get("id", "")
    has_part_names = _resolve_ids(id_to_has_part.get(cid, []), id_to_name)
    has_kind_names = _resolve_ids(id_to_has_kind.get(cid, []), id_to_name)

    flat: Dict[str, Any] = {
        "name":        raw.get("name", ""),
        "type":        _reverse_type(raw),
        "synonyms":    list(terminology.get("synonyms") or []),
        "tags":        list(raw.get("tags") or []),
        "keywords":    keywords,
        "description": raw.get("description", ""),
        "parent":      parent,
        # ── relation fields (resolved to names) ──
        "part_of":     part_of_names,       # child → parent  (SKOS broader)
        "is_a":        is_a_names,           # child → parent  (SKOS broader, generic)
        "related_to":  related_to_names,
        "replaces":    replaces_names,
        "requires":    requires_names,
        # ── computed inverse relations (SKOS narrower) ──
        # Derived at load time from the child-side declarations above.
        # Never stored in JSON — single source of truth is always the child.
        "has_part":    has_part_names,       # parent → children via part_of
        "has_kind":    has_kind_names,       # parent → children via is_a
        # ── bonus fields from the richer taxonomy ──
        "id":          cid,
        "domain":      raw.get("domain", ""),
        "subdomain":   raw.get("subdomain", ""),
        "artifact_kind": raw.get("artifact_kind", ""),
        "facets":      raw.get("facets"),
        "api_surface": api_surface or None,
    }
    return flat


# ── public API ─────────────────────────────────────────────────────────────

def load_concepts(path: Optional[str | Path] = None) -> Dict[str, Any]:
    """Load xaf-taxonomy.json and return ``{"concepts": [flat_dicts]}``.

    The returned list has the same field shape that scripts previously got
    from ``yaml.safe_load()`` on ``concepts.yml``:

    - ``name``, ``type``, ``synonyms``, ``tags``, ``keywords``,
      ``description``, ``parent``

    Plus bonus fields: ``id``, ``domain``, ``subdomain``, ``artifact_kind``,
    ``facets``, ``api_surface``.

    Parameters
    ----------
    path : str or Path, optional
        Override taxonomy file location.  Defaults to
        ``config/xaf-taxonomy.json``.
    """
    taxonomy_path = Path(path) if path else _DEFAULT_TAXONOMY
    with taxonomy_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    raw_concepts = data.get("taxonomy", {}).get("concepts", [])
    id_to_name = {c["id"]: c["name"] for c in raw_concepts if "id" in c}
    id_to_has_part, id_to_has_kind = _build_inverse_maps(raw_concepts)
    return {
        "concepts": [
            _flatten_concept(c, id_to_name, id_to_has_part, id_to_has_kind)
            for c in raw_concepts
        ]
    }


def load_taxonomy_raw(path: Optional[str | Path] = None) -> Dict[str, Any]:
    """Load the full xaf-taxonomy.json without flattening.

    Use this when you want the rich taxonomy structure (domains, facets,
    api_surface, etc.) rather than the concepts.yml-compatible shape.
    """
    taxonomy_path = Path(path) if path else _DEFAULT_TAXONOMY
    with taxonomy_path.open("r", encoding="utf-8") as f:
        return json.load(f)
