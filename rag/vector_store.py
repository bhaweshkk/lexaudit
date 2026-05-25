"""
rag/vector_store.py
────────────────────
ChromaDB wrapper with sentence-transformer embeddings.

Two collections:
  - "statutes" : Indian acts and sections
  - "cases"    : SC / HC judgment summaries

Embeddings use sentence-transformers/all-MiniLM-L6-v2
(80 MB, runs locally, no API key needed).
"""

import os
from typing import List, Dict, Any

import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()

PERSIST_DIR     = os.getenv("CHROMA_PERSIST_DIR", "./chroma_db")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")


class LegalVectorStore:

    def __init__(self):
        self.client = chromadb.PersistentClient(
            path=PERSIST_DIR,
            settings=Settings(anonymized_telemetry=False),
        )
        print(f"[VectorStore] Loading embedding model: {EMBEDDING_MODEL}")
        self.embedder = SentenceTransformer(EMBEDDING_MODEL)
        self.statutes = self.client.get_or_create_collection("statutes")
        self.cases    = self.client.get_or_create_collection("cases")
        print("[VectorStore] Ready.")

    def _embed(self, texts: List[str]) -> List[List[float]]:
        return self.embedder.encode(texts, show_progress_bar=False).tolist()

    def _collection(self, name: str):
        return self.statutes if name == "statutes" else self.cases

    def add_documents(self, docs: List[Dict[str, Any]], collection: str = "statutes") -> int:
        """
        Add documents to the vector store.

        Args:
            docs: list of dicts with keys:
                  id       (str)  — unique identifier
                  text     (str)  — content to embed
                  metadata (dict) — arbitrary metadata stored alongside the chunk
            collection: "statutes" or "cases"

        Returns:
            Number of documents added.
        """
        col = self._collection(collection)

        ids       = [d["id"] for d in docs]
        texts     = [d["text"] for d in docs]
        metadatas = [d.get("metadata", {}) for d in docs]

        existing  = set(col.get(ids=ids)["ids"])
        new_docs  = [d for d in docs if d["id"] not in existing]

        if not new_docs:
            print(f"[VectorStore] All {len(docs)} docs already in '{collection}' — skipping.")
            return 0

        new_ids   = [d["id"] for d in new_docs]
        new_texts = [d["text"] for d in new_docs]
        new_meta  = [d.get("metadata", {}) for d in new_docs]
        embeds    = self._embed(new_texts)

        col.add(ids=new_ids, documents=new_texts, embeddings=embeds, metadatas=new_meta)
        print(f"[VectorStore] Added {len(new_docs)} docs to '{collection}'.")
        return len(new_docs)

    def query(self, query_text: str, collection: str = "statutes", k: int = 5) -> List[Dict]:
        """
        Retrieve the top-k most similar documents for a query.

        Args:
            query_text: natural language query string
            collection: "statutes" or "cases"
            k:          number of results to return

        Returns:
            List of dicts: {"id", "text", "metadata", "distance"}
        """
        col    = self._collection(collection)
        embed  = self._embed([query_text])
        result = col.query(query_embeddings=embed, n_results=min(k, col.count()))

        if not result["ids"] or not result["ids"][0]:
            return []

        results = []
        for i in range(len(result["ids"][0])):
            results.append({
                "id":       result["ids"][0][i],
                "text":     result["documents"][0][i],
                "metadata": result["metadatas"][0][i],
                "distance": result["distances"][0][i],
            })
        return results

    def stats(self) -> Dict[str, int]:
        return {
            "statutes": self.statutes.count(),
            "cases":    self.cases.count(),
        }

    def reset(self, collection: str = None):
        if collection:
            self._collection(collection).delete(
                where={"_dummy": {"$ne": True}}
            )
        else:
            self.client.delete_collection("statutes")
            self.client.delete_collection("cases")
            self.statutes = self.client.get_or_create_collection("statutes")
            self.cases    = self.client.get_or_create_collection("cases")
        print(f"[VectorStore] Reset {'all collections' if not collection else collection}.")
