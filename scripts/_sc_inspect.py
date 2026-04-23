import json
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config_loader import cfg

parser = argparse.ArgumentParser(description="Inspect taxonomy concept definitions")
parser.add_argument(
    "--concept", dest="concepts", metavar="NAME", action="append", default=[],
    help="Concept name to inspect (may be repeated). Omit to use the default sample list."
)
args = parser.parse_args()

with open(cfg.taxonomy_path(), encoding="utf-8") as f:
    t = json.load(f)
concepts = t['taxonomy']['concepts']

_DEFAULT_TARGETS = [
    'Conditional Appearance', 'Filtering UI', 'Application Model', 'State Machine',
    'Lookup Property Editors', 'Web API Service', 'Business Object Lifecycle', 'Multi-Tenancy',
]
targets = set(args.concepts) if args.concepts else set(_DEFAULT_TARGETS)

for c in concepts:
    if c['name'] in targets:
        print("=== " + c['name'] + " [" + c['domain'] + "/" + c['subdomain'] + "] ===")
        print("  synonyms: " + str(c.get('terminology',{}).get('synonyms',[])))
        print("  keywords: " + str(c.get('terminology',{}).get('keywords',[])))
        print("  api_primary: " + str(c.get('api_surface',{}).get('primary_types',[])))
        print("  api_related: " + str(c.get('api_surface',{}).get('related_types',[])))
        print("  relations: " + str(c.get('relations',{})))
        print()
