# XAF Documentation Semantic Analysis — Environment Setup Guide

This guide walks you from **zero → first successful pipeline run** for the **XAF documentation semantic analysis project**, without guesswork.

The setup is:
- Local and reproducible
- CPU‑only
- Deterministic and testable
- Friendly to both engineers and technical writers

---

## 1. Prerequisites (One‑time)

### 1.1 Operating System
Supported:
- Windows 10/11
- macOS
- Linux

> Windows users: PowerShell is recommended. WSL2 works but is not required.

---

### 1.2 Python

**Required version**
- Python **3.10 or 3.11**

Check:
```bash
python --version
```

### 1.3 Git

Check:
```bash
git --version
```

## Project Directory Setup

## 2.1 Create the Repository

```bash
mkdir xaf-doc-analysis
cd xaf-doc-analysis
git init
```

## 2.2. Create the Directory Structure

```bash
mkdir -p \
  data/raw_md \
  data/interim \
  data/processed \
  config/prompts \
  scripts \
  notebooks \
  outputs
```

Your tree should look like this:

xaf-doc-analysis/
  data/
    raw_md/
    interim/
    processed/
  config/
    concepts.yml
    patterns.yml
    prompts/
  scripts/
  notebooks/
  outputs/

### 2.3 Add Documentation

Copy your Markdown files into data/raw_md/

Preserve subfolders: path structure is a semantic signal.

## Python Environment (Critical for Reproducibility)

### 3.1 Create a Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Confirm:

```bash
which python
```

You should see .venv.

### 3.2 Upgrade Base Tooling

```bash
pip install --upgrade pip setuptools wheel
```

## Install Required Dependencies

Create requirements.txt:

```txt
# Core
pandas>=2.1
numpy>=1.26
pyarrow>=14.0

# Markdown parsing
markdown-it-py>=3.0
beautifulsoup4>=4.12

# NLP / ML
regex>=2023.10
scikit-learn>=1.4
sentence-transformers>=2.6
spacy>=3.7

# Graph analysis
networkx>=3.2

# Visualization (optional but useful)
matplotlib>=3.8
seaborn>=0.13
pyvis>=0.3

# CLI / DX
typer>=0.9
tqdm>=4.66
```

Install:

```bash
pip install -r requirements.txt
```

### 4.1 spaCy Language Model

```bash
python -m spacy download en_core_web_sm
```

This is used for:
- Sentence splitting
- Light NER
- Dependency cues

## Configuration Files

Place the yml configuration files in the corresponding directory:

config/
  concepts.yml
  patterns.yml

Do not modify them yet -- the first run should validate extraction.

## Environment Variables (optional but recommended)

Create a .env file (ignored by Git later):

```env
PROJECT_ROOT=.
DATA_DIR=data
OUTPUT_DIR=outputs
```

If you later add LLMs:

```env
OPENAI_API_KEY=sk-...
AZURE_OPENAI_ENDPOINT=...
```

Load automatically (optional):

```bash
pip install python-dotenv
```

## Git Hygiene

Create .gitignore

```txt
.venv/
__pycache__/
.ipynb_checkpoints/
.env
outputs/
data/interim/
data/processed/
*.parquet
*.pickle
```

Commit baseline:

```bash
git add .
git commit -m "Initial project structure and environment"
```

## Validation Checklist

Run this short checklist before moving on:

### Python

```bash
python -c "import pandas, numpy, sklearn, spacy; print('OK')"
```

### spaCY

```bash
python -c "import spacy; spacy.load('en_core_web_sm'); print('spaCy OK')"
```

### Sentence Transformers

```bash
python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2'); print('Embeddings OK')"
```

If all pass → environment is correct.

## Recommended Development Workflow

### 9.1. Order of Execution

You will implement and run scripts in this order:

- 01_ingest_parse.py
- 02_build_explicit_graph.py
- 03_extract_concepts.py
- 04_make_sections_embeddings.py
- 05_find_semantic_pairs.py

Stop there. **Do not add LLMs yet.**

### Use Notebooks Only For Inspection

- notebooks/EDA_structural.ipynb
- notebooks/Viz_graph.ipynb

Scripts produce artifacts → notebooks inspect them.

## Next Steps

Once this environment is set up, you can immediately:

- Generate a **Doc → Concept → Platform** matrix
- Detect orphaned topics
- Find missing cross‑links
- Build your first XAF knowledge graph
- Prepare the corpus for human + AI navigation