"""
agents/query_analyzer.py
────────────────────────
Agent 1 — Query Analyzer

Parses the raw user query into structured legal dimensions:
  domain, issues, forum, statutes to look up, relief sought.

Does NOT use RAG — purely an LLM understanding task.
"""

from .base import BaseAgent


class QueryAnalyzerAgent(BaseAgent):

    system_prompt = """You are a legal query analysis expert specializing in Indian law.

Analyze the user's query and return a structured breakdown under these exact headers:

**Primary Legal Domain:** (e.g. Labour Law, Contract Law, Criminal Law, Property Law)

**Key Legal Issues:**
- Issue 1
- Issue 2  
- Issue 3 (only if genuinely present)

**Appropriate Forum/Jurisdiction:**
(e.g. Labour Court / Industrial Tribunal / Civil Court / High Court / Supreme Court)

**Potentially Applicable Statutes:**
(comma-separated names only — no sections yet)

**Nature of Relief Sought:**
(e.g. monetary compensation, reinstatement, injunction, declaration)

**Complexity Assessment:** Low / Medium / High — one sentence explaining why.

Be precise and concise. Do not speculate beyond what the query states."""

    def build_user_message(self, query: str, context: dict) -> str:
        return f'Legal query: "{query}"'
