# XAF Concept Analysis Runbook

Use this runbook to perform a full analysis of one or more XAF taxonomy concepts.  
Replace `{CONCEPT NAME}` with the exact taxonomy `name` value (e.g. `"Reports V2"`).  
Replace `{SLUG}` with a short filesystem-safe label (e.g. `reports_v2`).  
Replace `{KEYWORD LIST}` with a comma-separated list of primary API type names from the concept's `api_surface`.  
Replace `{OUTPUT DIR}` with the target directory for all results (e.g. `outputs/my_analysis/`).

---

## Pre-flight checklist

Before running, confirm the following files exist in `outputs/`:

| File | Required by |
|---|---|
| `doc_concepts.parquet` | Phase 1 (drilldown, isolated links) |
| `semantic_pairs.parquet` | Phase 1 (drilldown, isolated links) |
| `classified_pairs.parquet` | Phase 2 (query_graph) |
| `sections_embeddings_conceptual.parquet` | Phase 1 (isolated links) |
| `sections_embeddings_api.parquet` | Phase 1 (isolated links) |
| `api_implements_concept.parquet` | Phase 1 (drilldown API mappings) |
| `knowledge_graph.json` | Phase 4 (visualization) |

If any are missing, run the appropriate pipeline phase first (see `scripts/run_kg_pipeline_with_validation.py`).

Set the UTF-8 environment variable to avoid encoding errors on Windows:

```powershell
$env:PYTHONUTF8=1
```

---

## Phase 1 — Concept-Level Analysis

Run all steps in this phase independently (they share no dependencies).

### Step 1 — Concept drilldown

Produces: section count, API vs conceptual split, connectivity stats (avg/median/isolated), top/least connected sections, API mappings.

```
python tools/concept_drilldown.py --concept "{CONCEPT NAME}" --top 20 \
  | tee {OUTPUT DIR}/drilldown_{SLUG}.txt
```

The tool also saves `outputs/concept_{SLUG}_sections.csv` — copy it to `{OUTPUT DIR}` afterwards.

**What to look for:**
- `isolated (0)` — any value > 0 means sections with no semantic connections; feed them into Step 2.
- `avg connections/section` — below ~10 suggests the concept is underconnected relative to the corpus average.
- `unique APIs mapped` — compare to the number of `primary_types` in the taxonomy definition; a large gap means APIs are not resolving to sections.
- Least-connected sections — candidates for crosslink work.

### Step 2 — Isolated section link suggestions

Produces: link candidates (similar sections from other documents) for each isolated section. Outputs a CSV and a Markdown report.

```
python tools/suggest_isolated_links.py --concept "{CONCEPT NAME}" \
  --top-sources 50 --topk 8 \
  | tee {OUTPUT DIR}/isolated_links_{SLUG}.txt
```

If the concept has 0 isolated sections, this will exit early — that is a healthy result, not an error.

---

## Phase 2 — Graph & Relationship Analysis

### Step 3 — Query graph by concept

Produces: top 20 related sections ranked by classified relationship confidence, with relationship type labels (`uses`, `extends`, `explains`, `requires`, `contrasts_with`, `related_to`, `applies_to`).

```
python query_graph.py --mode query --concept "{CONCEPT NAME}" \
  | tee {OUTPUT DIR}/query_{SLUG}.txt
```

**What to look for:**
- Dominant relationship type — a healthy conceptual concept should have a mix. Predominantly `related_to` may signal weak classification.
- Bidirectional edges — note them; they may indicate circular dependency or dual ownership.
- High-confidence `contrasts_with` edges — signal migration/deprecation comparisons in the docs.

### Step 4 — Prerequisites / learning paths

Produces: documents that should be understood before this concept, with confidence scores.

```
python query_graph.py --mode prereqs --concept "{CONCEPT NAME}" \
  | tee {OUTPUT DIR}/prereqs_{SLUG}.txt
```

**What to look for:**
- Compare the prerequisite list to the concept's `relations` in the taxonomy. If the graph identifies a prerequisite that is not reflected in `requires` or `part_of` relations, the taxonomy is missing a dependency link.
- No prerequisites found is normal for foundational concepts.

### Step 5 — Keyword search for untagged content

Produces: `{OUTPUT DIR}/keyword_hits_{SLUG}.csv` — sections mentioning key API names that may not be tagged to the concept. These are tagging gap candidates.

Construct `{KEYWORD LIST}` from the concept's `api_surface.primary_types` and any well-known synonyms.

```
python tools/keyword_section_query.py \
  --keywords "{KEYWORD LIST}" \
  --out {OUTPUT DIR}/keyword_hits_{SLUG}.csv \
  --max-total 200 \
  | tee {OUTPUT DIR}/keyword_hits_{SLUG}_log.txt
```

**What to look for:**
- Documents in the hit list that are NOT already tagged to this concept — these are tagging gaps.
- Documents from unrelated domains (e.g. performance, security) that reference the concept's APIs — may warrant cross-tagging or a `related_to` taxonomy link.

---

## Phase 3 — Coverage & Gap Analysis

### Step 6 — Coverage matrix

Produces: `outputs/coverage_reports/` with `coverage_matrix.csv`, `high_priority_gaps.csv`, and `summary_report.txt`.

```
python tools/coverage_matrix_xaf.py
```

Then extract the rows for your concepts:

```powershell
Get-Content outputs/coverage_reports/coverage_matrix.csv | Select-String -Pattern "{CONCEPT NAME}" | Format-Table -Wrap
```

Copy relevant files to your output directory:

```powershell
Copy-Item outputs/coverage_reports/coverage_matrix.csv {OUTPUT DIR}/coverage_matrix_full.csv
Copy-Item outputs/coverage_reports/high_priority_gaps.csv {OUTPUT DIR}/high_priority_gaps.csv
Copy-Item outputs/coverage_reports/summary_report.txt {OUTPUT DIR}/coverage_summary.txt
```

**What to look for:**
- `well_covered` / `partial` / `missing` status.
- `Doc Depth Score` — reflects documentation breadth relative to ticket volume.
- Concepts with high ticket counts but low depth scores are under-documented relative to user demand.

### Step 7 — Documentation gaps backlog

Regenerates the full gap report and filters for your concepts:

```
python tools/generate_documentation_gaps_backlog.py
```

```powershell
Get-Content docs/DOCUMENTATION_GAPS_BACKLOG.md | Select-String -Pattern "{CONCEPT NAME}" -Context 1,3 \
  | Out-File {OUTPUT DIR}/gaps_backlog_filter_{SLUG}.txt -Encoding utf8
```

---

## Phase 4 — Visualization

### Step 8 — Interactive knowledge graph

Produces a self-contained HTML file (~9 MB). Open in a browser; use the search box to filter to concept nodes, then explore neighbors.

```
python tools/visualize_graph.py --output {OUTPUT DIR}/graph_{SLUG}.html
```

**What to look for:**
- Isolation of the target concept node — few edges to neighboring concepts suggests the taxonomy relations are incomplete.
- Unexpected neighbors — concepts showing high co-occurrence that have no declared taxonomy relation are candidates for `related_to` additions.

---

## Phase 5 — Taxonomy Quality Inspection

### Step 9 — Inspect taxonomy definition

Prints the full definition of the concept from `config/xaf-taxonomy.json`:

```powershell
$env:PYTHONUTF8=1; & .venv\Scripts\python.exe -c "
import json
with open('config/xaf-taxonomy.json') as f:
    t = json.load(f)
targets = ['{CONCEPT NAME}']
for c in t['taxonomy']['concepts']:
    if c['name'] in targets:
        print('=== ' + c['name'] + ' [' + c['domain'] + '/' + c['subdomain'] + '] ===')
        print('  description:    ' + c.get('description',''))
        print('  artifact_kind:  ' + c.get('artifact_kind',''))
        print('  stability:      ' + c.get('facets',{}).get('stability',''))
        print('  platforms:      ' + str(c.get('facets',{}).get('platforms',[])))
        print('  audiences:      ' + str(c.get('facets',{}).get('audiences',[])))
        print('  doc_intents:    ' + str(c.get('documentation',{}).get('doc_intents',[])))
        print('  synonyms:       ' + str(c.get('terminology',{}).get('synonyms',[])))
        print('  keywords:       ' + str(c.get('terminology',{}).get('keywords',[])))
        print('  api_primary:    ' + str(c.get('api_surface',{}).get('primary_types',[])))
        print('  api_related:    ' + str(c.get('api_surface',{}).get('related_types',[])))
        print('  relations:      ' + str(c.get('relations',{})))
        print('  tags:           ' + str(c.get('tags',[])))
        print()
" | tee {OUTPUT DIR}/taxonomy_inspect_{SLUG}.txt
```

**Taxonomy quality checklist:**

| Check | What to verify |
|---|---|
| Synonyms coverage | Do synonyms match terms that appear in the raw docs? Run keyword search on missing synonym candidates. |
| Keywords | Empty `keywords` is common but worth filling — they improve tagging recall for non-API sections. |
| API surface completeness | Are the `primary_types` the actual entry-point classes a developer would search for? |
| API overlap with other concepts | If an API type appears in multiple concepts, check which concept owns the doc sections via `doc_concepts.parquet`. |
| Relations accuracy | Do `part_of` / `requires` / `replaces` match what the learning path analysis found in Step 4? |
| `doc_intents` completeness | Should match the actual content types present: `concept`, `how_to`, `configuration`, `reference`, `tutorial`. |
| `stability` accuracy | `deprecated` concepts should have a `replaces`/`superseded_by` target. `evolving` concepts should have `related_to` their stable predecessor. |

---

## Phase 6 — Dual-Tagging Investigation (for related concept clusters)

When analyzing a cluster of related concepts (e.g. a parent and its children, or a deprecated concept and its replacement), check for sections dual-tagged to both:

```powershell
$env:PYTHONUTF8=1; & .venv\Scripts\python.exe -c "
import pandas as pd
dc = pd.read_parquet('outputs/doc_concepts.parquet')
# Find sections tagged to both concept A and concept B
both = dc[dc['concepts'].apply(lambda cs: '{CONCEPT A}' in list(cs) and '{CONCEPT B}' in list(cs))]
print(both[['doc_id','concepts','kept']].to_string())
"
```

**What to look for:**
- Dual-tagged sections are expected when a concept's APIs are listed in both taxonomy entries (API overlap). The fix is to remove the overlapping API from the deprecated/parent concept's `api_surface`.
- A large number of dual-tagged sections with no API overlap suggests the section text is genuinely about both concepts — consider adding an explicit `related_to` taxonomy relation instead of relying on implicit co-tagging.

---

## Synthesis — What to include in the analysis summary

After running all phases, write a summary covering:

1. **Concept overview table** — `artifact_kind`, `stability`, `platforms`, `audiences`, `doc_intents`, key relation.
2. **Section & connectivity table** — tagged sections, API/conceptual split, avg/median connections, isolated count, cross-corpus pairs, unique APIs mapped.
3. **Most/least connected sections** — top 5 and bottom 5 from drilldown output.
4. **Graph relationship patterns** — dominant types, bidirectional edges, notable `contrasts_with` edges.
5. **Prerequisites** — compare graph output to taxonomy relations; flag mismatches.
6. **Coverage matrix results** — ticket count, depth score, status.
7. **Keyword search findings** — untagged sections, cross-domain hits.
8. **Taxonomy issues** — ranked: Critical / Important / Nice to Have.
9. **File index** — list every output file with a one-line description.

---

## Output directory structure

```
{OUTPUT DIR}/
  ANALYSIS_SUMMARY.md                  # Hand-written synthesis (see above)
  drilldown_{SLUG}.txt                 # Phase 1 Step 1
  concept_{SLUG}_sections.csv          # Phase 1 Step 1 (copied from outputs/)
  isolated_links_{SLUG}.txt            # Phase 1 Step 2
  query_{SLUG}.txt                     # Phase 2 Step 3
  prereqs_{SLUG}.txt                   # Phase 2 Step 4
  keyword_hits_{SLUG}.csv              # Phase 2 Step 5
  keyword_hits_{SLUG}_log.txt          # Phase 2 Step 5
  coverage_matrix_full.csv             # Phase 3 Step 6
  high_priority_gaps.csv               # Phase 3 Step 6
  coverage_summary.txt                 # Phase 3 Step 6
  gaps_backlog_filter_{SLUG}.txt       # Phase 3 Step 7
  graph_{SLUG}.html                    # Phase 4 Step 8
  taxonomy_inspect_{SLUG}.txt          # Phase 5 Step 9
```
