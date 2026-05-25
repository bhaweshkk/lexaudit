"""
agents/orchestrator.py
───────────────────────
LegalOrchestrator — runs all 6 agents in sequence.

Pipeline:
  1. QueryAnalyzerAgent      → query_analysis
  2. StatuteRetrievalAgent   → statute_results    (uses RAG: statutes collection)
  3. CaseLawRetrievalAgent   → caselaw_results    (uses RAG: cases collection)
  4. FactCheckerAgent        → factcheck_results
  5. MemoDrafterAgent        → draft_memo
  6. CitationVerifierAgent   → citation_report
  7. Audit trail generation  → audit_trail (JSON list)

Returns a structured dict with all agent outputs + audit trail.
"""

import json
import time
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

from .query_analyzer    import QueryAnalyzerAgent
from .statute_retrieval import StatuteRetrievalAgent
from .caselaw_retrieval import CaseLawRetrievalAgent
from .fact_checker      import FactCheckerAgent
from .memo_drafter      import MemoDrafterAgent
from .citation_verifier import CitationVerifierAgent
from rag.retriever      import LegalRetriever


AUDIT_SYSTEM = """Generate a JSON audit trail for a legal memo. 
Identify 8 key legal claims from the memo and trace each to its source.
Return ONLY a valid JSON array — no markdown fences, no explanation:
[
  {"claim": "brief description of the claim",
   "source": "authority name (act name + section OR case citation)",
   "type": "statute|case|both",
   "confidence": "high|medium|low"},
  ...
]"""


class LegalOrchestrator:

    def __init__(self, retriever: LegalRetriever = None):
        r = retriever or LegalRetriever()
        self.agents = {
            "query_analyzer":    QueryAnalyzerAgent(retriever=None),
            "statute_retrieval": StatuteRetrievalAgent(retriever=r),
            "caselaw_retrieval": CaseLawRetrievalAgent(retriever=r),
            "fact_checker":      FactCheckerAgent(retriever=None),
            "memo_drafter":      MemoDrafterAgent(retriever=None),
            "citation_verifier": CitationVerifierAgent(retriever=None),
        }
        self.claude = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.model  = os.getenv("CLAUDE_MODEL", "claude-sonnet-4-20250514")

    def _build_audit_trail(self, context: dict) -> list:
        user_msg = (
            f"Memo:\n{context.get('draft_memo','')}\n\n"
            f"Statutes used:\n{context.get('statute_results','')}\n\n"
            f"Cases used:\n{context.get('caselaw_results','')}"
        )
        try:
            r = self.claude.messages.create(
                model=self.model, max_tokens=800,
                system=AUDIT_SYSTEM,
                messages=[{"role": "user", "content": user_msg}],
            )
            raw = r.content[0].text.replace("```json", "").replace("```", "").strip()
            return json.loads(raw)
        except Exception as e:
            print(f"[Orchestrator] Audit trail generation failed: {e}")
            return []

    def run(self, query: str, verbose: bool = True) -> dict:
        """
        Run the full 6-agent pipeline for a legal query.

        Args:
            query:   the user's natural language legal question
            verbose: print progress to stdout

        Returns:
            dict with keys:
              query, query_analysis, statute_results, caselaw_results,
              factcheck_results, draft_memo, citation_report,
              audit_trail, timing
        """
        context = {}
        timing  = {}

        steps = [
            ("query_analysis",    "query_analyzer",    "Query analysis"),
            ("statute_results",   "statute_retrieval", "Statute retrieval (RAG)"),
            ("caselaw_results",   "caselaw_retrieval", "Case law retrieval (RAG)"),
            ("factcheck_results", "fact_checker",      "Fact-checking"),
            ("draft_memo",        "memo_drafter",      "Memo drafting"),
            ("citation_report",   "citation_verifier", "Citation verification"),
        ]

        for out_key, agent_key, label in steps:
            if verbose:
                print(f"  [{label}] running…", end="", flush=True)
            t0 = time.time()
            result = self.agents[agent_key].run(query, context)
            elapsed = round(time.time() - t0, 1)
            context[out_key] = result
            timing[agent_key] = elapsed
            if verbose:
                print(f" done ({elapsed}s)")

        if verbose:
            print("  [Audit trail] generating…", end="", flush=True)
        t0 = time.time()
        audit = self._build_audit_trail(context)
        timing["audit_trail"] = round(time.time() - t0, 1)
        if verbose:
            print(f" done ({timing['audit_trail']}s)")

        return {
            "query":              query,
            "query_analysis":     context.get("query_analysis", ""),
            "statute_results":    context.get("statute_results", ""),
            "caselaw_results":    context.get("caselaw_results", ""),
            "factcheck_results":  context.get("factcheck_results", ""),
            "draft_memo":         context.get("draft_memo", ""),
            "citation_report":    context.get("citation_report", ""),
            "audit_trail":        audit,
            "timing":             timing,
        }
