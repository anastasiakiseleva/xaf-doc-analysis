#!/usr/bin/env python3
"""
Unit tests for Phase D improvements in scripts/06_classify_relationships.py.

Covers:
  D1 - classify_pairs() accepts taxonomy_index parameter
  D2 - build_taxonomy_context() emits correct lines for relations, domain,
       platform overlap/mismatch, and audience mismatch
  D2 - build_classification_prompt() injects taxonomy_context block in the
       rendered prompt when taxonomy_context is non-empty
"""

import sys
import importlib.util
import unittest
from pathlib import Path

# ---------------------------------------------------------------------------
# Load script via importlib (numeric prefix, side-effect-free on import)
# ---------------------------------------------------------------------------
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
_script_path = Path(__file__).parent.parent / "scripts" / "06_classify_relationships.py"
_spec = importlib.util.spec_from_file_location("cls_module", _script_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

build_taxonomy_context = _mod.build_taxonomy_context
build_classification_prompt = _mod.build_classification_prompt
classify_pairs = _mod.classify_pairs


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

_TAXONOMY_INDEX = {
    "Security System": {
        "domain": "security",
        "subdomain": "access-control",
        "requires": ["Authentication"],
        "related_to": ["Permission"],
        "part_of": [],
        "is_a": [],
        "has_part": [],
        "has_kind": [],
        "replaces": [],
        "facets": {"platforms": ["WinForms", "Blazor"], "audiences": ["developer"]},
    },
    "Authentication": {
        "domain": "security",
        "subdomain": "access-control",
        "requires": [],
        "related_to": [],
        "part_of": [],
        "is_a": [],
        "has_part": [],
        "has_kind": [],
        "replaces": [],
        "facets": {"platforms": ["WinForms", "Blazor"], "audiences": ["developer"]},
    },
    "XPO": {
        "domain": "data",
        "subdomain": "orm",
        "requires": [],
        "related_to": [],
        "part_of": [],
        "is_a": [],
        "has_part": [],
        "has_kind": [],
        "replaces": [],
        "facets": {"platforms": ["WinForms"], "audiences": ["advanced-developer"]},
    },
    "Blazor UI": {
        "domain": "ui",
        "subdomain": "web",
        "requires": [],
        "related_to": [],
        "part_of": [],
        "is_a": [],
        "has_part": [],
        "has_kind": [],
        "replaces": [],
        "facets": {"platforms": ["Blazor"], "audiences": ["developer"]},
    },
}

_BASE_PROMPT = "You are a relationship classifier."


# ---------------------------------------------------------------------------
# D2a — build_taxonomy_context: known relations
# ---------------------------------------------------------------------------
class TestBuildTaxonomyContextRelations(unittest.TestCase):

    def test_requires_relation_detected(self):
        ctx = build_taxonomy_context(
            ["Security System"], ["Authentication"], _TAXONOMY_INDEX
        )
        self.assertIn("Security System requires Authentication", ctx)

    def test_related_to_relation_detected(self):
        ctx = build_taxonomy_context(
            ["Security System"], ["Permission"],
            {**_TAXONOMY_INDEX, "Permission": {"domain": "", "subdomain": "", "requires": [],
             "related_to": [], "part_of": [], "is_a": [], "has_part": [], "has_kind": [],
             "replaces": [], "facets": {}}},
        )
        self.assertIn("Security System is related to Permission", ctx)

    def test_no_relation_when_unrelated_concepts(self):
        ctx = build_taxonomy_context(
            ["XPO"], ["Blazor UI"], _TAXONOMY_INDEX
        )
        # No relation line expected between XPO and Blazor UI
        self.assertNotIn("Known relations", ctx)

    def test_returns_empty_string_for_empty_inputs(self):
        self.assertEqual("", build_taxonomy_context([], [], _TAXONOMY_INDEX))
        self.assertEqual("", build_taxonomy_context([], ["Authentication"], _TAXONOMY_INDEX))

    def test_returns_empty_string_for_empty_index(self):
        self.assertEqual("", build_taxonomy_context(["Security System"], ["Authentication"], {}))


# ---------------------------------------------------------------------------
# D2b — build_taxonomy_context: domain / subdomain
# ---------------------------------------------------------------------------
class TestBuildTaxonomyContextDomain(unittest.TestCase):

    def test_shared_domain_reported(self):
        ctx = build_taxonomy_context(
            ["Security System"], ["Authentication"], _TAXONOMY_INDEX
        )
        self.assertIn("Shared domain", ctx)
        self.assertIn("security", ctx)

    def test_shared_subdomain_reported(self):
        ctx = build_taxonomy_context(
            ["Security System"], ["Authentication"], _TAXONOMY_INDEX
        )
        self.assertIn("Shared subdomain", ctx)
        self.assertIn("access-control", ctx)

    def test_different_domains_no_shared_domain_line(self):
        ctx = build_taxonomy_context(
            ["XPO"], ["Blazor UI"], _TAXONOMY_INDEX
        )
        self.assertNotIn("Shared domain", ctx)


# ---------------------------------------------------------------------------
# D2c — build_taxonomy_context: platform overlap / mismatch
# ---------------------------------------------------------------------------
class TestBuildTaxonomyContextPlatform(unittest.TestCase):

    def test_platform_overlap_reported(self):
        ctx = build_taxonomy_context(
            ["Security System"], ["Authentication"], _TAXONOMY_INDEX
        )
        self.assertIn("Platform overlap", ctx)

    def test_platform_mismatch_reported(self):
        # XPO is WinForms-only, Blazor UI is Blazor-only → mismatch
        ctx = build_taxonomy_context(
            ["XPO"], ["Blazor UI"], _TAXONOMY_INDEX
        )
        self.assertIn("Platform mismatch", ctx)
        self.assertIn("WinForms", ctx)
        self.assertIn("Blazor", ctx)

    def test_no_platform_line_when_facets_absent(self):
        index_no_plats = {
            "A": {"domain": "x", "subdomain": "", "requires": [], "related_to": [],
                  "part_of": [], "is_a": [], "has_part": [], "has_kind": [],
                  "replaces": [], "facets": {}},
            "B": {"domain": "x", "subdomain": "", "requires": [], "related_to": [],
                  "part_of": [], "is_a": [], "has_part": [], "has_kind": [],
                  "replaces": [], "facets": {}},
        }
        ctx = build_taxonomy_context(["A"], ["B"], index_no_plats)
        self.assertNotIn("Platform", ctx)


# ---------------------------------------------------------------------------
# D2d — build_taxonomy_context: audience mismatch
# ---------------------------------------------------------------------------
class TestBuildTaxonomyContextAudience(unittest.TestCase):

    def test_audience_mismatch_reported(self):
        # XPO targets advanced-developer; Blazor UI targets developer
        ctx = build_taxonomy_context(
            ["XPO"], ["Blazor UI"], _TAXONOMY_INDEX
        )
        self.assertIn("Audience mismatch", ctx)

    def test_no_audience_line_when_same(self):
        # Both Security System and Authentication have audiences: [developer]
        ctx = build_taxonomy_context(
            ["Security System"], ["Authentication"], _TAXONOMY_INDEX
        )
        self.assertNotIn("Audience mismatch", ctx)


# ---------------------------------------------------------------------------
# D2e — build_classification_prompt: Taxonomy Context block injected
# ---------------------------------------------------------------------------
class TestBuildClassificationPromptTaxonomyContext(unittest.TestCase):

    def _make_prompt(self, taxonomy_context: str = "") -> str:
        return build_classification_prompt(
            _BASE_PROMPT,
            "docs/security.md", "sec-1",
            "Configure Security System.",
            ["Security System"], False,
            "docs/auth.md", "auth-1",
            "Authentication overview.",
            ["Authentication"], False,
            0.85,
            taxonomy_context=taxonomy_context,
        )

    def test_taxonomy_context_block_present_when_provided(self):
        ctx = "## Taxonomy Context\n- Security System requires Authentication"
        prompt = self._make_prompt(taxonomy_context=ctx)
        self.assertIn("## Taxonomy Context", prompt)
        self.assertIn("Security System requires Authentication", prompt)

    def test_no_taxonomy_context_block_when_empty(self):
        prompt = self._make_prompt(taxonomy_context="")
        self.assertNotIn("## Taxonomy Context", prompt)

    def test_prompt_still_contains_sections_a_and_b(self):
        prompt = self._make_prompt()
        self.assertIn("## Section A (Source)", prompt)
        self.assertIn("## Section B (Target)", prompt)

    def test_prompt_contains_context_block(self):
        prompt = self._make_prompt()
        self.assertIn("## Context", prompt)
        self.assertIn("Semantic similarity: 0.850", prompt)


# ---------------------------------------------------------------------------
# D1 — classify_pairs accepts taxonomy_index parameter
# ---------------------------------------------------------------------------
class TestClassifyPairsSignature(unittest.TestCase):

    def test_taxonomy_index_is_accepted_kwarg(self):
        """classify_pairs must accept taxonomy_index without raising TypeError."""
        import inspect
        sig = inspect.signature(classify_pairs)
        self.assertIn("taxonomy_index", sig.parameters)

    def test_taxonomy_index_defaults_to_none(self):
        import inspect
        sig = inspect.signature(classify_pairs)
        default = sig.parameters["taxonomy_index"].default
        self.assertIsNone(default)


if __name__ == "__main__":
    unittest.main()
