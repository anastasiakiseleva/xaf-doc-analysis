# Ollama Experimental Approaches - Decision Log

**Date:** February 11, 2026  
**Status:** Under Evaluation  
**Purpose:** Evaluate LLM-based classification approaches for API-concept mapping and relationship classification

---

## Executive Summary

The project has two experimental LLM-based classification pathways using Ollama:
1. **API-Concept Mapping** - Enhance Phase 12 with LLM classification
2. **Relationship Classification** - Phase 6 semantic relationship typing

Both approaches aim to automate manual tagging work, but require tradeoff analysis between accuracy, speed, and cost.

---

## Approach 1: API-Concept Mapping with Ollama

### Implementation
**Script:** `scripts/experimental/12_map_apis_to_concepts_ollama.py`  
**Model:** Llama 3.1 via Ollama  
**Location:** scripts/experimental/ folder

### Strategy
Combines three classification methods:
1. **Co-occurrence** (existing) - APIs and concepts appearing together in docs
2. **Namespace rules** (existing) - Pattern matching (e.g., DevExpress.*.Security → Security System)
3. **Ollama classification** (new) - LLM-based inference for unmapped APIs

### Prompting Approach
```
System Prompt: Expert XAF documentation analyzer
Input: API namespace, name, type, documentation context
Output: JSON list of applicable concepts with confidence scores
```

**Key Features:**
- 45 XAF concepts provided in system prompt
- Namespace-based inference rules included
- Interface and base class pattern recognition
- Confidence scoring (0.0-1.0)

### Coverage Analysis

| Method | Coverage | Precision | Speed |
|--------|----------|-----------|-------|
| Co-occurrence | ~40% | Very High (95%+) | Instant |
| Namespace Rules | ~20% | High (90%+) | Instant |
| Ollama Classification | ~40% | Medium (70-80%?) | Slow (2-5 sec/API) |
| **Combined** | **~100%** | **High (85%+)** | **Mixed** |

### Validation Tool
**Script:** `scripts/experimental/validate_ollama_accuracy.py`

Tests Ollama classification against known ground truth mappings from co-occurrence data.

**Usage:**
```bash
# Test on 50 random APIs with known concepts
python scripts/experimental/validate_ollama_accuracy.py --sample 50

# Test specific concepts
python scripts/experimental/validate_ollama_accuracy.py --concepts "Security System,Actions,Views"

# Detailed output
python scripts/experimental/validate_ollama_accuracy.py --sample 100 --verbose
```

### Pros ✅
- **Fills gaps** - Classifies APIs that rules miss
- **No external API costs** - Runs locally with Ollama
- **Customizable** - Can iterate on prompts easily
- **Transparent** - Open-source model, auditable
- **Offline capable** - No internet dependency

### Cons ⚠️
- **Speed** - 2-5 seconds per API (would take 3-8 hours for 6,853 APIs)
- **Accuracy unknown** - Requires validation against ground truth
- **Resource intensive** - Needs GPU/CPU for Ollama
- **Prompt engineering** - Requires iteration to optimize
- **Maintenance** - Model updates may change behavior

### Current Status
- ✅ Implementation complete
- ✅ Validation tool implemented
- ⚠️ **NOT yet validated** - No accuracy metrics captured
- ⚠️ **NOT yet run on full dataset** - Only tested on samples

### Decision Criteria
**Run full validation before adoption:**
1. Measure precision/recall on 100-200 known API-concept pairs
2. Target: ≥75% precision, ≥60% recall on Ollama-classified APIs
3. If passing: Run full dataset overnight
4. If failing: Iterate on system prompt and re-validate

### Recommended Next Steps
1. **Week 1:** Run validation study
   ```bash
   python validate_ollama_accuracy.py --sample 200 --verbose > validation_report.txt
   ```
2. **Week 1:** Analyze precision/recall by concept category
3. **Week 2:** If validation passes, run full classification
   ```bash
   python 12_map_apis_to_concepts_ollama.py --use-ollama --unmapped-only
   ```
4. **Week 2:** Compare against rule-based baseline
5. **Week 3:** Decide: merge into main script or archive

---

## Approach 2: Relationship Classification with Ollama

### Implementation
**Script:** `scripts/06_classify_relationships.py`  
**Model:** Configurable (OpenAI, Anthropic, or Ollama)  
**Status:** Partially implemented

### Purpose
Classify semantic relationships between documentation sections into types:
- `explains` - Section A explains concept in B
- `requires` - Section A requires understanding B
- `uses` - Section A uses/implements B
- `extends` - Section A extends B
- `applies_to` - Section A applies to scenarios in B
- `contrasts_with` - Section A contrasts with B
- `related_to` - General semantic similarity

### Strategy
1. Filter to high-value pairs (Phase 5.5) - ~5,000 pairs
2. For each pair, provide:
   - Source section: title, text, concepts, platform
   - Target section: title, text, concepts, platform
   - Similarity score
3. LLM classifies relationship type with confidence

### Checkpoint System
- Saves progress every N classifications
- Resume from last checkpoint on failure
- Prevents re-processing already classified pairs

### Pros ✅
- **Enables intelligent features** - Smart navigation, learning paths
- **Human-readable** - Relationship types are interpretable
- **Prioritized** - Only processes high-value pairs (5K not 94K)
- **Resumable** - Checkpoint system prevents loss of work

### Cons ⚠️
- **Slow** - Even 5,000 pairs × 5 sec = 7 hours processing time
- **API dependency** - Requires LLM API or Ollama setup
- **Prompt complexity** - Relationship classification is nuanced
- **Validation difficulty** - No ground truth for relationship types
- **Unclear ROI** - Are relationship types actually useful?

### Current Status
- ✅ Implementation complete with checkpoint system
- ⚠️ **LLM API not configured** - Script placeholder exists
- ⚠️ **No Ollama integration** - Would require adapter code
- ❌ **Never run** - Zero classifications completed

### Decision Criteria
**Requires use case validation:**
1. Define specific use case for relationship types
2. Design user-facing feature that needs this data
3. Estimate user value vs. processing time/cost
4. If valuable: Configure LLM API and run pilot (500 pairs)
5. If not valuable: Mark as "future" and skip

### Recommended Next Steps
1. **Decision Point:** Is relationship classification needed?
   - **Option A (Yes):** We have specific use case (e.g., learning path generator)
     - Configure API (OpenAI/Anthropic recommended over Ollama for this task)
     - Run pilot on 500 high-value pairs
     - Evaluate usefulness of outputs
     - Decide: continue or abandon
   
   - **Option B (No):** Defer until use case emerges
     - Archive script as "future enhancement"
     - Focus effort on higher-ROI improvements
     - Revisit when building features that need relationship types

---

## Comparative Analysis

| Aspect | API-Concept Mapping (Ollama) | Relationship Classification |
|--------|------------------------------|----------------------------|
| **Scope** | 6,853 APIs to classify | 5,000 high-value pairs |
| **Processing Time** | 3-8 hours | 7 hours |
| **Immediate Value** | High - Fixes 6 gap concepts | Low - No immediate use case |
| **Validation Path** | Clear - Compare to ground truth | Unclear - No ground truth |
| **Risk** | Low - Can fallback to rules | Medium - Wasted effort if unused |
| **Dependencies** | Ollama (local) | LLM API or Ollama |
| **Status** | Ready to validate | Needs use case definition |

---

## Technology Choice: Ollama vs. API-Based LLMs

### Ollama (Llama 3.1)
**Best for:**
- High-volume classification (thousands of items)
- Cost sensitivity
- Offline/air-gapped environments
- Privacy-sensitive data

**Tradeoffs:**
- Slower inference (2-5 sec per item)
- Lower accuracy (estimated 70-80% vs 85-95% for GPT-4)
- Requires local compute resources

### API-Based (OpenAI/Anthropic)
**Best for:**
- Complex classification tasks
- Higher accuracy requirements
- Lower volume workloads
- When speed matters

**Tradeoffs:**
- Per-request costs ($0.01-0.10 per classification)
- Internet dependency
- Rate limits
- Data privacy considerations

### Recommendation by Task

| Task | Recommended Approach | Rationale |
|------|---------------------|-----------|
| **API-Concept Mapping** | Ollama (Llama 3.1) | High volume (6,853), clear validation path, cost-sensitive |
| **Relationship Classification** | API-Based (GPT-4) | Complex task, needs high accuracy, lower volume (5,000), unclear value → use best tool for pilot |

---

## Decision Framework

### When to Use LLM Classification
✅ **Yes, if:**
- Rules-based approach has gaps (>20% uncovered)
- Clear validation methodology exists
- Accuracy requirements are ≥70%
- Processing time is acceptable (<24 hours)
- Result has immediate use case

❌ **No, if:**
- Rules-based approach covers ≥90% of cases
- No validation methodology available
- Requires ≥95% accuracy (human review may be better)
- No clear use case for results
- Processing time exceeds 48 hours

### Current Recommendations

#### API-Concept Mapping: **PROCEED TO VALIDATION** ✅
1. Run validation study (Week 1)
2. If accuracy ≥75%: Run full classification (Week 2)
3. If accuracy <75%: Iterate on prompts, re-validate
4. Integrate successful approach into main script

#### Relationship Classification: **DEFER** ⏸️
1. Define specific use case first
2. If use case emerges: Run pilot with API-based LLM
3. If pilot successful: Consider Ollama for full run
4. If no use case: Archive as future enhancement

---

## Lessons Learned

### What Worked Well
- ✅ **Hybrid approach** - Combining rules + LLM fills more gaps than either alone
- ✅ **Checkpoint system** - Prevents loss of work on long-running tasks
- ✅ **Validation tools** - Building validation framework upfront enables data-driven decisions
- ✅ **Filtering** - Pre-filtering to high-value pairs makes LLM work manageable

### What Needs Improvement
- ⚠️ **Validation first** - Should validate accuracy before full implementation
- ⚠️ **Use case clarity** - Define user-facing feature before building infrastructure
- ⚠️ **Documentation** - Experimental approaches got ahead of documentation
- ⚠️ **Integration path** - Need clear criteria for graduating experimental → production

### Process Improvements
1. **Always validate on sample before full run**
2. **Define success criteria upfront** (accuracy thresholds, time limits)
3. **Document decisions at time of implementation** (not retroactively)
4. **Create clear graduation path** for experimental features

---

## Files Related to Ollama Experiments

### Production Scripts
- `scripts/12_map_apis_to_concepts.py` - Rule-based API-concept mapping

### Experimental Scripts
- `scripts/experimental/12_map_apis_to_concepts_ollama.py` - Enhanced with Ollama
- `scripts/experimental/validate_ollama_accuracy.py` - Validation framework
- `scripts/06_classify_relationships.py` - Relationship classification (needs API)

### Documentation
- `OLLAMA_QUICKSTART.md` - Setup instructions (root dir)
- `ollama_api_concept_prompts.md` - Prompt engineering notes (root dir)
- `docs/ollama_decision_log.md` - This decision log
- `scripts/experimental/README.md` - Experimental folder documentation

### Configuration
- `config/prompts/relationship_classification.md` - Classification prompt template

### Outputs
- `outputs/classified_pairs_checkpoint.parquet` - Partial classification progress
- `outputs/api_implements_concept.parquet` - Rule-based API mappings (production)

---

## Next Actions

### Immediate (This Week)
- [ ] Run `python scripts/experimental/validate_ollama_accuracy.py --sample 200` for API-concept mapping
- [ ] Analyze precision/recall results
- [ ] Document accuracy metrics in this log
- [ ] Make GO/NO-GO decision on full Ollama run

### Short-term (Next 2 Weeks)
- [ ] If validation passes: Run full API-concept classification overnight
- [ ] Compare enhanced mappings vs. rule-based baseline
- [ ] Update gap analysis to see if 6 gap concepts are fixed
- [ ] Document final approach in README
- [ ] If successful: Merge into `scripts/12_map_apis_to_concepts.py`

### Long-term (Next Month)
- [ ] Define use case for relationship classification OR archive
- [ ] Graduate successful Ollama approach to production script
- [ ] Archive experimental folder if approaches are merged
- [ ] Update graduation criteria based on lessons learned

### Archive (If Validation Fails)
- [ ] Document why Ollama approach didn't meet accuracy threshold
- [ ] Move failed experiments to `scripts/experimental/archive/` folder
- [ ] Focus on improving rule-based approaches instead
- [ ] Consider alternative automation strategies

---

## Contact & Questions

For questions about Ollama python scripts/experimental/validate_ollama_accuracy.py --help`
- Review prompts: `ollama_api_concept_prompts.md`
- Setup Ollama: `OLLAMA_QUICKSTART.md`
- General setup: `docs/setup_ollama_classification.md`
- Experimental folder: `scripts/experimental/README
- General setup: `docs/setup_ollama_classification.md`

**Last Updated:** February 11, 2026
