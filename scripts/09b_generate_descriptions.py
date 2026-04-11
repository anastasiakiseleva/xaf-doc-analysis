#!/usr/bin/env python3
"""
Phase 9b: Generate LLM metadata descriptions for XAF article documentation.

For each article (non-API doc), extracts structured signals from the raw markdown
(title, slug, doc type, platforms, concepts, H2 section headings) and calls
claude-haiku to write a 120-160 char metadata description per the prompt in
config/prompts/metadata_description.md.

Results are cached in outputs/article_descriptions.parquet so:
- Re-runs skip already-generated docs (free)
- Failed calls are retried on next run
- Whole dataset can be rebuilt by deleting the cache file

Usage:
    # First 10 docs (test mode):
    python scripts/09b_generate_descriptions.py --limit 10

    # Full run:
    python scripts/09b_generate_descriptions.py

    # just rebuild the reviewer HTML from cache (no API calls):
    python scripts/09b_generate_descriptions.py --rebuild-only
"""

import argparse
import os
import re
import time
from pathlib import Path

import anthropic
import pandas as pd

ROOT        = Path(__file__).resolve().parent.parent
CACHE_PATH  = ROOT / "outputs" / "article_descriptions.parquet"
REVIEW_CSV  = ROOT / "outputs" / "metadata_review.csv"
PROMPT_PATH = ROOT / "config" / "prompts" / "metadata_description.md"

# ---------------------------------------------------------------------------
# Markdown signal extraction  (title + h2s only — no body text sent to LLM)
# ---------------------------------------------------------------------------
_CLEAN_H2 = [
    (re.compile(r'\[([^\]]+)\]\([^)]+\)'), r'\1'),   # keep link text
    (re.compile(r'`[^`]+`'), ''),                      # strip inline code
    (re.compile(r'\*\*?([^*]+)\*\*?'), r'\1'),         # strip bold/italic
    (re.compile(r'<[^>]+>'), ''),                      # strip HTML
]

_SKIP_H2 = re.compile(
    r'^(prerequisites?|see also|overview|introduction|remarks?|notes?|'
    r'examples?|summary|next steps?|related topics?|what\'?s? next)$',
    re.IGNORECASE,
)

_GENERIC_HEADING_RE = re.compile(r'^[\d.]+\s+')  # "1. Something" -> strip leading number


def _clean_h2(text: str) -> str:
    for pat, repl in _CLEAN_H2:
        text = pat.sub(repl, text)
    text = _GENERIC_HEADING_RE.sub('', text)
    return re.sub(r'\s+', ' ', text).strip()


def extract_signals(doc_id: str, tags: str, platforms: str) -> dict | None:
    """
    Parse the raw .md file and return structured signals for the prompt.
    Returns None if the file cannot be read.
    """
    md_path = ROOT / (doc_id.lstrip('/') + '.md')
    if not md_path.exists():
        return None
    try:
        raw = md_path.read_text(encoding='utf-8', errors='ignore')
    except OSError:
        return None

    # ── Extract title from YAML frontmatter ──────────────────────────────────
    title = ''
    if raw.startswith('---'):
        end = raw.find('\n---', 3)
        if end != -1:
            fm = raw[3:end]
            m = re.search(r"title:\s*['\"]?(.+?)['\"]?\s*$", fm, re.MULTILINE)
            if m:
                title = m.group(1).strip().strip("'\"")
            raw = raw[end + 4:].lstrip()

    # ── Derive doc type from path/slug ───────────────────────────────────────
    slug = doc_id.rstrip('/').split('/')[-1]
    if not title:
        title = slug.replace('-', ' ').title()

    if slug.startswith('how-to-'):
        doc_type = 'how-to'
    elif 'tutorial' in doc_id or 'getting-started' in doc_id:
        doc_type = 'tutorial'
    else:
        doc_type = 'conceptual'

    # ── Collect H2 section headings (full document scan) ─────────────────────
    h2s: list[str] = []
    in_code = False
    for line in raw.splitlines():
        stripped = line.strip()
        if stripped.startswith('```'):
            in_code = not in_code
            continue
        if in_code:
            continue
        if stripped.startswith('## '):
            heading = _clean_h2(stripped.lstrip('# ').strip())
            if heading and not _SKIP_H2.match(heading):
                h2s.append(heading)

    # ── Normalise platforms ───────────────────────────────────────────────────
    # ".NET Runtime" is the underlying runtime, not a UI platform — exclude it
    # to avoid misleading descriptions like "across Blazor, WinForms, and .NET Runtime".
    _RUNTIME_TAGS = {'.net runtime', 'net runtime', '.net', 'runtime'}
    platforms = platforms if isinstance(platforms, str) else ''
    plat_list = [p.strip() for p in platforms.split(',')
                 if p.strip() and p.strip().lower() not in _RUNTIME_TAGS]
    plat_str = ', '.join(plat_list) if plat_list else 'All'

    return {
        'title':    title,
        'slug':     slug,
        'type':     doc_type,
        'platforms': plat_str,
        'concepts': tags or '(none)',
        'sections': ' | '.join(h2s[:8]) if h2s else '(none)',
    }


# ---------------------------------------------------------------------------
# Prompt loading + user message construction
# ---------------------------------------------------------------------------
def load_prompt() -> str:
    return PROMPT_PATH.read_text(encoding='utf-8')


def build_user_message(signals: dict) -> str:
    return (
        f"<title>{signals['title']}</title>\n"
        f"<slug>{signals['slug']}</slug>\n"
        f"<type>{signals['type']}</type>\n"
        f"<platforms>{signals['platforms']}</platforms>\n"
        f"<concepts>{signals['concepts']}</concepts>\n"
        f"<sections>{signals['sections']}</sections>"
    )


# ---------------------------------------------------------------------------
# LLM call  (Anthropic claude-haiku, with exponential back-off)
# ---------------------------------------------------------------------------
def _api_call(client: anthropic.Anthropic, model: str,
              system_prompt: str, messages: list) -> str | None:
    """Single API call with retry on rate limits."""
    max_retries = 4
    for attempt in range(max_retries):
        try:
            response = client.messages.create(
                model=model,
                max_tokens=80,
                system=system_prompt,
                messages=messages,
            )
            return response.content[0].text.strip().strip('"').strip("'")
        except anthropic.APIStatusError as e:
            if e.status_code in (429, 529, 503) and attempt < max_retries - 1:
                wait = 2 ** attempt * 3
                print(f"    Rate limit ({e.status_code}), waiting {wait}s …")
                time.sleep(wait)
                continue
            print(f"    API error {e.status_code}: {e}")
            return None
        except Exception as e:
            print(f"    Error: {e}")
            return None
    return None


def call_llm(client: anthropic.Anthropic, model: str,
             system_prompt: str, user_msg: str) -> str | None:
    messages = [{"role": "user", "content": user_msg}]
    text = _api_call(client, model, system_prompt, messages)
    if text is None:
        return None

    # If over limit, ask the model to shorten it — never truncate mid-sentence
    if len(text) > 150:
        messages = messages + [
            {"role": "assistant", "content": text},
            {"role": "user", "content":
             f"Too long ({len(text)} chars). Rewrite as one complete sentence under 145 characters. "
             f"Keep all key technical terms. Output ONLY the description."},
        ]
        shortened = _api_call(client, model, system_prompt, messages)
        if shortened and 40 <= len(shortened) <= 160:
            text = shortened
        # If the retry is also long or failed, accept the original rather than truncating
        # (reviewer can edit it)

    return text if len(text) >= 40 else None


# ---------------------------------------------------------------------------
# Cache helpers
# ---------------------------------------------------------------------------
def load_cache() -> dict[str, str]:
    if CACHE_PATH.exists():
        try:
            df = pd.read_parquet(CACHE_PATH)
            return dict(zip(df['doc_id'], df['description']))
        except Exception as e:
            print(f"Warning: could not load cache: {e}")
    return {}


def save_cache(cache: dict[str, str]) -> None:
    rows = [{'doc_id': k, 'description': v} for k, v in cache.items()]
    pd.DataFrame(rows).to_parquet(CACHE_PATH, index=False, engine='pyarrow')


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description='Generate LLM metadata descriptions for XAF articles'
    )
    parser.add_argument('--model',    default='claude-haiku-4-5',
                        help='Anthropic model (default: claude-haiku-4-5)')
    parser.add_argument('--delay',    type=float, default=0.1,
                        help='Seconds between API calls (default: 0.1)')
    parser.add_argument('--limit',    type=int, default=None,
                        help='Process at most N articles (for testing)')
    parser.add_argument('--rebuild-only', action='store_true',
                        help='Skip LLM calls; rebuild reviewer HTML from cache')
    args = parser.parse_args()

    # Load review CSV — articles only
    print(f"Loading {REVIEW_CSV} …")
    df = pd.read_csv(REVIEW_CSV)
    articles = (
        df[df['is_api'] == False]
        .drop_duplicates('doc_id')
        [['doc_id', 'suggested_tags', 'original_platforms']]
        .reset_index(drop=True)
    )
    print(f"  {len(articles)} unique article docs")

    cache = load_cache()
    print(f"  Cache: {len(cache)} descriptions already generated")

    if not args.rebuild_only:
        # Filter to docs not yet cached
        todo = articles[~articles['doc_id'].isin(cache)].reset_index(drop=True)
        if args.limit:
            todo = todo.head(args.limit)

        if len(todo) == 0:
            print("  All articles already have cached descriptions.")
        else:
            print(f"\n  {len(todo)} articles to describe")
            # Cost estimate: claude-haiku ~$0.08/1M input tokens; ~300 input tokens each
            est_cost = len(todo) * 300 / 1_000_000 * 0.08
            print(f"  Estimated cost: ~${est_cost:.2f} ({args.model})")

            if len(todo) > 50:
                answer = input(f"\nProceed with {len(todo)} API calls? (yes/no): ")
                if answer.lower() not in ('yes', 'y'):
                    print("Aborted.")
                    return

            api_key = os.getenv('ANTHROPIC_API_KEY')
            if not api_key:
                print("Error: ANTHROPIC_API_KEY not set")
                return
            client = anthropic.Anthropic(api_key=api_key)
            system_prompt = load_prompt()

            new_count = 0
            fail_count = 0
            skip_count = 0

            print()
            for i, row in todo.iterrows():
                doc_id   = row['doc_id']
                tags     = row.get('suggested_tags', '') or ''
                platforms = row.get('original_platforms', '') or ''
                slug     = doc_id.rstrip('/').split('/')[-1]
                n        = i + 1

                signals = extract_signals(doc_id, tags, platforms)
                if not signals:
                    print(f"  [{n}/{len(todo)}] SKIP (no file): {slug}")
                    skip_count += 1
                    continue

                user_msg = build_user_message(signals)
                desc = call_llm(client, args.model, system_prompt, user_msg)

                if desc:
                    cache[doc_id] = desc
                    new_count += 1
                    preview = desc[:90] + '…' if len(desc) > 90 else desc
                    print(f"  [{n}/{len(todo)}] OK ({len(desc)}c): {preview}")
                else:
                    fail_count += 1
                    print(f"  [{n}/{len(todo)}] FAILED: {slug}")

                # Save cache every 50 docs in case of interruption
                if new_count % 50 == 0 and new_count > 0:
                    save_cache(cache)
                    print(f"    … checkpoint saved ({new_count} new)")

                if args.delay > 0:
                    time.sleep(args.delay)

            save_cache(cache)
            print(f"\n✅ Done: {new_count} new, {fail_count} failed, {skip_count} skipped")
            print(f"   Cache: {CACHE_PATH}")

    # Rebuild reviewer HTML
    print("\nRebuilding reviewer HTML …")
    import subprocess, sys
    result = subprocess.run(
        [sys.executable, str(ROOT / 'tools' / 'build_metadata_reviewer.py')],
        cwd=ROOT,
    )
    if result.returncode != 0:
        print("Warning: reviewer build exited with non-zero status")


if __name__ == '__main__':
    main()
