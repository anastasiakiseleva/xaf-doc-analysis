import pandas as pd
import numpy as np

def has_gate(g, gate):
    if isinstance(g, (list, np.ndarray)):
        return gate in g
    return False

sp = pd.read_parquet('outputs/semantic_pairs.parquet', engine='pyarrow')
hv = pd.read_parquet('outputs/semantic_pairs_high_value.parquet', engine='pyarrow')

xref_sp = sp[sp['gates_passed'].apply(lambda g: has_gate(g, 'xref_link'))]
print(f"xref_link pairs in semantic_pairs: {len(xref_sp)}")
if len(xref_sp):
    print(f"sim range: {xref_sp['sim_score'].min():.3f} - {xref_sp['sim_score'].max():.3f}")

xref_hv = hv[hv['gates_passed'].apply(lambda g: has_gate(g, 'xref_link'))] if 'gates_passed' in hv.columns else hv.iloc[0:0]
print(f"xref_link pairs in high_value: {len(xref_hv)}")

# Save a 50-pair sample for Phase 6 test run
sample = xref_sp.sample(n=min(50, len(xref_sp)), random_state=42)
sample.to_parquet('outputs/semantic_pairs_xref_test.parquet', engine='pyarrow', index=False)
print(f"Saved test sample: {len(sample)} pairs -> outputs/semantic_pairs_xref_test.parquet")
