# Experimental Scripts

This folder contains experimental approaches that are under evaluation before potential graduation to production use.

## Current Experiments

### 1. Ollama-Based API-Concept Mapping
**Script:** `12_map_apis_to_concepts_ollama.py`

Enhanced version of Phase 12 that adds LLM-based classification using Ollama (Llama 3.1).

**Purpose:** Fill gaps in rule-based API-to-concept mapping by using LLM inference.

**Status:** ⚠️ Ready for validation testing

**Usage:**
```bash
# Test on 10 APIs
python scripts/experimental/12_map_apis_to_concepts_ollama.py --sample 10 --use-ollama

# Run on unmapped APIs only
python scripts/experimental/12_map_apis_to_concepts_ollama.py --use-ollama --unmapped-only

# Full run (overnight)
python scripts/experimental/12_map_apis_to_concepts_ollama.py --use-ollama
```

**Next Steps:**
1. Run validation study: `python scripts/experimental/validate_ollama_accuracy.py --sample 200`
2. If accuracy ≥75%: Run full classification
3. If successful: Merge into `scripts/12_map_apis_to_concepts.py`

### 2. Ollama Accuracy Validation
**Script:** `validate_ollama_accuracy.py`

Tests Ollama classification accuracy against known ground truth API-concept mappings.

**Purpose:** Measure precision/recall before committing to full LLM-based classification run.

**Status:** ✅ Ready to use

**Usage:**
```bash
# Test on 50 random APIs with known concepts
python scripts/experimental/validate_ollama_accuracy.py --sample 50

# Test specific concepts
python scripts/experimental/validate_ollama_accuracy.py --concepts "Security System,Actions,Views"

# Detailed output
python scripts/experimental/validate_ollama_accuracy.py --sample 100 --verbose
```

**Validation Criteria:**
- Target: ≥75% precision, ≥60% recall
- Ground truth: Co-occurrence from doc_concepts.parquet
- Sample size: Minimum 100 APIs for reliable metrics

## Graduation Criteria

An experimental script graduates to production when:

1. ✅ **Validated** - Accuracy meets defined thresholds
2. ✅ **Documented** - Usage and limitations clearly explained
3. ✅ **ROI positive** - Value justifies maintenance cost
4. ✅ **Integrated** - Merged into production pipeline or standalone tool
5. ✅ **Tested** - Run on full dataset with successful results

## Decision Framework

See [docs/ollama_decision_log.md](../../docs/ollama_decision_log.md) for:
- Technology tradeoffs (Ollama vs API-based LLMs)
- Use case evaluation
- Recommended next steps
- Lessons learned

## Archived Experiments

None yet. When experiments are abandoned or graduated, they'll be documented here with rationale.

---

**Last Updated:** February 11, 2026
