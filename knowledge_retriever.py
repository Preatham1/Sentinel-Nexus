#knowledge_retriever.py
from pathlib import Path

DATA_FOLDER = Path("data")


def retrieve_documents():

    documents = []

    for file in DATA_FOLDER.glob("*.txt"):

        documents.append(
            {
                "filename": file.name,
                "content": file.read_text()
            }
        )

    return documents