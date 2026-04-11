import json
from collections import Counter

kg = json.load(open('outputs/knowledge_graph.json', encoding='utf-8'))

bad_titles = ['C#', 'VB.NET', 'C++ / CLI', 'F#', 'JavaScript', 'TypeScript']
bad = [n for n in kg['nodes'] if n.get('title', '').strip() in bad_titles]
print('Nodes with language-tab titles:', len(bad))

for t in bad_titles:
    count = sum(1 for n in bad if n.get('title', '').strip() == t)
    if count:
        print(f'  {repr(t)}: {count}')

print()
print('Sample bad nodes:')
for n in bad[:6]:
    node_id = n['id']
    title = n.get('title', '')
    path = n.get('doc_id', '')
    ntype = n.get('type', '')
    print(f'  [{ntype}] title={repr(title)}')
    print(f'    path={path}')
    print()

# Also check document_metadata.csv
import pandas as pd
meta = pd.read_csv('outputs/document_metadata.csv')
bad_meta = meta[meta['title'].isin(bad_titles)]
print('document_metadata.csv rows with language-tab titles:', len(bad_meta))
if len(bad_meta):
    print(bad_meta[['doc_id', 'title']].head(10).to_string(index=False))
