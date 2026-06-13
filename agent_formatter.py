def format_operations(findings):

    cleaned = []

    for item in findings:

        item = item.replace("*", "")
        item = item.replace("#", "")
        item = item.strip()

        if not item:
            continue

        if (
            "Operational Issues" in item
            or "Delay Factors" in item
            or "Resource Constraints" in item
            or "Critical Blockers" in item
        ):
            cleaned.append("")
            cleaned.append(f"### {item}")
            cleaned.append("")
        else:
            cleaned.append(f"• {item}")

    return cleaned


def format_risk(risk):

    output = []

    output.append(
        f"Severity: {risk['severity']}"
    )

    output.append(
        f"Exposure: {risk['exposure']}"
    )

    output.append("")
    output.append("Business Impact:")

    for impact in risk["impact"]:
        output.append(
            f"• {impact}"
        )

    output.append("")
    output.append(
        f"Recommendation: {risk['recommendation']}"
    )

    return "\n".join(output)


def format_executive(summary):

    return summary