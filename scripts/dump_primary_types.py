import json

with open('config/xaf-taxonomy.json') as f:
    data = json.load(f)

concepts = data['taxonomy']['concepts']
for i, c in enumerate(concepts, 1):
    api = c.get('api_surface', {})
    pts = api.get('primary_types', [])
    cid = c['id'].split('.', 2)[-1]
    name = c['name']
    print(f"{i}. {cid} ({name})")
    if pts:
        print(f"   primary_types: {pts}")
    else:
        print(f"   primary_types: (none)")
    print()
