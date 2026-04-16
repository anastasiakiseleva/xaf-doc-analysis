"""Sort taxonomy concepts by domain > subdomain > name (alphabetical)."""
import json
from pathlib import Path

TAXONOMY_PATH = Path(__file__).parent.parent / "config" / "xaf-taxonomy.json"

with open(TAXONOMY_PATH, "r", encoding="utf-8") as f:
    taxonomy = json.load(f)

concepts = taxonomy["taxonomy"]["concepts"]
concepts.sort(key=lambda c: (c.get("domain", ""), c.get("subdomain", ""), c.get("name", "")))

with open(TAXONOMY_PATH, "w", encoding="utf-8") as f:
    json.dump(taxonomy, f, indent=2, ensure_ascii=False)
    f.write("\n")

print(f"Sorted {len(concepts)} concepts by domain > subdomain > name")
for c in concepts:
    print(f"  {c['domain']:15} {c.get('subdomain',''):25} {c['name']}")
