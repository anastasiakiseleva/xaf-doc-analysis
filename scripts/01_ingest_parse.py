# scripts/01_ingest_parse.py
import re, pathlib, json, sys, argparse
import pandas as pd
from markdown_it import MarkdownIt
from bs4 import BeautifulSoup
from typing import List, Dict, Any
from markdown_it import MarkdownIt
md = MarkdownIt("commonmark")

# Add parent directory to path for imports
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from utils.pipeline_validators import (
    PipelineValidator, ValidationReport, ValidationResult, 
    save_validation_report, load_validation_thresholds
)

# ============================================================================
# Include Resolution
# ============================================================================

# Global template lookup (populated in main())
_TEMPLATE_LOOKUP: Dict[str, str] = {}

# Pattern: [!include[optional label](path)] or [!includeShorthand]
# DocFX forms:
#   [!include[label](~/templates/foo.md)]
#   [!includeMySnippetName]
#   [!include<code or xref>]  (these we skip)
_INCLUDE_WITH_PATH_RE = re.compile(
    r'\[!include[^\]]*\]\(([^)]+)\)', re.IGNORECASE
)
_INCLUDE_SHORTHAND_RE = re.compile(
    r'\[!include([A-Za-z0-9_.\-]+)\]', re.IGNORECASE
)


def build_template_lookup(templates_dir: pathlib.Path) -> Dict[str, str]:
    """
    Build a lookup dict from template filename (without extension, case-insensitive)
    to its content.
    """
    lookup = {}
    if not templates_dir.exists():
        return lookup
    for f in templates_dir.rglob('*.md'):
        content = f.read_text(encoding='utf-8', errors='ignore').strip()
        # Key by filename without extension (lowercase for case-insensitive match)
        key = f.stem.lower()
        lookup[key] = content
    return lookup


def resolve_includes(text: str) -> str:
    """
    Resolve [!include] directives in markdown text using the global template lookup.
    
    Handles:
      1. [!include[label](~/templates/foo.md)] -> content of foo.md
      2. [!includeMySnippet] -> content of mysnippet.md (by filename match)
    
    Skips [!include<...>] (code/xref references).
    """
    if not _TEMPLATE_LOOKUP or '[!include' not in text.lower():
        return text
    
    # First pass: resolve path-based includes [!include[label](path)]
    def replace_path_include(match):
        full = match.group(0)
        path_str = match.group(1).strip()
        # Extract filename from path like ~/templates/foo.md
        fname = pathlib.PurePosixPath(path_str).stem.lower()
        if fname in _TEMPLATE_LOOKUP:
            return _TEMPLATE_LOOKUP[fname]
        return full  # keep original if not found
    
    text = _INCLUDE_WITH_PATH_RE.sub(replace_path_include, text)
    
    # Second pass: resolve shorthand includes [!includeMySnippet]
    def replace_shorthand_include(match):
        full = match.group(0)
        name = match.group(1).strip().lower()
        if name in _TEMPLATE_LOOKUP:
            return _TEMPLATE_LOOKUP[name]
        return full  # keep original if not found
    
    text = _INCLUDE_SHORTHAND_RE.sub(replace_shorthand_include, text)
    
    return text


def parse_markdown(path: pathlib.Path) -> Dict[str, Any]:
    """
    Parse a Markdown document into a normalized structure for XAF doc analysis.

    - Extracts page UID (front matter or 'uid:' line).
    - Extracts internal links of both forms:
        1) [text](xref:UID)
        2) <xref:UID>
      where UID may contain dots, colons, backticks for generics, etc.
    - Builds sections, headings, and collects first code block per section.
    """

    # ---------- Regex helpers ----------
    FRONT_MATTER_RE = re.compile(r"(?s)^---\s*(.*?)\s*---")
    UID_LINE_RE     = re.compile(r'(?im)^\s*uid\s*:\s*"?([A-Za-z0-9._:\-`]+)"?\s*$')

    # Strip fenced code blocks (``` or ~~~) to avoid harvesting from samples
    FENCE_RE = re.compile(
        r"(^|\n)(```|~~~)[^\n]*\n.*?\n[ \t]*\2[ \t]*\n",  # open line → body → matching closing fence
        re.DOTALL,
    )

    # 1) Markdown link form: [text](xref:UID[?params][#anchor] "optional title")
    #    Capture until a space, closing paren or quote starts a title.
    XREF_MD_RE      = re.compile(r"\]\(\s*xref:([^) \t\"'>]+)", re.IGNORECASE)

    # 2) Angle form: <xref:UID[?params][#anchor]>
    XREF_ANGLE_RE   = re.compile(r"<\s*xref:([^>\s]+)\s*>", re.IGNORECASE)
    
    # NEW: <xref uid="My.Uid">...</xref>  or <xref uid="My.Uid" />
    XREF_TAG_UID_ATTR_RE = re.compile(r"<\s*xref\b[^>]*\buid\s*=\s*['\"]([^'\"\s]+)['\"][^>]*>", re.IGNORECASE)

    # NEW: <a href="xref:My.Uid">text</a>
    HTML_HREF_XREF_RE    = re.compile(r"<\s*a\b[^>]*\bhref\s*=\s*['\"]\s*xref:([^'\" >#?]+)", re.IGNORECASE)

    def extract_uid(text: str) -> str | None:
        m = FRONT_MATTER_RE.search(text or "")
        if m:
            fm = m.group(1)
            m_uid = UID_LINE_RE.search(fm or "")
            if m_uid:
                return m_uid.group(1)
        m2 = UID_LINE_RE.search(text or "")
        return m2.group(1) if m2 else None

    def extract_type_from_frontmatter(text: str) -> str | None:
        """Extract 'type' field from YAML frontmatter"""
        m = FRONT_MATTER_RE.search(text or "")
        if m:
            fm = m.group(1)
            type_match = re.search(r'(?im)^\s*type\s*:\s*(\w+)\s*$', fm)
            if type_match:
                return type_match.group(1)
        return None

    def strip_code_fences(raw: str) -> str:
        return FENCE_RE.sub("\n", raw or "")

    def normalize_uid(u: str) -> str:
        r"""
        Normalize a captured xref target:
        - Remove query/anchor (?..., #...)
        - Unescape backslash-escaped backticks:  \`1  ->  `1
        - Trim surrounding punctuation/whitespace
        """
        if not u:
            return u
        u = re.split(r"[?#]", u, maxsplit=1)[0]
        u = u.replace(r"\`", "`")   # ← this line is fine already
        return u.strip()

    def extract_xrefs_from_text(raw: str) -> list[str]:
        text_wo_code = strip_code_fences(raw or "")
        u1 = [normalize_uid(m) for m in XREF_MD_RE.findall(text_wo_code)]
        u2 = [normalize_uid(m) for m in XREF_ANGLE_RE.findall(text_wo_code)]
        u3 = [normalize_uid(m) for m in XREF_TAG_UID_ATTR_RE.findall(text_wo_code)]
        u4 = [normalize_uid(m) for m in HTML_HREF_XREF_RE.findall(text_wo_code)]
        return [u for u in (u1 + u2 + u3 + u4) if u]

    # ---------- Read & tokenize ----------
    text = path.read_text(encoding="utf-8", errors="ignore")
    text = resolve_includes(text)
    tokens = md.parse(text)

    page_uid = extract_uid(text)

    title: str | None = None
    headings: List[Dict[str, Any]] = []
    sections: List[Dict[str, Any]] = []
    collected_uids: List[str] = []
    current = {"h_path": [], "text": [], "code_blocks": []}

    def flush_section():
        if current["text"] or current["code_blocks"]:
            sections.append(
                {
                    "section_id": f"{path.stem}::{len(sections) + 1}",
                    "h_path": current["h_path"].copy(),
                    "text": "\n".join(current["text"]).strip(),
                    "code_blocks": current["code_blocks"].copy(),
                }
            )
        current["text"].clear()
        current["code_blocks"].clear()

    for i, t in enumerate(tokens):
        if t.type == "heading_open":
            flush_section()

        elif t.type == "inline" and t.map and i > 0 and tokens[i - 1].type == "heading_open":
            prev = tokens[i - 1]
            txt = "".join([c.content for c in (t.children or []) if c.type == "text"])
            if prev.tag == "h1" and not title:
                title = txt
            lvl = int(prev.tag[1])
            headings.append({"level": lvl, "text": txt})
            current["h_path"] = [h["text"] for h in headings if 2 <= h["level"] <= lvl]

        elif t.type == "fence":
            current["code_blocks"].append(t.content)

        elif t.type == "inline":
            # Token-based capture if markdown-it populates link_open → href
            for c in t.children or []:
                if c.type == "link_open":
                    attrs = c.attrs or []
                    href = next((a[1] for a in attrs if a[0] == "href"), None)
                    if href and href.lower().startswith("xref:"):
                        uid = normalize_uid(href.split(":", 1)[1])
                        if uid:
                            collected_uids.append(uid)

            current["text"].append(
                "".join([c.content for c in (t.children or []) if c.type == "text"])
            )

    flush_section()

    # Regex fallbacks over raw text (handles <xref:...> and tricky cases)
    regex_uids = extract_xrefs_from_text(text)

    # Merge + de-duplicate
    internal_links = sorted({*collected_uids, *regex_uids})
    
    # Extract document type from frontmatter
    doc_type = extract_type_from_frontmatter(text)

    return {
        "doc_id": str(path.with_suffix("")).replace("\\", "/"),
        "path": str(path),
        "uid": page_uid,
        "title": title or path.stem,
        "headings": headings,
        "sections": sections,
        "internal_links": internal_links,  # list of UIDs (from xref:UID)
        "word_count": sum(len(s["text"].split()) for s in sections),
        "doc_type": doc_type,  # Type from frontmatter (e.g., Field, Class, etc.)
    }


def validate_phase1_output(df: pd.DataFrame, run_quality_checks: bool = False) -> ValidationReport:
    """
    Validate Phase 1 output data.
    
    Args:
        df: The topics_inventory DataFrame
        run_quality_checks: Whether to run deeper quality validation
    
    Returns:
        ValidationReport with validation results
    """
    config_path = pathlib.Path(__file__).parent.parent / "config" / "validation_thresholds.yml"
    validator = PipelineValidator(config_path)
    report = ValidationReport(phase_name="Ingest & Parse", phase_number=1)
    
    # Level 1: Quick Sanity Checks
    print("\n🔍 Running Level 1 validation (quick sanity checks)...")
    
    # Check schema
    required_cols = ["doc_id", "path", "uid", "title", "headings", "sections", "internal_links", "word_count", "doc_type"]
    column_types = {
        "doc_id": str,
        "path": str,
        "title": str,
        "headings": list,
        "sections": list,
        "internal_links": list,
        "word_count": int
    }
    report.add_result(validator.validate_schema(df, required_cols, column_types, "Schema validation"))
    
    # Check row count
    thresholds = load_validation_thresholds(config_path)
    min_docs = thresholds.get('phase1_ingest', {}).get('min_docs', 8000)
    report.add_result(validator.validate_row_count(df, min_rows=min_docs, check_name="Minimum documents"))
    
    # Check xref extraction
    has_links = df["internal_links"].apply(lambda x: isinstance(x, list) and len(x) > 0)
    docs_with_links = int(has_links.sum())
    min_links = thresholds.get('phase1_ingest', {}).get('min_docs_with_links', 1000)
    
    result = validator.validate_threshold(
        actual_value=docs_with_links,
        threshold_key='min_docs_with_links',
        phase_key='phase1_ingest',
        comparison='>=',
        check_name="Documents with xref links"
    )
    report.add_result(result)
    
    # Check average word count
    avg_words = df["word_count"].mean()
    report.add_result(validator.validate_threshold(
        actual_value=avg_words,
        threshold_key='min_avg_word_count',
        phase_key='phase1_ingest',
        comparison='>=',
        check_name="Average word count"
    ))
    
    if run_quality_checks:
        print("\n🔍 Running Level 2 validation (quality checks)...")
        
        # Check for section_id uniqueness
        all_section_ids = []
        for _, row in df.iterrows():
            sections = row['sections']
            if isinstance(sections, list):
                all_section_ids.extend([s.get('section_id', '') for s in sections])
        
        unique_sections = len(set(all_section_ids))
        total_sections = len(all_section_ids)
        
        if unique_sections < total_sections:
            report.add_result(ValidationResult(
                check_name="Section ID uniqueness",
                passed=False,
                message=f"Found {total_sections - unique_sections} duplicate section IDs",
                severity="error",
                details={"unique": unique_sections, "total": total_sections}
            ))
        else:
            report.add_result(ValidationResult(
                check_name="Section ID uniqueness",
                passed=True,
                message=f"All {total_sections:,} section IDs are unique",
                severity="info"
            ))
        
        # Check for empty text sections
        empty_text_count = 0
        total_section_count = 0
        for _, row in df.iterrows():
            sections = row['sections']
            if isinstance(sections, list):
                for section in sections:
                    total_section_count += 1
                    if not section.get('text', '').strip():
                        empty_text_count += 1
        
        empty_pct = (empty_text_count / total_section_count * 100) if total_section_count > 0 else 0
        max_empty = thresholds.get('phase1_ingest', {}).get('max_empty_text_sections', 0.10) * 100
        
        if empty_pct > max_empty:
            report.add_result(ValidationResult(
                check_name="Empty text sections",
                passed=False,
                message=f"{empty_pct:.1f}% sections have empty text (max: {max_empty:.1f}%)",
                severity="warning",
                details={"empty_count": empty_text_count, "total_sections": total_section_count}
            ))
        else:
            report.add_result(ValidationResult(
                check_name="Empty text sections",
                passed=True,
                message=f"Only {empty_pct:.1f}% sections have empty text (within threshold)",
                severity="info",
                details={"empty_count": empty_text_count, "total_sections": total_section_count}
            ))
        
        # Check internal links format
        invalid_links = 0
        total_links = 0
        for links in df['internal_links']:
            if isinstance(links, list):
                for link in links:
                    total_links += 1
                    if not isinstance(link, str) or not link.strip():
                        invalid_links += 1
        
        if invalid_links > 0:
            report.add_result(ValidationResult(
                check_name="Internal links format",
                passed=False,
                message=f"Found {invalid_links} invalid links out of {total_links:,}",
                severity="warning",
                details={"invalid": invalid_links, "total": total_links}
            ))
        else:
            report.add_result(ValidationResult(
                check_name="Internal links format",
                passed=True,
                message=f"All {total_links:,} internal links are properly formatted",
                severity="info"
            ))
    
    return report


def main():
    parser = argparse.ArgumentParser(description="Phase 1: Ingest and parse markdown documents")
    parser.add_argument('--skip-validation', action='store_true', help='Skip validation checks')
    parser.add_argument('--validate-quality', action='store_true', help='Run deeper quality validation (Level 2)')
    parser.add_argument('--save-report', action='store_true', help='Save validation report to JSON')
    parser.add_argument('--include-enum-fields', action='store_true', help='Include enum/field/constant documents (excluded by default)')
    args = parser.parse_args()
    
    print("="*70)
    print("Phase 1: Ingest & Parse")
    print("="*70)
    
    files = list(pathlib.Path('data/raw_md').rglob('*.md'))
    
    # Load templates for include resolution
    global _TEMPLATE_LOOKUP
    templates_dir = pathlib.Path('data/raw_md/templates')
    _TEMPLATE_LOOKUP = build_template_lookup(templates_dir)
    if _TEMPLATE_LOOKUP:
        print(f"📎 Loaded {len(_TEMPLATE_LOOKUP)} templates for include resolution")
    
    # Exclude template files from the document corpus
    files = [f for f in files if not str(f).replace('\\', '/').startswith('data/raw_md/templates')]
    
    print(f"\n📁 Found {len(files):,} markdown files")

    if len(files) == 0:
        print("\n❌ No input Markdown files found under data/raw_md/")
        print("   Add your documentation corpus under data/raw_md/ (subfolders preserved), then rerun.")
        print("   Example: data/raw_md/articles/... and data/raw_md/apidoc/...")
        sys.exit(1)
    
    print("🔄 Parsing documents...")
    rows  = [parse_markdown(p) for p in files]
    df_all = pd.DataFrame(rows)

    # Ensure expected columns exist (defensive; helps avoid crashes if upstream parsing changes)
    if 'doc_type' not in df_all.columns:
        df_all['doc_type'] = None
    
    # Filter out enum/field/constant documents unless explicitly requested
    if not args.include_enum_fields:
        field_docs = df_all[df_all['doc_type'] == 'Field']
        df = df_all[df_all['doc_type'] != 'Field'].copy()
        print(f"\n🗑️  Filtered out {len(field_docs):,} enum/field/constant documents")
        
        # Save excluded documents report
        if len(field_docs) > 0:
            excluded_path = pathlib.Path('outputs/excluded_enum_fields.csv')
            field_docs[['doc_id', 'title', 'doc_type', 'word_count', 'uid']].to_csv(excluded_path, index=False)
            print(f"   └─ Excluded documents saved to: {excluded_path}")
    else:
        df = df_all
        print(f"\n⚠️  Including all documents (enum/field/constants not filtered)")
    
    # Identify hub/index pages (articles with 0 words and links only)
    hub_pages = df[
        (df['word_count'] == 0) & 
        (df['doc_id'].str.contains('/articles/')) &
        (df['internal_links'].apply(lambda x: len(x) > 0))
    ].copy()
    
    if len(hub_pages) > 0:
        hub_report_path = pathlib.Path('outputs/hub_pages_for_review.md')
        with open(hub_report_path, 'w', encoding='utf-8') as f:
            f.write("# Hub/Index Pages Requiring Manual Descriptions\n\n")
            f.write("These pages have zero words of content and only contain xref links.\n")
            f.write("They need manual descriptions to improve LLM training quality.\n\n")
            f.write(f"**Total:** {len(hub_pages)} pages\n\n")
            f.write("---\n\n")
            
            for _, row in hub_pages.sort_values('doc_id').iterrows():
                f.write(f"## {row['title']}\n\n")
                f.write(f"- **Doc ID:** `{row['doc_id']}`\n")
                f.write(f"- **UID:** `{row['uid']}`\n")
                f.write(f"- **Links:** {len(row['internal_links'])} xref links\n")
                f.write(f"- **File:** `{row['path']}`\n\n")
                f.write("**Action needed:** Add a 2-3 sentence description explaining what this section covers.\n\n")
                f.write("---\n\n")
        
        print(f"\n📋 Generated hub pages review report:")
        print(f"   └─ {hub_report_path}")
        print(f"   └─ Found {len(hub_pages)} hub/index pages needing manual descriptions")

    # --- quick diagnostics ---
    has_links = df["internal_links"].apply(lambda x: isinstance(x, list) and len(x) > 0)
    print(f"\n📊 Parsed {len(df):,} documents (after filtering)")
    print(f"   └─ Documents with xref links: {int(has_links.sum()):,}")
    print(f"   └─ Average word count: {df['word_count'].mean():.0f}")
    print(f"   └─ Total sections: {sum(len(row['sections']) for _, row in df.iterrows()):,}")

    pathlib.Path("outputs").mkdir(parents=True, exist_ok=True)
    output_path = pathlib.Path('outputs/topics_inventory.parquet')
    df.to_parquet(output_path, index=False, engine='pyarrow')
    print(f"\n💾 Saved to: {output_path}")
    
    # Run validation
    if not args.skip_validation:
        report = validate_phase1_output(df, run_quality_checks=args.validate_quality)
        report.print_summary()
        
        if args.save_report:
            report_path = pathlib.Path('outputs/validation_phase1.json')
            save_validation_report(report, report_path)
        
        if report.has_errors:
            print("\n❌ Phase 1 validation failed with errors. Review issues above.")
            sys.exit(1)
    else:
        print("\n⏭️  Validation skipped")
    
    print("\n✅ Phase 1 complete!")

if __name__ == "__main__":
    main()

    
def test_phase1_extracts_some_xrefs():
    import pandas as pd
    df = pd.read_parquet("outputs/topics_inventory.parquet", engine="pyarrow")
    assert df["internal_links"].apply(lambda x: isinstance(x, list) and len(x) > 0).sum() > 0
