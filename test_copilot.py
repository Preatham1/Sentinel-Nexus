from executive_copilot import generate_action_plan

sample = """
Risk Level: Critical

Security vulnerability discovered.
Deployment postponed.
Customer data unavailable.
"""

print(
    generate_action_plan(sample)
)