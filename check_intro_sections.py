import pandas as pd, ast

topics = pd.read_parquet('outputs/topics_inventory.parquet')
topics['num_sections'] = topics['sections'].apply(
    lambda s: len(s) if isinstance(s, list) else len(ast.literal_eval(s))
)

v = topics[topics['doc_id'] == 'data/raw_md/articles/ui-construction/views'].iloc[0]
print('views doc sections:', v['num_sections'])
sections = v['sections'] if isinstance(v['sections'], list) else ast.literal_eval(v['sections'])
for i, s in enumerate(sections[:4]):
    txt = s['text']
    words = len(txt.split())
    hp = s['h_path']
    print(f'  section {i+1}: {words} words | h_path={hp}')
    print(f'    {txt[:120]}')
    print()

df = pd.read_parquet('outputs/semantic_pairs.parquet')
df['src_sec_num'] = df['source_section'].str.extract(r'::(\d+)$').astype(float)
early = df[(df['src_sec_num'] <= 2) & (~df['source_is_api'])]
print(f'Early (sec<=2) non-API source pairs: {len(early):,} of {len(df):,} ({100*len(early)/len(df):.1f}%)')

# What fraction of those are conceptual->API cross-corpus?
early_cross = early[early['source_is_api'] != early['target_is_api']]
print(f'Of those, cross-corpus: {len(early_cross):,}')

# Build a section word-count lookup from topics for intro sections
print()
print('Checking intro section word counts for known hub docs:')
hub_docs = [
    'data/raw_md/articles/ui-construction/views',
    'data/raw_md/articles/security-system/authorization-and-data-protection',
    'data/raw_md/articles/business-model-design-with-entity-framework-core',
]
for doc_id in hub_docs:
    row = topics[topics['doc_id'] == doc_id]
    if len(row) == 0:
        print(f'  {doc_id.split("/")[-1]}: NOT FOUND')
        continue
    row = row.iloc[0]
    secs = row['sections'] if isinstance(row['sections'], list) else ast.literal_eval(row['sections'])
    for i in range(min(2, len(secs))):
        words = len(secs[i]['text'].split())
        print(f'  {doc_id.split("/")[-1]} sec{i+1}: {words} words')
