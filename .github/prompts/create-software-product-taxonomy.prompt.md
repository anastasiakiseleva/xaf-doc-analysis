## Skill: Create a Taxonomy for a Software Product

Build a structured, governed taxonomy for a software product's documentation and knowledge management. This skill follows the methodology from Heather Hedden's *The Accidental Taxonomist* (2nd edition), adapted for software product domains.

The taxonomy is a **knowledge organization system** — a controlled vocabulary with hierarchical, equivalence, and associative relationships designed to support content findability, discovery, and consistent indexing.

---

### Inputs

Gather these before starting. If any are missing, ask the user.

| Input | Description | Required |
|---|---|---|
| `product_name` | Canonical name of the software product | Yes |
| `content_corpus` | Path(s) to documentation, API references, release notes, support tickets | Yes |
| `audience` | Primary users of the taxonomy (developers, end-users, doc authors, support) | Yes |
| `purpose` | Primary function: indexing support, retrieval support, or navigation support | Yes |
| `existing_taxonomy` | Path to any existing taxonomy file to extend (e.g., `config/xaf-taxonomy.json`) | No |
| `schema` | Path to taxonomy schema (e.g., `config/xaf-taxonomy.schema.json`) | No |
| `scope_constraints` | Domains or areas explicitly in/out of scope | No |

---

### Phase 1 — Project Planning & Research

**Objective:** Answer the five fundamental planning questions before creating any terms.

#### Step 1.1 — Define Purpose, Users, Content, Scope, Resources

Answer each explicitly:

1. **Purpose:** What will the taxonomy be used for?
   - Indexing support (manual or automated tagging of docs/articles)
   - Retrieval support (search, discovery, faceted browse)
   - Organization & navigation support (site maps, doc structure, menus)

2. **Users:** Who are all taxonomy users?
   - Taxonomist/maintainer (internal governance)
   - Indexers/taggers (doc authors, content creators)
   - End-user searchers (developers, customers)
   - Subject area: expertise level of each group

3. **Content:** What content will the taxonomy cover?
   - Content types (API docs, conceptual guides, tutorials, how-tos, troubleshooting, release notes)
   - Proficiency levels (beginner, intermediate, advanced, expert)
   - Volume and growth rate

4. **Scope:** What are the topic boundaries?
   - Domains included (e.g., UI, data, security, architecture)
   - Named entities policy (API types, modules, product names)
   - Explicit exclusions (internal implementation details, one-off helpers)

5. **Resources:** Constraints on tools, timing, personnel

#### Step 1.2 — Conduct Content Audit

Systematically survey representative content to extract candidate concepts:

- **Read titles and headings** of documents, sections, and subsections
- **Scan abstracts, summaries, and lead paragraphs**
- **Collect navigation labels, site maps, and TOC entries**
- **Extract existing metadata** (keywords, tags, categories already applied)
- **Analyze API surface** (namespaces, primary types, key interfaces)
- **Review support tickets and search logs** for user-facing terminology

Record each candidate concept in a spreadsheet with columns:
- Candidate term(s)
- Source document/file
- Content type
- Potential synonyms noted
- Frequency/importance signal

Use automated keyword extraction on the corpus where feasible (noun-phrase extraction, TF-IDF) to supplement manual review.

#### Step 1.3 — Gather Stakeholder Input

- Interview product owners for strategic priorities and top-level concepts
- Consult subject matter experts for correct terminology in specialized areas
- Analyze search logs for terms users actually enter
- Review support ticket language for how users describe features
- Note proprietary jargon, acronyms, and internal code names unique to the product

---

### Phase 2 — Taxonomy Structural Design

**Objective:** Decide the taxonomy's structure before creating terms.

#### Step 2.1 — Choose Taxonomy Type

Select based on purpose and content characteristics:

| Type | When to use |
|---|---|
| **Hierarchical taxonomy** | Content naturally classifies into categories; users will drill down |
| **Faceted taxonomy** | Content has multiple independent aspects (platform, audience, lifecycle phase) |
| **Thesaurus** | Large vocabulary with human indexing; need BT/NT/RT/UF relationships |
| **Controlled vocabulary** | Simple consistent tagging; small term sets |

For software products, a **faceted taxonomy with hierarchies within facets** is typically best. Common software product facets:
- **Domain/Topic** (the subject matter hierarchy)
- **Artifact kind** (conceptual, module, API, pattern, tool, feature)
- **Platform** (e.g., web, desktop, mobile)
- **Audience** (beginner, intermediate, advanced, architect)
- **Lifecycle phase** (design-time, runtime, deployment)
- **Content type / Doc intent** (concept, how-to, tutorial, reference, configuration, troubleshooting)
- **Stability** (stable, evolving, deprecated)

#### Step 2.2 — Define Relationship Types

At minimum, support these standard relationship types:

| Relationship | Notation | Rule | Example |
|---|---|---|---|
| **Equivalence** | USE / UF | Nonpreferred term → preferred term | "grid control" USE "List View" |
| **Generic-specific** | BT / NT (is_a) | All Xs are Ys; only some Ys are Xs | List View NT Grouped List View |
| **Whole-part** | BTP / NTP (part_of) | X is a constituent part of Y | Security System NTP Authorization |
| **Associative** | RT (related_to) | Meaningful but non-hierarchical | List View RT Detail View |
| **Instance** | BTI / NTI | Named entity of a class | Modules NTI ReportsV2Module |

For software products, add domain-specific relation types as needed:
- `requires` — concept X requires concept Y as a prerequisite
- `replaces` — concept X supersedes deprecated concept Y
- `implements` — API type X implements concept Y

#### Step 2.3 — Set Structural Policies

Document these decisions before building:

- **Polyhierarchies:** Allowed or not? (Recommended: allowed with discretion)
- **Maximum depth:** Target 3–5 levels for navigation taxonomies
- **Terms per level:** 5–12 for navigation; more for thesaurus-style
- **Node labels:** Allow non-indexable category headers at top levels?
- **Scope notes:** Required for ambiguous terms? Recommended: yes
- **Named entities vs. generic terms:** Separate authority files or integrated?

#### Step 2.4 — Design the ID Scheme

For software products, use a namespace-based stable identifier:
```
{product}.{domain}.{subdomain}.{concept-name}
```
Example: `xaf.security.authorization.permission-policy`

Rules:
- IDs must never change once published
- Use lowercase, dot-separated segments
- IDs are for machines; `name` is for humans

---

### Phase 3 — Creating Terms

**Objective:** Identify concepts, choose preferred terms, and format them consistently.

#### Step 3.1 — Evaluate Concept Inclusion

For each candidate from the content audit, apply these four gates:

1. **Within scope?** Is the concept within the defined subject area boundaries?
2. **Important enough?** Is it something users are likely to look up? Is it mentioned in search logs or support tickets?
3. **Sufficient content?** Are there at least 2–3 documents on this concept (or anticipated future content)?
4. **User demand?** Do users want and expect this concept to be findable?

Reject candidates that fail any gate. For borderline cases, consider creating a nonpreferred term pointing to a broader concept (upward posting) instead of a full concept.

#### Step 3.2 — Choose Preferred Terms

Apply these criteria in priority order:

1. **User language first.** Use the wording users most likely search for, given their expertise level
2. **Match content scope.** Align with the product's established terminology
3. **Enforce product vocabulary.** Use the product's official names for features, modules, APIs
4. **Follow industry standards.** Align with accepted technical terminology where applicable
5. **Maintain style consistency.** Keep the same level of formality across the taxonomy

#### Step 3.3 — Apply Term Format Rules

- **Capitalization:** Use initial caps for hierarchical category labels; lowercase for thesaurus-style terms. Never use title case for generic terms (e.g., "Business services" not "Business Services")
- **Length:** 1–4 words typically; complete proper nouns regardless of length
- **Grammar:** Nouns or noun phrases. No verbs. Verbal nouns (e.g., "filtering") acceptable
- **Plurals:** Countable nouns in plural ("reports", "views"); abstract concepts singular ("security", "authorization")
- **Disambiguation:** Use parenthetical qualifiers for homographs: "Model (Application Model)" vs. "Model (data model)". Choose either domain or category qualifiers, not both
- **Acronyms:** Use only if the acronym is better known than the spelled-out form AND is unambiguous within scope. Spell out as nonpreferred term
- **No inversions:** "Business objects" not "objects, business"

#### Step 3.4 — Create Nonpreferred Terms (Equivalences)

For each preferred term, add nonpreferred terms covering:

| Type | Example |
|---|---|
| Synonyms | "grid" UF "List View" |
| Near-synonyms | "permissions" UF "authorization rules" |
| Variant spellings | "colour" UF "color" |
| Acronyms / spelled-out | "ORM" UF "Object-Relational Mapping" |
| Technical / popular names | "CRUD operations" UF "data manipulation" |
| Phrase variations | "view, list" UF "List View" |
| API names as entry points | "XafApplication" UF "Application object" |

More nonpreferred terms are needed when:
- Users access content via a search box (can't browse)
- Automated indexing matches terms to document text
- Users are diverse (mixed expertise levels)

#### Step 3.5 — Write Scope Notes

Add scope notes (descriptions) for any term that is:
- Ambiguous without context
- Easily confused with a similar term
- Technical and requires definition for some audiences
- New to the product domain

Format: 1–3 sentences. State what the concept IS and how it differs from similar concepts. Do not repeat information already conveyed by the term name and its hierarchical position.

---

### Phase 4 — Creating Relationships

**Objective:** Build the hierarchical backbone and associative network.

#### Step 4.1 — Build Hierarchical Relationships

For each BT/NT pair, validate with the **all-and-some test:**

- **Generic-specific (is_a):** "All [NT] are [BT]" must be true. "Only some [BT] are [NT]" must also be true.
  - ✅ "All Detail Views are Views" → valid
  - ❌ "All Dashboard items are List Views" → invalid

- **Instance:** "[NT] is a specific instance of [BT]"
  - ✅ "ReportsV2Module is a specific instance of Modules" → valid

- **Whole-part (part_of):** "[NT] is a constituent part of [BT]"
  - ✅ "Authorization is a part of the Security System" → valid
  - ❌ "Action is a part of Controller" → questionable (actions can exist independently)

**Polyhierarchy rules:**
- A term may have multiple broader terms only if each BT relationship independently passes the all-and-some test
- Never make a term narrower to both a parent and a grandparent simultaneously
- Use polyhierarchies sparingly; they complicate navigation

#### Step 4.2 — Build Associative Relationships

Create RT (related_to) links between terms that are:
- **Conceptually related** but not hierarchically connected
- Terms that a user looking at one would **likely want to explore** the other
- Terms that **frequently co-occur** in the same documents

Do NOT create associative relationships:
- Between terms that already share a direct hierarchical relationship (BT/NT)
- Between terms that share a common broader term at the same level (siblings)
- Between terms with only a vague or trivial connection

For software products, focus associative relationships on:
- Feature ↔ Feature interactions (e.g., "List View" RT "Filtering")
- Concept ↔ Pattern (e.g., "Business Objects" RT "Domain-Driven Design")
- Tool ↔ Concept (e.g., "Model Editor" RT "Application Model")

#### Step 4.3 — Create Domain-Specific Relationships

For software product taxonomies, add typed relationships:

- **requires:** Concept X is a prerequisite for understanding/using concept Y
- **replaces:** Concept X supersedes concept Y (for migration/deprecation tracking)

Each relationship must be reciprocal and documented with its inverse.

---

### Phase 5 — Quality Validation

**Objective:** Verify structural integrity and coverage.

#### Step 5.1 — Structural Checks

Run these validation rules:

| Check | Rule |
|---|---|
| No orphans | Every term has at least one relationship (BT, NT, or RT) |
| No cycles | No term is its own ancestor in any hierarchy |
| All-and-some | Every BT/NT pair passes the all-and-some test |
| Unique IDs | Every concept has a globally unique stable identifier |
| No duplicate concepts | No two concepts represent the same idea |
| Consistent formatting | Term format rules applied uniformly |
| Scope notes present | Required for ambiguous or technical terms |
| Polyhierarchy validation | No term narrower to both parent and grandparent |
| Reciprocal relations | Every directional relationship has its inverse |

#### Step 5.2 — Coverage Checks

- **Content coverage:** Sample 20–30 documents. Can each be adequately indexed with existing terms? If >20% need new terms, expand the taxonomy
- **User query coverage:** Test 20–30 representative search queries against the taxonomy. Each should match a preferred or nonpreferred term
- **Hierarchy balance:** No single broader term should have >15 narrower terms without subcategories; no hierarchy should have only 1 narrower term (consider merging upward)
- **Facet completeness:** Each facet should have ≥3 values; single-value facets are not useful

#### Step 5.3 — Schema Validation

If a JSON schema exists, validate the taxonomy output against it. Fix all validation errors before delivery.

---

### Phase 6 — Documentation & Governance

**Objective:** Produce the governance artifacts that ensure the taxonomy remains maintainable.

#### Step 6.1 — Taxonomy Design Document

Create or update a governance document covering:

- Purpose, users, and scope
- Structural decisions (type, facets, relationship types, policies)
- Term format rules
- Sources consulted
- ID scheme
- Procedures for proposing, reviewing, and approving changes
- Maintenance schedule and responsibilities

#### Step 6.2 — Contribution Guide

Create or update a contribution guide for future editors covering:

- When to add a new concept (inclusion criteria)
- Required and optional fields per concept
- How to choose preferred terms and create nonpreferred terms
- How to validate relationships
- Review and approval workflow

#### Step 6.3 — Plan for Maintenance

A taxonomy is never finished. Plan for:

- Reviewing newly added content for new concepts
- Monitoring search logs for unmatched queries → new nonpreferred terms
- Tracking low-use terms for possible removal or merging
- Tracking high-use terms for possible splitting into narrower terms
- Periodic stakeholder review (quarterly recommended)

---

### Output Format

Produce the taxonomy in the format matching the project's schema. If using the XAF taxonomy schema:

```json
{
  "schema_version": "1.0",
  "taxonomy": {
    "metadata": {
      "product": "{product_name}",
      "purpose": "{stated purpose}",
      "owner": "{team or role}",
      "last_updated": "{ISO 8601 date}"
    },
    "concepts": [
      {
        "id": "{product}.{domain}.{subdomain}.{name}",
        "name": "Human-readable name",
        "artifact_kind": "conceptual|module|api|pattern|tool|feature",
        "domain": "{domain}",
        "subdomain": "{subdomain}",
        "description": "Scope note: 1–3 sentences",
        "terminology": {
          "synonyms": ["nonpreferred term 1", "nonpreferred term 2"],
          "keywords": ["related keyword not in taxonomy"]
        },
        "relations": {
          "is_a": ["broader.concept.id"],
          "part_of": ["parent.concept.id"],
          "related_to": ["associated.concept.id"],
          "requires": ["prerequisite.concept.id"],
          "replaces": ["deprecated.concept.id"]
        },
        "facets": {
          "platforms": ["platform1"],
          "lifecycle_phases": ["design_time", "runtime"],
          "audiences": ["intermediate", "advanced"],
          "stability": "stable"
        },
        "api_surface": {
          "primary_types": ["IMainInterface"],
          "related_types": ["HelperClass"]
        },
        "documentation": {
          "doc_intents": ["concept", "how_to"],
          "see_also": ["related doc references"]
        }
      }
    ]
  }
}
```

---

### Key Principles (from *The Accidental Taxonomist*)

1. **A taxonomy is a knowledge organization system** — not just a list. Structure and relationships are what make it useful.
2. **The preferred term reflects user language**, not internal implementation terminology.
3. **Every hierarchical relationship must pass the all-and-some test.** If "all Xs are Ys" is not always true, the relationship is invalid.
4. **Equivalence is not strict synonymy.** Two terms need only be "sufficiently similar with respect to the content being indexed" that maintaining them as distinct would cause confusion.
5. **Scope drives everything.** A taxonomy must have defined boundaries; without them, it grows uncontrollably.
6. **Content audit before term creation.** Concepts come from analyzing real content, not from abstract brainstorming alone.
7. **Consult users, not just experts.** The taxonomy must match how users think and search, not just how experts classify.
8. **A taxonomy is never done.** Plan for continuous maintenance from day one.
9. **Consistency over perfection.** Uniform style, depth, and term formatting across the entire taxonomy is more important than getting any single term perfectly right.
10. **Avoid precoordination unless necessary.** Prefer combining simple terms over creating compound terms. Use faceted search to compose queries from independent facets.
