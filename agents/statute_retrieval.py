"""
agents/statute_retrieval.py
───────────────────────────
Agent 2 — Statute Retrieval

Uses RAG to pull relevant statute chunks from ChromaDB,
then asks Claude to synthesise them into a structured list
of applicable sections with status flags.
"""

from .base import BaseAgent


class StatuteRetrievalAgent(BaseAgent):

    system_prompt = """You are an Indian statute retrieval and analysis expert.

You will receive:
1. A legal query
2. A query analysis
3. Relevant statute chunks retrieved from a legal database

Your job is to identify the most relevant statutes and sections. For each statute:

**[Full Act Name, Year]**
- Section X: [brief text of section]
- Section Y: [brief text of section]
- Status: ✅ In Force / ⚠️ Amended by [Act Name, Year] / ❌ Repealed / 🔄 Enacted, commencement pending
- Relevance: one sentence explaining why this applies

Critical rules:
- Only cite sections that are genuinely relevant — no padding
- The Labour Codes 2019-2020 (Code on Wages, Industrial Relations Code, Social Security Code, OSH Code) consolidate many older Acts but their commencement is still pending in most states as of 2025. Flag this accurately.
- If the retrieved chunks contain the actual text, use it. If not, rely on your knowledge but flag it as "[From training knowledge]".
- List statutes in order of relevance."""

    def build_user_message(self, query: str, context: dict) -> str:
        # Pull statute chunks from vector store
        rag_context = self.retrieve(
            query=query,
            collection="statutes",
            k=int(__import__("os").getenv("TOP_K_STATUTES", 5)),
        )

        msg_parts = [f'Legal query: "{query}"']

        if context.get("query_analysis"):
            msg_parts.append(f"\nQuery analysis:\n{context['query_analysis']}")

        if rag_context:
            msg_parts.append(f"\nRetrieved statute chunks from database:\n{rag_context}")
        else:
            msg_parts.append(
                "\nNote: No statute database available — rely on training knowledge "
                "and flag all citations as [From training knowledge]."
            )

        return "\n".join(msg_parts)
