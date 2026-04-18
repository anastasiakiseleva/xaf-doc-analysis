"""Phase 3.5 — Metrics Snapshot (run after Phases 1-3 and 5)."""
import sys
sys.path.insert(0, ".")
import numpy as np
import pandas as pd
from pathlib import Path
from collections import Counter

OUTPUT = Path("outputs")

# ── Load data ──────────────────────────────────────────────────────────────
inv = pd.read_parquet(OUTPUT / "topics_inventory.parquet")
dc  = pd.read_parquet(OUTPUT / "doc_concepts.parquet")
sp  = pd.read_parquet(OUTPUT / "semantic_pairs.parquet")

kept    = dc[dc.kept == True]
dropped = dc[dc.kept == False]

def safe_len(x):
    try:
        return len(x) if x is not None else 0
    except Exception:
        return 0

# ── 1. Section retention ───────────────────────────────────────────────────
print("=" * 60)
print("1. SECTION RETENTION")
print("=" * 60)
total  = len(dc)
n_kept = len(kept)
n_api  = kept["is_api"].sum()
n_conc = n_kept - n_api
print(f"  Total sections:         {total:>7,}")
print(f"  Kept:                   {n_kept:>7,}  ({100*n_kept/total:.1f}%)")
print(f"    Conceptual:           {n_conc:>7,}  ({100*n_conc/n_kept:.1f}% of kept)")
print(f"    API reference:        {n_api:>7,}  ({100*n_api/n_kept:.1f}% of kept)")
print(f"  Dropped:                {len(dropped):>7,}  ({100*len(dropped)/total:.1f}%)")
if dropped["skip_reason"].notna().any():
    reasons = dropped["skip_reason"].value_counts().head(6)
    for r, c in reasons.items():
        print(f"    {r}: {c:,}")

# ── 2. Concept density ─────────────────────────────────────────────────────
print()
print("=" * 60)
print("2. CONCEPT DENSITY")
print("=" * 60)
has_concepts = kept["concepts"].apply(lambda x: len(x) > 0 if hasattr(x, "__len__") else False)
n_with = has_concepts.sum()
print(f"  Sections with >=1 concept: {n_with:,} / {n_kept:,}  ({100*n_with/n_kept:.1f}%)")
avg_all   = kept["concepts"].apply(lambda x: len(x) if hasattr(x, "__len__") else 0).mean()
avg_match = kept[has_concepts]["concepts"].apply(len).mean()
print(f"  Avg concepts/section (all):      {avg_all:.2f}")
print(f"  Avg concepts/section (matched):  {avg_match:.2f}")

# ── 3. Platform coverage ───────────────────────────────────────────────────
print()
print("=" * 60)
print("3. PLATFORM COVERAGE")
print("=" * 60)
plat_counter = Counter()
for row in kept["platforms"]:
    if hasattr(row, "__iter__") and not isinstance(row, str):
        plat_counter.update(row)
if plat_counter:
    for p, c in plat_counter.most_common():
        print(f"  {p}: {c:,}")
else:
    print("  (no platform data — patterns.yml not present; platform tags come from text extraction)")

# ── 4. Section length distribution ────────────────────────────────────────
print()
print("=" * 60)
print("4. SECTION LENGTH (word count percentiles, conceptual corpus)")
print("=" * 60)
try:
    ec = pd.read_parquet(OUTPUT / "sections_embeddings_conceptual.parquet")
    wc = ec["word_count"]
    for label, pct in zip(["p10", "p25", "p50", "p75", "p90", "p95"], [10, 25, 50, 75, 90, 95]):
        print(f"  {label}: {np.percentile(wc, pct):.0f} words")
    print(f"  <50 words (too short): {(wc < 50).sum():,} ({100*(wc < 50).mean():.1f}%)")
    print(f"  >500 words (long):     {(wc > 500).sum():,} ({100*(wc > 500).mean():.1f}%)")
except Exception as e:
    print(f"  (skipped: {e})")

# ── 5. Semantic pairs ──────────────────────────────────────────────────────
print()
print("=" * 60)
print("5. SEMANTIC PAIRS SUMMARY")
print("=" * 60)
total_pairs = len(sp)
by_type = sp["neighbor_type"].value_counts()
cross   = sp[sp["neighbor_type"].isin(["ca", "ac"])]
print(f"  Total pairs:            {total_pairs:>7,}")
for t, c in by_type.items():
    print(f"    {t}: {c:>6,}  ({100*c/total_pairs:.1f}%)")
print(f"  Cross-corpus (ca+ac):   {len(cross):>7,}  ({100*len(cross)/total_pairs:.1f}%)")
print(f"  Avg similarity (all):   {sp['sim_score'].mean():.3f}")
for ntype in ["cc", "aa", "ca", "ac"]:
    subset = sp[sp["neighbor_type"] == ntype]
    if len(subset):
        print(f"  Avg similarity {ntype}:      {subset['sim_score'].mean():.3f}")

connections = sp.groupby(["source_doc", "source_section"]).size()
avg_conn = connections.mean()
isolated = n_kept - len(connections)
print(f"  Avg connections/section:{avg_conn:>8.1f}")
print(f"  Sections with 0 pairs:  {isolated:>7,}  ({100*isolated/n_kept:.1f}%)")

# ── 6. Concept vocabulary ─────────────────────────────────────────────────
print()
print("=" * 60)
print("6. CONCEPT VOCABULARY & GAP SUMMARY")
print("=" * 60)
from utils.taxonomy_loader import load_concepts
cfg = load_concepts()
all_concepts = [c["name"] for c in cfg.get("concepts", [])]
print(f"  Taxonomy concepts:          {len(all_concepts):,}")
matched = set()
for row in kept["concepts"]:
    if hasattr(row, "__iter__") and not isinstance(row, str):
        matched.update(row)
print(f"  Concepts matched in corpus: {len(matched):,}  ({100*len(matched)/len(all_concepts):.1f}%)")
unmatched = [c for c in all_concepts if c not in matched]
print(f"  Concepts with 0 sections:   {len(unmatched):,}")
if unmatched:
    print("  Zero-match concepts:", unmatched)

print()
print("=" * 60)
print("PHASE 3.5 COMPLETE — corpus readiness assessment done.")
print("=" * 60)
