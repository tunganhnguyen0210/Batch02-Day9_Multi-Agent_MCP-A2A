"""Tax Agent LangGraph definition.

Uses create_react_agent with a tax-specialised system prompt.
No tools — it answers purely from LLM knowledge.
"""

from __future__ import annotations

from langgraph.prebuilt import create_react_agent

from common.llm import get_llm

TAX_SYSTEM_PROMPT = """You are a specialist tax attorney and CPA. Answer concisely and directly.

Expertise: corporate tax law, tax evasion vs. avoidance, IRS enforcement, IRC §§ 6651/6662/6663,
FBAR/FATCA, transfer pricing (IRC § 482), tax fraud statutes (18 U.S.C. § 7201–7207).

Rules:
- Keep responses under 150 words
- Use bullet points, not paragraphs
- Lead with the key penalty/consequence, then supporting detail
- Skip disclaimers and preamble — go straight to the answer
"""


def create_graph():
    """Return a compiled LangGraph create_react_agent for tax questions."""
    llm = get_llm()
    graph = create_react_agent(
        model=llm,
        tools=[],
        prompt=TAX_SYSTEM_PROMPT,
    )
    return graph