def analyze_risk(analysis):

    analysis = analysis.lower()

    if "critical" in analysis:

        return {
            "severity": "CRITICAL",
            "exposure": "Enterprise Wide",
            "impact": [
                "Revenue Loss",
                "Operational Disruption",
                "Customer Impact"
            ],
            "recommendation":
            "Immediate executive escalation required."
        }

    elif "high" in analysis:

        return {
            "severity": "HIGH",
            "exposure": "Multiple Business Units",
            "impact": [
                "Service Disruption",
                "Customer Impact"
            ],
            "recommendation":
            "Accelerated mitigation required."
        }

    else:

        return {
            "severity": "MODERATE",
            "exposure": "Limited",
            "impact": [
                "Localized Impact"
            ],
            "recommendation":
            "Continue monitoring."
        }