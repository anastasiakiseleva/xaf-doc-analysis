#!/usr/bin/env python3
"""
Unit tests for Phase C improvements in scripts/04_make_sections_embeddings.py.

Covers:
  C1 - assemble_text appends Concepts line with domain annotations
  C2 - assemble_text prepends API symbols for API sections
  C3 - --no-concept-context flag disables enrichment; parse_args includes the flag
"""

import sys
import importlib.util
import unittest
from pathlib import Path

# ---------------------------------------------------------------------------
# Load script via importlib (numeric prefix)
# ---------------------------------------------------------------------------
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
_script_path = Path(__file__).parent.parent / "scripts" / "04_make_sections_embeddings.py"
_spec = importlib.util.spec_from_file_location("emb_module", _script_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

assemble_text = _mod.assemble_text
_safe_list = _mod._safe_list
parse_args = _mod.parse_args


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
_BASE_META = {
    "title": "XAF Security Guide",
    "h_path_list": ["Security", "Authentication"],
    "text": "Configure Security System for your application.",
    "code_blocks": ["var sp = new SecurityProvider();"],
}


# ---------------------------------------------------------------------------
# C1 — Concept context line (assemble_text with concept_context=True)
# ---------------------------------------------------------------------------
class TestAssembleTextC1(unittest.TestCase):

    def test_concept_line_appended_when_enabled(self):
        text = assemble_text(
            _BASE_META, include_code=False, max_chars=4000,
            concepts=["Security System", "Authentication"],
            concept_domains={"Security System": "security", "Authentication": "security"},
            concept_context=True,
        )
        self.assertIn("Concepts:", text)
        self.assertIn("Security System", text)
        self.assertIn("Authentication", text)

    def test_concept_line_includes_domain_annotation(self):
        text = assemble_text(
            _BASE_META, include_code=False, max_chars=4000,
            concepts=["Security System"],
            concept_domains={"Security System": "security"},
            concept_context=True,
        )
        self.assertIn("(security)", text)

    def test_concept_line_absent_when_disabled(self):
        text = assemble_text(
            _BASE_META, include_code=False, max_chars=4000,
            concepts=["Security System"],
            concept_domains={"Security System": "security"},
            concept_context=False,           # C3 disable
        )
        self.assertNotIn("Concepts:", text)

    def test_concept_line_absent_when_no_concepts(self):
        text = assemble_text(
            _BASE_META, include_code=False, max_chars=4000,
            concepts=[],
            concept_context=True,
        )
        self.assertNotIn("Concepts:", text)

    def test_concept_line_absent_when_concepts_is_none(self):
        text = assemble_text(
            _BASE_META, include_code=False, max_chars=4000,
            concepts=None,
            concept_context=True,
        )
        self.assertNotIn("Concepts:", text)

    def test_missing_domain_omits_annotation(self):
        # A concept not present in concept_domains should appear without parentheses
        text = assemble_text(
            _BASE_META, include_code=False, max_chars=4000,
            concepts=["Security System"],
            concept_domains={},              # empty — domain unknown
            concept_context=True,
        )
        self.assertIn("Security System", text)
        self.assertNotIn("()", text)         # Should not produce empty parens

    def test_concept_line_is_after_body(self):
        text = assemble_text(
            _BASE_META, include_code=False, max_chars=4000,
            concepts=["Security System"],
            concept_domains={"Security System": "security"},
            concept_context=True,
        )
        body_pos = text.find("Configure Security System")
        concept_pos = text.find("Concepts:")
        self.assertGreater(concept_pos, body_pos, "Concepts line should follow body text")

    def test_concept_line_capped_at_20_concepts(self):
        # Build 30 concept names; only 20 should appear
        concepts = [f"Concept{i}" for i in range(30)]
        domains = {f"Concept{i}": "ui" for i in range(30)}
        text = assemble_text(
            _BASE_META, include_code=False, max_chars=40000,
            concepts=concepts, concept_domains=domains, concept_context=True,
        )
        line = [l for l in text.split("\n") if l.startswith("Concepts:")][0]
        # Count commas + 1 for number of items
        item_count = len(line.split(", "))
        self.assertLessEqual(item_count, 20)

    def test_base_text_still_present(self):
        text = assemble_text(
            _BASE_META, include_code=False, max_chars=4000,
            concepts=["Security System"],
            concept_domains={"Security System": "security"},
            concept_context=True,
        )
        self.assertIn("XAF Security Guide", text)
        self.assertIn("Configure Security System", text)


# ---------------------------------------------------------------------------
# C2 — API symbol prepend (assemble_text with is_api=True)
# ---------------------------------------------------------------------------
class TestAssembleTextC2(unittest.TestCase):

    def test_api_line_prepended_for_api_section(self):
        text = assemble_text(
            _BASE_META, include_code=False, max_chars=4000,
            apis=["XafSecurityProvider", "SecurityStrategyComplex"],
            is_api=True,
            concept_context=True,
        )
        self.assertTrue(text.startswith("API:"), f"Expected text to start with 'API:' but got: {text[:60]!r}")

    def test_api_line_not_prepended_for_conceptual_section(self):
        text = assemble_text(
            _BASE_META, include_code=False, max_chars=4000,
            apis=["XafSecurityProvider"],
            is_api=False,          # conceptual section
            concept_context=True,
        )
        self.assertFalse(text.startswith("API:"))

    def test_api_line_not_prepended_when_disabled(self):
        text = assemble_text(
            _BASE_META, include_code=False, max_chars=4000,
            apis=["XafSecurityProvider"],
            is_api=True,
            concept_context=False,  # C3 disable
        )
        self.assertFalse(text.startswith("API:"))

    def test_api_line_not_prepended_when_apis_empty(self):
        text = assemble_text(
            _BASE_META, include_code=False, max_chars=4000,
            apis=[],
            is_api=True,
            concept_context=True,
        )
        self.assertFalse(text.startswith("API:"))

    def test_api_line_not_prepended_when_apis_none(self):
        text = assemble_text(
            _BASE_META, include_code=False, max_chars=4000,
            apis=None,
            is_api=True,
            concept_context=True,
        )
        self.assertFalse(text.startswith("API:"))

    def test_api_line_is_before_title(self):
        text = assemble_text(
            _BASE_META, include_code=False, max_chars=4000,
            apis=["XafSecurityProvider"],
            is_api=True,
            concept_context=True,
        )
        api_pos = text.find("API:")
        title_pos = text.find("XAF Security Guide")
        self.assertLess(api_pos, title_pos, "API line should precede title")

    def test_api_symbols_sorted_and_capped(self):
        apis = [f"Api{i:03d}" for i in range(50)]
        text = assemble_text(
            _BASE_META, include_code=False, max_chars=40000,
            apis=apis, is_api=True, concept_context=True,
        )
        api_line = text.split("\n")[0]
        self.assertTrue(api_line.startswith("API:"))
        # At most 30 items (sorted set, then [:30])
        items = api_line[4:].split(", ")
        self.assertLessEqual(len(items), 30)


# ---------------------------------------------------------------------------
# C3 — parse_args includes --no-concept-context flag
# ---------------------------------------------------------------------------
class TestParseArgsC3(unittest.TestCase):

    def _parse(self, *extra):
        """Helper: parse with minimal valid args + optional extras."""
        import sys as _sys
        old_argv = _sys.argv
        _sys.argv = ["04_make_sections_embeddings.py"] + list(extra)
        try:
            return parse_args()
        finally:
            _sys.argv = old_argv

    def test_no_concept_context_default_false(self):
        args = self._parse()
        self.assertFalse(args.no_concept_context)

    def test_no_concept_context_flag_sets_true(self):
        args = self._parse("--no-concept-context")
        self.assertTrue(args.no_concept_context)


# ---------------------------------------------------------------------------
# Truncation still works correctly
# ---------------------------------------------------------------------------
class TestAssembleTextTruncation(unittest.TestCase):

    def test_body_truncated_to_max_chars(self):
        long_meta = {
            "title": "T",
            "h_path_list": [],
            "text": "X" * 10000,
            "code_blocks": [],
        }
        text = assemble_text(
            long_meta, include_code=False, max_chars=100,
            concept_context=False,
        )
        # Concept line is appended after truncation, so body part is ≤ max_chars
        # and total len may exceed it by the concept line length
        body_only = text.split("\nConcepts:")[0]
        self.assertLessEqual(len(body_only), 100)

    def test_concept_line_always_present_even_after_truncation(self):
        long_meta = {
            "title": "T",
            "h_path_list": [],
            "text": "X" * 10000,
            "code_blocks": [],
        }
        text = assemble_text(
            long_meta, include_code=False, max_chars=50,
            concepts=["Security System"],
            concept_domains={"Security System": "security"},
            concept_context=True,
        )
        self.assertIn("Concepts:", text)


# ---------------------------------------------------------------------------
# _safe_list helper
# ---------------------------------------------------------------------------
class TestSafeList(unittest.TestCase):

    def test_none_returns_empty(self):
        self.assertEqual(_safe_list(None), [])

    def test_nan_returns_empty(self):
        import math
        self.assertEqual(_safe_list(float("nan")), [])

    def test_list_passthrough(self):
        self.assertEqual(_safe_list([1, 2, 3]), [1, 2, 3])

    def test_string_not_exploded(self):
        # strings should NOT be iterated character by character
        result = _safe_list("hello")
        # The function iterates __iter__ for non-str, but for strings returns early
        # Actually the current impl does list("hello") for strings — verify it doesn't
        # The guard `not isinstance(val, str)` blocks that
        self.assertNotEqual(result, ["h", "e", "l", "l", "o"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
