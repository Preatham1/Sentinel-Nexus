from risk_agent import analyze_risk

sample = """
Risk Level: Critical
Major outage detected.
"""

result = analyze_risk(
    sample
)

print(result)