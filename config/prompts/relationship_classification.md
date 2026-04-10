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

**explains**
- Use when: A provides the conceptual overview/rationale and B is the concrete how-to or API detail that A describes.

**uses**
- Use when: A actively invokes, configures, calls, or depends on an API/feature documented in B (often A=how-to/tutorial, B=API reference).
- Tie-breaker vs explains: if A contains actionable steps that call/configure B, prefer uses.

**extends**
- Use when: A customizes or adds behavior to B via subclassing, overriding, implementing interfaces, or plugging in custom components (not merely configuring).

**applies_to**
- Use when: A is explicitly scoped to a platform/version/deployment target and B defines that scope (e.g., Blazor, WinForms, EF Core, XPO). Scope must be explicit in A.

**contrasts_with**
- Use when: A and B are presented as alternative approaches to the same goal/problem (not just different topics).

**related_to**
- Use only if none of the above fit cleanly AND the sections share significant concepts/vocabulary.

## Decision order (tie-breaker only)
Apply this order **only when two or more relationships seem equally applicable**. Do not treat it as a ranking to always follow — choose the relationship that best fits the text regardless of position in this list:
contrasts_with → applies_to → extends → uses → requires → explains → related_to

## Confidence calibration
- **0.9–1.0**: unambiguous from the text alone
- **0.7–0.9**: strongly implied; minor inference
- **0.5–0.7**: plausible but uncertain
- **< 0.5**: avoid; choose related_to at low confidence

## Bidirectionality
Default `bidirectional: false`.
Set `bidirectional: true` only for genuinely symmetric relationships (typically `contrasts_with`; occasionally `related_to`).

## Output format
Return ONLY valid JSON with exactly these keys (no extra keys, no prose):
```json
{
  "relationship": "<one of: requires|explains|uses|extends|applies_to|contrasts_with|related_to>",
  "confidence": <float between 0 and 1, e.g. 0.85>,
  "bidirectional": <true|false>
}
```