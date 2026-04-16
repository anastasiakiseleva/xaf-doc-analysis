# Taxonomy Review: XAF Documentation Taxonomy v1.0

**Date:** 2026-04-16  
**Reviewer:** GitHub Copilot (Claude Sonnet 4.6)  
**Standards applied:** Hedden, *The Accidental Taxonomist* (2010, §4.3) · ANSI/NISO Z39.19 · W3C SKOS Primer

---

## 1. Vocabulary Control & Term Selection (Z39.19 §5–6; Hedden §4.3.1)

**Strengths:**
- `terminology.synonyms` provides equivalence relationships for 85% of concepts — good USE/UF coverage.
- The `name` field functions as the preferred term (SKOS `prefLabel`); `synonyms` function as `altLabel`. This mapping is clean.

**Issues:**

| Problem | Standard violated | Severity |
|---|---|---|
| **Synonyms mix natural-language labels with code identifiers.** E.g., "Application Model" concept has synonyms like `"UI metadata"` alongside `"Model Editor"` (a tool, not a synonym). | Z39.19 §6.2.1: equivalence relations must be between truly synonymous terms, not between a concept and a tool that manipulates it. | Medium |
| **No `hiddenLabel` equivalent for typos/search variants.** Terms like `"Nonpersistent"`, `"Non persistent"`, `"NPO"` are stored in `synonyms` alongside real synonyms like `"DTO"`. | SKOS §2.4: `hiddenLabel` exists specifically for misspellings and lexical variants that aren't true synonyms. | Low |
| **`keywords` vs. `synonyms` distinction is undocumented.** 18% of concepts use `keywords` but there's no scope note explaining how keywords differ from synonyms. | Z39.19 §8.3: scope notes should clarify usage rules for any non-obvious vocabulary feature. | Medium |
| **15% of concepts have NO synonyms at all** (30 concepts, including Object Space Provider, Performance Optimization, Testing). These are findability gaps. | Hedden §4.3.1: "every concept that users might look for by more than one name should have entry terms." | Medium |

---

## 2. Hierarchical Relationships (Z39.19 §7.2; Hedden §4.3.2; SKOS `broader`/`narrower`)

**Strengths:**
- Maximum hierarchy depth is 2 levels — appropriate for a flat domain taxonomy.
- `part_of` chains are correctly unidirectional (child → parent). No cycles.
- Zero dangling references — all relation targets resolve to valid concept IDs.

**Issues:**

| Problem | Standard violated | Severity |
|---|---|---|
| **Three distinct hierarchical relation types (`is_a`, `part_of`, `related_to`) conflate different semantics.** `is_a` was used for both true generic relationships (ListView `is_a` View Types) AND compositional membership (Audit Trail `is_a` Security System, which should be `part_of`). | Z39.19 §7.2 distinguishes three valid BT/NT types: generic (genus-species), instance, and whole-part. Mixing them under a single `is_a` violates this. Hedden §4.3.2: "A hierarchical relationship should pass the 'all-and-some' test." | High — ✅ Fixed 2026-04-16 |
| **`is_a` failed the all-and-some test in multiple cases.** "All Audit Trails are Security Systems" is false — Audit Trail is a *part* of the security subsystem, not a *kind* of security system. Same for: Optimistic Locking, Clone Object, State Machine, Charts, Dashboards. | Z39.19 §7.2.1: Generic relationship requires that "all members of the narrower concept class are also members of the broader concept class." | High — ✅ Fixed 2026-04-16 |
| **26 orphan concepts** (13% of taxonomy at initial assessment; 84 at current count with 201 concepts) have zero incoming references. They exist as vocabulary islands. Tooling (5), Localization (4), and UI/UX (8) domains are worst affected. | Hedden §4.3: "Every term in a taxonomy should ideally have at least one relationship to another term." SKOS §4.6.3: isolated concepts violate scheme coherence. | High — ⬜ Open |
| **Parents with a single child** violate the minimum sibling rule. Validation→Custom Validation Rules, Multi-Tenancy→Tenant, Deployment→Scaling Architecture each have exactly 1 child. | Z39.19 §7.2: "Each term in a hierarchical array should have at least one sibling." If a broader term has only one narrower term, it suggests the hierarchy level is unnecessary. | Medium — ⬜ Open |
| **Reciprocity was missing.** `part_of` was stored only on the child with no inverse `has_part` on the parent; no `narrower` to complement `broader`. Same for `is_a` — no inverse `has_kind`. | Z39.19 §7.1: "Reciprocal entries shall be made for all relationships." SKOS maps `broader`↔`narrower` as inverse pairs. | Medium — ✅ Fixed 2026-04-16 (Option B: computed at load time) |

---

## 3. Associative Relationships (Z39.19 §8; Hedden §4.3.3; SKOS `related`)

**Strengths:**
- `related_to` is the most-used relation type (68 concepts). Coverage of cross-domain links is reasonable.
- `related_to` symmetry is enforced by CI test (`test_related_to_symmetric`).

**Issues:**

| Problem | Standard violated | Severity |
|---|---|---|
| **8 asymmetric `related_to` pairs.** E.g., Business Object → Property Editors but Property Editors ⊘ Business Object (as reported by initial subagent analysis — confirmed 0 true asymmetries in current data after verification). | Z39.19 §8.1: "Associative relationships are reciprocal." SKOS `related` is symmetric by definition. | High — ✅ Verified clean |
| **`related_to` is undifferentiated.** A single relation type covers "depends on", "extends", "see also", "works with", and "complements". | Hedden §4.3.3: associative relationships should be distinguishable by type when the taxonomy supports more than simple see-also linking. Z39.19 §8.2 lists specific subtypes. | Medium — ⬜ Open |
| **102 concepts (51%) have NO explicit relations at all.** Over half the taxonomy has no connections to any other concept. | SKOS §4.6: a concept with no semantic relationships to other concepts in the same scheme is "isolated" and represents incomplete modeling. | High — ⬜ Open |

---

## 4. Concept Identity & Scope (SKOS §2; Z39.19 §5.3)

**Strengths:**
- 100% consistent ID pattern: `xaf.{domain}.{subdomain}.{name}` — excellent for machine processing.
- Every concept has a `description` — functioning as SKOS `definition` / Z39.19 scope note.

**Issues:**

| Problem | Standard violated | Severity |
|---|---|---|
| **Descriptions vary wildly in granularity.** Compare "Accordion-style collapsible panel control" (41 chars) to "Headless backend service exposing OData/REST endpoints for CRUD operations, authentication, and data access from non-XAF clients" (127 chars). No consistent depth. | Z39.19 §9.2: scope notes should be "brief, clear statements" of consistent depth. | Low — ⬜ Open |
| **No `scopeNote` distinguished from `definition`.** The single `description` field conflates definitional scope (what the concept IS) with usage guidance (when/how to apply it). | SKOS distinguishes `definition` (what it is) from `scopeNote` (how to apply it in context). | Low — ⬜ Open |
| **`artifact_kind` mixes abstraction levels.** "conceptual" is an abstraction level, while "module" and "tool" are concrete packaging types. This confuses what a concept *is* with how it's *delivered*. | Hedden §3.2: facets in a taxonomy should be orthogonal — each facet should represent one independent dimension. | Medium — ⬜ Open |

---

## 5. Concept Scheme Structure (SKOS §4; Z39.19 §7)

**Strengths:**
- 9 top-level domains provide reasonable high-level faceting.
- `facets` (platforms, audiences, lifecycle_phases, stability) are cleanly orthogonal to each other.

**Issues:**

| Problem | Standard violated | Severity |
|---|---|---|
| **Severe domain imbalance.** UI has 92 concepts (46%), Data has 55 (27%). Migration has 2, Quality has 3, Ops has 5. This means retrieval precision varies enormously across domains. | Hedden §5.4: "A well-balanced taxonomy has a relatively even distribution of terms across its top categories." | Medium — ⬜ Open |
| **No top concept (`skos:hasTopConcept`).** There is no explicit designation of which concepts are entry points vs. subordinate. The schema has no `isTopConcept` flag. | SKOS §4.6.1: every concept scheme should declare its top concepts for navigational entry. | Medium — ⬜ Open |
| **`replaces` relation used by only 2 concepts** (Template Kit, Reports V2) but is schema-defined. This is under-used or premature. | Z39.19 §6.3: historical note relationships should be systematic, not sporadic. | Low — ⬜ Open |
| **`tags` field is an uncontrolled vocabulary.** 63 concepts use freeform tags like `"lifecycle"`, `"threading"`, `"compliance"` with no controlled list. Tags like `"hierarchy"` and `"tree"` potentially overlap. | Z39.19 §5.1: all terms in a controlled vocabulary should be governed by a controlled authority list. | Medium — ⬜ Open |

---

## 6. Hybrid API-Documentation Nature (Structural Observation)

This taxonomy serves a dual purpose that is unusual: it's both a **documentation knowledge organization system** (via `terminology`, `relations`, `doc_intents`) and an **API surface registry** (via `api_surface.primary_types`, `related_types`).

This is not inherently wrong, but:

- **`api_surface` has no parallel in Z39.19 or SKOS.** It's a custom extension. The 45 remaining primary_types overlaps suggest the "one type → one concept" ideal isn't achievable for API mapping.
- **`doc_intents` are a facet, not a relationship.** Placing them under `documentation` works, but they'd be more powerful as a formal facet in `facets` to enable cross-cutting queries.

---

## 7. Summary & Priority Recommendations

| # | Issue | Impact | Status |
|---|---|---|---|
| 1 | Fix `is_a` vs. `part_of` misclassifications — 9 concepts used `is_a` where Z39.19 requires whole-part | Semantic integrity | ✅ Done 2026-04-16 |
| 2 | Make `related_to` symmetric — reciprocal CI enforcement and load-time verification | Graph navigability | ✅ Verified clean |
| 3 | Implement reciprocal inverse relations (`has_part`, `has_kind`) computed at load time | Z39.19 §7.1 compliance | ✅ Done 2026-04-16 |
| 4 | Connect the orphan concepts — at minimum `part_of` or `related_to` (84 concepts, 42% of 201) | Findability, scheme coherence | ⬜ Open |
| 5 | Connect the relation-less concepts — at least `related_to` for obvious neighbors | Findability | ⬜ Open |
| 6 | Resolve single-child hierarchies — add siblings or promote | Structural validity | ⬜ Open |
| 7 | Separate `synonyms` from search variants — add a `search_variants` or `hidden_labels` field | Vocabulary precision | ⬜ Open |
| 8 | Control the `tags` vocabulary — define an enum in the schema | Consistency | ⬜ Open |
| 9 | Document the `keywords` vs. `synonyms` distinction — add a scope note to the schema contract | Usability | ⬜ Open |

---

## 8. Metrics Snapshot

| Metric | Value at Review | Notes |
|---|---|---|
| Total concepts | 201 | Up from 148 at start of primary_types review session |
| Overlapping `primary_types` | 45 | Down from ~130 after full primary_types review pass |
| Orphan concepts (no incoming refs) | 84 | 42% of taxonomy |
| Asymmetric `related_to` pairs | 0 | Enforced by CI test |
| `is_a` misclassified as whole-part | 0 | Fixed 2026-04-16 |
| Hierarchy max depth | 2 | Appropriate for this taxonomy |
| Concepts with no relations at all | 102 | 51% |
| Test suite | 54 passed, 4 skipped | After all 2026-04-16 fixes |
