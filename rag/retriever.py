"""
rag/retriever.py
─────────────────
High-level retriever that agents call to get relevant legal chunks.

Wraps VectorStore.query() and formats results into a clean
string for prompt injection.
"""

import os
from typing import List, Dict, Optional
from .vector_store import LegalVectorStore


class LegalRetriever:

    def __init__(self, store: Optional[LegalVectorStore] = None):
        self.store = store or LegalVectorStore()

    def retrieve(
        self,
        query: str,
        collection: str = "statutes",
        k: int = 5,
        max_distance: float = 1.5,
    ) -> List[Dict]:
        """
        Retrieve top-k relevant chunks for a query.

        Args:
            query:        natural language search string
            collection:   "statutes" or "cases"
            k:            max results to return
            max_distance: discard chunks beyond this cosine distance
                          (lower = more similar; 0 = identical)

        Returns:
            List of result dicts: {id, text, metadata, distance}
        """
        results = self.store.query(query, collection=collection, k=k)
        return [r for r in results if r["distance"] <= max_distance]

    def retrieve_as_string(
        self,
        query: str,
        collection: str = "statutes",
        k: int = 5,
    ) -> str:
        """
        Retrieve and format as a single string for prompt injection.

        Returns empty string if the collection is empty or no results found.
        """
        results = self.retrieve(query, collection=collection, k=k)
        if not results:
            return ""

        lines = []
        for i, r in enumerate(results, 1):
            meta = r["metadata"]
            src  = meta.get("sections") or meta.get("act") or "Unknown source"
            lines.append(
                f"[Chunk {i} — {src} | similarity distance: {r['distance']:.3f}]\n"
                f"{r['text']}\n"
            )

        return "\n".join(lines)

    def stats(self) -> Dict[str, int]:
        return self.store.stats()
