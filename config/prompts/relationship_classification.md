You are classifying the directional relationship FROM Section A TO Section B in XAF (eXpressApp Framework) documentation.

Evaluate all relationship types below before choosing one.

## Section types
- **API Reference**: auto-generated class/method/property reference page
- **How-to Task**: step-by-step guide for a single focused scenario (path contains "how-to"); assumes the reader already understands the concept
- **Tutorial**: end-to-end walkthrough covering multiple related scenarios to achieve a larger goal; reader learns by doing
- **Conceptual**: explains what something is, why it exists, and how it fits — no hands-on steps

## Relationship definitions (from A → B)
Choose exactly one:

**requires**
- Use when: A is materially incomplete or likely to be misapplied without first reading B; B provides prerequisite concepts A builds on.
- Do NOT use when: A only mentions B's topic or links to B as "more info".
- Taxonomy signal: if `## Taxonomy Context` reports that A's concept *requires* B's concept, or A's concept *is part of* B's concept (B is the parent structure), treat this as strong evidence for `requires`.

**explains**
- Use when: A provides the conceptual overview/rationale and B is the concrete how-to or API detail that A describes.
- Taxonomy signal: if `## Taxonomy Context` reports that A's concept *has kind* or *has part* B's concept (A is the parent that subsumes B), treat this as evidence for `explains`.

**uses**
- Use when: A actively invokes, configures, calls, or depends on an API/feature documented in B (often A=how-to/tutorial, B=API reference).
- Structural shortcut: if A is Conceptual, How-to, or Tutorial AND B is API Reference AND they share concept vocabulary → default to `uses` unless A is clearly a parent-level overview of B (→ `explains`) or B defines a concept A cannot work without (→ `requires`).
- Tie-breaker vs explains: if A contains actionable steps that call/configure B, prefer `uses`.

**extends**
- Use when: A customizes or adds behavior to B via subclassing, overriding, implementing interfaces, or plugging in custom components (not merely configuring).
- Taxonomy signal: if `## Taxonomy Context` reports that A's concept *is a kind of* B's concept, treat this as strong evidence for `extends`.

**applies_to**
- Use when: A is explicitly scoped to a platform, version, deployment target, audience level, or lifecycle phase, and B defines that scope (e.g., Blazor, WinForms, EF Core, XPO, designer-only, evaluator). Scope must be explicit in A or indicated by a taxonomy signal.
- Taxonomy signal: a **Platform mismatch** or **Audience mismatch** line in `## Taxonomy Context` is strong evidence for `applies_to` even when the text is implicit about the scope.

**contrasts_with**
- Use when: A and B are presented as alternative approaches to the same goal/problem (not just different topics).
- Also use when: A and B are sibling API Reference pages with the same member name (method/property) on different types — each is a parallel implementation of the same contract (e.g., `ModuleA.GetModuleUpdaters` and `ModuleB.GetModuleUpdaters`). Set `bidirectional: true`.

**related_to**
- Use only as a last resort when none of the above fit AND you cannot identify any directional signal between A and B.
- Do NOT use when A is Conceptual/How-to/Tutorial and B is API Reference sharing concepts → use `uses`.
- Do NOT use when A and B are sibling API Reference pages with the same member name on different types → use `contrasts_with`.
- Do NOT use when A is a conceptual overview and B is the how-to/tutorial it describes → use `explains`.
- Do NOT use merely because you are uncertain about relationship strength — if you can identify direction, assign the directional type at low confidence (0.5–0.6) rather than defaulting here.

## Decision order (tie-breaker only)
Apply this order **only when two or more relationships seem equally applicable**. Do not treat it as a ranking to always follow — choose the relationship that best fits the text regardless of position in this list:
contrasts_with → applies_to → extends → uses → requires → explains → related_to

## Confidence calibration
- **0.9–1.0**: unambiguous from the text alone
- **0.7–0.9**: strongly implied; minor inference
- **0.5–0.7**: plausible but uncertain; structural shortcuts (section type + shared concepts) can justify this band
- **< 0.5**: choose the most likely directional type and assign low confidence rather than defaulting to `related_to`. Only use `related_to` if you genuinely cannot identify any direction at all.

## Bidirectionality
Default `bidirectional: false`.
Set `bidirectional: true` only for genuinely symmetric relationships (typically `contrasts_with`; occasionally `related_to`).

## Using Taxonomy Context
When a `## Taxonomy Context` block appears in the pair data, use it to bias your classification. These signals come from the authoritative XAF taxonomy and should be weighted above text inference when they are present.

**Known relations** — declared associations between the concepts covered by each section:
| Taxonomy signal | Preferred relationship |
|---|---|
| A's concept *requires* B's concept | `requires` |
| A's concept *is a kind of* B's concept | `extends` |
| A's concept *is part of* B's concept | `requires` (B is the parent structure A depends on) |
| A's concept *has kind* or *has part* B's concept | `explains` (A is the broader concept describing B) |
| A's concept *replaces* B's concept | `contrasts_with` (A is the modern replacement) |
| A's concept *is related to* B's concept | Look hard for a directional type first (`uses`, `explains`, `requires`); fall back to `related_to` only if the section text provides no directional signal at all |

**Platform mismatch** (A's concepts are platform-exclusive vs. B's) → strong signal for `applies_to`. Lower confidence only if the text does not reference scope differences.

**Audience mismatch** (e.g., A=evaluator, B=developer) → also a valid signal for `applies_to`.

**Shared domain / subdomain** alone does not change the classification; it merely confirms the pair is within scope of the same XAF area.

When taxonomy signals conflict with each other or with the text, **prefer the text** but reduce confidence to the 0.5–0.7 band.

## Output format
Return ONLY valid JSON with exactly these keys (no extra keys, no prose):
```json
{
  "relationship": "<one of: requires|explains|uses|extends|applies_to|contrasts_with|related_to>",
  "confidence": <float between 0 and 1, e.g. 0.85>,
  "bidirectional": <true|false>
}
```