"""
One-off script: scan primary_types for non-API artefacts.
Flags: file formats, protocol names, abbreviations (<= 4 chars all-caps),
member paths (contains '.'), MSBuild/CLI terms, and bare event/method names.
"""
import json, re

KNOWN_BAD_PATTERNS = [
    r"^[A-Z]{2,4}$",            # all-caps abbreviations: DI, MDI, SVG, ARR, AWS
    r"\.[a-z]",                 # member paths: IModelApplication.PreferredLanguage
    r"^(WebForms|OData|WebAPI|XAFML|Selenium|EASYTEST|Kestrel|PublishSingleFile)$",
    r"T\d{7}",                  # KB ticket numbers: T1312589
    r"^SDK-",                   # project format strings
    r"^(TargetFramework|MultiTargeting|ConnectionString|LocalDB|MultipleActiveResultSets)$",
    r"^(Cross-IDE)$",
]

NON_TYPE_KEYWORDS = {
    "DI", "MDI", "SVG", "ARR", "AWS", "Kestrel", "OData", "WebAPI",
    "WebForms", "XAFML", "Selenium", "EASYTEST", "PublishSingleFile",
    "Cross-IDE",
}

def is_suspect(name: str) -> str | None:
    for pat in KNOWN_BAD_PATTERNS:
        if re.search(pat, name):
            return f"matches pattern /{pat}/"
    if name in NON_TYPE_KEYWORDS:
        return "known non-type keyword"
    return None

data = json.load(open("config/xaf-taxonomy.json", encoding="utf-8"))
hits = []
for concept in data["taxonomy"]["concepts"]:
    api = concept.get("api_surface", {})
    for pt in api.get("primary_types", []):
        reason = is_suspect(pt)
        if reason:
            hits.append((concept["id"], pt, reason))

if hits:
    print(f"SUSPECTED primary_types violations ({len(hits)}):")
    for cid, pt, reason in hits:
        print(f"  [{cid}]  '{pt}'  — {reason}")
else:
    print("No obvious violations found in primary_types.")
