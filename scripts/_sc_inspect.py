import json
with open(r'c:\Documentation\xaf-doc-analysis\config\xaf-taxonomy.json') as f:
    t = json.load(f)
concepts = t['taxonomy']['concepts']

targets = ['Conditional Appearance', 'Filtering UI', 'Application Model', 'State Machine',
           'Lookup Property Editors', 'Web API Service', 'Business Object Lifecycle', 'Multi-Tenancy']
for c in concepts:
    if c['name'] in targets:
        print("=== " + c['name'] + " [" + c['domain'] + "/" + c['subdomain'] + "] ===")
        print("  synonyms: " + str(c.get('terminology',{}).get('synonyms',[])))
        print("  keywords: " + str(c.get('terminology',{}).get('keywords',[])))
        print("  api_primary: " + str(c.get('api_surface',{}).get('primary_types',[])))
        print("  api_related: " + str(c.get('api_surface',{}).get('related_types',[])))
        print("  relations: " + str(c.get('relations',{})))
        print()
