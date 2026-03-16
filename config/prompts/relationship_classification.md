You are classifying relationships between two XAF documentation sections.

Return JSON with fields: relationship (one of: explains, requires, uses, extends, applies_to, contrasts_with, related_to), confidence (0–1), rationale (bullet points), evidence (direct quotes), and which concepts/APIs overlap.

Prefer 'requires' when one topic is prerequisite knowledge or feature dependency. Prefer 'uses' when APIs or features are invoked. Prefer 'explains' when one is conceptual overview and the other is a how-to. Use 'contrasts_with' for side-by-side alternatives (e.g., Blazor vs WinForms). Use 'applies_to' when platform scoping is explicit. Fall back to 'related_to' if none fit.