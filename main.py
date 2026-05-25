"""
main.py
────────
LexAudit FastAPI server.

Endpoints:
  GET  /              — health check
  GET  /stats         — vector DB document counts
  POST /analyze       — run the full 6-agent pipeline
  POST /ingest/sample — ingest bundled sample data
  POST /ingest/kanoon — fetch + ingest from Indian Kanoon API
  POST /retrieve      — raw retrieval (debugging)

Start with:
  uvicorn main:app --reload --port 8000
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

from agents.orchestrator import LegalOrchestrator
from rag.retriever       import LegalRetriever
from rag.vector_store    import LegalVectorStore
from data.ingest         import ingest_sample_data, ingest_from_kanoon


app = FastAPI(
    title="LexAudit — Indian Legal Research API",
    description="Multi-agent RAG pipeline for Indian labour and employment law.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

store       = LegalVectorStore()
retriever   = LegalRetriever(store=store)
orchestrator = LegalOrchestrator(retriever=retriever)


# ── Request / Response models ────────────────────────────────────────────────

class AnalyzeRequest(BaseModel):
    query: str

class RetrieveRequest(BaseModel):
    query:      str
    collection: str = "statutes"
    k:          int = 5

class KanoonIngestRequest(BaseModel):
    query:      str
    max_docs:   int = 10
    collection: str = "cases"


# ── Endpoints ────────────────────────────────────────────────────────────────

@app.get("/")
def root():
    return {
        "status":  "LexAudit API running",
        "docs":    "http://localhost:8000/docs",
        "db_stats": store.stats(),
    }


@app.get("/stats")
def stats():
    s = store.stats()
    return {
        "statutes_chunks": s["statutes"],
        "cases_chunks":    s["cases"],
        "message": (
            "Database is empty — run POST /ingest/sample first"
            if s["statutes"] == 0 and s["cases"] == 0
            else "Database ready"
        ),
    }


@app.post("/analyze")
def analyze(req: AnalyzeRequest):
    """
    Run the full 6-agent pipeline on a legal query.

    Returns all agent outputs + citation audit trail.
    Typical response time: 30–60 seconds (6 Claude calls in sequence).
    """
    if not req.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")
    try:
        result = orchestrator.run(req.query, verbose=True)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/ingest/sample")
def ingest_sample():
    """Ingest the bundled sample Indian legal texts into ChromaDB."""
    try:
        stats = ingest_sample_data(store)
        return {"status": "ok", "added": stats}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/ingest/kanoon")
def ingest_kanoon(req: KanoonIngestRequest):
    """
    Fetch documents from Indian Kanoon and ingest into ChromaDB.
    Requires INDIANKANOON_API_KEY in .env
    """
    try:
        n = ingest_from_kanoon(store, query=req.query, max_docs=req.max_docs, collection=req.collection)
        return {"status": "ok", "chunks_added": n}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/retrieve")
def retrieve_raw(req: RetrieveRequest):
    """Raw retrieval endpoint for debugging the vector store."""
    results = retriever.retrieve(req.query, collection=req.collection, k=req.k)
    return {"query": req.query, "collection": req.collection, "results": results}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
