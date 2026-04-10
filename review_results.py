import pandas as pd

df = pd.read_parquet('outputs/classified_pairs.parquet')

low = df[(df['relationship_type'] == 'related_to') & (df['relationship_confidence'] < 0.7)]
print('Low-conf related_to:', len(low))
for _, r in low.iterrows():
    src = '/'.join(r['source_doc'].split('/')[-2:])
    tgt = '/'.join(r['target_doc'].split('/')[-2:])
    conf = r['relationship_confidence']
    sc = r['source_concepts']
    tc = r['target_concepts']
    print(f'  conf={conf} | {src} -> {tgt}')
    print(f'    concepts: {sc} / {tc}')

print()
print('--- explains examples ---')
for _, r in df[df['relationship_type'] == 'explains'].iterrows():
    src = r['source_doc'].split('/')[-1]
    tgt = r['target_doc'].split('/')[-1]
    label = 'cross' if r['is_cross_corpus'] else 'same'
    conf = r['relationship_confidence']
    bidir = r['relationship_bidirectional']
    print(f'  conf={conf} bidir={bidir} [{label}]')
    print(f'    {src} -> {tgt}')

print()
print('--- uses examples ---')
for _, r in df[df['relationship_type'] == 'uses'].iterrows():
    src = r['source_doc'].split('/')[-1]
    tgt = r['target_doc'].split('/')[-1]
    label = 'cross' if r['is_cross_corpus'] else 'same'
    conf = r['relationship_confidence']
    src_api = r['source_is_api']
    tgt_api = r['target_is_api']
    print(f'  conf={conf} [{label}] src_api={src_api} tgt_api={tgt_api}')
    print(f'    {src} -> {tgt}')

print()
print('--- contrasts_with ---')
for _, r in df[df['relationship_type'] == 'contrasts_with'].iterrows():
    src = r['source_doc'].split('/')[-1]
    tgt = r['target_doc'].split('/')[-1]
    conf = r['relationship_confidence']
    bidir = r['relationship_bidirectional']
    print(f'  conf={conf} bidir={bidir}')
    print(f'    {src} -> {tgt}')
