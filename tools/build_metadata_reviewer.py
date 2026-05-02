#!/usr/bin/env python3
"""
Build a self-contained HTML metadata review tool.

Loads outputs/metadata_review.csv, deduplicates to doc level,
embeds data as JSON, and generates an interactive single-file HTML app
for personal review with approve / flag / skip workflow.
"""

import json
import re
from pathlib import Path

import pandas as pd

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT           = Path(__file__).resolve().parent.parent
CSV_PATH       = ROOT / "outputs" / "metadata_review.csv"
OUT_PATH       = ROOT / "outputs" / "metadata_reviewer.html"
LLM_CACHE_PATH = ROOT / "outputs" / "article_descriptions.parquet"


def _load_llm_cache() -> dict[str, str]:
    if LLM_CACHE_PATH.exists():
        try:
            df = pd.read_parquet(LLM_CACHE_PATH)
            cache = dict(zip(df['doc_id'], df['description']))
            print(f"  LLM description cache: {len(cache)} entries")
            return cache
        except Exception as e:
            print(f"  Warning: could not load LLM cache: {e}")
    return {}


# ---------------------------------------------------------------------------
# Description extraction from raw markdown
# ---------------------------------------------------------------------------

# Inline markdown cleaners applied in order
_MD_CLEANUP = [
    (re.compile(r'```[\s\S]*?```'), ''),                        # code blocks
    (re.compile(r'\[!\w+\]'), ''),                              # admonition markers
    (re.compile(r'\[\]\([^)]+\)'), ''),                         # empty-text links  [](...)
    (re.compile(r'@[\w.`<>]+'), ''),                            # @DevExpress.Xyz bare xrefs
    (re.compile(r'\[([^\]]+)\]\([^)]+\)'), r'\1'),              # keep link text
    (re.compile(r'<xref:[^>]+>'), ''),                          # <xref:...> tags
    (re.compile(r'<[^>]+>'), ''),                               # HTML tags
    (re.compile(r'`[^`]+`'), ''),                               # inline code
    (re.compile(r'\*\*([^*]+)\*\*'), r'\1'),                    # bold
    (re.compile(r'\*([^*]+)\*'), r'\1'),                        # italic
]

# Matches sentences where the author explicitly describes the document's purpose
_PURPOSE_RE = re.compile(
    r'(?:^|(?<=[.!?])\s+)'
    r'((?:This|The following)\s+(?:article|topic|guide|example|section|page|document|tutorial|reference)\b'
    r'[^.!?]{20,}[.!?])',
    re.IGNORECASE,
)


def _clean_inline(text: str) -> str:
    """Apply inline markdown cleanup and collapse whitespace."""
    for pattern, repl in _MD_CLEANUP:
        text = pattern.sub(repl, text)
    # Remove leftover punctuation artifacts like ", and" or "( )"
    text = re.sub(r'\(\s*\)', '', text)
    text = re.sub(r',\s*,', ',', text)
    text = re.sub(r'\s{2,}', ' ', text)
    return text.strip()


def _trim(text: str, max_chars: int = 160) -> str:
    """Trim to max_chars at a word boundary, append ellipsis if trimmed."""
    if len(text) <= max_chars:
        return text
    trimmed = text[:max_chars - 3].rsplit(' ', 1)[0]
    return trimmed.rstrip(',:;') + '...'


def _parse_md(raw: str) -> tuple[list[str], list[str]]:
    """
    Parse raw markdown (post-frontmatter) into:
      paragraphs: list of paragraph strings (first 5)
      h2s: list of h2 heading strings
    """
    paragraphs: list[str] = []
    h2s: list[str] = []
    current: list[str] = []
    in_code = False
    skipped_h1 = False

    for line in raw.splitlines():
        stripped = line.strip()
        if stripped.startswith('```'):
            in_code = not in_code
            if current:
                paragraphs.append(' '.join(current))
                current = []
            continue
        if in_code:
            continue
        if stripped.startswith('## '):
            h2s.append(stripped.lstrip('# ').strip())
            if current:
                paragraphs.append(' '.join(current))
                current = []
            continue
        if stripped.startswith('#'):
            if current:
                paragraphs.append(' '.join(current))
                current = []
            skipped_h1 = True
            continue
        if not skipped_h1:
            continue
        if stripped:
            current.append(stripped)
        elif current:
            paragraphs.append(' '.join(current))
            current = []
        if len(paragraphs) >= 5:
            break

    if current:
        paragraphs.append(' '.join(current))

    return paragraphs, h2s


def _slug_to_title(slug: str) -> str:
    """Convert a URL slug into a readable phrase."""
    # Remove leading "how-to-" for verb-first phrasing
    return slug.replace('-', ' ')


def article_description_from_md(doc_id: str) -> str:
    """
    Generate a metadata description for an article — not a quote from it.

    Strategy (in priority order):
    1. Purpose sentence: the author's own "This article explains/covers/demonstrates..."
    2. H2 synthesis: "Covers X, Y, and Z." built from section headings + title context
    3. First-paragraph best sentence: longest clean sentence ≥ 60 chars
    4. Empty string (let reviewer fill in manually)
    """
    md_path = ROOT / (doc_id.lstrip('/') + '.md')
    if not md_path.exists():
        return ''
    try:
        raw = md_path.read_text(encoding='utf-8', errors='ignore')
    except OSError:
        return ''

    # Strip YAML frontmatter
    if raw.startswith('---'):
        end = raw.find('\n---', 3)
        raw = raw[end + 4:].lstrip() if end != -1 else raw

    paragraphs, h2s = _parse_md(raw)

    # ── Tier 1: purpose sentence ─────────────────────────────────────────────
    search_text = ' '.join(paragraphs[:3])
    m = _PURPOSE_RE.search(search_text)
    if m:
        candidate = _clean_inline(m.group(1).strip())
        # Reject if still contains unfixable artifacts (bare @, empty parens)
        if len(candidate) >= 50 and '@' not in candidate:
            if not candidate.endswith(('.', '!', '?')):
                candidate += '.'
            return _trim(candidate)

    # ── Tier 2: h2 synthesis ─────────────────────────────────────────────────
    if h2s:
        # Clean h2 text and take the 2-3 most informative (skip generic ones)
        _SKIP_H2 = re.compile(
            r'^(prerequisites?|see also|overview|introduction|remarks?|notes?|example)$',
            re.IGNORECASE,
        )
        useful = [_clean_inline(h) for h in h2s if not _SKIP_H2.match(h.strip())]
        if len(useful) >= 2:
            slug = doc_id.rstrip('/').split('/')[-1]
            if slug.startswith('how-to-'):
                # how-to articles: rephrase as "Learn how to X. Covers Y and Z."
                action = _slug_to_title(slug[len('how-to-'):])
                topics = useful[:2]
                desc = f"Learn how to {action}."
                if len(desc) + len(topics[0]) + 10 <= 160:
                    desc += f" Covers {topics[0].lower()}"
                    if len(topics) > 1 and len(desc) + len(topics[1]) + 6 <= 160:
                        desc += f" and {topics[1].lower()}"
                    desc = desc.rstrip('.') + '.'
            else:
                # Concept/reference articles: "Covers X, Y, and Z."
                parts = useful[:3]
                if len(parts) == 1:
                    desc = f"Covers {parts[0].lower()}."
                elif len(parts) == 2:
                    desc = f"Covers {parts[0].lower()} and {parts[1].lower()}."
                else:
                    desc = f"Covers {parts[0].lower()}, {parts[1].lower()}, and {parts[2].lower()}."
            return _trim(desc)

    # ── Tier 3: first-paragraph best sentence ────────────────────────────────
    if paragraphs:
        para = _clean_inline(paragraphs[0])
        sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', para) if s.strip()]
        # Prefer a sentence that is descriptive (≥60 chars, not a bullet/list intro)
        for sent in sentences:
            if len(sent) >= 60 and not sent.endswith(':'):
                if not sent.endswith(('.', '!', '?')):
                    sent += '.'
                return _trim(sent)

    return ''


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def _normalize_list_col(val) -> str:
    """Convert parquet list/array/string column value to a comma-joined string."""
    if val is None:
        return ""
    try:
        if isinstance(val, float) and pd.isna(val):
            return ""
    except Exception:
        pass
    if isinstance(val, (list, tuple)):
        return ", ".join(str(v) for v in val if v)
    try:
        import numpy as np  # noqa: PLC0415
        if isinstance(val, np.ndarray):
            return ", ".join(str(v) for v in val if v)
    except ImportError:
        pass
    s = str(val).strip()
    if s.startswith("["):
        import ast  # noqa: PLC0415
        try:
            items = ast.literal_eval(s)
            return ", ".join(str(i) for i in items if i)
        except Exception:
            pass
    return s if s not in ("nan", "None", "") else ""


def load_data():
    # ── Helpers ──────────────────────────────────────────────────────────────
    def _join_unique(vals) -> str:
        result: set = set()
        for v in vals:
            for part in _normalize_list_col(v).split(","):
                p = part.strip()
                if p:
                    result.add(p)
        return ", ".join(sorted(result))

    def _phase7_desc(series) -> str:
        for v in series:
            if pd.notna(v) and str(v).strip():
                return str(v).strip()
        return ""

    def _most_common(series) -> str:
        mode = series.mode()
        return mode.iloc[0] if len(mode) else ""

    def _max_val(series) -> int:
        return int(series.max()) if len(series) else 0

    # ── Primary: document_metadata.parquet (Phase 10 rolled-up) ─────────────
    dm_path = ROOT / "outputs" / "document_metadata.parquet"
    if dm_path.exists():
        dm = pd.read_parquet(dm_path)
        if "is_api_reference" in dm.columns and "is_api" not in dm.columns:
            dm = dm.rename(columns={"is_api_reference": "is_api"})
        for col, default in [
            ("tags", ""), ("description", ""), ("proficiency_level", ""),
            ("total_connections", 0), ("num_sections", 1),
            ("concepts", ""), ("platforms", ""), ("apis", ""),
        ]:
            if col not in dm.columns:
                dm[col] = default
    else:
        # Fallback: aggregate from Phase 7 CSV
        df = pd.read_csv(CSV_PATH)
        dm = (
            df.groupby("doc_id", sort=False)
            .agg(
                is_api=("is_api", "first"),
                tags=("suggested_tags", _join_unique),
                description=("suggested_description", _phase7_desc),
                proficiency_level=("proficiency_level", _most_common),
                total_connections=("num_semantic_connections", _max_val),
                concepts=("original_concepts", _join_unique),
                platforms=("original_platforms", _join_unique),
            )
            .reset_index()
        )
        dm["num_sections"] = 1
        dm["apis"] = ""

    # ── Concept domains via taxonomy index (from doc concepts list) ───────────
    doc_domains: dict[str, str] = {}
    try:
        import sys as _sys  # noqa: PLC0415
        if str(ROOT) not in _sys.path:
            _sys.path.insert(0, str(ROOT))
        from utils.taxonomy_loader import load_taxonomy_index  # noqa: PLC0415
        _tax_index = load_taxonomy_index()
        for _, _row in dm.iterrows():
            _concepts_str = _normalize_list_col(_row.get("concepts", ""))
            _domains: set = set()
            for _cname in _concepts_str.split(","):
                _cname = _cname.strip()
                if _cname:
                    _domain = _tax_index.get(_cname, {}).get("domain", "")
                    if _domain:
                        _domains.add(_domain)
            doc_domains[_row["doc_id"]] = ", ".join(sorted(_domains))
    except Exception as e:
        print(f"  Warning: could not load concept domains: {e}")

    # ── Per-doc relationship summary (prefer corrected pairs) ──────────────────
    rel_summary: dict[str, dict] = {}
    cp_path = ROOT / "outputs" / "classified_pairs_corrected.parquet"
    if not cp_path.exists():
        cp_path = ROOT / "outputs" / "classified_pairs.parquet"
    if cp_path.exists():
        try:
            from collections import Counter  # noqa: PLC0415
            cp = pd.read_parquet(cp_path, columns=["source_doc", "target_doc", "relationship_type"])
            _rel_cnts: dict[str, Counter] = {}
            for row in cp.itertuples(index=False):
                for doc in (row.source_doc, row.target_doc):
                    if doc not in _rel_cnts:
                        _rel_cnts[doc] = Counter()
                    _rel_cnts[doc][str(row.relationship_type)] += 1
            rel_summary = {k: dict(v) for k, v in _rel_cnts.items()}
        except Exception as e:
            print(f"  Warning: could not load relationship summary: {e}")

    # ── Per-doc related-docs index from metadata_suggestions related_sections ──
    related_docs_index: dict[str, list] = {}
    ms_path = ROOT / "outputs" / "metadata_suggestions.parquet"
    if ms_path.exists():
        try:
            ms = pd.read_parquet(ms_path, columns=["doc_id", "related_sections"])
            _best: dict[str, dict] = {}  # src_doc -> {tgt_doc -> best entry}
            for _, _row in ms.iterrows():
                _src = _row["doc_id"]
                _rels = _row.get("related_sections", [])
                if not hasattr(_rels, "__len__") or len(_rels) == 0:
                    continue
                if _src not in _best:
                    _best[_src] = {}
                for _item in _rels:
                    _tgt = _item.get("doc_id", "")
                    if not _tgt or _tgt == _src:
                        continue
                    _conf = float(_item.get("confidence", 0.0))
                    _rel  = _item.get("relationship", "related_to")
                    _dir  = _item.get("direction", "outgoing")
                    _prev = _best[_src].get(_tgt)
                    if _prev is None or _conf > _prev["confidence"]:
                        _best[_src][_tgt] = {
                            "doc_id":       _tgt,
                            "slug":         _tgt.rstrip("/").split("/")[-1],
                            "relationship": _rel,
                            "direction":    _dir,
                            "confidence":   _conf,
                        }
            for _src, _tgt_map in _best.items():
                related_docs_index[_src] = sorted(
                    _tgt_map.values(), key=lambda x: x["confidence"], reverse=True
                )[:8]
            print(f"  Related-docs index: {len(related_docs_index)} source docs")
        except Exception as e:
            print(f"  Warning: could not build related_docs index: {e}")

    # Metadata descriptions are only relevant for articles, not API reference docs
    if "is_api" in dm.columns:
        dm = dm[dm["is_api"] != True].copy()
    total = len(dm)
    llm_cache = _load_llm_cache()
    print(f"Building descriptions for {total} article docs (API docs excluded)...")
    llm_hits = heuristic_hits = 0

    records = []
    for _, row in dm.iterrows():
        doc_id = row["doc_id"]
        slug   = doc_id.rstrip("/").split("/")[-1]
        is_api = bool(row.get("is_api", False))

        # Description priority: LLM cache > heuristic markdown > parquet value
        if not is_api:
            if doc_id in llm_cache:
                description = llm_cache[doc_id]
                llm_hits += 1
            else:
                md_desc = article_description_from_md(doc_id)
                if md_desc:
                    description = md_desc
                    heuristic_hits += 1
                else:
                    description = str(row.get("description", "") or "")
        else:
            description = str(row.get("description", "") or "")

        records.append({
            "id":          doc_id,
            "slug":        slug,
            "is_api":      is_api,
            "tags":        _normalize_list_col(row.get("tags", "")),
            "description": description,
            "proficiency": str(row.get("proficiency_level", "") or ""),
            "connections": int(row.get("total_connections", 0) or 0),
            "num_sections": int(row.get("num_sections", 1) or 1),
            "concepts":    _normalize_list_col(row.get("concepts", "")),
            "platforms":   _normalize_list_col(row.get("platforms", "")),
            "apis":        _normalize_list_col(row.get("apis", "")),
            "domains":        doc_domains.get(doc_id, ""),
            "rel_summary":    rel_summary.get(doc_id, {}),
            "related_docs":   related_docs_index.get(doc_id, []),
            "classified_conns": sum(rel_summary.get(doc_id, {}).values()),
            "dominant_rel":   max(rel_summary.get(doc_id, {}), key=rel_summary.get(doc_id, {}).get) if rel_summary.get(doc_id) else "",
        })

    article_count = sum(1 for r in records if not r["is_api"])
    fallback = article_count - llm_hits - heuristic_hits
    print(f"Loaded {len(records)} unique docs from {total} rows")
    print(f"  LLM (cache):      {llm_hits}/{article_count}")
    print(f"  Heuristic (md):   {heuristic_hits}/{article_count}")
    print(f"  Phase 7 fallback: {fallback}/{article_count}")
    return records


# ---------------------------------------------------------------------------
# HTML template
# ---------------------------------------------------------------------------
HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>XAF Doc Metadata Reviewer</title>
<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: Segoe UI, Arial, sans-serif; font-size: 13px; background: #1e1e2e; color: #cdd6f4; height: 100vh; display: flex; flex-direction: column; overflow: hidden; }

/* ---- top bar ---- */
#topbar { flex: 0 0 auto; display: flex; align-items: center; gap: 10px; padding: 6px 12px; background: #181825; border-bottom: 1px solid #313244; }
#topbar h1 { font-size: 14px; font-weight: 600; color: #cba6f7; white-space: nowrap; }
#topbar .sep { flex: 1; }
#progress-bar { display: flex; align-items: center; gap: 8px; font-size: 12px; }
#prog-approved { color: #a6e3a1; }
#prog-flagged  { color: #f38ba8; }
#prog-skip     { color: #fab387; }
#prog-total    { color: #6c7086; }
button.action { padding: 4px 10px; border: none; border-radius: 4px; cursor: pointer; font-size: 12px; font-weight: 600; }
#btn-export { background: #cba6f7; color: #1e1e2e; }
#btn-clear  { background: #313244; color: #cdd6f4; }

/* ---- main layout ---- */
#main { flex: 1 1 auto; display: flex; overflow: hidden; }

/* ---- left list panel ---- */
#list-panel { width: 320px; flex: 0 0 320px; display: flex; flex-direction: column; border-right: 1px solid #313244; overflow: hidden; }
#filters { flex: 0 0 auto; padding: 8px; display: flex; flex-direction: column; gap: 6px; border-bottom: 1px solid #313244; }
#search-input { width: 100%; padding: 5px 8px; background: #313244; border: 1px solid #45475a; border-radius: 4px; color: #cdd6f4; font-size: 12px; }
#search-input::placeholder { color: #6c7086; }
.filter-row { display: flex; gap: 5px; flex-wrap: wrap; }
.filter-row select, .filter-row button.fbtn { background: #313244; color: #cdd6f4; border: 1px solid #45475a; border-radius: 4px; padding: 3px 7px; font-size: 11px; cursor: pointer; }
.filter-row button.fbtn.active { border-color: #cba6f7; color: #cba6f7; }
#list-count { font-size: 11px; color: #6c7086; padding: 4px 8px; flex: 0 0 auto; }

#doclist { flex: 1 1 auto; overflow-y: auto; }
.doc-item { padding: 7px 10px; border-bottom: 1px solid #1e1e2e; cursor: pointer; display: flex; align-items: flex-start; gap: 6px; }
.doc-item:hover { background: #313244; }
.doc-item.selected { background: #45475a; }
.doc-item .badge { flex: 0 0 auto; margin-top: 1px; font-size: 10px; padding: 1px 5px; border-radius: 3px; font-weight: 700; }
.badge.api  { background: #89b4fa; color: #1e1e2e; }
.badge.art  { background: #a6e3a1; color: #1e1e2e; }
.doc-item .item-text { flex: 1 1 auto; min-width: 0; }
.item-slug { font-weight: 600; font-size: 12px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.item-path { font-size: 10px; color: #6c7086; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.doc-item .status-dot { flex: 0 0 auto; width: 8px; height: 8px; border-radius: 50%; margin-top: 4px; }
.dot-approved { background: #a6e3a1; }
.dot-flagged  { background: #f38ba8; }
.dot-skip     { background: #fab387; }
.dot-none     { background: #313244; border: 1px solid #45475a; }

/* ---- right detail panel ---- */
#detail-panel { flex: 1 1 auto; display: flex; flex-direction: column; overflow: hidden; }
#detail-header { flex: 0 0 auto; padding: 10px 14px 6px; border-bottom: 1px solid #313244; }
#detail-header .doc-title { font-size: 15px; font-weight: 700; color: #89b4fa; }
#detail-header .doc-path  { font-size: 11px; color: #6c7086; margin-top: 2px; }
#detail-meta { flex: 0 0 auto; display: flex; gap: 10px; padding: 6px 14px; border-bottom: 1px solid #313244; align-items: center; flex-wrap: wrap; }
.meta-pill { font-size: 11px; padding: 2px 8px; border-radius: 10px; font-weight: 600; }
.pill-api  { background: #89b4fa22; color: #89b4fa; border: 1px solid #89b4fa55; }
.pill-art  { background: #a6e3a122; color: #a6e3a1; border: 1px solid #a6e3a155; }
.pill-beg  { background: #a6e3a122; color: #a6e3a1; border: 1px solid #a6e3a155; }
.pill-adv  { background: #fab38722; color: #fab387; border: 1px solid #fab38755; }
.pill-exp  { background: #f38ba822; color: #f38ba8; border: 1px solid #f38ba855; }
.pill-conn { background: #31324488; color: #6c7086; border: 1px solid #45475a; }

#detail-body { flex: 1 1 auto; display: flex; overflow: hidden; }
#yaml-panel { flex: 1 1 auto; display: flex; flex-direction: column; overflow: hidden; border-right: 1px solid #313244; }
#yaml-panel h3 { flex: 0 0 auto; font-size: 11px; text-transform: uppercase; letter-spacing: .08em; color: #6c7086; padding: 8px 12px 4px; }
#yaml-editor { flex: 1 1 auto; font-family: Cascadia Code, Consolas, monospace; font-size: 12px; background: #181825; color: #cdd6f4; border: none; outline: none; padding: 8px 12px; resize: none; width: 100%; line-height: 1.5; }

#info-panel { flex: 0 0 280px; display: flex; flex-direction: column; overflow: hidden; }
#info-panel h3 { flex: 0 0 auto; font-size: 11px; text-transform: uppercase; letter-spacing: .08em; color: #6c7086; padding: 8px 12px 4px; }
#info-body { flex: 1 1 auto; overflow-y: auto; padding: 4px 12px 12px; display: flex; flex-direction: column; gap: 10px; }
.info-section label { font-size: 10px; text-transform: uppercase; letter-spacing: .08em; color: #6c7086; display: block; margin-bottom: 3px; }
.info-section .tags-wrap { display: flex; flex-wrap: wrap; gap: 4px; }
.tag { font-size: 11px; padding: 2px 7px; border-radius: 3px; background: #313244; color: #cdd6f4; }
.info-section .concepts-text { font-size: 11px; color: #6c7086; line-height: 1.4; }
.info-section .plat-text { font-size: 11px; color: #89dceb; }
.rel-chip { display: inline-flex; align-items: center; font-size: 10px; padding: 1px 6px; border-radius: 3px; margin: 2px; font-weight: 600; }
/* ---- related docs list ---- */
#related-docs-list { list-style: none; display: flex; flex-direction: column; gap: 4px; }
.related-doc-item { font-size: 11px; display: flex; align-items: center; gap: 5px; padding: 3px 0; border-bottom: 1px solid #313244; }
.related-doc-item:last-child { border-bottom: none; }
.related-doc-slug { flex: 1; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; color: #89b4fa; font-weight: 600; }
.dir-out { font-size: 10px; color: #a6e3a1; flex: 0 0 auto; }
.dir-in  { font-size: 10px; color: #cba6f7; flex: 0 0 auto; }
.pill-rel { font-size: 10px; padding: 1px 5px; border-radius: 3px; font-weight: 600; flex: 0 0 auto; }

/* ---- verdict bar ---- */
#verdict-bar { flex: 0 0 auto; display: flex; gap: 8px; align-items: center; padding: 8px 14px; border-top: 1px solid #313244; background: #181825; }
#verdict-bar label { font-size: 11px; color: #6c7086; }
button.verdict { padding: 5px 18px; border: 2px solid transparent; border-radius: 5px; cursor: pointer; font-size: 13px; font-weight: 700; background: #313244; color: #cdd6f4; }
button.verdict:hover { filter: brightness(1.2); }
button.verdict.active-approved { background: #a6e3a122; border-color: #a6e3a1; color: #a6e3a1; }
button.verdict.active-flagged  { background: #f38ba822; border-color: #f38ba8; color: #f38ba8; }
button.verdict.active-skip     { background: #fab38722; border-color: #fab387; color: #fab387; }
#verdict-note { flex: 1 1 auto; padding: 4px 8px; background: #313244; border: 1px solid #45475a; border-radius: 4px; color: #cdd6f4; font-size: 12px; }
#verdict-note::placeholder { color: #6c7086; }
#nav-btns { margin-left: auto; display: flex; gap: 4px; }
button.nav { background: #313244; border: 1px solid #45475a; color: #cdd6f4; border-radius: 4px; padding: 4px 10px; cursor: pointer; font-size: 12px; }
button.nav:hover { background: #45475a; }

/* ---- empty state ---- */
#empty-state { flex: 1; display: flex; align-items: center; justify-content: center; color: #6c7086; font-size: 14px; }

::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #1e1e2e; }
::-webkit-scrollbar-thumb { background: #45475a; border-radius: 3px; }

/* ---- light theme ---- */
body.light { background: #f6f8fa; color: #24292f; }
body.light #topbar { background: #ffffff; border-bottom-color: #d0d7de; }
body.light #topbar h1 { color: #8250df; }
body.light #prog-approved { color: #1a7f37; }
body.light #prog-flagged  { color: #cf222e; }
body.light #prog-skip     { color: #953800; }
body.light #prog-total    { color: #8c959f; }
body.light #btn-export { background: #8250df; color: #fff; }
body.light #btn-clear  { background: #f6f8fa; color: #24292f; border: 1px solid #d0d7de; }
body.light #list-panel { border-right-color: #d0d7de; }
body.light #filters { border-bottom-color: #d0d7de; }
body.light #search-input { background: #ffffff; border-color: #d0d7de; color: #24292f; }
body.light #search-input::placeholder { color: #8c959f; }
body.light .filter-row select, body.light .filter-row button.fbtn { background: #f6f8fa; color: #24292f; border-color: #d0d7de; }
body.light .filter-row button.fbtn.active { border-color: #8250df; color: #8250df; }
body.light #list-count { color: #8c959f; }
body.light .doc-item { border-bottom-color: #f6f8fa; }
body.light .doc-item:hover { background: #eaeef2; }
body.light .doc-item.selected { background: #ddf4ff; }
body.light .badge.api  { background: #0969da; color: #fff; }
body.light .badge.art  { background: #1a7f37; color: #fff; }
body.light .item-path { color: #8c959f; }
body.light .dot-none     { background: #d0d7de; border-color: #8c959f; }
body.light #detail-header { border-bottom-color: #d0d7de; }
body.light #detail-header .doc-title { color: #0969da; }
body.light #detail-header .doc-path  { color: #8c959f; }
body.light #detail-meta { border-bottom-color: #d0d7de; }
body.light .pill-api  { background: #ddf4ff; color: #0969da; border-color: #0969da55; }
body.light .pill-art  { background: #dafbe1; color: #1a7f37; border-color: #1a7f3755; }
body.light .pill-beg  { background: #dafbe1; color: #1a7f37; border-color: #1a7f3755; }
body.light .pill-adv  { background: #fff8c5; color: #7d4e00; border-color: #7d4e0055; }
body.light .pill-exp  { background: #ffebe9; color: #cf222e; border-color: #cf222e55; }
body.light .pill-conn { background: #f6f8fa; color: #57606a; border-color: #d0d7de; }
body.light #yaml-panel { border-right-color: #d0d7de; }
body.light #yaml-panel h3 { color: #8c959f; }
body.light #yaml-editor { background: #ffffff; color: #24292f; }
body.light #info-panel h3 { color: #8c959f; }
body.light .info-section label { color: #8c959f; }
body.light .tag { background: #eaeef2; color: #24292f; }
body.light .info-section .concepts-text { color: #57606a; }
body.light .info-section .plat-text { color: #0550ae; }
body.light #verdict-bar { border-top-color: #d0d7de; background: #ffffff; }
body.light #verdict-bar label { color: #8c959f; }
body.light button.verdict { background: #f6f8fa; color: #24292f; border-color: #d0d7de; }
body.light button.verdict.active-approved { background: #dafbe1; border-color: #1a7f37; color: #1a7f37; }
body.light button.verdict.active-flagged  { background: #ffebe9; border-color: #cf222e; color: #cf222e; }
body.light button.verdict.active-skip     { background: #fff8c5; border-color: #7d4e00; color: #7d4e00; }
body.light #verdict-note { background: #ffffff; border-color: #d0d7de; color: #24292f; }
body.light #verdict-note::placeholder { color: #8c959f; }
body.light button.nav { background: #f6f8fa; border-color: #d0d7de; color: #24292f; }
body.light button.nav:hover { background: #eaeef2; }
body.light #empty-state { color: #8c959f; }
body.light .related-doc-item { border-bottom-color: #eaeef2; }
body.light .related-doc-slug { color: #0969da; }
body.light .dir-out { color: #1a7f37; }
body.light .dir-in  { color: #8250df; }
body.light ::-webkit-scrollbar-track { background: #f6f8fa; }
body.light ::-webkit-scrollbar-thumb { background: #d0d7de; }
</style>
</head>
<body>

<div id="topbar">
  <h1>XAF Doc Metadata Reviewer</h1>
  <div id="progress-bar">
    <span id="prog-approved">✓ 0 approved</span>
    <span id="prog-flagged">⚑ 0 flagged</span>
    <span id="prog-skip">→ 0 skipped</span>
    <span id="prog-total">/ __TOTAL__ docs</span>
  </div>
  <div class="sep"></div>
  <button class="action" id="btn-export">Export results ↓</button>
  <button class="action" id="btn-clear">Clear all</button>
  <button class="action" id="btn-theme" onclick="toggleTheme()" style="background:#313244;color:#cdd6f4;margin-left:4px">☀ Light</button>
</div>

<div id="main">
  <!-- List panel -->
  <div id="list-panel">
    <div id="filters">
      <input id="search-input" type="text" placeholder="Search slug or path…" autocomplete="off">
      <div class="filter-row">
        <select id="filter-type">
          <option value="all">All types</option>
          <option value="api">API Reference</option>
          <option value="article">Articles</option>
        </select>
        <select id="filter-proficiency">
          <option value="all">All levels</option>
          <option value="Beginner">Beginner</option>
          <option value="Advanced">Advanced</option>
          <option value="Expert">Expert</option>
        </select>
        <select id="filter-status">
          <option value="all">All statuses</option>
          <option value="none">Unreviewed</option>
          <option value="approved">Approved</option>
          <option value="flagged">Flagged</option>
          <option value="skip">Skipped</option>
        </select>
        <select id="filter-domain">
          <option value="all">All domains</option>
        </select>
        <select id="filter-tag">
          <option value="all">All tags</option>
        </select>
      </div>
      <div class="filter-row">
        <button class="fbtn" id="filter-has-desc" title="Only show docs with a description">Has description</button>
        <button class="fbtn" id="filter-no-desc" title="Only show docs without a description">No description</button>
        <button class="fbtn" id="filter-isolated" title="0 semantic connections">Isolated</button>
        <button class="fbtn" id="filter-connected" title=">10 connections">Well-connected</button>
        <button class="fbtn" id="filter-has-related" title="Has classified neighbours">Has related docs</button>
      </div>
    </div>
    <div id="list-count"></div>
    <div id="doclist"></div>
  </div>

  <!-- Detail panel -->
  <div id="detail-panel">
    <div id="empty-state">← Select a document to review</div>

    <div id="doc-view" style="display:none; flex:1; flex-direction:column; overflow:hidden;">
      <div id="detail-header">
        <div class="doc-title" id="dh-title"></div>
        <div class="doc-path"  id="dh-path"></div>
      </div>
      <div id="detail-meta">
        <span class="meta-pill" id="dm-type"></span>
        <span class="meta-pill" id="dm-prof"></span>
        <span class="meta-pill pill-conn" id="dm-conn"></span>
        <span class="meta-pill pill-conn" id="dm-classified" style="display:none"></span>
        <span class="meta-pill pill-conn" id="dm-sections" style="display:none"></span>
        <span class="meta-pill" id="dm-plat" style="background:#89dceb22;color:#89dceb;border:1px solid #89dceb55;"></span>
      </div>
      <div id="detail-body">
        <div id="yaml-panel">
          <h3>YAML front matter (editable)</h3>
          <textarea id="yaml-editor" spellcheck="false"></textarea>
        </div>
        <div id="info-panel">
          <h3>Source signals</h3>
          <div id="info-body">
            <div class="info-section" id="is-platforms">
              <label>Platforms</label>
              <div class="plat-text" id="is-plat-text"></div>
            </div>
            <div class="info-section">
              <label>Detected concepts</label>
              <div class="concepts-text" id="is-concepts"></div>
            </div>
            <div class="info-section">
              <label>Suggested tags</label>
              <div class="tags-wrap" id="is-tags"></div>
            </div>
            <div class="info-section" id="is-apis">
              <label>Related APIs</label>
              <div class="concepts-text" id="is-apis-text"></div>
            </div>
            <div class="info-section">
              <label>Relationships (Phase 6)</label>
              <div class="tags-wrap" id="is-rels-wrap"></div>
            </div>
            <div class="info-section" id="is-related-docs">
              <label>Related documents</label>
              <ul id="related-docs-list"></ul>
            </div>
          </div>
        </div>
      </div>
      <div id="verdict-bar">
        <label>Verdict:</label>
        <button class="verdict" id="btn-approve">✓ Approve</button>
        <button class="verdict" id="btn-flag">⚑ Flag</button>
        <button class="verdict" id="btn-skip">→ Skip</button>
        <input id="verdict-note" type="text" placeholder="Optional note…" maxlength="300">
        <div id="nav-btns">
          <button class="nav" id="btn-prev">‹ Prev</button>
          <button class="nav" id="btn-next">Next ›</button>
        </div>
      </div>
    </div>
  </div>
</div>

<script>
// ============================================================
// DATA
// ============================================================
const ALL_DOCS = __DATA__;

// ============================================================
// STATE
// ============================================================
const STORAGE_KEY = 'xaf_meta_review_v1';

function loadState() {
  try { return JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}'); }
  catch { return {}; }
}

function saveState() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
}

let state = loadState(); // { [doc_id]: { verdict, note, yaml } }
let filtered = [...ALL_DOCS];
let selectedIdx = -1;
let activeToggles = { hasDesc: false, noDesc: false, isolated: false, connected: false, hasRelated: false };

// ============================================================
// FILTER + RENDER LIST
// ============================================================
function applyFilters() {
  const q       = document.getElementById('search-input').value.toLowerCase();
  const type    = document.getElementById('filter-type').value;
  const prof    = document.getElementById('filter-proficiency').value;
  const status  = document.getElementById('filter-status').value;
  const domain  = document.getElementById('filter-domain').value;
  const tag     = document.getElementById('filter-tag').value;

  filtered = ALL_DOCS.filter(d => {
    if (q && !d.id.toLowerCase().includes(q) && !d.slug.toLowerCase().includes(q)) return false;
    if (type === 'api' && !d.is_api) return false;
    if (type === 'article' && d.is_api) return false;
    if (prof !== 'all' && d.proficiency !== prof) return false;
    const v = (state[d.id] || {}).verdict || 'none';
    if (status !== 'all' && v !== status) return false;
    if (domain !== 'all' && !(d.domains || '').split(',').map(s => s.trim()).includes(domain)) return false;
    if (tag !== 'all' && !(d.tags || '').split(',').map(s => s.trim()).includes(tag)) return false;
    if (activeToggles.hasDesc && !d.description) return false;
    if (activeToggles.noDesc && d.description) return false;
    if (activeToggles.isolated && d.connections !== 0) return false;
    if (activeToggles.connected && d.connections <= 10) return false;
    if (activeToggles.hasRelated && (!d.related_docs || d.related_docs.length === 0)) return false;
    return true;
  });

  renderList();
  updateProgress();
}

function renderList() {
  const list = document.getElementById('doclist');
  document.getElementById('list-count').textContent = `${filtered.length} docs`;

  list.innerHTML = filtered.map((d, i) => {
    const v = (state[d.id] || {}).verdict || 'none';
    const badge = d.is_api
      ? '<span class="badge api">API</span>'
      : '<span class="badge art">ART</span>';
    const dot = `<div class="status-dot dot-${v}"></div>`;
    const sel = (i === selectedIdx) ? ' selected' : '';
    return `<div class="doc-item${sel}" data-idx="${i}">
      ${dot}${badge}
      <div class="item-text">
        <div class="item-slug">${escHtml(d.slug)}</div>
        <div class="item-path">${escHtml(d.id)}</div>
      </div>
    </div>`;
  }).join('');

  list.querySelectorAll('.doc-item').forEach(el => {
    el.addEventListener('click', () => selectDoc(+el.dataset.idx));
  });
}

function updateProgress() {
  let approved = 0, flagged = 0, skip = 0;
  for (const v of Object.values(state)) {
    if (v.verdict === 'approved') approved++;
    else if (v.verdict === 'flagged') flagged++;
    else if (v.verdict === 'skip') skip++;
  }
  document.getElementById('prog-approved').textContent = `✓ ${approved} approved`;
  document.getElementById('prog-flagged').textContent  = `⚑ ${flagged} flagged`;
  document.getElementById('prog-skip').textContent     = `→ ${skip} skipped`;
}

// ============================================================
// DETAIL VIEW
// ============================================================
function selectDoc(idx) {
  if (selectedIdx >= 0 && selectedIdx < filtered.length) {
    // save yaml edits for previous doc
    const prev = filtered[selectedIdx];
    if (!state[prev.id]) state[prev.id] = {};
    state[prev.id].yaml = document.getElementById('yaml-editor').value;
    saveState();
  }

  selectedIdx = idx;
  renderList();

  const d = filtered[idx];
  if (!d) return;

  document.getElementById('empty-state').style.display = 'none';
  const view = document.getElementById('doc-view');
  view.style.display = 'flex';

  document.getElementById('dh-title').textContent = d.slug;
  document.getElementById('dh-path').textContent  = d.id;

  // meta pills
  const typeEl = document.getElementById('dm-type');
  typeEl.textContent = d.is_api ? 'API Reference' : 'Article';
  typeEl.className = 'meta-pill ' + (d.is_api ? 'pill-api' : 'pill-art');

  const profEl = document.getElementById('dm-prof');
  profEl.textContent = d.proficiency;
  const profCls = { Beginner: 'pill-beg', Advanced: 'pill-adv', Expert: 'pill-exp' };
  profEl.className = 'meta-pill ' + (profCls[d.proficiency] || '');

  document.getElementById('dm-conn').textContent = `${d.connections} connections`;

  const platEl = document.getElementById('dm-plat');
  platEl.textContent = d.platforms || 'All platforms';
  platEl.style.display = '';

  // info panel
  document.getElementById('is-plat-text').textContent = d.platforms || '—';
  document.getElementById('is-concepts').textContent  = d.concepts  || '—';

  const tagsWrap = document.getElementById('is-tags');
  tagsWrap.innerHTML = (d.tags || '').split(',').map(t => t.trim()).filter(Boolean)
    .map(t => `<span class="tag">${escHtml(t)}</span>`).join('');
  // Related APIs
  const apisEl = document.getElementById('is-apis');
  document.getElementById('is-apis-text').textContent = d.apis || '\u2014';
  apisEl.style.display = d.is_api ? 'none' : '';

  // Relationship summary
  const relsWrap = document.getElementById('is-rels-wrap');
  const relSummary = d.rel_summary || {};
  const relOrder = ['uses','explains','requires','extends','contrasts_with','applies_to','related_to'];
  const relColors = {uses:'#ef9a9a',explains:'#80cbc4',requires:'#f48fb1',extends:'#ce93d8',related_to:'#bdbdbd',contrasts_with:'#ffb74d',applies_to:'#a5d6a7'};
  const relEntries = relOrder.filter(r => relSummary[r]).map(r =>
    `<span class="rel-chip" style="background:${relColors[r]}22;color:${relColors[r]};border:1px solid ${relColors[r]}44">${r}\u00a0${relSummary[r]}</span>`
  );
  relsWrap.innerHTML = relEntries.join('') || '<span style="color:#6c7086;font-size:11px">None classified</span>';

  // Sections count pill
  const secEl = document.getElementById('dm-sections');
  if (d.num_sections) {
    secEl.textContent = `${d.num_sections} section${d.num_sections === 1 ? '' : 's'}`;
    secEl.style.display = '';
  } else { secEl.style.display = 'none'; }

  // Classified connections pill
  const classEl = document.getElementById('dm-classified');
  if (d.classified_conns > 0) {
    classEl.textContent = `${d.classified_conns} classified`;
    classEl.style.display = '';
  } else { classEl.style.display = 'none'; }

  // Related documents list
  const relDocsList = document.getElementById('related-docs-list');
  const relDocs = d.related_docs || [];
  const relDocColors = {uses:'#ef9a9a',explains:'#80cbc4',requires:'#f48fb1',extends:'#ce93d8',related_to:'#bdbdbd',contrasts_with:'#ffb74d',applies_to:'#a5d6a7'};
  if (relDocs.length) {
    relDocsList.innerHTML = relDocs.map(r => {
      const col = relDocColors[r.relationship] || '#888';
      const arrow = r.direction === 'outgoing'
        ? `<span class="dir-out">\u2192</span>`
        : `<span class="dir-in">\u2190</span>`;
      const chip = `<span class="pill-rel" style="background:${col}22;color:${col};border:1px solid ${col}44">${escHtml(r.relationship)}</span>`;
      return `<li class="related-doc-item">${arrow}${chip}<span class="related-doc-slug" title="${escHtml(r.doc_id)}">${escHtml(r.slug)}</span><span style="color:#6c7086;font-size:10px">${r.confidence.toFixed(2)}</span></li>`;
    }).join('');
  } else {
    relDocsList.innerHTML = '<li style="color:#6c7086;font-size:11px">None found</li>';
  }
  document.getElementById('is-related-docs').style.display = '';

  // YAML editor — use saved edit if any, else build from data
  const saved = state[d.id];
  const yaml  = (saved && saved.yaml) ? saved.yaml : buildYaml(d);
  document.getElementById('yaml-editor').value = yaml;

  // verdict buttons
  const verdict = (saved && saved.verdict) || 'none';
  setVerdictButtons(verdict);

  const note = (saved && saved.note) || '';
  document.getElementById('verdict-note').value = note;
}

function buildYaml(d) {
  const lines = ['---'];
  if (d.description) lines.push(`description: "${d.description.replace(/"/g, "'")}"`);
  else               lines.push('description: null');
  lines.push(`proficiencyLevel: ${d.proficiency}`);
  const tags = (d.tags || '').split(',').map(t => t.trim()).filter(Boolean);
  if (tags.length) {
    lines.push('tags:');
    tags.forEach(t => lines.push(`  - ${t}`));
  }
  if (d.platforms) {
    lines.push('# platforms (informational):');
    d.platforms.split(',').map(p => p.trim()).filter(Boolean)
      .forEach(p => lines.push(`#   - ${p}`));
  }
  lines.push('---');
  return lines.join('\n');
}

function setVerdictButtons(verdict) {
  ['approve','flag','skip'].forEach(v => {
    const btn = document.getElementById(`btn-${v}`);
    btn.className = 'verdict' + (verdict === (v === 'approve' ? 'approved' : v) ? ` active-${v === 'approve' ? 'approved' : v}` : '');
  });
}

function setVerdict(verdict) {
  if (selectedIdx < 0 || selectedIdx >= filtered.length) return;
  const d = filtered[selectedIdx];
  if (!state[d.id]) state[d.id] = {};
  const current = state[d.id].verdict;
  // toggle off if same
  if (current === verdict) verdict = 'none';
  state[d.id].verdict = verdict;
  state[d.id].note    = document.getElementById('verdict-note').value;
  state[d.id].yaml    = document.getElementById('yaml-editor').value;
  saveState();
  setVerdictButtons(verdict);
  renderList();
  updateProgress();
}

// ============================================================
// NAVIGATION
// ============================================================
function navigate(delta) {
  // save current yaml first
  if (selectedIdx >= 0 && selectedIdx < filtered.length) {
    const d = filtered[selectedIdx];
    if (!state[d.id]) state[d.id] = {};
    state[d.id].yaml = document.getElementById('yaml-editor').value;
    state[d.id].note = document.getElementById('verdict-note').value;
    saveState();
  }
  const next = selectedIdx + delta;
  if (next >= 0 && next < filtered.length) selectDoc(next);
}

// ============================================================
// EXPORT
// ============================================================
function exportResults() {
  const rows = ['doc_id,is_api,verdict,note,yaml_edited'];
  ALL_DOCS.forEach(d => {
    const s = state[d.id] || {};
    const verdict = s.verdict || 'none';
    const note    = (s.note || '').replace(/"/g, '""');
    const yaml    = (s.yaml || buildYaml(d)).replace(/"/g, '""');
    rows.push(`"${d.id}",${d.is_api},"${verdict}","${note}","${yaml}"`);
  });
  const blob = new Blob([rows.join('\n')], { type: 'text/csv' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'metadata_review_decisions.csv';
  a.click();
}

// ============================================================
// THEME
// ============================================================
let _lightTheme = false;
function toggleTheme() {
  _lightTheme = !_lightTheme;
  document.body.classList.toggle('light', _lightTheme);
  const btn = document.getElementById('btn-theme');
  if (_lightTheme) {
    btn.textContent = '\u263d Dark';
    btn.style.background = '#eaeef2';
    btn.style.color = '#24292f';
  } else {
    btn.textContent = '\u2600 Light';
    btn.style.background = '#313244';
    btn.style.color = '#cdd6f4';
  }
}

// ============================================================
// HELPERS
// ============================================================
function escHtml(s) {
  return String(s || '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}

// ============================================================
// INIT
// ============================================================
document.getElementById('prog-total').textContent = `/ ${ALL_DOCS.length} docs`;

// Filters
// Populate domain dropdown from data
const domainSel = document.getElementById('filter-domain');
const domainSet = new Set(ALL_DOCS.flatMap(d => (d.domains || '').split(',').map(s => s.trim()).filter(Boolean)));
[...domainSet].sort().forEach(dom => {
  const opt = document.createElement('option');
  opt.value = dom; opt.textContent = dom;
  domainSel.appendChild(opt);
});

// Populate tag dropdown from taxonomy-controlled tags
const tagSel = document.getElementById('filter-tag');
const tagSet = new Set(ALL_DOCS.flatMap(d => (d.tags || '').split(',').map(s => s.trim()).filter(Boolean)));
[...tagSet].sort().forEach(tag => {
  const opt = document.createElement('option');
  opt.value = tag; opt.textContent = tag;
  tagSel.appendChild(opt);
});

['search-input','filter-type','filter-proficiency','filter-status','filter-domain','filter-tag'].forEach(id => {
  document.getElementById(id).addEventListener('input', applyFilters);
  document.getElementById(id).addEventListener('change', applyFilters);
});

['filter-has-desc','filter-no-desc','filter-isolated','filter-connected','filter-has-related'].forEach(btnId => {
  const key = { 'filter-has-desc':'hasDesc','filter-no-desc':'noDesc','filter-isolated':'isolated','filter-connected':'connected','filter-has-related':'hasRelated' }[btnId];
  document.getElementById(btnId).addEventListener('click', function() {
    activeToggles[key] = !activeToggles[key];
    this.classList.toggle('active', activeToggles[key]);
    applyFilters();
  });
});

document.getElementById('btn-approve').addEventListener('click', () => setVerdict('approved'));
document.getElementById('btn-flag').addEventListener('click',    () => setVerdict('flagged'));
document.getElementById('btn-skip').addEventListener('click',    () => setVerdict('skip'));

document.getElementById('btn-next').addEventListener('click', () => navigate(+1));
document.getElementById('btn-prev').addEventListener('click', () => navigate(-1));

document.getElementById('btn-export').addEventListener('click', exportResults);
document.getElementById('btn-clear').addEventListener('click', () => {
  if (!confirm('Clear all review decisions? This cannot be undone.')) return;
  state = {};
  saveState();
  applyFilters();
  updateProgress();
});

// Keyboard navigation
document.addEventListener('keydown', e => {
  if (e.target.tagName === 'TEXTAREA' || e.target.tagName === 'INPUT') return;
  if (e.key === 'ArrowDown'  || e.key === 'j') navigate(+1);
  if (e.key === 'ArrowUp'    || e.key === 'k') navigate(-1);
  if (e.key === 'a') setVerdict('approved');
  if (e.key === 'f') setVerdict('flagged');
  if (e.key === 's') setVerdict('skip');
});

// Note auto-save on blur
document.getElementById('verdict-note').addEventListener('blur', () => {
  if (selectedIdx < 0 || selectedIdx >= filtered.length) return;
  const d = filtered[selectedIdx];
  if (!state[d.id]) state[d.id] = {};
  state[d.id].note = document.getElementById('verdict-note').value;
  saveState();
});

applyFilters();
updateProgress();
</script>
</body>
</html>
"""


def build_html(records: list[dict]) -> str:
    data_json = json.dumps(records, ensure_ascii=False, separators=(",", ":"))
    html = HTML_TEMPLATE.replace("__DATA__", data_json)
    html = html.replace("__TOTAL__", str(len(records)))
    return html


def main():
    print(f"Loading {CSV_PATH} …")
    records = load_data()

    print(f"Building HTML reviewer for {len(records)} docs …")
    html = build_html(records)

    OUT_PATH.write_text(html, encoding="utf-8")
    size_kb = OUT_PATH.stat().st_size // 1024
    print(f"✅ Written to {OUT_PATH}  ({size_kb} KB)")

    # Auto-copy to docs/ for GitHub Pages deployment
    docs_path = ROOT / "docs" / "metadata_reviewer.html"
    try:
        import shutil
        shutil.copy2(OUT_PATH, docs_path)
        print(f"   Copied to {docs_path} (GitHub Pages)")
    except Exception as e:
        print(f"   Warning: could not copy to docs/: {e}")

    print()
    print("Keyboard shortcuts inside the tool:")
    print("  a  → Approve    f → Flag    s → Skip")
    print("  j/↓ → Next      k/↑ → Prev")
    print("  Edits to the YAML textarea are saved per-doc in localStorage")
    print("  'Export results ↓' downloads a CSV with all decisions + edited YAMLs")


if __name__ == "__main__":
    main()
