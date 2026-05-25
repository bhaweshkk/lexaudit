# LexAudit — Multi-Agent Indian Legal Research System

A RAG-powered, multi-agent legal assistant for Indian labour and employment law.
Built for research: compares a plain RAG chatbot against a 6-agent pipeline with
fact-checking, amendment awareness, and citation auditing.

---

## Project structure

```
lexaudit/
├── main.py                        # FastAPI server (all endpoints)
├── requirements.txt
├── .env.example                   # copy to .env and fill in your keys
│
├── agents/
│   ├── base.py                    # Base class all agents extend
│   ├── query_analyzer.py          # Agent 1 — parse legal domain and issues
│   ├── statute_retrieval.py       # Agent 2 — RAG over statutes collection
│   ├── caselaw_retrieval.py       # Agent 3 — RAG over cases collection
│   ├── fact_checker.py            # Agent 4 — amendment and repeal verification
│   ├── memo_drafter.py            # Agent 5 — formal legal opinion memo
│   ├── citation_verifier.py       # Agent 6 — audit every citation in memo
│   └── orchestrator.py            # Runs all 6 agents in sequence
│
├── rag/
│   ├── vector_store.py            # ChromaDB wrapper with sentence-transformer embeddings
│   ├── chunker.py                 # Legal text chunking (section-aware)
│   └── retriever.py               # High-level retrieval interface
│
├── data/
│   ├── sample_statutes.py         # 14 Indian statute excerpts (Payment of Wages, IDA, MWA…)
│   ├── sample_cases.py            # 12 landmark SC/HC judgment summaries
│   └── ingest.py                  # Ingestion pipeline + Indian Kanoon API fetcher
│
├── benchmark/
│   ├── queries.json               # 15 labeled test queries with ground truth citations
│   └── evaluator.py               # Baseline vs LexAudit comparison framework
│
└── scripts/
    └── setup_db.py                # One-shot database setup script
```

---

## Setup — step by step

### Step 1 — Clone and enter the project

```bash
git clone <your-repo-url>
cd lexaudit
```

### Step 2 — Create a virtual environment

```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On Mac / Linux:
source venv/bin/activate
```

### Step 3 — Install dependencies

```bash
pip install -r requirements.txt
```

> The first run downloads the `all-MiniLM-L6-v2` embedding model (~80 MB).
> This is a one-time download and is cached automatically.

### Step 4 — Set up your API key

```bash
cp .env.example .env
```

Open `.env` and add your Anthropic API key:

```
ANTHROPIC_API_KEY=sk-ant-...your-key-here...
```

Get a key at: https://console.anthropic.com

### Step 5 — Build the vector database

```bash
python scripts/setup_db.py
```

This ingests all bundled statute excerpts and case summaries into ChromaDB.
You will see output like:

```
[VectorStore] Loading embedding model: all-MiniLM-L6-v2
[VectorStore] Ready.
── Ingesting sample statutes ─────────────────
Chunking statutes: 100%|████████| 14/14
[VectorStore] Added 38 docs to 'statutes'.
── Ingesting sample cases ────────────────────
Chunking cases: 100%|████████| 12/12
[VectorStore] Added 12 docs to 'cases'.
✓ Database ready: 38 statute chunks | 12 case chunks
```

### Step 6 — Start the API server

```bash
uvicorn main:app --reload --port 8000
```

Open http://localhost:8000/docs for the interactive API docs.

---

## How to use

### Option A — REST API (recommended)

**Run a full legal analysis:**
```bash
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{"query": "Can I sue my employer for unpaid wages after termination without notice?"}'
```

**Response includes all agent outputs:**
```json
{
  "query": "...",
  "query_analysis": "...",
  "statute_results": "...",
  "caselaw_results": "...",
  "factcheck_results": "...",
  "draft_memo": "...",
  "citation_report": "...",
  "audit_trail": [...],
  "timing": {...}
}
```

**Check database stats:**
```bash
curl http://localhost:8000/stats
```

**Debug raw retrieval:**
```bash
curl -X POST http://localhost:8000/retrieve \
  -H "Content-Type: application/json" \
  -d '{"query": "unpaid wages", "collection": "statutes", "k": 3}'
```

**Ingest more data from Indian Kanoon** (requires INDIANKANOON_API_KEY in .env):
```bash
curl -X POST http://localhost:8000/ingest/kanoon \
  -H "Content-Type: application/json" \
  -d '{"query": "maternity benefit dismissal", "max_docs": 15, "collection": "cases"}'
```

### Option B — Python directly

```python
from agents.orchestrator import LegalOrchestrator

orch   = LegalOrchestrator()
result = orch.run("Can I sue my employer for unpaid wages?")

print(result["draft_memo"])
print(result["citation_report"])
print(result["audit_trail"])
```

### Option C — Run the benchmark

```bash
# Run all 15 test queries (takes ~20 minutes, 7 API calls per query)
python -m benchmark.evaluator

# Run only specific queries
python -m benchmark.evaluator --ids q01 q02 q03

# Run only the baseline (1 API call per query, fast)
python -m benchmark.evaluator --baseline-only
```

Results are saved to:
- `benchmark_results.json` — raw per-query scores
- `benchmark_summary.txt`  — comparison table (Baseline vs LexAudit)

---

## Adding more data

### From Indian Kanoon (free API, 500 calls/day)

1. Sign up at https://api.indiankanoon.org/
2. Add your key to `.env`: `INDIANKANOON_API_KEY=your-key`
3. Run:

```bash
python -m data.ingest --kanoon "retrenchment compensation" --max 20
python -m data.ingest --kanoon "maternity benefit dismissal" --max 20
python -m data.ingest --kanoon "minimum wages claim" --max 20
```

### From India Code (statutes)

Download Acts as PDF from https://indiacode.nic.in, then add entries to
`data/sample_statutes.py` following the same structure (id, title, text, act, sections, status, tags).
Re-run `python scripts/setup_db.py` to re-ingest.

---

## Research angle — what to measure

The benchmark evaluator computes these metrics for every query:

| Metric | What it measures |
|--------|-----------------|
| `citation_accuracy` | Fraction of expected citations found in output |
| `fact_check_coverage` | Whether Labour Code commencement issue is flagged |
| `amendment_awareness` | Whether amended/pending statutes are flagged |
| `key_facts_score` | Fraction of key legal facts mentioned |
| `hallucination_flag` | Whether ❌ Suspect citations appear in output |

**The research contribution:** Show that LexAudit's multi-agent pipeline
achieves higher `citation_accuracy` and `fact_check_coverage` than the
single-call baseline, especially on hard queries involving Labour Code
commencement status and amended statutes.

---

## API keys needed

| Service | Free tier | Where to get |
|---------|-----------|-------------|
| Anthropic (Claude) | Pay-per-use | https://console.anthropic.com |
| Indian Kanoon | 500 calls/day free | https://api.indiankanoon.org/ |

The embedding model (sentence-transformers) is fully local — no API key needed.

---

## Typical response times

| Component | Time |
|-----------|------|
| Database setup (first time) | ~60 seconds |
| Single query — baseline | 5–10 seconds |
| Single query — LexAudit (6 agents) | 40–70 seconds |
| Full benchmark (15 queries × 7 calls) | ~15–20 minutes |

---

## Troubleshooting

**`No module named 'chromadb'`** → run `pip install -r requirements.txt`

**`ANTHROPIC_API_KEY not found`** → make sure `.env` exists and has the key

**Empty retrieval results** → run `python scripts/setup_db.py` first

**Rate limit errors** → the orchestrator retries automatically with exponential backoff

**Indian Kanoon returns nothing** → check your API key and that you have calls remaining
