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
def load_data():
    df = pd.read_csv(CSV_PATH)

    # Deduplicate: collapse multiple sections per doc by joining unique values
    def join_unique(series):
        vals = set()
        for v in series:
            if pd.notna(v) and str(v).strip():
                for part in str(v).split(","):
                    s = part.strip()
                    if s:
                        vals.add(s)
        return ", ".join(sorted(vals))

    def phase7_desc(series):
        # Fallback: first non-null description from Phase 7
        for v in series:
            if pd.notna(v) and str(v).strip():
                return str(v).strip()
        return ""

    def most_common(series):
        mode = series.mode()
        return mode.iloc[0] if len(mode) else ""

    def max_val(series):
        return int(series.max()) if len(series) else 0

    agg = (
        df.groupby("doc_id", sort=False)
        .agg(
            is_api=("is_api", "first"),
            suggested_tags=("suggested_tags", join_unique),
            suggested_description=("suggested_description", phase7_desc),
            proficiency_level=("proficiency_level", most_common),
            num_semantic_connections=("num_semantic_connections", max_val),
            original_concepts=("original_concepts", join_unique),
            original_platforms=("original_platforms", join_unique),
        )
        .reset_index()
    )

    total = len(agg)
    llm_cache = _load_llm_cache()
    print(f"Building descriptions for {total} docs...")
    llm_hits = heuristic_hits = 0

    # Build JSON records for the HTML
    records = []
    for _, row in agg.iterrows():
        doc_id = row["doc_id"]
        slug = doc_id.rstrip("/").split("/")[-1]

        # Priority for articles: LLM cache > heuristic (raw markdown) > Phase 7
        # API docs always use Phase 7 structured summary.
        if not row["is_api"]:
            if doc_id in llm_cache:
                description = llm_cache[doc_id]
                llm_hits += 1
            else:
                md_desc = article_description_from_md(doc_id)
                if md_desc:
                    description = md_desc
                    heuristic_hits += 1
                else:
                    description = row["suggested_description"]
        else:
            description = row["suggested_description"]

        records.append(
            {
                "id": doc_id,
                "slug": slug,
                "is_api": bool(row["is_api"]),
                "tags": row["suggested_tags"],
                "description": description,
                "proficiency": row["proficiency_level"],
                "connections": int(row["num_semantic_connections"]),
                "concepts": row["original_concepts"],
                "platforms": row["original_platforms"],
            }
        )

    article_count = agg[~agg["is_api"]].shape[0]
    fallback = article_count - llm_hits - heuristic_hits
    print(f"Loaded {len(records)} unique docs from {len(df)} sections")
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
      </div>
      <div class="filter-row">
        <button class="fbtn" id="filter-has-desc" title="Only show docs with a description">Has description</button>
        <button class="fbtn" id="filter-no-desc" title="Only show docs without a description">No description</button>
        <button class="fbtn" id="filter-isolated" title="0 semantic connections">Isolated</button>
        <button class="fbtn" id="filter-connected" title=">10 connections">Well-connected</button>
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
let activeToggles = { hasDesc: false, noDesc: false, isolated: false, connected: false };

// ============================================================
// FILTER + RENDER LIST
// ============================================================
function applyFilters() {
  const q       = document.getElementById('search-input').value.toLowerCase();
  const type    = document.getElementById('filter-type').value;
  const prof    = document.getElementById('filter-proficiency').value;
  const status  = document.getElementById('filter-status').value;

  filtered = ALL_DOCS.filter(d => {
    if (q && !d.id.toLowerCase().includes(q) && !d.slug.toLowerCase().includes(q)) return false;
    if (type === 'api' && !d.is_api) return false;
    if (type === 'article' && d.is_api) return false;
    if (prof !== 'all' && d.proficiency !== prof) return false;
    const v = (state[d.id] || {}).verdict || 'none';
    if (status !== 'all' && v !== status) return false;
    if (activeToggles.hasDesc && !d.description) return false;
    if (activeToggles.noDesc && d.description) return false;
    if (activeToggles.isolated && d.connections !== 0) return false;
    if (activeToggles.connected && d.connections <= 10) return false;
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
['search-input','filter-type','filter-proficiency','filter-status'].forEach(id => {
  document.getElementById(id).addEventListener('input', applyFilters);
  document.getElementById(id).addEventListener('change', applyFilters);
});

['filter-has-desc','filter-no-desc','filter-isolated','filter-connected'].forEach(btnId => {
  const key = { 'filter-has-desc':'hasDesc','filter-no-desc':'noDesc','filter-isolated':'isolated','filter-connected':'connected' }[btnId];
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
    print()
    print("Keyboard shortcuts inside the tool:")
    print("  a  → Approve    f → Flag    s → Skip")
    print("  j/↓ → Next      k/↑ → Prev")
    print("  Edits to the YAML textarea are saved per-doc in localStorage")
    print("  'Export results ↓' downloads a CSV with all decisions + edited YAMLs")


if __name__ == "__main__":
    main()
