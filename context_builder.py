#context_builder.py
def build_context(selected_documents):

    context = ""

    for doc in selected_documents:

        context += f"\n\nDOCUMENT: {doc['filename']}\n"
        context += doc["content"]

    return context