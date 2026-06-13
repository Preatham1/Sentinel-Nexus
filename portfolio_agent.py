from knowledge_retriever import retrieve_documents


def analyze_portfolio():

    documents = retrieve_documents()

    results = []

    for doc in documents:

        if not doc["filename"].startswith("project_"):
            continue

        content = doc["content"].lower()

        score = 0

        if "at risk" in content:
            score += 80

        if "delayed" in content:
            score += 70

        if "blocked" in content:
            score += 50

        if "security" in content:
            score += 40

        if "on track" in content:
            score -= 40

        # Prevent negative scores
        score = max(score, 0)

        if score >= 100:
            status = "HIGH RISK"

        elif score >= 40:
            status = "MEDIUM RISK"

        else:
            status = "LOW RISK"

        # Clean project name
        project_name = (
            doc["filename"]
            .replace("project_", "")
            .replace(".txt", "")
            .title()
        )

        results.append({
            "project": project_name,
            "score": score,
            "status": status
        })

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results