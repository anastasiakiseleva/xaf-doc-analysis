# Environment Setup Guide

This guide walks you from **zero to first successful pipeline run**.

---

## 1. Prerequisites

### Python

**Required: Python 3.10 or 3.11**

```bash
python --version
```

### Git

```bash
git --version
```

---

## 2. Clone and Set Up the Project

```bash
git clone <repo-url>
cd xaf-doc-analysis
```

Create a virtual environment:

```bash
python -m venv .venv

# Windows
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate
```

Upgrade base tooling:

```bash
pip install --upgrade pip setuptools wheel
```

---

## 3. Install Dependencies

```bash
pip install -r docs/requirements.txt
```

**Core packages installed:**

| Package | Used for |
|---------|---------|
| `pandas`, `numpy`, `pyarrow` | Data processing and Parquet I/O |
| `markdown-it-py`, `beautifulsoup4` | Markdown parsing (Phase 1) |
| `sentence-transformers` | Vector embeddings (Phase 4) |
| `scikit-learn` | Nearest-neighbor search (Phase 5) |
| `PyYAML` | Config and metadata export |
| `tqdm`, `regex` | Progress display and text matching |

**Optional — only needed for specific tools:**

```bash
# Phase 6: LLM relationship classification
pip install openai anthropic

# tools/visualize_graph.py: interactive graph
pip install pyvis
```

---

## 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
PROJECT_ROOT=.
DATA_DIR=data
OUTPUT_DIR=outputs
```

For Phase 6 (LLM classification), add your API key:

```env
OPENAI_API_KEY=sk-...
# or
ANTHROPIC_API_KEY=...
```

---

## 5. Add Documentation Source Files

Copy your Markdown documentation into `data/raw_md/`, preserving the folder structure — path depth is a semantic signal used by the pipeline.

```
data/raw_md/
├── apidoc/          # API reference namespaces
└── articles/        # Conceptual articles
```

---

## 6. Validate the Environment

```bash
python -c "import pandas, numpy, sklearn; print('Core OK')"
python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2'); print('Embeddings OK')"
python -c "import yaml; print('YAML OK')"
```

All three should print without errors. The embeddings check will download the model (~80 MB) on first run.

---

## 7. Run the Environment Check Script

```powershell
.\tools\env_check.ps1
```

---

## 8. First Pipeline Run

```bash
python scripts/run_kg_pipeline_with_validation.py
```

Or phase by phase:

```bash
python scripts/01_ingest_parse.py
python scripts/02_build_explicit_graph.py
python scripts/03_extract_concepts.py
python scripts/04_make_sections_embeddings.py
python scripts/05_find_semantic_pairs.py
python scripts/11_extract_api_entities.py
python scripts/12_map_apis_to_concepts.py
python scripts/13_build_knowledge_graph.py
```

Stop after Phase 5 on first run to validate the corpus before investing in API phases.
