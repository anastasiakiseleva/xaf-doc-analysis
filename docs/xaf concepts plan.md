# How to Determine Optimal Numbers

## Step 1: Start with Core Concept Analysis (Week 1)

**Create a 50-concept starter set:**

- Security & Auth: 8-12 concepts
  (authentication, authorization, roles, permissions)
  
- Data Access: 10-15 concepts
  (persistence, object spaces, transactions, queries)
  
- UI Components: 15-20 concepts
  (grid view, detail view, list view, editors)
  
- Architecture: 8-12 concepts
  (modules, controllers, business objects)
  
- Platforms: 5-8 concepts
  (Blazor, WinForms, Web API)
  
- Common Patterns: 10-15 concepts
  (validation, filtering, sorting, CRUD)

**Total:** 50 concepts, ~160 searchable terms

**Run Phase 3 and check:**

```python
# Load results
df = pd.read_parquet('outputs/doc_concepts.parquet')

# Key metrics:
coverage = df[df['concepts'].apply(len) > 0].shape[0] / len(df)
print(f"Coverage: {coverage:.1%}")  # Goal: >60%

density = df['concepts'].apply(len).mean()
print(f"Density: {density:.2f}")    # Goal: 0.08-0.15

# Concept frequency distribution
all_concepts = [c for concepts in df['concepts'] for c in concepts]
freq = pd.Series(all_concepts).value_counts()
print(freq.head(20))  # Top concepts should appear 50+ times
```

**Success criteria for 50 concepts:**
- Coverage ≥ 60% (at least 60% of sections have ≥1 concept)
- Density = 0.08-0.12 (average 1 concept per ~10 words)
- Top 10 concepts appear in 50+ sections each

## Step 2: Expand Based on Gaps (Week 2)

**Find missing concepts:**
```python
# Sections with 0 concepts - these are gaps
no_concepts = df[df['concepts'].apply(len) == 0]
print(f"Gap sections: {len(no_concepts)}")

# Sample 50 random gap sections - manually review
sample = no_concepts.sample(50)
sample[['doc_id', 'h_path']].to_csv('gap_analysis.csv')
```

**Add 25-50 more concepts** to cover the gaps

**Target metrics with 100 concepts:**
- Coverage ≥ 75%
- Density = 0.10-0.15
- Fewer than 20% of sections have 0 concepts

## Step 3: Synonym Tuning (Week 3)

**Check for missed matches:**
```python
# Find sections with low concept density but high word count
# These likely have missed synonyms
low_density = df[(df['concept_density'] < 0.05) & (df['word_count'] > 50)]

# Export sample for manual review
low_density.sample(30)[['doc_id', 'h_path', 'concepts']].to_csv('synonym_gaps.csv')
```

**For each concept, audit synonym coverage:**

```yaml
# Before (missing common variations):
- name: "Security Strategy"
  synonyms: ["SecurityStrategy"]

# After manual review of actual docs:
- name: "Security Strategy"
  synonyms: ["SecurityStrategy", "security policy", 
             "SecurityStrategyComplex", "auth strategy"]
```

## Synonym Count Decision Tree

Is this a...

1. XAF-specific class/API name?
   → 2-3 synonyms (PascalCase + spaced + common abbreviation)
   Example: "DetailView" → ["detail view", "DV"]

2. Generic UI component?
   → 3-5 synonyms (many spelling variations exist)
   Example: "Button" → ["command button", "action button", "button control"]

3. Abstract domain concept?
   → 2-3 synonyms (stable terminology)
   Example: "Validation" → ["validate", "data validation"]

4. Action/operation?
   → 3-4 synonyms (verb variations)
   Example: "Filter" → ["filtering", "filter data", "data filter"]

5. Platform/technology name?
   → 1-2 synonyms (proper nouns, limited variation)
   Example: "Blazor" → ["Blazor Server"]
