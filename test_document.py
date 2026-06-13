from document_analyzer import analyze_document

result = analyze_document(
    "data/project_atlas.txt"
)

print("\n=== DOCUMENT ANALYSIS ===\n")

for item in result:
    print("-", item)