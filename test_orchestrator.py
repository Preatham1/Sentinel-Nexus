from agent_orchestrator import run_orchestrator

sample = """
Critical outage detected.
Customer transactions failing.
"""

result = run_orchestrator(
    sample
)

print(result)