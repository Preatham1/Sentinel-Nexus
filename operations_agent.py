import google.generativeai as genai

from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def analyze(context):

    prompt = f"""
You are the Operations Agent of Sentinel Nexus.

Analyze the following enterprise context.

{context}

Identify:

1. Operational issues
2. Delay factors
3. Resource constraints
4. Critical blockers

Return concise bullet points.
"""

    try:
        response = model.generate_content(prompt)

        findings = []

        for line in response.text.split("\n"):

            line = line.strip()

            if line:
                findings.append(line)

        return findings

    except Exception:

        return [
            "AI quota exceeded.",
            "Using fallback operations analysis.",
            "Review incident manually."
        ]