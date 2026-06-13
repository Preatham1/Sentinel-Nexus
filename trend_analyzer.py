from incident_database import get_incidents


def analyze_trends():

    incidents = get_incidents()

    if len(incidents) < 2:
        return "Not enough incident history."

    latest = incidents[-1]
    previous = incidents[-2]

    current_risk = latest["risk"]
    previous_risk = previous["risk"]

    if current_risk == previous_risk:

        return (
            f"No change detected. "
            f"Risk remains {current_risk}."
        )

    return (
        f"Risk changed from "
        f"{previous_risk} "
        f"to "
        f"{current_risk}."
    )