#semantic_retriever.py
from portfolio_agent import analyze_portfolio


def find_relevant_projects(question):

    question = question.lower()

    projects = analyze_portfolio()

    if any(word in question for word in [
        "attention",
        "urgent",
        "critical"
    ]):

        return projects[:1]

    elif any(word in question for word in [
        "risk",
        "risky",
        "struggling"
    ]):

        return projects[:2]

    elif any(word in question for word in [
        "healthy",
        "healthiest",
        "best",
        "successful"
    ]):

        return [projects[-1]]

    return projects