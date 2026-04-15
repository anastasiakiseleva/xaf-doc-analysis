
# DevExpress XAF Taxonomy – Contribution Guide

This guide explains **how to contribute safely and consistently** to the DevExpress XAF taxonomy. It is intended for **documentation authors, engineers, and architects** who add or modify taxonomy concepts.

The taxonomy is a **governed system**. Changes affect navigation, search, analytics, and documentation structure. Follow this guide strictly.

---

## 1. Guiding Principles

Before making any change, internalize these rules:

1. **Stability over convenience**  
   Once published, taxonomy identifiers must remain stable.

2. **One concept = one meaning**  
   Do not overload a single concept with multiple responsibilities.

3. **Explicit over implicit**  
   Use relations and facets instead of relying on naming or hierarchy guesswork.

4. **Favor clarity for users, not implementation**  
   Concepts model *how users think*, not how code happens to be structured.

---

## 2. When to Add a New Concept

✅ Add a new concept when:
- A feature or capability has **user‑visible documentation impact**
- Multiple docs will refer to the same idea
- The idea has a **stable mental identity** in XAF

❌ Do NOT add a concept for:
- Internal helper classes
- One‑off implementation details
- Temporary experiments

If unsure, propose the concept first (see workflow below).

---

## 3. Creating a New Concept Entry

### 3.1 Required Fields

Every concept **must** define:

```yaml
id
name
artifact_kind
domain
```

A concept missing any of these is invalid.

---

### 3.2 ID Naming Rules (Critical)

```text
xaf.<domain>.<subdomain>.<concept-name>
```

Examples:
- `xaf.ui.views.list-view`
- `xaf.security.authentication.jwt`
- `xaf.modules.reports.parameters`

**Rules:**
- Lowercase only
- Hyphen-separated words
- No version numbers
- Never reuse or rename an existing ID

🚨 Renaming an ID is a **breaking change** and requires approval.

---

### 3.3 Choosing `artifact_kind`

Ask: *What kind of thing is this?*

| Kind | Use When |
|----|--------|
| conceptual | Core ideas users reason about |
| module | Installable XAF modules |
| api | Specific public types or interfaces |
| pattern | Architectural or design patterns |
| tool | Standalone tools or designers |
| feature | UX or runtime capabilities |

Choose **exactly one**.

---

### 3.4 Choosing `domain` and `subdomain`

- `domain` determines documentation ownership and navigation
- `subdomain` groups related concepts

✅ Example:
```yaml
domain: ui
subdomain: views
```

❌ Avoid:
- Using modules as domains
- Over‑specific subdomains

---

## 4. Writing Good Descriptions

A good description:
- Explains *what it is*
- Avoids *how to implement*
- Fits in 2–4 lines

✅ Good:
> Grid-based view for displaying and managing collections of business objects.

❌ Bad:
> A ListView is created by calling CreateListView and assigning a CollectionSource.

Implementation belongs in documentation, not taxonomy.

---

## 5. Using Facets Correctly

Facets describe applicability, **not identity**.

### Platforms
Specify **where the concept applies**:
```yaml
platforms: [winforms, blazor]
```

Do not infer platforms implicitly.

---

### Lifecycle Phases
Use lifecycle to support learning paths:
- design_time
- runtime
- deployment

Many concepts belong to multiple phases — that is expected.

---

### Audiences
Audience helps structure docs priority:
- beginner
- intermediate
- advanced
- architect

Do not mark everything as beginner.

---

### Stability
Use conservatively:
- `stable`: long‑term API / behavior
- `evolving`: improving or expanding
- `deprecated`: discouraged or legacy

---

## 6. Defining Relationships (Very Important)

### is_a
Use only for **true specialization**.

✅ Example:
```yaml
is_a:
  - xaf.ui.views.view
```

---

### part_of
Use for structural composition.

✅ Example:
```yaml
part_of:
  - xaf.ui.framework
```

---

### related_to
Use for lateral semantic links ("See also").

Avoid overusing — 3–5 links are usually enough.

---

### replaces
Use only when explicitly deprecating an older concept.

This is required for clean migration paths.

---

## 7. Terminology & Search

### Synonyms
Add **user‑facing alternative names**, not code identifiers.

✅ Example:
```yaml
synonyms:
  - Grid View
  - Table View
```

---

### Keywords
Add **code-level search terms**:
- API names
- Class names
- Common symbols

These power search relevance.

---

## 8. API Surface Mapping

If users can point to code, map the bridge.

### primary_types
Main API types **representing the concept**.

### related_types
Supporting or adjacent API elements.

If a concept has no public API, omit this section.

---

## 9. Documentation Intent Responsibilities

Use `doc_intents` to declare **what documentation must exist**.

Examples:
```yaml
doc_intents:
  - concept
  - how_to
  - reference
```

This enables coverage tracking and doc backlogs.

---

## 10. Modifying Existing Concepts

### Allowed changes (safe)
✅ Adding synonyms or keywords  
✅ Adding related_to links  
✅ Expanding descriptions  
✅ Adding missing facets

### Restricted changes (approval required)
🚨 Changing `id`  
🚨 Changing `artifact_kind`  
🚨 Changing `domain`

These require explicit review.

---

## 11. Review & Approval Workflow

1. Open a PR with clear intent
2. Reference relevant concepts by ID
3. Explain *why* the change is necessary
4. Taxonomy owner approves or requests changes

No direct commits to main.

---

## 12. Common Mistakes to Avoid

- Using tags instead of relations
- Duplicating an existing concept under a new name
- Encoding tutorials in descriptions
- Overusing "related_to"
- Treating modules as domains

---

## Final Reminder

The taxonomy is a **shared contract**, not a scratchpad.

When in doubt:
> Add less, describe better, and ask early.

