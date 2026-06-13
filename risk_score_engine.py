from incident_database import get_incidents


def calculate_risk_score():

    incidents = get_incidents()

    if not incidents:
        return 0

    score = 0

    for incident in incidents:

        risk = incident["risk"]

        if risk == "CRITICAL":
            score += 100

        elif risk == "HIGH":
            score += 70

        elif risk == "MEDIUM":
            score += 40

        else:
            score += 10

    score = score / len(incidents)

    return round(score)