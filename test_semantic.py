from semantic_retriever import find_relevant_projects

question = input("Question:\n> ")

results = find_relevant_projects(question)

print("\n=== RESULTS ===\n")

for item in results:

    print(
        item["project"],
        "-",
        item["status"]
    )