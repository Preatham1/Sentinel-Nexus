from knowledge_retriever import retrieve_documents
from document_selector import select_documents
from context_builder import build_context

question = input("Question:\n> ")

documents = retrieve_documents()

selected = select_documents(
    question,
    documents
)

context = build_context(selected)

print(context)