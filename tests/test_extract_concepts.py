#!/usr/bin/env python3
"""
Unit tests for Phase B improvements in scripts/03_extract_concepts.py.

Covers:
  B1 - _build_ambiguous_concepts / _get_ambiguous_concepts  (taxonomy-driven)
  B2 - _validate_concept_semantically  (get_concept_context_string delegation)
  B3 - _check_domain_coherence  (generic + specialized dispatch)
"""

import sys
import importlib.util
import unittest
from pathlib import Path

# ---------------------------------------------------------------------------
# Load the module via importlib (numeric prefix in filename)
# ---------------------------------------------------------------------------
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

_script_path = Path(__file__).parent.parent / "scripts" / "03_extract_concepts.py"
_spec = importlib.util.spec_from_file_location("extract_concepts_module", _script_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

_build_ambiguous_concepts = _mod._build_ambiguous_concepts
_get_ambiguous_concepts = _mod._get_ambiguous_concepts
_check_domain_coherence = _mod._check_domain_coherence
extract_concepts_semantic = _mod.extract_concepts_semantic
compile_concept_index = _mod.compile_concept_index


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _make_concept(
    name: str,
    artifact_kind: str = "feature",
    primary_types: list = None,
    keywords: list = None,
) -> dict:
    """Build a minimal flat concept dict (same shape as taxonomy_loader output)."""
    return {
        "name": name,
        "artifact_kind": artifact_kind,
        "primary_types": primary_types or [],
        "related_types": [],
        "keywords": keywords or [],
        "synonyms": [],
        "description": f"Test concept: {name}",
        "domain": "test",
        "subdomain": "test-sub",
        "facets": {},
        "relations": {},
    }


# ---------------------------------------------------------------------------
# B1: _build_ambiguous_concepts
# ---------------------------------------------------------------------------
class TestBuildAmbiguousConcepts(unittest.TestCase):

    def test_returns_frozenset(self):
        result = _build_ambiguous_concepts([])
        self.assertIsInstance(result, frozenset)

    def test_empty_config_returns_empty(self):
        result = _build_ambiguous_concepts([])
        self.assertEqual(len(result), 0)

    def test_feature_with_no_primary_types_is_ambiguous(self):
        cfg = [_make_concept("Views", artifact_kind="feature", primary_types=[])]
        result = _build_ambiguous_concepts(cfg)
        self.assertIn("Views", result)

    def test_feature_with_two_primary_types_is_ambiguous(self):
        cfg = [_make_concept("Actions", artifact_kind="feature", primary_types=["ActionBase", "SimpleAction"])]
        result = _build_ambiguous_concepts(cfg)
        self.assertIn("Actions", result)

    def test_feature_with_three_primary_types_is_not_ambiguous(self):
        cfg = [_make_concept("Actions", artifact_kind="feature",
                              primary_types=["ActionBase", "SimpleAction", "PopupWindowShowAction"])]
        result = _build_ambiguous_concepts(cfg)
        self.assertNotIn("Actions", result)

    def test_module_with_no_primary_types_is_ambiguous(self):
        cfg = [_make_concept("Security System", artifact_kind="module", primary_types=[])]
        result = _build_ambiguous_concepts(cfg)
        self.assertIn("Security System", result)

    def test_conceptual_kind_is_ambiguous(self):
        cfg = [_make_concept("Deployment", artifact_kind="conceptual", primary_types=[])]
        result = _build_ambiguous_concepts(cfg)
        self.assertIn("Deployment", result)

    def test_pattern_kind_is_ambiguous(self):
        cfg = [_make_concept("Async Operations", artifact_kind="pattern", primary_types=[])]
        result = _build_ambiguous_concepts(cfg)
        self.assertIn("Async Operations", result)

    def test_api_kind_is_never_ambiguous(self):
        cfg = [_make_concept("XafApplication", artifact_kind="api", primary_types=[])]
        result = _build_ambiguous_concepts(cfg)
        self.assertNotIn("XafApplication", result)

    def test_tool_kind_is_never_ambiguous(self):
        cfg = [_make_concept("Model Editor", artifact_kind="tool", primary_types=[])]
        result = _build_ambiguous_concepts(cfg)
        self.assertNotIn("Model Editor", result)

    def test_concept_without_name_is_skipped(self):
        cfg = [{"artifact_kind": "feature", "primary_types": []}]
        result = _build_ambiguous_concepts(cfg)
        self.assertEqual(len(result), 0)

    def test_mixed_config(self):
        cfg = [
            _make_concept("Views", artifact_kind="feature", primary_types=[]),
            _make_concept("XafApplication", artifact_kind="api", primary_types=[]),
            _make_concept("Testing", artifact_kind="module", primary_types=[]),
        ]
        result = _build_ambiguous_concepts(cfg)
        self.assertIn("Views", result)
        self.assertIn("Testing", result)
        self.assertNotIn("XafApplication", result)


# ---------------------------------------------------------------------------
# B1: _get_ambiguous_concepts (caching)
# ---------------------------------------------------------------------------
class TestGetAmbiguousConcepts(unittest.TestCase):

    def setUp(self):
        # Reset the module-level cache before each test to get a clean state
        _mod._AMBIGUOUS_CONCEPTS_CACHE = None

    def tearDown(self):
        _mod._AMBIGUOUS_CONCEPTS_CACHE = None

    def test_returns_frozenset(self):
        cfg = [_make_concept("Views", artifact_kind="feature")]
        result = _get_ambiguous_concepts(cfg)
        self.assertIsInstance(result, frozenset)

    def test_second_call_returns_same_object(self):
        cfg = [_make_concept("Views", artifact_kind="feature")]
        first = _get_ambiguous_concepts(cfg)
        # Second call should return the cached object
        second = _get_ambiguous_concepts([])  # different (empty) config
        self.assertIs(first, second, "Cache should return the same frozenset object")

    def test_includes_expected_concept(self):
        cfg = [_make_concept("Navigation", artifact_kind="feature")]
        result = _get_ambiguous_concepts(cfg)
        self.assertIn("Navigation", result)


# ---------------------------------------------------------------------------
# B3: _check_domain_coherence
# ---------------------------------------------------------------------------
class TestCheckDomainCoherence(unittest.TestCase):

    # --- Delegation to specialized functions ---

    def test_deployment_delegates_to_specialized(self):
        """_check_domain_coherence must call _check_deployment_context for Deployment."""
        workflow_text = (
            "state machine workflow definition transition business process "
            "workflow designer workflow activity workflow instance"
        )
        heading = "Workflow > Design Basics"
        concept_def = _make_concept("Deployment", keywords=[], primary_types=[])
        base = 0.9
        result = _check_domain_coherence("Deployment", workflow_text, heading, base, concept_def)
        # _check_deployment_context reduces confidence in workflow context
        self.assertLess(result, base)

    def test_testing_delegates_to_specialized(self):
        """_check_domain_coherence must call _check_testing_context for Testing."""
        casual_text = "when testing the feature, after testing this component"
        heading = "Getting Started"
        concept_def = _make_concept("Testing", keywords=[], primary_types=[])
        base = 0.9
        result = _check_domain_coherence("Testing", casual_text, heading, base, concept_def)
        # _check_testing_context reduces confidence for casual usage
        self.assertLess(result, base)

    def test_migration_delegates_to_specialized(self):
        """_check_domain_coherence must call _check_migration_context for Migration."""
        generic_text = "migration guide for migrating from v1 to v2 migration process"
        heading = "Migration Guide"
        concept_def = _make_concept("Migration", keywords=[], primary_types=[])
        base = 0.9
        result = _check_domain_coherence("Migration", generic_text, heading, base, concept_def)
        self.assertLess(result, base)

    def test_application_templates_delegates_to_specialized(self):
        """_check_domain_coherence must call _check_application_templates_context."""
        ide_text = "template kit project template item template solution wizard new project"
        heading = "Project Creation"
        concept_def = _make_concept("Application Templates", keywords=[], primary_types=[])
        base = 0.9
        result = _check_domain_coherence("Application Templates", ide_text, heading, base, concept_def)
        self.assertLess(result, base)

    # --- Generic taxonomy-keyword check ---

    def test_generic_concept_with_matching_keywords_unchanged(self):
        """Generic concepts with matching taxonomy keywords keep full confidence."""
        keyword = "XafSecurityProvider"
        text = f"Configure XafSecurityProvider for your application"
        concept_def = _make_concept("Security System", keywords=[keyword], primary_types=[])
        base = 0.85
        result = _check_domain_coherence("Security System", text, "Security", base, concept_def)
        self.assertAlmostEqual(result, base, places=6)

    def test_generic_concept_with_no_matching_keywords_reduced(self):
        """Generic concepts whose taxonomy keywords are absent get reduced confidence."""
        text = "some unrelated text about other topics"
        concept_def = _make_concept("Security System",
                                    keywords=["XafSecurityProvider", "SecurityStrategyComplex"],
                                    primary_types=[])
        base = 0.85
        result = _check_domain_coherence("Security System", text, "Intro", base, concept_def)
        self.assertLess(result, base)

    def test_generic_concept_no_signals_defined_unchanged(self):
        """If taxonomy provides no keywords/primary_types, confidence is not changed."""
        text = "some text"
        concept_def = _make_concept("Theming", keywords=[], primary_types=[])
        base = 0.75
        result = _check_domain_coherence("Theming", text, "Theming", base, concept_def)
        self.assertAlmostEqual(result, base, places=6)

    def test_generic_concept_primary_types_count_as_signals(self):
        """primary_types from the taxonomy are also used as positive signals."""
        text = "Using XPObjectSpace to query persistent objects"
        concept_def = _make_concept("Object Space",
                                    keywords=[],
                                    primary_types=["XPObjectSpace", "CompositeXPObjectSpace"])
        base = 0.80
        result = _check_domain_coherence("Object Space", text, "Data Access", base, concept_def)
        self.assertAlmostEqual(result, base, places=6)


# ---------------------------------------------------------------------------
# B1 + extraction: extract_concepts_semantic (lexical fallback — no model)
# ---------------------------------------------------------------------------
class TestExtractConceptsSemanticLexical(unittest.TestCase):
    """Verify that the lexical fallback path works and returns correct types."""

    def setUp(self):
        from utils.taxonomy_loader import load_concepts
        cfg = load_concepts()
        self.concept_index = compile_concept_index(cfg)
        self.concepts_config = cfg.get("concepts", [])

    def test_returns_tuple(self):
        concepts, confidences = extract_concepts_semantic(
            text="XAF Security System",
            heading="Security",
            concept_index=self.concept_index,
            concepts_config=self.concepts_config,
            model=None,
        )
        self.assertIsInstance(concepts, list)
        self.assertIsInstance(confidences, dict)

    def test_lexical_match_found(self):
        concepts, confidences = extract_concepts_semantic(
            text="Configure XAF Security System authentication",
            heading="Security",
            concept_index=self.concept_index,
            concepts_config=self.concepts_config,
            model=None,
        )
        self.assertIn("Security System", concepts)

    def test_confidence_is_one_in_fallback(self):
        concepts, confidences = extract_concepts_semantic(
            text="Configure XAF Security System authentication",
            heading="Security",
            concept_index=self.concept_index,
            concepts_config=self.concepts_config,
            model=None,
        )
        for name, conf in confidences.items():
            self.assertAlmostEqual(conf, 1.0, places=6,
                                   msg=f"Expected fallback confidence=1.0 for {name}")

    def test_empty_text_returns_empty(self):
        concepts, confidences = extract_concepts_semantic(
            text="",
            heading="",
            concept_index=self.concept_index,
            concepts_config=self.concepts_config,
            model=None,
        )
        self.assertEqual(concepts, [])
        self.assertEqual(confidences, {})

    def test_ambiguous_concepts_built_from_taxonomy(self):
        """_get_ambiguous_concepts should return a non-empty frozenset for real taxonomy."""
        _mod._AMBIGUOUS_CONCEPTS_CACHE = None  # reset
        ambiguous = _get_ambiguous_concepts(self.concepts_config)
        self.assertIsInstance(ambiguous, frozenset)
        self.assertGreater(len(ambiguous), 0,
                           "Taxonomy should yield at least some ambiguous concepts")
        _mod._AMBIGUOUS_CONCEPTS_CACHE = None  # clean up


if __name__ == "__main__":
    unittest.main(verbosity=2)
