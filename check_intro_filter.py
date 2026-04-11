import pandas as pd
df = pd.read_parquet('outputs/semantic_pairs.parquet')

df['src_sec_idx'] = df['source_section'].str.extract(r'::(\d+)$').astype(float)
df['src_n_concepts'] = df['source_concepts'].apply(lambda x: len(x) if hasattr(x, '__len__') else 0)
df['n_overlap'] = df['overlap_concepts'].apply(lambda x: len(x) if hasattr(x, '__len__') else 0)

bad_pattern = (
    (~df['source_is_api']) &
    df['target_is_api'] &
    (df['src_sec_idx'] <= 2) &
    (df['src_n_concepts'] <= 5)
)

print('Pairs matching broad-intro filter:', bad_pattern.sum(), 'of', len(df))
print()
print('Cross-corpus (conceptual->API):', ((~df['source_is_api']) & df['target_is_api']).sum())
print('Of those, early (<=2):', ((~df['source_is_api']) & df['target_is_api'] & (df['src_sec_idx'] <= 2)).sum())
print('Of those, also few concepts (<=5):', bad_pattern.sum())
print()

bad_case = df[df['source_section'] == 'views::2']
print('views::2 rows:', len(bad_case))
if len(bad_case):
    r = bad_case.iloc[0]
    idx = r['src_sec_idx']
    nc = r['src_n_concepts']
    is_api = r['target_is_api']
    print(f'  src_sec_idx={idx} src_n_concepts={nc} target_is_api={is_api}')
    print(f'  caught={bool(bad_pattern[bad_case.index[0]])}')

good_case = df[df['source_section'].str.startswith('list-view-data-access')]
print()
print('list-view-data-access-modes sections:', len(good_case))
if len(good_case):
    r = good_case.iloc[0]
    idx = r['src_sec_idx']
    nc = r['src_n_concepts']
    print(f'  src_sec_idx={idx} src_n_concepts={nc}')
    print(f'  caught={bool(bad_pattern[good_case.index[0]])}')

# Also check: what does the high-value filtered output look like?
# i.e. how many cross-corpus pairs survive above 0.7 similarity?
hv = pd.read_parquet('outputs/semantic_pairs_high_value.parquet')
hv['src_sec_idx'] = hv['source_section'].str.extract(r'::(\d+)$').astype(float)
hv['src_n_concepts'] = hv['source_concepts'].apply(lambda x: len(x) if hasattr(x, '__len__') else 0)
bad_in_hv = (
    (~hv['source_is_api']) &
    hv['target_is_api'] &
    (hv['src_sec_idx'] <= 2) &
    (hv['src_n_concepts'] <= 5)
)
print()
print('--- In high_value pairs (3302 rows) ---')
print('Matching broad-intro filter:', bad_in_hv.sum())
print('Total pairs:', len(hv))
