from pathlib import Path


def analyze_document(file_path):

    content = Path(file_path).read_text()

    findings = []

    text = content.lower()

    if "security" in text:
        findings.append("Security issue detected")

    if "delayed" in text:
        findings.append("Project delay detected")

    if "blocked" in text:
        findings.append("Critical blocker detected")

    if "failure" in text:
        findings.append("Failure reported")

    if not findings:
        findings.append("No major risks detected")

    return findings