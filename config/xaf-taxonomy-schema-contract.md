
# DevExpress XAF Taxonomy Schema Contract

## Purpose

This document defines the **official schema contract** for the DevExpress XAF Documentation Taxonomy. It explains **every field**, its **semantic meaning**, **intended usage**, and **governance rules**. The schema is designed to support scalable documentation, semantic search, knowledge graphs, and long-term maintainability.

---

## 1. Top-Level Document Structure

```yaml
schema_version: 1.0
taxonomy:
  metadata: …
  concepts: …
```

### schema_version
**Type:** string | number  
**Required:** Yes  

Defines the version of the taxonomy schema contract (not the XAF product version).

**Purpose:**
- Enables backward-compatible evolution of the taxonomy
- Allows tooling and CI validation
- Supports migration strategies

---

## 2. taxonomy.metadata

### metadata.product
**Type:** string  
**Required:** Yes

Canonical product name the taxonomy applies to (e.g., "DevExpress XAF").

---

### metadata.purpose
**Type:** string  
**Required:** Yes

Human-readable explanation of why this taxonomy exists (e.g., Documentation taxonomy, Knowledge graph).

---

### metadata.owner
**Type:** string  
**Required:** No

Team or role responsible for taxonomy maintenance and governance.

---

### metadata.last_updated
**Type:** ISO 8601 date string  
**Required:** No

Used for auditing, freshness checks, and CI warnings.

---

## 3. taxonomy.concepts[]

Each entry represents exactly **one canonical concept** in the XAF universe.

```yaml
- id: xaf.ui.list-view
  name: List View
  artifact_kind: conceptual
  domain: ui
```

---

## 4. Concept Identity & Naming

### id
**Type:** string  
**Required:** Yes

Globally unique, stable identifier for the concept.

**Rules:**
- Must never change once published
- Namespace-based (xaf.<domain>.<subdomain>.<name>)
- Used for references, URLs, analytics

---

### name
**Type:** string  
**Required:** Yes

Canonical human-readable name of the concept.

---

### short_name
**Type:** string  
**Required:** No

Abbreviated or code-style name (e.g., ListView, XPO).

---

### description
**Type:** string  
**Required:** No

Concise definition of what the concept *is*, not how to use it.

---

## 5. Core Classification

### artifact_kind
**Type:** enum  
**Required:** Yes

Allowed values:
- conceptual
- module
- api
- pattern
- tool
- feature

Defines what kind of artifact the concept represents.

---

### domain
**Type:** enum  
**Required:** Yes

Allowed values include:
- architecture
- ui
- data
- security
- modules
- ops
- quality
- tooling
- migration
- localization

Defines the primary documentation domain.

---

### subdomain
**Type:** string  
**Required:** No

Logical grouping inside a domain (e.g., views, controllers, orm).

---

## 6. Ownership & Governance

### ownership.module
**Type:** string  
**Required:** No

Allowed values:
- reports
- charts
- dashboards
- pivot-grid
- id: scheduler
- state-machine
- notifications
- office
- clone-object
- file-attachments
- tree-list-editors
- view-variants
- conditional-appearance
- audit-trail

XAF module primarily responsible for this concept.

---

### ownership.team
**Type:** string  
**Required:** No

Internal team responsible for accuracy and evolution.

---

## 7. Facets (Orthogonal Classification)

Facets describe *where* and *for whom* the concept applies.

### facets.platforms
**Type:** enum[]

Allowed values:
- winforms
- blazor

---

### facets.lifecycle_phases
**Type:** enum[]

Allowed values:
- design_time
- runtime
- deployment

---

### facets.complexity
**Type:** enum[]

Allowed values:
- beginner
- intermediate
- advanced

### facets.audience
**Type:** enum[]

Allowed values:
- developer
- evaluator

---

### facets.stability
**Type:** enum

Allowed values:
- stable
- evolving
- deprecated

---

## 8. Semantic Relationships

### relations.is_a
Defines specialization or inheritance relationships.

---

### relations.part_of
Defines structural containment or composition.

---

### relations.related_to
Defines lateral conceptual relationships.

**Symmetry rule:** Every `related_to` entry must be reciprocated — if A lists B, B must list A. This is enforced by CI (`test_related_to_symmetric`).

Use for: peer associations, works-with, see-also, alternative-to. Do **not** use for learning prerequisites or structural dependencies — use `requires` instead.

---

### relations.replaces
Defines replacement relationships for deprecated concepts.

---

### relations.requires
Defines prerequisite or dependency relationships.
The referenced concept must be understood before this one.

**Asymmetric by design** — do not add a reciprocal entry on the target concept.

---

### has_part *(computed, read-only)*

**Source:** Derived at load time from all concepts that declare `part_of` this concept.  
**Never stored in JSON** — the child's `part_of` declaration is the single source of truth.

SKOS equivalent: `skos:narrower` (whole-part axis).  
Z39.19 §7.1: satisfies the reciprocal-entry requirement without duplicating data in the source file.

**Governance rule:** Do not add `has_part` entries manually to the JSON. They are always computed. To connect a child to a parent, set `part_of` on the child.

---

### has_kind *(computed, read-only)*

**Source:** Derived at load time from all concepts that declare `is_a` this concept.  
**Never stored in JSON** — the child's `is_a` declaration is the single source of truth.

SKOS equivalent: `skos:narrower` (generic/specialisation axis).  
Z39.19 §7.1: satisfies the reciprocal-entry requirement without duplicating data in the source file.

**Governance rule:** Do not add `has_kind` entries manually to the JSON. They are always computed. To connect a specialisation to its parent, set `is_a` on the child.

---

## 9. Terminology

### terminology.synonyms
Alternative names the concept is commonly known by.

---

### terminology.keywords
Search and code-level terms linked to the concept.

---

## 10. API Surface Mapping

### api_surface.primary_types
Main API types representing this concept.

---

### api_surface.related_types
Supporting or adjacent API types.

---

## 11. Documentation Intent Mapping

### documentation.doc_intents
Defines what kinds of documentation should exist:
- concept
- how_to
- tutorial
- reference
- configuration
- troubleshooting
- example

---

## 12. Tags

### tags
Free-form, non-structural labels used only for analytics or temporary grouping.

---

## Final Notes

This schema contract enables:
- Consistent documentation structure
- Semantic search and navigation
- Scalable knowledge management
- Long-term governance and maintainability

