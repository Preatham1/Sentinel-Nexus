from incident_database import get_incidents


def predict_next_risk():

    incidents = get_incidents()

    if len(incidents) < 3:

        return "Not enough historical data."

    critical_count = 0

    for incident in incidents:

        if incident["risk"] == "CRITICAL":

            critical_count += 1

    ratio = critical_count / len(incidents)

    if ratio >= 0.7:

        return (
            "High probability of future critical incidents."
        )

    elif ratio >= 0.4:

        return (
            "Medium probability of future escalation."
        )

    else:

        return (
            "Risk trend appears stable."
        )