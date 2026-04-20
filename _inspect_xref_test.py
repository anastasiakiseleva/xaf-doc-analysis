import pandas as pd

old = set(pd.read_parquet('outputs/classified_pairs.parquet', engine='pyarrow')['source_section'].tolist())
df = pd.read_parquet('outputs/classified_pairs_xref_test.parquet', engine='pyarrow')
new = df[~df['source_section'].isin(old)]
print(f'New xref_link classifications: {len(new)}')
print()

def short(p):
    return p.split('/')[-1] if isinstance(p, str) else p

new2 = new.copy()
new2['src'] = new2['source_doc'].apply(short)
new2['tgt'] = new2['target_doc'].apply(short)
print(new2[['src','tgt','relationship_type','relationship_confidence']].to_string(index=False))
print()
print('Type breakdown:')
print(new['relationship_type'].value_counts())
print(f"Avg confidence: {new['relationship_confidence'].mean():.3f}")
