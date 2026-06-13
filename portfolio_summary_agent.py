from portfolio_agent import analyze_portfolio


def generate_portfolio_summary():

    projects = analyze_portfolio()

    print("\n=== EXECUTIVE PORTFOLIO SUMMARY ===\n")

    highest_risk = projects[0]

    print(
        f"Immediate attention required: {highest_risk['project']}"
    )

    print("\nProject Overview:\n")

    for project in projects:

        if project["status"] == "HIGH RISK":

            print(
                f"{project['project']} -> Escalate immediately"
            )

        elif project["status"] == "MEDIUM RISK":

            print(
                f"{project['project']} -> Recovery plan recommended"
            )

        else:

            print(
                f"{project['project']} -> Healthy"
            )