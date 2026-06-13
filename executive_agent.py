def generate_summary(findings, risk_report):

    summary = []

    risk_level = risk_report["risk_level"]

    summary.append(
        f"Project risk level is {risk_level}."
    )

    if risk_level == "CRITICAL":

        summary.append(
            "Immediate executive escalation required."
        )

        summary.append(
            "Business continuity procedures should be activated."
        )

        summary.append(
            "Critical blockers must be resolved immediately."
        )

    elif risk_level == "HIGH":

        summary.append(
            "Immediate action is recommended."
        )

        summary.append(
            "Critical blockers should be resolved first."
        )

    elif risk_level == "MEDIUM":

        summary.append(
            "Project requires close monitoring."
        )

        summary.append(
            "Preventive actions are recommended."
        )

    else:

        summary.append(
            "Project appears healthy."
        )

        summary.append(
            "Continue normal execution."
        )

    return "\n".join(summary)