from executive_agent import generate_summary

findings = [
    "Critical outage detected",
    "Customer transactions failing"
]

risk_report = {
    "risk_level": "CRITICAL"
}

print(
    generate_summary(
        findings,
        risk_report
    )
)