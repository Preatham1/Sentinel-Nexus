from incident_database import get_incidents


def get_risk_timeline():

    incidents = get_incidents()

    risk_map = {
        "LOW": 10,
        "MEDIUM": 40,
        "HIGH": 70,
        "CRITICAL": 100
    }

    timeline = []

    for incident in incidents:

        timestamp = incident.get(
            "timestamp",
            incident.get("date", "Unknown")
        )

        timeline.append(
            {
                "timestamp": timestamp,
                "score": risk_map.get(
                    incident["risk"],
                    0
                )
            }
        )

    return timeline