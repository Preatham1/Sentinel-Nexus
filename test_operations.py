from operations_agent import analyze

sample = """
Critical outage detected.
Customer transactions failing.
Resource shortage observed.
"""

print(
    analyze(sample)
)