from knowledge_retriever import retrieve_documents
from context_builder import build_context

from operations_agent import analyze
from risk_agent import analyze_risk
from executive_agent import generate_summary


def run_orchestrator(context):

    documents = retrieve_documents()

    knowledge_context = build_context(
        documents
    )

    enhanced_context = f"""
ENTERPRISE KNOWLEDGE BASE

{knowledge_context}

--------------------------------

CURRENT DOCUMENT

{context}
"""

    operations = analyze(
        enhanced_context
    )

    risk = analyze_risk(
        enhanced_context
    )

    executive = generate_summary(
        operations,
        {
            "risk_level":
            risk["severity"]
        }
    )

    return {
        "operations": operations,
        "risk": risk,
        "executive": executive
    }