from knowledge_retriever import retrieve_documents
from document_selector import select_documents

question = input("Ask a question:\n> ")

documents = retrieve_documents()

selected = select_documents(
    question,
    documents
)

print("\nSELECTED DOCUMENTS:\n")

for doc in selected:

    print("-", doc["filename"])