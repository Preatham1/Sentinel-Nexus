from knowledge_retriever import retrieve_documents
from document_selector import select_documents
from context_builder import build_context

from executive_agent import generate_summary
from operations_agent import analyze
from risk_agent import assess_risk


question = input("Ask Sentinel Nexus a question:\n> ")
question_lower = question.lower()


# =================================
# KNOWLEDGE RETRIEVAL PIPELINE
# =================================

documents = retrieve_documents()

selected_documents = select_documents(
    question,
    documents
)

context = build_context(
    selected_documents
)

print("\n=== RETRIEVED DOCUMENTS ===\n")

for doc in selected_documents:
    print("-", doc["filename"])


# =================================
# RISK WORKFLOW
# =================================

if "risk" in question_lower:

    findings = analyze(context)

    risk_report = assess_risk(findings)

    print("\n=== RISK AGENT REPORT ===\n")

    print(f"Risk Score : {risk_report['risk_score']}")
    print(f"Risk Level : {risk_report['risk_level']}")


# =================================
# STATUS WORKFLOW
# =================================

elif "status" in question_lower:

    findings = analyze(context)

    print("\n=== PROJECT STATUS ===\n")

    for item in findings:
        print("-", item)


# =================================
# ANALYSIS WORKFLOW
# =================================

elif any(word in question_lower for word in [
    "delay",
    "delayed",
    "success",
    "successful",
    "performance",
    "project"
]):

    findings = analyze(context)

    risk_report = assess_risk(findings)

    executive_summary = generate_summary(
        findings,
        risk_report
    )

    print("\n=== OPERATIONS AGENT REPORT ===\n")

    for item in findings:
        print("-", item)

    print("\n=== RISK AGENT REPORT ===\n")

    print(f"Risk Score : {risk_report['risk_score']}")
    print(f"Risk Level : {risk_report['risk_level']}")

    print("\n=== EXECUTIVE AGENT REPORT ===\n")

    print(executive_summary)


# =================================
# UNKNOWN QUESTION
# =================================

else:

    print("\nSentinel Nexus cannot answer that question yet.")