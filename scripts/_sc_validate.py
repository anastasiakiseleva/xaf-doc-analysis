import json, re
from collections import defaultdict

sc = {
  'Core': ['General','API','Customization','Extensibility','Compatibility','Breaking Changes','Migration','Upgrade','Deployment','Licensing','Localization','Documentation'],
  'UI & Views': ['UI','Layout','DetailView','ListView','DashboardView','Nested ListView','View Variants','Property Editor','View Item','Custom View Item','Templates','Tabs','Navigation','Popup Window','Conditional Appearance','Theming','Responsive Layout'],
  'Actions & Controllers': ['Actions','SimpleAction','PopupWindowShowAction','ParametrizedAction','SingleChoiceAction','Controllers','ObjectViewController','WindowController','DialogController','Frame','ShowViewStrategy'],
  'Application Model': ['Application Model','Model Editor','Model Differences','Model Cache','Runtime Model Customization'],
  'Data Access & ORM': ['XPO','Entity Framework','EF Core','ORM Integration','Persistent Objects','Associations','Aggregated Objects','Oid','ObjectSpace','Nested ObjectSpace','NonPersistentObjectSpace','Data Access','Data Binding','Criteria','CriteriaOperator','LINQ','Filtering','Sorting','Grouping','CollectionSource','Large Data Sources'],
  'Security': ['Security','Authentication','Authorization','Permissions','Role-based Security','Object-level Security','Member-level Security','Current User','Multi-Tenancy','Security System'],
  'Dashboards Module': ['Dashboards','Dashboard Parameters','Dashboard Filtering','IDashboardData','DashboardViewer','ASPxDashboard','InitialDashboardState','Parameters','Criteria Passing','Dynamic Filters','Data Source'],
  'Reports Module': ['Reporting','Reports Module','ReportDataV2','ReportServiceController','Report Parameters','Report Filtering','Report Storage','Runtime Reports','Printing','Export','Import'],
  'Chart Module': ['Chart Module','ChartListEditor','Chart Data Binding'],
  'Validation Module': ['Validation','Validation Rules','RuleCriteria','RuleRequiredField'],
  'Additional Modules': ['Audit Trail','File Attachments','Scheduler','Workflow'],
  'Platform - Blazor': ['Blazor','DxDashboardViewer','Blazor Security','Razor Components'],
  'Platform - WinForms': ['WinForms','WinDashboardViewer','Windows-specific Behavior'],
  'Integration': ['Web API','OData','Office Integration','RichEdit Integration','Spreadsheet Integration','Third-party Integration'],
  'Performance & Diagnostics': ['Performance','Memory Usage','Threading','Async','Caching','Object Lifecycle','ObjectSaving','OnLoaded','OnSaving','Search','Full Text Search','Error Handling','Exception','Logging','Diagnostics','UX','Accessibility'],
}

# Reverse map: term -> sc_category
term_to_sc_cat = {}
for cat, terms in sc.items():
    for term in terms:
        term_to_sc_cat[term.lower()] = cat

with open(r'c:\Documentation\xaf-doc-analysis\config\xaf-taxonomy.json') as f:
    t = json.load(f)
concepts = t['taxonomy']['concepts']

def get_all_labels(c):
    labels = {}
    labels[c['name'].lower()] = 'name'
    for s in c.get('terminology', {}).get('synonyms', []):
        labels[s.lower()] = 'synonym'
    for k in c.get('terminology', {}).get('keywords', []):
        labels[k.lower()] = 'keyword'
    for k in c.get('api_surface', {}).get('primary_types', []):
        labels[k.lower()] = 'api_primary'
    for k in c.get('api_surface', {}).get('related_types', []):
        labels[k.lower()] = 'api_related'
    return labels

# ---------- PASS 1: for each SC category, find XT concepts that match any of its terms ----------
# Then check if those XT concepts are scattered across different domains/subdomains
print("=" * 80)
print("PASS 1: SC category coherence — are 'related' SC terms mapped to the same XT domain?")
print("=" * 80)

for cat, terms in sc.items():
    xt_hits = []  # (sc_term, xt_concept_name, xt_domain/subdomain, label_field)
    for term in terms:
        for c in concepts:
            labels = get_all_labels(c)
            if term.lower() in labels:
                xt_hits.append((term, c['name'], f"{c['domain']}/{c['subdomain']}", labels[term.lower()]))
    if not xt_hits:
        continue
    # Check if hits span multiple domains
    domains_hit = set(h[2].split('/')[0] for h in xt_hits)
    subdomains_hit = set(h[2] for h in xt_hits)
    flag = " *** CROSS-DOMAIN ***" if len(domains_hit) > 1 else ""
    print(f"\n[{cat}]{flag}")
    for sc_term, xt_name, xt_loc, field in xt_hits:
        print(f"  SC:'{sc_term}' -> XT:'{xt_name}' [{xt_loc}] via {field}")

# ---------- PASS 2: SC term matched into a *wrong-seeming* XT location ----------
print("\n")
print("=" * 80)
print("PASS 2: Specific placement mismatches — SC term location vs XT concept location")
print("=" * 80)

mismatches = []
for cat, terms in sc.items():
    for term in terms:
        for c in concepts:
            labels = get_all_labels(c)
            if term.lower() not in labels:
                continue
            field = labels[term.lower()]
            xt_domain = c['domain']
            xt_subdomain = c['subdomain']
            xt_loc = f"{xt_domain}/{xt_subdomain}"

            # Define expected xt domain per sc category
            expected_domains = {
                'Core': {'architecture', 'ops', 'migration'},
                'UI & Views': {'ui'},
                'Actions & Controllers': {'ui'},
                'Application Model': {'architecture'},
                'Data Access & ORM': {'data'},
                'Security': {'security'},
                'Dashboards Module': {'ui'},
                'Reports Module': {'ui'},
                'Chart Module': {'ui'},
                'Validation Module': {'data', 'quality'},
                'Additional Modules': {'ui', 'data', 'security'},
                'Platform - Blazor': {'ui', 'architecture', 'security'},
                'Platform - WinForms': {'ui'},
                'Integration': {'architecture', 'ui'},
                'Performance & Diagnostics': {'quality', 'ops'},
            }
            expected = expected_domains.get(cat, set())
            if expected and xt_domain not in expected:
                mismatches.append({
                    'sc_cat': cat,
                    'sc_term': term,
                    'xt_concept': c['name'],
                    'xt_loc': xt_loc,
                    'field': field,
                    'expected_domains': expected,
                })

for m in mismatches:
    print(f"  MISMATCH: SC[{m['sc_cat']}] '{m['sc_term']}' (via {m['field']}) "
          f"-> XT '{m['xt_concept']}' [{m['xt_loc']}]  (expected domain: {m['expected_domains']})")

# ---------- PASS 3: synonyms shared across different XT concepts ----------
print("\n")
print("=" * 80)
print("PASS 3: Terms that appear as labels on MULTIPLE XT concepts (ambiguous labeling)")
print("=" * 80)

label_to_concepts = defaultdict(list)
for c in concepts:
    labels = get_all_labels(c)
    for label, field in labels.items():
        label_to_concepts[label].append((c['name'], f"{c['domain']}/{c['subdomain']}", field))

for label, hits in sorted(label_to_concepts.items()):
    if len(hits) > 1:
        # Only report if sc knows about this term
        if label in term_to_sc_cat:
            print(f"  AMBIGUOUS label '{label}' (SC cat: {term_to_sc_cat[label]}):")
            for name, loc, field in hits:
                print(f"    XT '{name}' [{loc}] as {field}")

# ---------- PASS 4: SC groups closely related terms that XT splits with no relation ----------
print("\n")
print("=" * 80)
print("PASS 4: SC co-located terms whose XT concepts have NO declared relation to each other")
print("=" * 80)

def find_concept_by_label(label, concepts):
    label_l = label.lower()
    for c in concepts:
        if get_all_labels(c).get(label_l):
            return c
    return None

for cat, terms in sc.items():
    # find XT concepts for each term (by name only for precision)
    xt_concepts_in_cat = []
    for term in terms:
        c = None
        for candidate in concepts:
            if candidate['name'].lower() == term.lower():
                c = candidate
                break
        if c:
            xt_concepts_in_cat.append(c)

    if len(xt_concepts_in_cat) < 2:
        continue

    # Check pairs: do they share domain or have explicit relations?
    ids = set(c['id'] for c in xt_concepts_in_cat)
    unrelated_pairs = []
    for i, a in enumerate(xt_concepts_in_cat):
        for b in xt_concepts_in_cat[i+1:]:
            same_domain = a['domain'] == b['domain']
            same_subdomain = a['subdomain'] == b['subdomain']
            a_rels = set()
            for rel_list in a.get('relations', {}).values():
                a_rels.update(rel_list)
            b_rels = set()
            for rel_list in b.get('relations', {}).values():
                b_rels.update(rel_list)
            cross_linked = (b['id'] in a_rels) or (a['id'] in b_rels)
            if not same_domain and not cross_linked:
                unrelated_pairs.append((a, b))

    if unrelated_pairs:
        print(f"\n[{cat}] — unrelated pairs in XT:")
        for a, b in unrelated_pairs:
            print(f"    '{a['name']}' [{a['domain']}/{a['subdomain']}]  <->  "
                  f"'{b['name']}' [{b['domain']}/{b['subdomain']}]  (no relation, different domain)")

print("\nDone.")
