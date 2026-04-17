#!/usr/bin/env python
"""
04_make_sections_embeddings.py

Builds section-level embeddings for the XAF documentation corpus.

Inputs
------
- outputs/topics_inventory.parquet   (from 01_ingest_parse.py)
- outputs/doc_concepts.parquet       (from 03_extract_concepts.py)

Behavior
--------
- Reconstructs section text from topics_inventory (title + h_path + text [+ 1st code block]).
- Uses doc_concepts to:
  * decide which sections are kept (kept==True)
  * retrieve section metadata (concepts, platforms, apis, is_api)
- Generates TWO outputs:
  * outputs/sections_embeddings_conceptual.parquet
  * outputs/sections_embeddings_api.parquet
- Embeddings model defaults to 'sentence-transformers/all-MiniLM-L6-v2'
  * configurable via --model CLI arg or MODEL_NAME env var
- Batching, progress bars, and optional persistent embedding cache included.

Outputs (Parquet schema)
------------------------
- doc_id: str
- section_id: str
- title: str
- h_path: str
- is_api: bool
- concepts: list[str]
- platforms: list[str]
- apis: list[str]
- text_len: int              (characters after truncation)
- word_count: int
- model: str
- embedding: array[float]    (normalized)

Usage
-----
python scripts/04_make_sections_embeddings.py \
  --batch-size 64 \
  --max-chars 4000 \
  --include-code True \
  --cache True

Requirements
------------
- sentence-transformers
- pandas, numpy, tqdm, pyarrow
"""

from __future__ import annotations

import os
import sys
import math
import json
import pickle
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
from tqdm import tqdm

# Lazy import to avoid startup cost if env not ready
try:
    from sentence_transformers import SentenceTransformer
except Exception as e:
    SentenceTransformer = None


# ------------------------------ Paths ------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR   = PROJECT_ROOT / "outputs"

TOPICS_INVENTORY = OUTPUT_DIR / "topics_inventory.parquet"
DOC_CONCEPTS     = OUTPUT_DIR / "doc_concepts.parquet"

OUT_CONCEPTUAL = OUTPUT_DIR / "sections_embeddings_conceptual.parquet"
OUT_API        = OUTPUT_DIR / "sections_embeddings_api.parquet"

# Optional persistent embedding cache
CACHE_DIR = OUTPUT_DIR / ".emb_cache"


# ------------------------------ CLI ------------------------------
import argparse

def parse_args():
    p = argparse.ArgumentParser(description="Create section-level embeddings for XAF docs.")
    p.add_argument("--model", type=str, default=os.environ.get("MODEL_NAME", "sentence-transformers/all-MiniLM-L6-v2"),
                   help="Sentence-Transformers model name or path.")
    p.add_argument("--batch-size", type=int, default=int(os.environ.get("EMB_BATCH", "64")),
                   help="Encoding batch size.")
    p.add_argument("--max-chars", type=int, default=int(os.environ.get("EMB_MAX_CHARS", "4000")),
                   help="Max characters per section text (truncate).")
    p.add_argument("--min-words", type=int, default=int(os.environ.get("EMB_MIN_WORDS", "5")),
                   help="Minimum words per section text to embed.")
    p.add_argument("--include-code", type=lambda x: str(x).lower() in {"1","t","true","y","yes"},
                   default=os.environ.get("EMB_INCLUDE_CODE", "true"),
                   help="Append first code block to text.")
    p.add_argument("--cache", type=lambda x: str(x).lower() in {"1","t","true","y","yes"},
                   default=os.environ.get("EMB_CACHE", "true"),
                   help="Use on-disk cache for embeddings.")
    p.add_argument("--normalize", type=lambda x: str(x).lower() in {"1","t","true","y","yes"},
                   default=os.environ.get("EMB_NORMALIZE", "true"),
                   help="Normalize embeddings (recommended for cosine similarity).")
    p.add_argument("--no-concept-context", action="store_true",
                   default=False,
                   help="Disable taxonomy-concept context enrichment (C1/C2). "
                        "Use to compare embedding quality against the baseline.")
    return p.parse_args()


# ------------------------------ Helpers ------------------------------
def ensure_exists(path: Path, what: str):
    if not path.exists():
        print(f"❌ Missing {what}: {path}")
        sys.exit(1)

def _safe_list(val) -> list:
    """Coerce parquet list-like values (pyarrow/numpy) into a plain Python list."""
    if val is None or (isinstance(val, float) and pd.isna(val)):
        return []
    if isinstance(val, list):
        return val
    if hasattr(val, "tolist"):
        return list(val.tolist())
    if hasattr(val, "__iter__") and not isinstance(val, str):
        return list(val)
    return []

def build_section_lookup(topics_df: pd.DataFrame) -> Dict[Tuple[str, str], dict]:
    """
    Create a fast lookup: (doc_id, section_id) -> {title, h_path_list, text, code_blocks}
    """
    def safe_get_list(val):
        """Handle numpy arrays from parquet"""
        if val is None or (isinstance(val, float) and pd.isna(val)):
            return []
        if isinstance(val, (list, tuple)):
            return list(val)
        if hasattr(val, '__iter__') and not isinstance(val, str):
            return list(val)
        return []
    
    lookup = {}
    # Iterate rows (docs), expand sections list
    for _, row in topics_df.iterrows():
        doc_id = row["doc_id"]
        title  = row.get("title", "") or ""
        sections = safe_get_list(row.get("sections"))
        for s in sections:
            section_id = s["section_id"]
            # Store raw fields; text assembly later
            lookup[(doc_id, section_id)] = {
                "title": title,
                "h_path_list": safe_get_list(s.get("h_path")),
                "text": (s.get("text", "") or "").strip(),
                "code_blocks": safe_get_list(s.get("code_blocks")),
            }
    return lookup

def assemble_text(
    meta: dict,
    include_code: bool,
    max_chars: int,
    *,
    concepts: list = None,
    concept_domains: dict = None,
    apis: list = None,
    is_api: bool = False,
    concept_context: bool = True,
) -> str:
    """
    Build embed-ready section text from raw metadata and optional taxonomy context.

    C1 (concept_context=True): Appends a ``Concepts:`` line listing each concept with
    its taxonomy domain, anchoring the embedding in the XAF concept space.

    C2 (concept_context=True, is_api=True): Prepends extracted API symbols before the
    heading/body so cross-corpus (API ↔ conceptual) matching reflects the actual API surface.
    """
    title = meta.get("title", "")
    h_path_list = meta.get("h_path_list", [])
    h_path = " > ".join(h_path_list)
    body = meta.get("text", "")

    parts = []

    # C2: For API sections, prepend the extracted API symbols as a compact anchor line.
    # This improves cross-corpus retrieval between API reference and conceptual docs.
    if concept_context and is_api and apis:
        api_line = "API: " + ", ".join(sorted(set(apis))[:30])
        parts.append(api_line)

    parts.append(title)
    if h_path:
        parts.append(h_path)
    if body:
        parts.append(body)

    # optionally include just the first code block (API examples are valuable)
    if include_code:
        code_blocks = meta.get("code_blocks", []) or []
        if code_blocks:
            parts.append(code_blocks[0])

    text = "\n".join([p for p in parts if p]).strip()

    # truncate hard limit before appending concept context so we don't cut the concept line
    if len(text) > max_chars:
        text = text[:max_chars]

    # C1: Append concept context line ("Concepts: XYZ (domain/sub), ABC (domain/sub)")
    # Appended AFTER truncation so it is always present, even for very long sections.
    if concept_context and concepts:
        _domains = concept_domains or {}
        concept_parts = []
        for name in concepts[:20]:  # cap at 20 to stay within token budgets
            domain = _domains.get(name, "")
            concept_parts.append(f"{name} ({domain})" if domain else name)
        text = text + "\nConcepts: " + ", ".join(concept_parts)

    return text

def est_word_count(text: str) -> int:
    return len((text or "").split())

def aslist(x):
    # Convert numpy array to list for parquet
    if isinstance(x, np.ndarray):
        return x.astype(np.float32).tolist()
    return x

def load_cache(cache_file: Path) -> dict:
    if not cache_file.exists():
        return {}
    try:
        with cache_file.open("rb") as f:
            return pickle.load(f)
    except Exception:
        return {}

def save_cache(cache_file: Path, obj: dict):
    cache_file.parent.mkdir(parents=True, exist_ok=True)
    with cache_file.open("wb") as f:
        pickle.dump(obj, f)

def text_key(model: str, text: str) -> str:
    # A deterministic key per (model, text)
    import hashlib
    h = hashlib.sha1()
    h.update(model.encode("utf-8"))
    h.update(b"|")
    h.update((text or "").encode("utf-8"))
    return h.hexdigest()


# ------------------------------ Main ------------------------------
def main():
    args = parse_args()

    ensure_exists(TOPICS_INVENTORY, "topics inventory")
    ensure_exists(DOC_CONCEPTS, "doc concepts")

    print("📚 Loading inputs…")
    topics_df = pd.read_parquet(TOPICS_INVENTORY)  # title + sections[]
    dc_df     = pd.read_parquet(DOC_CONCEPTS)      # kept + is_api + concepts/platforms/apis

    # Keep only sections marked as kept by 03_extract_concepts
    dc_df = dc_df[dc_df["kept"] == True].copy()

    # Build lookup for section raw text
    sec_lookup = build_section_lookup(topics_df)

    # Reconstruct rows with merged metadata + assembled text
    # Resolve concept_context flag (C3): default True, disabled by --no-concept-context
    concept_context = not args.no_concept_context
    if concept_context:
        print("🏷️  Concept context enrichment: ENABLED (C1+C2) — use --no-concept-context to disable")

    # Determine whether doc_concepts.parquet carries the Phase-B4 taxonomy metadata columns
    has_concept_domains = "concept_domains" in dc_df.columns

    records = []
    missing = 0
    for _, row in dc_df.iterrows():
        key = (row["doc_id"], row["section_id"])
        meta = sec_lookup.get(key)
        if not meta:
            missing += 1
            continue

        # Pull concept metadata for text enrichment; gracefully absent in old parquet files
        row_concepts = _safe_list(row.get("concepts"))
        row_apis = _safe_list(row.get("apis"))
        row_is_api = bool(row.get("is_api", False))
        row_concept_domains: dict = {}
        if has_concept_domains:
            cd = row.get("concept_domains")
            if isinstance(cd, dict):
                row_concept_domains = cd

        text = assemble_text(
            meta,
            include_code=args.include_code,
            max_chars=args.max_chars,
            concepts=row_concepts,
            concept_domains=row_concept_domains,
            apis=row_apis,
            is_api=row_is_api,
            concept_context=concept_context,
        )
        wc = est_word_count(text)
        if wc < args.min_words:
            # silently skip ultra-short fragments; 03 already filtered most of them
            continue

        records.append({
            "doc_id": row["doc_id"],
            "section_id": row["section_id"],
            "title": meta.get("title", ""),
            "h_path": row.get("h_path", ""),
            "is_api": row_is_api,
            "concepts": row_concepts,
            "platforms": _safe_list(row.get("platforms")),
            "apis": row_apis,
            "text": text,
            "text_len": len(text),
            "word_count": wc,
        })

    if missing > 0:
        print(f"⚠️  {missing} kept sections referenced in doc_concepts were not found in topics_inventory (skipped).")

    if not records:
        print("❌ No sections to embed. Check previous stages.")
        sys.exit(1)

    df = pd.DataFrame(records)

    # Split into conceptual vs API corpora
    df_conceptual = df[df["is_api"] == False].copy()
    df_api        = df[df["is_api"] == True].copy()

    print(f"📏 Conceptual sections to embed: {len(df_conceptual)}")
    print(f"🔧 API sections to embed:        {len(df_api)}")

    # Load model
    if SentenceTransformer is None:
        print("❌ sentence-transformers is not installed or failed to import.")
        sys.exit(1)

    print(f"🧠 Loading model: {args.model}")
    model = SentenceTransformer(args.model)

    # Optional cache
    cache = {}
    cache_file = CACHE_DIR / f"emb_cache_{args.model.replace('/','_')}.pkl"
    if args.cache:
        cache = load_cache(cache_file)
        print(f"🗄️  Embedding cache loaded: {len(cache)} entries")

    def encode_df(in_df: pd.DataFrame) -> pd.DataFrame:
        """Encode text column into embeddings with caching & batching."""
        if in_df.empty:
            return in_df.assign(model=args.model, embedding=[[]]*0)

        texts = in_df["text"].tolist()
        to_compute_idx = []
        cached_embs = [None] * len(texts)

        # Cache lookup
        for i, t in enumerate(texts):
            k = text_key(args.model, t)
            if args.cache and k in cache:
                cached_embs[i] = cache[k]
            else:
                to_compute_idx.append(i)

        # Compute missing
        if to_compute_idx:
            # Batch compute
            batch = args.batch_size
            new_vectors = []
            for start in tqdm(range(0, len(to_compute_idx), batch), desc="💡 Encoding", unit="batch"):
                batch_idx = to_compute_idx[start:start+batch]
                batch_texts = [texts[j] for j in batch_idx]
                embs = model.encode(
                    batch_texts,
                    batch_size=batch,
                    show_progress_bar=False,
                    normalize_embeddings=args.normalize,
                )
                # convert to lists for parquet and caching
                for j, v in zip(batch_idx, embs):
                    vec = np.asarray(v, dtype=np.float32)
                    cached_embs[j] = vec
                    if args.cache:
                        cache[text_key(args.model, texts[j])] = vec
                    new_vectors.append(1)
            print(f"🧷 Encoded {len(to_compute_idx)} new sections.")
        else:
            print("✅ All embeddings served from cache.")

        out = in_df.copy()
        out["model"] = args.model
        out["embedding"] = [np.asarray(v, dtype=np.float32) for v in cached_embs]
        return out

    # Encode each corpus
    out_conceptual = encode_df(df_conceptual)
    out_api        = encode_df(df_api)

    # Persist cache
    if args.cache:
        save_cache(cache_file, cache)
        print(f"🗃️  Cache saved: {len(cache)} entries → {cache_file}")

    # Convert embeddings to lists for parquet
    out_conceptual["embedding"] = out_conceptual["embedding"].apply(lambda v: v.astype(np.float32).tolist())
    out_api["embedding"]        = out_api["embedding"].apply(lambda v: v.astype(np.float32).tolist())

    # Remove raw text (optional; comment this out if you want the text in parquet)
    out_conceptual = out_conceptual.drop(columns=["text"])
    out_api        = out_api.drop(columns=["text"])

    # Save outputs
    OUT_CONCEPTUAL.parent.mkdir(parents=True, exist_ok=True)
    print(f"💾 Writing → {OUT_CONCEPTUAL}")
    out_conceptual.to_parquet(OUT_CONCEPTUAL, index=False)

    print(f"💾 Writing → {OUT_API}")
    out_api.to_parquet(OUT_API, index=False)

    # Summary
    def emb_dim(df_emb: pd.DataFrame) -> int:
        if df_emb.empty: return 0
        arr = df_emb.iloc[0]["embedding"]
        return len(arr) if isinstance(arr, list) else int(np.asarray(arr).shape[-1])

    print("✅ Embedding build complete.")
    print(f"   Conceptual: {len(out_conceptual)} sections | dim={emb_dim(out_conceptual)}")
    print(f"   API:        {len(out_api)} sections       | dim={emb_dim(out_api)}")


if __name__ == "__main__":
    main()