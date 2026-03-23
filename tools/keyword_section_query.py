#!/usr/bin/env python3
"""Keyword-based section query over the corpus.

Use when the thing you want isn't a first-class concept name in concepts.yml.
Scans Phase 1 section text and joins Phase 3 tags.

Outputs
-------
- outputs/keyword_hits.csv

Example
-------
python tools/keyword_section_query.py --keywords "lockout,brute force,brute-force,isecurityuserlockout" --out outputs/lockout_bruteforce_hits.csv
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any, Dict, List, Tuple

import pandas as pd


OUT = Path("outputs")


def safe_list(v: Any) -> List[Any]:
    if v is None:
        return []
    if isinstance(v, float) and pd.isna(v):
        return []
    if isinstance(v, (list, tuple)):
        return list(v)
    tolist = getattr(v, "tolist", None)
    if callable(tolist):
        try:
            r = tolist()
            return r if isinstance(r, list) else list(r)
        except Exception:
            return []
    if hasattr(v, "__iter__") and not isinstance(v, str):
        try:
            return list(v)
        except Exception:
            return []
    return []


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Query corpus sections by keywords")
    p.add_argument("--keywords", required=True, help="Comma-separated keywords/phrases (case-insensitive)")
    p.add_argument("--concept", default=None, help="Optional: require section to be tagged with this concept")
    p.add_argument("--kept-only", action="store_true", help="Optional: only include sections where kept==True")
    p.add_argument("--out", default=str(OUT / "keyword_hits.csv"), help="Output CSV path")
    p.add_argument("--max-per-doc", type=int, default=20, help="Cap hits per document")
    p.add_argument("--max-total", type=int, default=5000, help="Cap total hits")
    p.add_argument("--snippet-chars", type=int, default=220, help="Snippet length")
    return p.parse_args()


def build_patterns(keywords: List[str]) -> List[Tuple[str, re.Pattern]]:
    pats: List[Tuple[str, re.Pattern]] = []
    for kw in keywords:
        kw = kw.strip()
        if not kw:
            continue
        # Treat keyword as a literal phrase, but allow flexible whitespace/hyphen for common cases
        if kw.lower() in {"brute force", "brute-force"}:
            pat = re.compile(r"brute\s*-?\s*force", re.IGNORECASE)
            pats.append(("brute force", pat))
        else:
            pats.append((kw, re.compile(re.escape(kw), re.IGNORECASE)))
    return pats


def main() -> int:
    args = parse_args()
    keywords = [k.strip() for k in (args.keywords or "").split(",") if k.strip()]
    patterns = build_patterns(keywords)

    target_concept = (args.concept or "").strip() or None

    topics = pd.read_parquet(OUT / "topics_inventory.parquet")
    dc = pd.read_parquet(OUT / "doc_concepts.parquet")

    # Quick lookup for tags
    dc_idx: Dict[Tuple[str, str], Dict[str, Any]] = {}
    for r in dc.itertuples(index=False):
        dc_idx[(str(r.doc_id), str(r.section_id))] = {
            "is_api": bool(getattr(r, "is_api", False)),
            "kept": bool(getattr(r, "kept", True)),
            "concepts": safe_list(getattr(r, "concepts", [])),
            "platforms": safe_list(getattr(r, "platforms", [])),
            "apis": safe_list(getattr(r, "apis", [])),
            "h_path": safe_list(getattr(r, "h_path", [])),
        }

    hits: List[Dict[str, Any]] = []
    hits_per_doc: Dict[str, int] = {}

    for doc_row in topics.itertuples(index=False):
        doc_id = str(getattr(doc_row, "doc_id"))
        title = getattr(doc_row, "title", "")
        sections = safe_list(getattr(doc_row, "sections", []))

        for s in sections:
            if not isinstance(s, dict):
                continue

            section_id = str(s.get("section_id", ""))
            text = (s.get("text", "") or "")
            if not text:
                continue

            matched = []
            for label, pat in patterns:
                if pat.search(text):
                    matched.append(label)

            if not matched:
                continue

            if hits_per_doc.get(doc_id, 0) >= args.max_per_doc:
                continue

            meta = dc_idx.get((doc_id, section_id), {})

            if args.kept_only and meta.get("kept") is not True:
                continue

            if target_concept:
                concepts = meta.get("concepts", [])
                if target_concept not in concepts:
                    continue

            # Basic snippet around first match
            lower = text.lower()
            first_pos = None
            for label in matched:
                if label == "brute force":
                    m = re.search(r"brute\s*-?\s*force", text, re.IGNORECASE)
                    if m:
                        first_pos = m.start()
                        break
                else:
                    pos = lower.find(label.lower())
                    if pos != -1:
                        first_pos = pos
                        break
            if first_pos is None:
                first_pos = 0
            start = max(0, first_pos - 80)
            end = min(len(text), start + args.snippet_chars)
            snippet = text[start:end].replace("\n", " ").strip()

            hits.append({
                "doc_id": doc_id,
                "title": title,
                "section_id": section_id,
                "matched": ", ".join(matched),
                "is_api": meta.get("is_api"),
                "kept": meta.get("kept"),
                "concepts": ", ".join([c for c in meta.get("concepts", []) if isinstance(c, str)][:20]),
                "platforms": ", ".join([p for p in meta.get("platforms", []) if isinstance(p, str)][:10]),
                "apis": ", ".join([a for a in meta.get("apis", []) if isinstance(a, str)][:10]),
                "h_path": " > ".join([h for h in meta.get("h_path", []) if isinstance(h, str)]),
                "snippet": snippet,
            })

            hits_per_doc[doc_id] = hits_per_doc.get(doc_id, 0) + 1

            if len(hits) >= args.max_total:
                break
        if len(hits) >= args.max_total:
            break

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(hits).to_csv(out_path, index=False, encoding="utf-8")

    print(f"Keywords: {keywords}")
    if target_concept:
        print(f"Concept filter: {target_concept}")
    if args.kept_only:
        print("Kept-only: True")
    print(f"Total hits: {len(hits)}")
    print(f"Wrote: {out_path}")

    # Print top docs by hit count
    top = sorted(hits_per_doc.items(), key=lambda x: x[1], reverse=True)[:15]
    print("\nTop documents by hit count:")
    for doc, c in top:
        print(f"  {c:3d}  {doc}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
