import google.generativeai as genai

from config import GEMINI_API_KEY
from knowledge_retriever import retrieve_documents
from context_builder import build_context

genai.configure(
    api_key=GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def ask_executive_copilot(question):

    docs = retrieve_documents()

    context = build_context(docs)

    prompt = f"""
You are Sentinel Nexus Executive Copilot.

Enterprise Knowledge:

{context}

Question:

{question}

Provide a concise executive response.
"""

    try:

        response = model.generate_content(
            prompt
        )

        return response.text

    except Exception:

        return (
            "Executive Copilot is "
            "currently unavailable."
        )