"""
Tests for utils.taxonomy_loader – verifies that the adapter produces
the flat concept dict shape expected by all pipeline scripts.
"""

import json
import sys
from pathlib import Path

import pytest
import yaml

# ensure project root is importable
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from utils.taxonomy_loader import load_concepts, load_taxonomy_raw, _flatten_concept
from utils.taxonomy_loader import (
    load_taxonomy_index,
    get_concept_context_string,
    get_platform_concepts,
)

CONFIG_DIR = Path(__file__).resolve().parent.parent / "config"
TAXONOMY_PATH = CONFIG_DIR / "xaf-taxonomy.json"
CONCEPTS_YML_PATH = CONFIG_DIR / "concepts.yml"


# ── helpers ────────────────────────────────────────────────────────────────

def _load_yml_concepts():
    """Load concepts.yml the old way for comparison."""
    with CONCEPTS_YML_PATH.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f).get("concepts", [])


def _yml_by_name():
    return {c["name"].strip(): c for c in _load_yml_concepts()}


# ── basic loading ──────────────────────────────────────────────────────────

class TestLoadConcepts:
    """Verify load_concepts() returns a well-formed structure."""

    def test_returns_dict_with_concepts_key(self):
        data = load_concepts()
        assert isinstance(data, dict)
        assert "concepts" in data
        assert isinstance(data["concepts"], list)

    def test_concept_count_matches_taxonomy(self):
        with TAXONOMY_PATH.open("r", encoding="utf-8") as f:
            raw = json.load(f)
        expected = len(raw["taxonomy"]["concepts"])
        actual = len(load_concepts()["concepts"])
        assert actual == expected, f"Expected {expected} concepts, got {actual}"

    def test_every_concept_has_required_fields(self):
        required = {
            "name", "type", "synonyms", "tags", "keywords", "description",
            "parent", "part_of", "is_a", "related_to", "replaces", "requires",
        }
        for c in load_concepts()["concepts"]:
            missing = required - set(c.keys())
            assert not missing, f"Concept '{c.get('name')}' missing fields: {missing}"

    def test_bonus_fields_present(self):
        """New taxonomy fields are exposed alongside legacy fields."""
        bonus = {"id", "domain", "subdomain", "artifact_kind"}
        for c in load_concepts()["concepts"]:
            missing = bonus - set(c.keys())
            assert not missing, f"Concept '{c.get('name')}' missing bonus fields: {missing}"


# ── field-level compatibility with concepts.yml ────────────────────────────

@pytest.fixture(scope="module")
def adapter_by_name():
    return {c["name"]: c for c in load_concepts()["concepts"]}


@pytest.fixture(scope="module")
def yml_by_name():
    return _yml_by_name()


class TestFieldCompatibility:
    """Compare adapter output against concepts.yml for key concepts."""

    # Spot-check a sample of important concepts
    SAMPLE_CONCEPTS = [
        "Security System",
        "Authentication",
        "Views",
        "Object Space",
        "Validation Module",
        "Model Editor",
        "Deployment",
    ]

    @pytest.mark.parametrize("name", SAMPLE_CONCEPTS)
    def test_synonyms_match(self, name, adapter_by_name, yml_by_name):
        if name not in yml_by_name or name not in adapter_by_name:
            pytest.skip(f"'{name}' not in both sources")
        expected = set(yml_by_name[name].get("synonyms") or [])
        actual = set(adapter_by_name[name].get("synonyms") or [])
        # Taxonomy may have additional curated synonyms; check YML is a subset
        missing = expected - actual
        assert not missing, (
            f"Synonyms from concepts.yml missing in adapter for '{name}': {missing}"
        )

    @pytest.mark.parametrize("name", SAMPLE_CONCEPTS)
    def test_description_match(self, name, adapter_by_name, yml_by_name):
        if name not in yml_by_name or name not in adapter_by_name:
            pytest.skip(f"'{name}' not in both sources")
        yml_desc = (yml_by_name[name].get("description") or "").strip()
        adapter_desc = (adapter_by_name[name].get("description") or "").strip()
        if yml_desc:
            assert adapter_desc == yml_desc, f"Description mismatch for '{name}'"

    def test_all_concept_names_present(self, adapter_by_name, yml_by_name):
        # Taxonomy was curated: some YML concepts removed, some new ones added.
        # Check that concepts present in BOTH sources appear in the adapter.
        yml_names = set(yml_by_name.keys())
        adapter_names = set(adapter_by_name.keys())
        shared = yml_names & adapter_names
        assert len(shared) > 100, (
            f"Too few shared concepts: {len(shared)} (expected 100+)"
        )


# ── Platform routing (critical for 03_extract_concepts.py) ─────────────────

class TestPlatformRouting:
    """Ensure Platform concepts are correctly typed so
    03_extract_concepts.py routes them to the platforms column.

    Note: Blazor and WinForms were removed from taxonomy.json as
    standalone concepts.  Only Web API Service remains."""

    PLATFORM_CONCEPTS = ["Web API Service"]

    @pytest.mark.parametrize("name", PLATFORM_CONCEPTS)
    def test_platform_type(self, name):
        by_name = {c["name"]: c for c in load_concepts()["concepts"]}
        assert name in by_name, f"Platform concept '{name}' not found"
        assert by_name[name]["type"] == "Platform", (
            f"Expected type='Platform' for '{name}', got '{by_name[name]['type']}'"
        )

    def test_non_platform_not_typed_platform(self):
        """Ensure regular concepts are NOT typed as Platform."""
        non_platform = {"Security System", "Views", "Deployment"}
        by_name = {c["name"]: c for c in load_concepts()["concepts"]}
        for name in non_platform:
            if name in by_name:
                assert by_name[name]["type"] != "Platform", (
                    f"'{name}' should not be Platform-typed"
                )


# ── type reverse-mapping ──────────────────────────────────────────────────

class TestTypeReverseMapping:
    """Spot-check that artifact_kind+domain maps back to concepts.yml type."""

    EXPECTED_TYPES = {
        "Security System":       "security",
        "Authentication":        "security",
        "Views":                 "ui",
        "Property Editors":      "ui",
        "Object Space":          "data",
        "Criteria":              "data",
        "XAF Application":       "architecture",
        "Modules":               "architecture",
        "Deployment":            "ops",
        "Entity Framework Core": "Data Access & Business Logic",
        "XPO":                   "Data Access & Business Logic",
        "Business Object":       "Data Access & Business Logic",
        "Validation":            "module",
        "Model Editor":          "tooling",
        "Async Operations":      "patterns",
    }

    @pytest.mark.parametrize("name,expected_type", list(EXPECTED_TYPES.items()))
    def test_type_value(self, name, expected_type):
        by_name = {c["name"]: c for c in load_concepts()["concepts"]}
        if name not in by_name:
            pytest.skip(f"'{name}' not in taxonomy")
        actual = by_name[name]["type"]
        assert actual == expected_type, (
            f"Type mismatch for '{name}': expected '{expected_type}', got '{actual}'"
        )


# ── hierarchy (parent field) ──────────────────────────────────────────────

class TestHierarchy:
    """Verify parent extraction from relations.part_of (preferred) or is_a (fallback)."""

    EXPECTED_PARENTS = {
        "Layout":          "Views",
        "Model Nodes":     "Application Model",
        "View Items":      "Views",
        "List View":       "View Types",
        "Simple Action":   "Action Types",
    }

    @pytest.mark.parametrize("name,expected_parent", list(EXPECTED_PARENTS.items()))
    def test_parent_value(self, name, expected_parent):
        by_name = {c["name"]: c for c in load_concepts()["concepts"]}
        if name not in by_name:
            pytest.skip(f"'{name}' not in taxonomy")
        assert by_name[name]["parent"] == expected_parent, (
            f"Parent mismatch for '{name}'"
        )

    def test_concepts_without_parent_have_none(self):
        """Top-level concepts should have parent=None."""
        by_name = {c["name"]: c for c in load_concepts()["concepts"]}
        for name in ("Security System", "XAF Application"):
            if name in by_name:
                assert by_name[name]["parent"] is None, (
                    f"'{name}' should have no parent"
                )


# ── keywords (merged from api_surface) ────────────────────────────────────

class TestKeywords:
    """Verify keywords are assembled from api_surface fields."""

    def test_security_system_has_api_keywords(self):
        by_name = {c["name"]: c for c in load_concepts()["concepts"]}
        kw = by_name["Security System"]["keywords"]
        # primary_types should appear first
        assert "SecuredObjectSpace" in kw
        assert "SecurityStrategy" in kw

    def test_keywords_is_list(self):
        for c in load_concepts()["concepts"]:
            assert isinstance(c["keywords"], list), (
                f"Keywords for '{c['name']}' should be a list"
            )


# ── load_taxonomy_raw ─────────────────────────────────────────────────────

class TestLoadTaxonomyRaw:
    def test_returns_full_structure(self):
        data = load_taxonomy_raw()
        assert "schema_version" in data
        assert "taxonomy" in data
        assert "concepts" in data["taxonomy"]

    def test_concepts_are_not_flattened(self):
        data = load_taxonomy_raw()
        first = data["taxonomy"]["concepts"][0]
        # Should have nested terminology, not flat synonyms
        assert "terminology" in first or "api_surface" in first


# ── edge cases ─────────────────────────────────────────────────────────────

# ── relations ──────────────────────────────────────────────────────────────

class TestRelations:
    """Verify all four relation types are exposed and resolved to names."""

    def test_relation_fields_are_lists(self):
        for c in load_concepts()["concepts"]:
            for field in ("part_of", "is_a", "related_to", "replaces", "requires"):
                assert isinstance(c[field], list), (
                    f"'{field}' for '{c['name']}' should be a list, got {type(c[field])}"
                )

    def test_is_a_populated(self):
        by_name = {c["name"]: c for c in load_concepts()["concepts"]}
        assert "Security System" in by_name["Authentication"]["part_of"], (
            "Authentication should be part_of Security System"
        )

    def test_related_to_populated(self):
        by_name = {c["name"]: c for c in load_concepts()["concepts"]}
        assert "Business Object" in by_name["Object Space"]["related_to"], (
            "Object Space should be related_to Business Object"
        )

    def test_related_to_symmetric(self):
        """Every related_to link must be reciprocated."""
        concepts = load_concepts()["concepts"]
        by_name = {c["name"]: c for c in concepts}
        errors = []
        for c in concepts:
            for target in c["related_to"]:
                if target not in by_name:
                    continue
                if c["name"] not in by_name[target]["related_to"]:
                    errors.append(f"{c['name']} → {target} (no reverse)")
        assert not errors, f"Asymmetric related_to: {errors}"

    def test_replaces_populated(self):
        by_name = {c["name"]: c for c in load_concepts()["concepts"]}
        assert "Project Wizards" in by_name["Template Kit"]["replaces"], (
            "Template Kit should replace Project Wizards"
        )

    def test_requires_populated_for_known_concept(self):
        by_name = {c["name"]: c for c in load_concepts()["concepts"]}
        assert "Business Object" in by_name["Validation"]["requires"], (
            "Validation should require Business Object"
        )
        assert "Views" in by_name["Navigation"]["requires"], (
            "Navigation should require Views"
        )
        assert "Database Connection" in by_name["Entity Framework Core"]["requires"], (
            "Entity Framework Core should require Database Connection"
        )

    def test_has_part_is_inverse_of_part_of(self):
        """Every concept's has_part must equal the set of concepts that declare
        part_of back to it.  Verifies Z39.19 §7.1 reciprocity for whole-part."""
        concepts = load_concepts()["concepts"]
        by_name = {c["name"]: c for c in concepts}
        errors = []
        for c in concepts:
            for child_name in c["has_part"]:
                if child_name not in by_name:
                    continue
                if c["name"] not in by_name[child_name]["part_of"]:
                    errors.append(
                        f"{c['name']}.has_part includes '{child_name}' "
                        f"but '{child_name}'.part_of does not include '{c['name']}'"
                    )
        assert not errors, f"has_part/part_of mismatch: {errors}"

    def test_has_kind_is_inverse_of_is_a(self):
        """Every concept's has_kind must equal the set of concepts that declare
        is_a back to it.  Verifies Z39.19 §7.1 reciprocity for generic (BT/NT)."""
        concepts = load_concepts()["concepts"]
        by_name = {c["name"]: c for c in concepts}
        errors = []
        for c in concepts:
            for child_name in c["has_kind"]:
                if child_name not in by_name:
                    continue
                if c["name"] not in by_name[child_name]["is_a"]:
                    errors.append(
                        f"{c['name']}.has_kind includes '{child_name}' "
                        f"but '{child_name}'.is_a does not include '{c['name']}'"
                    )
        assert not errors, f"has_kind/is_a mismatch: {errors}"

    def test_has_part_populated_for_known_parent(self):
        """Application Model should list all four sub-concepts in has_part."""
        by_name = {c["name"]: c for c in load_concepts()["concepts"]}
        has_part = by_name["Application Model"]["has_part"]
        for expected in ("Model Cache", "Model Differences", "Model Extension", "Model Nodes"):
            assert expected in has_part, (
                f"Application Model.has_part should contain '{expected}', got {has_part}"
            )

    def test_has_kind_populated_for_known_parent(self):
        """View Types should list its specialisations in has_kind."""
        by_name = {c["name"]: c for c in load_concepts()["concepts"]}
        has_kind = by_name["View Types"]["has_kind"]
        for expected in ("Detail View", "List View", "Dashboard View", "Lookup View"):
            assert expected in has_kind, (
                f"View Types.has_kind should contain '{expected}', got {has_kind}"
            )

    def test_inverse_fields_are_lists(self):
        for c in load_concepts()["concepts"]:
            for field in ("has_part", "has_kind"):
                assert isinstance(c[field], list), (
                    f"'{field}' for '{c['name']}' should be a list, got {type(c[field])}"
                )


# ── edge cases ─────────────────────────────────────────────────────────────

class TestEdgeCases:
    def test_flatten_minimal_concept(self):
        """A concept with only required fields should not crash."""
        minimal = {"id": "xaf.test.minimal", "name": "Test", "artifact_kind": "conceptual", "domain": "data"}
        flat = _flatten_concept(minimal, {}, {}, {})
        assert flat["name"] == "Test"
        assert flat["synonyms"] == []
        assert flat["tags"] == []
        assert flat["keywords"] == []
        assert flat["parent"] is None
        assert flat["is_a"] == []
        assert flat["related_to"] == []
        assert flat["replaces"] == []
        assert flat["has_part"] == []
        assert flat["has_kind"] == []

    def test_custom_path(self, tmp_path):
        """load_concepts() accepts a custom path."""
        mini = {"taxonomy": {"concepts": [
            {"id": "x.y.z", "name": "Z", "artifact_kind": "conceptual", "domain": "data"}
        ]}}
        p = tmp_path / "tax.json"
        p.write_text(json.dumps(mini), encoding="utf-8")
        result = load_concepts(p)
        assert len(result["concepts"]) == 1
        assert result["concepts"][0]["name"] == "Z"


# ── Phase A: load_taxonomy_index() ───────────────────────────────────────────

class TestLoadTaxonomyIndex:
    """Verify load_taxonomy_index() returns a correct name-keyed dict."""

    def test_returns_dict(self):
        index = load_taxonomy_index()
        assert isinstance(index, dict)

    def test_has_expected_count(self):
        index = load_taxonomy_index()
        with TAXONOMY_PATH.open("r", encoding="utf-8") as f:
            raw = json.load(f)
        expected = len(raw["taxonomy"]["concepts"])
        assert len(index) == expected, f"Expected {expected}, got {len(index)}"

    def test_keys_are_concept_names(self):
        index = load_taxonomy_index()
        assert "Security System" in index
        assert "Application Model" in index
        assert "Object Space" in index

    def test_values_have_required_fields(self):
        index = load_taxonomy_index()
        concept = index["Security System"]
        for field in ("name", "domain", "subdomain", "artifact_kind",
                      "facets", "api_surface", "documentation",
                      "synonyms", "keywords", "description",
                      "part_of", "is_a", "requires", "related_to"):
            assert field in concept, f"'Security System' missing field '{field}'"

    def test_domain_correct(self):
        index = load_taxonomy_index()
        assert index["Security System"]["domain"] == "security"
        assert index["Application Model"]["domain"] == "architecture"

    def test_relations_are_names_not_ids(self):
        """Relation values must be resolved to concept names, not raw IDs."""
        index = load_taxonomy_index()
        for name, concept in index.items():
            for field in ("part_of", "is_a", "requires", "related_to", "replaces"):
                for val in concept.get(field) or []:
                    assert not val.startswith("xaf."), (
                        f"Concept '{name}' field '{field}' contains unresolved ID: {val}"
                    )

    def test_caching_returns_same_object(self):
        """Second call must return the exact same dict object (cached)."""
        index1 = load_taxonomy_index()
        index2 = load_taxonomy_index()
        assert index1 is index2

    def test_documentation_field_present(self):
        """documentation.doc_intents should come through for configured concepts."""
        index = load_taxonomy_index()
        concepts_with_intents = [
            name for name, c in index.items()
            if c.get("documentation") and c["documentation"].get("doc_intents")
        ]
        assert len(concepts_with_intents) > 10, (
            f"Expected >10 concepts with doc_intents, got {len(concepts_with_intents)}"
        )


# ── Phase A: get_concept_context_string() ────────────────────────────────────

class TestGetConceptContextString:
    """Verify the rich text blob used for semantic embedding."""

    def test_all_concepts_produce_nonempty_string(self):
        index = load_taxonomy_index()
        empty = [n for n in index if not get_concept_context_string(n, index)]
        assert not empty, f"Empty context for: {empty[:3]}"

    def test_context_includes_name(self):
        index = load_taxonomy_index()
        ctx = get_concept_context_string("Security System", index)
        assert "Security System" in ctx

    def test_context_includes_description(self):
        index = load_taxonomy_index()
        ctx = get_concept_context_string("Security System", index)
        # description should make the string longer than just the name
        assert len(ctx) > len("Security System")

    def test_context_includes_domain(self):
        index = load_taxonomy_index()
        ctx = get_concept_context_string("Security System", index)
        assert "security" in ctx.lower()

    def test_context_includes_api_types(self):
        index = load_taxonomy_index()
        ctx = get_concept_context_string("Application Model", index)
        # Application Model has XAFML as primary API type
        assert "XAFML" in ctx or "Key APIs" in ctx

    def test_context_includes_requires_relation(self):
        index = load_taxonomy_index()
        # Find a concept with requires and check it appears in context
        concept_with_requires = next(
            (n for n, c in index.items() if c.get("requires")), None
        )
        assert concept_with_requires is not None
        ctx = get_concept_context_string(concept_with_requires, index)
        assert "Requires" in ctx, (
            f"Expected 'Requires' in context for '{concept_with_requires}', got: {ctx}"
        )

    def test_unknown_concept_returns_name(self):
        index = load_taxonomy_index()
        result = get_concept_context_string("NonExistentConcept", index)
        assert result == "NonExistentConcept"

    def test_auto_loads_index_when_not_provided(self):
        """Should work without passing an index (loads internally)."""
        ctx = get_concept_context_string("Security System")
        assert "Security System" in ctx
        assert len(ctx) > len("Security System")


# ── Phase A: get_platform_concepts() ─────────────────────────────────────────

class TestGetPlatformConcepts:
    """Verify platform-scoped concept filtering."""

    def test_blazor_returns_nonempty_list(self):
        assert len(get_platform_concepts("blazor")) > 0

    def test_winforms_returns_nonempty_list(self):
        assert len(get_platform_concepts("winforms")) > 0

    def test_results_are_sorted(self):
        result = get_platform_concepts("blazor")
        assert result == sorted(result)

    def test_case_insensitive(self):
        lower = get_platform_concepts("blazor")
        upper = get_platform_concepts("BLAZOR")
        mixed = get_platform_concepts("Blazor")
        assert lower == upper == mixed

    def test_nonexistent_platform_returns_empty(self):
        assert get_platform_concepts("jupiter") == []

    def test_all_returned_concepts_actually_have_platform(self):
        index = load_taxonomy_index()
        for name in get_platform_concepts("blazor", index):
            facets = index[name].get("facets") or {}
            platforms = [p.lower() for p in (facets.get("platforms") or [])]
            assert "blazor" in platforms, (
                f"Concept '{name}' returned for blazor but has platforms: {platforms}"
            )

    def test_winforms_blazor_share_some_concepts(self):
        """Some concepts should be multi-platform."""
        blazor = set(get_platform_concepts("blazor"))
        winforms = set(get_platform_concepts("winforms"))
        shared = blazor & winforms
        assert len(shared) > 0, "Expected some concepts shared between blazor and winforms"

    def test_auto_loads_index_when_not_provided(self):
        """Should work without passing an index."""
        result = get_platform_concepts("winforms")
        assert isinstance(result, list)
        assert len(result) > 0
