# AI Agent Action Plan: Documentation Gaps & Improvements

## 📁 Essential Project Files Overview

### Core Data Files (outputs/)
- `topics_inventory.parquet` - All parsed documents with sections and text
- `doc_concepts.parquet` - Sections tagged with concepts, platforms, APIs
- `semantic_pairs.parquet` - 93,905 semantic relationships between sections
- `sections_embeddings_conceptual.parquet` - Embeddings for tutorial/guide content
- `sections_embeddings_api.parquet` - Embeddings for API reference content
- `explicit_graph.parquet` - Explicit document links from Phase 2

### Configuration
- `config/concepts.yml` - 40 domain concepts with synonyms and descriptions

### Analysis Tools
- `query_graph.py` - Query knowledge graph, find gaps, analyze connectivity
- `extractor_sanity_check.py` - Validate concept tagging results

---

## 🎯 Action 1: Fill Cross-Corpus Gaps (Critical)

**Problem**: 6 concepts have ZERO connections between conceptual docs and API docs

### Files Needed
```
outputs/semantic_pairs.parquet
outputs/doc_concepts.parquet
outputs/topics_inventory.parquet
config/concepts.yml
```

### Initial Analysis Query
```bash
python query_graph.py --mode gaps
```

### AI Agent Prompt Template

```
CONTEXT:
I have a documentation corpus for DevExpress XAF (eXpressApp Framework) with 11,082 sections 
tagged with 40 concepts. A semantic knowledge graph found that these 6 concepts have NO links 
between conceptual documentation and API reference documentation:

1. Legacy .NET Framework (226 sections)
2. Multi-Tenancy (24 sections)
3. Deployment (125 sections)
4. Performance Optimization (21 sections)
5. Migration (66 sections)
6. Logging (65 sections)

TASK:
For the concept "[CONCEPT_NAME]", analyze sections and suggest:

1. Which conceptual sections could reference which API sections
2. What bridging content is missing
3. Specific documentation improvements to connect conceptual ↔ API content

PROJECT FILES TO REFERENCE:
- outputs/semantic_pairs.parquet: Current semantic connections
- outputs/doc_concepts.parquet: All sections with concept tags
- outputs/topics_inventory.parquet: Full document text and structure

ANALYSIS STEPS:
1. Load sections tagged with "[CONCEPT_NAME]"
2. Separate conceptual sections from API sections
3. Identify semantic gaps (why aren't they connected?)
4. Suggest specific document pairs that should reference each other
5. Propose new bridging content (tutorials, how-to guides)

OUTPUT FORMAT:
- Gap Analysis Report
- Top 10 conceptual sections that need API references
- Top 10 API sections that need tutorial examples
- 3-5 new documentation topics to bridge the gap
```

### Python Starter Code
```python
import pandas as pd

# Load data
pairs = pd.read_parquet('outputs/semantic_pairs.parquet')
concepts = pd.read_parquet('outputs/doc_concepts.parquet')
inventory = pd.read_parquet('outputs/topics_inventory.parquet')

# Pick a concept with no cross-links
target_concept = "Deployment"

# Find all sections with this concept
kept = concepts[concepts["kept"] == True]
concept_sections = kept[kept["concepts"].apply(lambda cs: target_concept in (cs or []))]

# Separate by type
conceptual = concept_sections[concept_sections["is_api"] == False]
api_docs = concept_sections[concept_sections["is_api"] == True]

print(f"Conceptual sections: {len(conceptual)}")
print(f"API sections: {len(api_docs)}")

# Check for any cross-links (should be 0)
cross_pairs = pairs[pairs["neighbor_type"].isin(["ca", "ac"])]
cross_with_concept = cross_pairs[
    cross_pairs["overlap_concepts"].apply(lambda cs: target_concept in (cs or []))
]
print(f"Cross-corpus links: {len(cross_with_concept)}")

# Show sample sections
print("\nSample conceptual sections:")
for doc_id in conceptual["doc_id"].head(5):
    print(f"  - {doc_id}")

print("\nSample API sections:")
for doc_id in api_docs["doc_id"].head(5):
    print(f"  - {doc_id}")
```

---

## 🎯 Action 2: Strengthen Under-Connected Concepts

**Problem**: Concepts with low semantic connectivity ratio (links per section)

### Files Needed
```
outputs/semantic_pairs.parquet
outputs/doc_concepts.parquet
outputs/topics_inventory.parquet
outputs/sections_embeddings_conceptual.parquet
```

### Target Concepts (Priority Order)
1. **Legacy .NET Framework** - 3.5 links/section
2. **Template Kit** - 4.3 links/section (NEW concept, Blazor-specific)
3. **Application Model** - 4.8 links/section (core concept, should be higher)
4. **Reference Property** - 5.0 links/section (NEW concept)

### AI Agent Prompt Template

```
CONTEXT:
The concept "[CONCEPT_NAME]" has only [X] semantic connections per section, which is below 
the corpus average of 8.5. This suggests documentation for this concept is fragmented or 
isolated, making it harder for users to discover related content.

Well-connected concepts like "Blazor UI" (9.7 links/section) and "Audit Trail" (14.1 links/section) 
serve as good reference models.

TASK:
Analyze the "[CONCEPT_NAME]" concept and suggest improvements to increase connectivity:

1. Find sections with [CONCEPT_NAME] that have 0-2 semantic connections (isolated)
2. Identify why these sections aren't connecting to related content
3. Suggest specific cross-references to add
4. Recommend new tutorial/example content that would tie concepts together

PROJECT FILES:
- outputs/doc_concepts.parquet: Section metadata and concept tags
- outputs/semantic_pairs.parquet: Current semantic relationships
- outputs/sections_embeddings_conceptual.parquet: Embeddings for similarity search
- outputs/topics_inventory.parquet: Full text of sections

EXPECTED OUTPUT:
1. List of 20 most isolated [CONCEPT_NAME] sections
2. For each isolated section:
   - Current concept tags
   - Why it's isolated (technical, too specific, missing context?)
   - 3-5 related sections it SHOULD link to
   - Suggested improvements (add examples, cross-references, code samples)
3. Overall recommendations for strengthening [CONCEPT_NAME] documentation
```

### Python Starter Code
```python
# Find under-connected sections for a concept
target_concept = "Template Kit"

# Get all sections with this concept
mask = kept["concepts"].apply(lambda cs: target_concept in (cs or []))
concept_sections = kept[mask].copy()

# Count connections per section
section_connections = {}
for _, row in pairs.iterrows():
    src = (row["source_doc"], row["source_section"])
    tgt = (row["target_doc"], row["target_section"])
    section_connections[src] = section_connections.get(src, 0) + 1
    section_connections[tgt] = section_connections.get(tgt, 0) + 1

# Add connection counts
concept_sections["num_connections"] = concept_sections.apply(
    lambda r: section_connections.get((r["doc_id"], r["section_id"]), 0), 
    axis=1
)

# Find isolated sections
isolated = concept_sections[concept_sections["num_connections"] <= 2].sort_values("num_connections")

print(f"\nIsolated {target_concept} sections (≤2 connections):")
print(f"Total: {len(isolated)}/{len(concept_sections)}")
print("\nTop 10 most isolated:")
for _, row in isolated.head(10).iterrows():
    print(f"  {row['doc_id']}")
    print(f"    Connections: {row['num_connections']}")
    print(f"    Other concepts: {[c for c in row['concepts'] if c != target_concept][:3]}")
```

---

## 🎯 Action 3: Connect Isolated Sections

**Problem**: 603 sections (5.4%) have NO semantic connections at all

### Files Needed
```
outputs/semantic_pairs.parquet
outputs/doc_concepts.parquet
outputs/topics_inventory.parquet
outputs/sections_embeddings_conceptual.parquet
outputs/sections_embeddings_api.parquet
```

### AI Agent Prompt Template

```
CONTEXT:
Out of 11,082 documentation sections, 603 (5.4%) are completely isolated - they have zero 
semantic connections to any other content. These are "documentation islands" that users 
can only find through direct search, not through related content navigation.

Examples of isolated sections include:
- API reference pages (View/AllowDelete)
- Module configuration guides
- Specific property/event documentation

TASK:
For a subset of isolated sections, determine why they're isolated and how to connect them:

1. Analyze 50 random isolated sections
2. Categorize isolation causes:
   - Too specific/niche content
   - Missing concept tags
   - Wrong similarity threshold
   - Genuinely unique content
   - Documentation quality issues (stub pages, empty content)
3. Provide actionable recommendations for each category

PROJECT FILES:
- outputs/doc_concepts.parquet: Find sections without connections
- outputs/semantic_pairs.parquet: Verify they're truly isolated
- outputs/topics_inventory.parquet: Read actual section content
- outputs/sections_embeddings_*.parquet: Check manual similarity to find near-misses

ANALYSIS APPROACH:
1. Get list of all isolated section IDs
2. Load their full text from topics_inventory
3. Load their embeddings
4. For each isolated section:
   - Check if it has sufficient content (not a stub)
   - Manually find top 10 semantically similar sections (even if below threshold)
   - Check if concept tags are accurate
   - Determine if it's genuinely unique or just missed by thresholds
5. Group by isolation cause and provide recommendations

OUTPUT:
- Isolated sections categorized by cause
- For "near-miss" sections: suggested threshold adjustments
- For "missing tags" sections: suggested concept additions
- For "stub pages": list for documentation team review
- For "genuinely unique": confirm they're appropriately isolated
```

### Python Starter Code
```python
import random

# Find truly isolated sections
connected = set()
for _, row in pairs.iterrows():
    connected.add((row["source_doc"], row["source_section"]))
    connected.add((row["target_doc"], row["target_section"]))

all_sections = set(zip(kept["doc_id"], kept["section_id"]))
isolated = all_sections - connected

print(f"Isolated sections: {len(isolated)}")

# Sample 50 for analysis
sample = random.sample(list(isolated), min(50, len(isolated)))

# Get details for each
for doc_id, section_id in sample[:10]:
    row = kept[(kept["doc_id"] == doc_id) & (kept["section_id"] == section_id)].iloc[0]
    
    # Get full content from inventory
    doc_row = inventory[inventory["doc_id"] == doc_id].iloc[0]
    sections = doc_row["sections"]
    section_content = [s for s in sections if s["section_id"] == section_id]
    
    if section_content:
        text = section_content[0].get("text", "")[:200]  # First 200 chars
        print(f"\n{doc_id} ({section_id})")
        print(f"  Concepts: {row['concepts']}")
        print(f"  Text preview: {text}...")
        print(f"  Is API: {row['is_api']}")
```

---

## 🎯 Action 4: Leverage Well-Connected Patterns

**Problem**: Learn from high-connectivity concepts to improve others

### Files Needed
```
outputs/semantic_pairs.parquet
outputs/doc_concepts.parquet
outputs/topics_inventory.parquet
```

### Top Well-Connected Concepts (Reference Models)
1. **Audit Trail** - 14.1 links/section
2. **Conditional Appearance** - 10.0 links/section
3. **Blazor UI** - 9.7 links/section
4. **Reports** - 9.5 links/section

### AI Agent Prompt Template

```
CONTEXT:
Some concepts in the XAF documentation have exceptionally high semantic connectivity, 
meaning their sections are well cross-referenced and discoverable. The best performers are:

- Audit Trail: 14.1 semantic links per section
- Conditional Appearance: 10.0 links per section
- Blazor UI: 9.7 links per section
- Reports: 9.5 links per section

In contrast, under-connected concepts average only 3.5-5.0 links per section.

TASK:
Analyze what makes these high-connectivity concepts successful, and create a playbook 
for improving other concepts:

1. Study documentation structure for "Audit Trail" and "Conditional Appearance"
2. Identify patterns:
   - How are sections organized?
   - What types of cross-references are used?
   - How do tutorials link to API docs?
   - What makes them discoverable?
3. Create a replicable template for improving under-connected concepts

PROJECT FILES:
- outputs/doc_concepts.parquet: All section metadata
- outputs/semantic_pairs.parquet: Connection patterns
- outputs/topics_inventory.parquet: Full section text

ANALYSIS STEPS:
1. Extract all "Audit Trail" sections
2. Analyze their connection patterns:
   - Which concepts do they co-occur with?
   - What's the distribution of cc/aa/ca/ac links?
   - What quality gates do they pass?
3. Read actual section content to identify documentation patterns
4. Create documentation template/guidelines

OUTPUT:
1. Connectivity Pattern Analysis Report
2. Documentation Structure Template (based on well-connected concepts)
3. Specific recommendations for applying patterns to:
   - Legacy .NET Framework
   - Template Kit
   - Reference Property
4. Quality metrics checklist for new documentation
```

### Python Starter Code
```python
# Analyze well-connected concept patterns
model_concept = "Audit Trail"

# Get all sections
mask = kept["concepts"].apply(lambda cs: model_concept in (cs or []))
model_sections = kept[mask]

print(f"\n{model_concept}: {len(model_sections)} sections")

# Analyze their connections
model_section_ids = set(zip(model_sections["doc_id"], model_sections["section_id"]))

# Find all connections
model_connections = []
for _, row in pairs.iterrows():
    src = (row["source_doc"], row["source_section"])
    tgt = (row["target_doc"], row["target_section"])
    
    if src in model_section_ids or tgt in model_section_ids:
        model_connections.append(row)

conn_df = pd.DataFrame(model_connections)

# Analyze patterns
print("\nConnection types:")
print(conn_df["neighbor_type"].value_counts())

print("\nTop gates passed:")
all_gates = []
for gates in conn_df["gates_passed"]:
    all_gates.extend(gates or [])
print(pd.Series(all_gates).value_counts().head())

print("\nCo-occurring concepts:")
all_overlap = []
for concepts in conn_df["overlap_concepts"]:
    all_overlap.extend([c for c in (concepts or []) if c != model_concept])
print(pd.Series(all_overlap).value_counts().head(10))

print("\nAverage similarity:")
print(f"  {conn_df['sim_score'].mean():.3f}")
```

---

## 📋 Quick Reference: File Purposes

| File | Purpose | When to Use |
|------|---------|-------------|
| `topics_inventory.parquet` | Full document text and structure | Need to read actual content, understand context |
| `doc_concepts.parquet` | Concept/platform/API tags per section | Filter by concept, check tagging quality |
| `semantic_pairs.parquet` | 93K semantic relationships | Analyze connectivity, find gaps |
| `sections_embeddings_*.parquet` | 384-dim vectors per section | Manual similarity search, find near-misses |
| `explicit_graph.parquet` | Explicit document links | Validate against semantic links |
| `config/concepts.yml` | Concept definitions | Understand concept taxonomy, add new concepts |

---

## 🔧 Utility Queries for AI Agents

### Find specific concept sections
```python
concept = "Template Kit"
mask = kept["concepts"].apply(lambda cs: concept in (cs or []))
sections = kept[mask]
```

### Get section text
```python
doc = inventory[inventory["doc_id"] == "article/security-system/authentication"].iloc[0]
for section in doc["sections"]:
    print(f"{section['section_id']}: {section.get('text', '')[:100]}")
```

### Find semantically similar sections (even below threshold)
```python
from sklearn.neighbors import NearestNeighbors
import numpy as np

# Load embeddings
emb_df = pd.read_parquet('outputs/sections_embeddings_conceptual.parquet')
X = np.vstack(emb_df["embedding"].tolist())

# Find 20 nearest neighbors for index 0
nn = NearestNeighbors(n_neighbors=20, metric='cosine').fit(X)
distances, indices = nn.kneighbors([X[0]])
similarities = 1.0 - distances[0]

for idx, sim in zip(indices[0], similarities):
    print(f"{emb_df.iloc[idx]['doc_id']}: {sim:.3f}")
```

### Check concept co-occurrence
```python
def concept_cooccurrence(concept_name):
    mask = kept["concepts"].apply(lambda cs: concept_name in (cs or []))
    sections = kept[mask]
    
    all_concepts = []
    for concepts_list in sections["concepts"]:
        all_concepts.extend([c for c in (concepts_list or []) if c != concept_name])
    
    return pd.Series(all_concepts).value_counts()

print(concept_cooccurrence("Blazor UI").head(10))
```

---

## 🎯 Action 5: Generate AI-Friendly Metadata (NEW!)

**Problem**: XAF docs need metadata tags to be discoverable by AI chatbots and RAG systems

### Files Needed
```
outputs/doc_concepts.parquet
outputs/semantic_pairs.parquet
outputs/topics_inventory.parquet
config/concepts.yml
```

### Scripts
```bash
# Generate metadata suggestions
python scripts/07_generate_metadata.py

# Export as YAML for documentation team
python scripts/08_export_yaml_metadata.py --export-yamls
```

### What It Does

Automatically generates three metadata fields for XAF documentation:

1. **`tags`** - Normalized concepts, platforms, APIs
   - Converts "Blazor UI" → `blazor-ui`
   - Converts "ASP.NET Core" → `asp-net-core`
   - Adds type tags: `api-reference`, `how-to`
   - Follows XAF rules: lowercase, no spaces, no dots

2. **`description`** - Concise 120-160 char summaries
   - Extracts first meaningful sentence for tutorials
   - Generates template descriptions for API docs
   - Uses heading context for better clarity

3. **`proficiencyLevel`** - Heuristic-based classification
   - **Beginner**: High connectivity, tutorial concepts
   - **Advanced**: API reference, medium connectivity
   - **Expert**: Low connectivity, performance/migration topics

### AI Agent Prompt Template

```
CONTEXT:
I have analyzed 11,082 XAF documentation sections and generated metadata suggestions
to make them more accessible to AI chatbots, RAG systems, and search engines.

The metadata includes:
- Tags (normalized from 40 concepts + platforms + APIs)
- Descriptions (extracted or generated)
- Proficiency levels (Beginner/Advanced/Expert)

TASK:
Review the metadata suggestions for quality and consistency:

1. Load outputs/metadata_suggestions.parquet
2. Check tag quality:
   - Are tags properly normalized? (lowercase, no spaces)
   - Are there redundant or overly generic tags?
   - Are important concepts missing?
3. Review descriptions:
   - Are they concise (120-160 chars)?
   - Do they complement (not repeat) the title?
   - Are they technically accurate?
4. Validate proficiency levels:
   - Does the distribution make sense? (most should be Beginner)
   - Are Expert-level docs truly specialized?

PROJECT FILES:
- outputs/metadata_suggestions.parquet: Generated metadata
- outputs/metadata_review.csv: Human-readable export

OUTPUT:
1. Tag quality report (duplicates, generic tags, missing tags)
2. Description quality report (length, clarity, accuracy)
3. Proficiency distribution validation
4. Top 20 documents needing manual review
```

### Python Starter Code

```python
import pandas as pd

# Load metadata suggestions
metadata = pd.read_parquet('outputs/metadata_suggestions.parquet')

print(f"Generated metadata for {len(metadata)} documents")

# Check tag quality
def check_tag_quality(tags):
    issues = []
    for tag in tags or []:
        if tag != tag.lower():
            issues.append(f"Not lowercase: {tag}")
        if ' ' in tag:
            issues.append(f"Contains space: {tag}")
        if '.' in tag:
            issues.append(f"Contains dot: {tag}")
    return issues

# Find documents with tag issues
for idx, row in metadata.head(100).iterrows():
    issues = check_tag_quality(row['suggested_tags'])
    if issues:
        print(f"\n{row['doc_id']}")
        for issue in issues:
            print(f"  - {issue}")

# Check description lengths
desc_lengths = metadata['suggested_description'].dropna().str.len()
print(f"\nDescription length stats:")
print(f"  Mean: {desc_lengths.mean():.0f} chars")
print(f"  Median: {desc_lengths.median():.0f} chars")
print(f"  Too short (<80): {(desc_lengths < 80).sum()}")
print(f"  Too long (>200): {(desc_lengths > 200).sum()}")
```

### Integration Workflow

**Step 1: Generate Metadata**
```bash
# Full generation
python scripts/07_generate_metadata.py

# Test on sample first
python scripts/07_generate_metadata.py --sample 100
```

**Step 2: Export for Review**
```bash
# Export bulk CSV for team review
python scripts/08_export_yaml_metadata.py

# Export individual YAML files for automated integration
python scripts/08_export_yaml_metadata.py --export-yamls
```

**Step 3: Manual Review**
- Documentation team reviews `outputs/metadata_review.csv`
- Validates tags, descriptions, proficiency levels
- Flags any incorrect classifications

**Step 4: Integrate into XAF Docs**
- Use individual YAML files from `outputs/metadata_yamls/`
- Inject into documentation front matter
- Or import via documentation build pipeline

### Expected Output

```yaml
---
description: >
  Learn how to implement the Security System in XAF applications,
  configure authentication, and manage user permissions.
tags:
  - security-system
  - authentication
  - blazor
  - asp-net-core
  - how-to
  - securitystrategy
proficiencyLevel: Beginner
---
```

---

## 🚀 Recommended Workflow for AI Agent

1. **Start with gaps analysis**: `python query_graph.py --mode gaps`
2. **Pick one action** (start with Action 1 - highest impact)
3. **Generate AI metadata**: `python scripts/07_generate_metadata.py` (Action 5)
4. **Load relevant files** from the table above
5. **Run starter code** to understand the data
6. **Use prompt template** to frame the analysis task
7. **Generate specific recommendations** with doc IDs and section IDs
8. **Validate findings** by querying specific sections
9. **Export results** for documentation team review

---

## 📊 Success Metrics

After improvements, re-run Phase 5 and check:
- [ ] Reduced isolated sections (target: <3%)
- [ ] Increased connectivity for under-connected concepts (target: >7 links/section)
- [ ] All concepts have ≥10 cross-corpus links
- [ ] Average similarity score maintained (≥0.75)
- [ ] New documentation passes connectivity threshold on first run

After metadata generation (Phase 7):
- [ ] All documents have 3-8 relevant tags
- [ ] 90%+ documents have descriptions
- [ ] Proficiency distribution: ~70% Beginner, ~25% Advanced, ~5% Expert
- [ ] Tags follow XAF rules (lowercase, no spaces, no dots)
- [ ] No generic/noise tags (tutorial, guide, best, ultimate)
