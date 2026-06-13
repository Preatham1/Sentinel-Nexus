def select_documents(question, documents):

    question_lower = question.lower()

    selected_docs = []

    if "phoenix" in question_lower:

        for doc in documents:

            if "phoenix" in doc["filename"] \
               or "meeting_notes" in doc["filename"] \
               or "tickets" in doc["filename"]:

                selected_docs.append(doc)

    elif "zeus" in question_lower:

        for doc in documents:

            if "zeus" in doc["filename"]:

                selected_docs.append(doc)

    return selected_docs