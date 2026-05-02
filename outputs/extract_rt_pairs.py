import pandas as pd

cp = pd.read_parquet('outputs/classified_pairs.parquet')
rt = cp[cp.relationship_type == 'related_to']
rt_keys = set(zip(rt.source_doc, rt.source_section, rt.target_doc, rt.target_section))

sp = pd.read_parquet('outputs/semantic_pairs_high_value.parquet')
mask = sp.apply(lambda r: (r.source_doc, r.source_section, r.target_doc, r.target_section) in rt_keys, axis=1)
filtered = sp[mask]
filtered.to_parquet('outputs/semantic_pairs_rt_rerun.parquet', index=False)
print(f'Saved {len(filtered)} pairs for re-classification')
