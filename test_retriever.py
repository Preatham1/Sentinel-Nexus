from knowledge_retriever import retrieve_documents

docs = retrieve_documents()

for doc in docs:

    print("\n==========")
    print(doc["filename"])
    print("==========")

    print(doc["content"])