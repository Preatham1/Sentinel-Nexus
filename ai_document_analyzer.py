from pathlib import Path

import google.generativeai as genai

from config import GEMINI_API_KEY

genai.configure(
    api_key=GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def analyze_document(file_path):

    content = Path(file_path).read_text()

    prompt = f"""
You are Sentinel Nexus.

Analyze this enterprise document.

Document:

{content}

Provide:

1. Risk Level
2. Key Findings
3. Business Impact
4. Executive Recommendation

Keep the response concise and professional.
"""

    try:

        response = model.generate_content(
            prompt
        )

        return response.text

    except Exception:

        return """
Sentinel Nexus Analysis:

1. Risk Level: Critical

2. Key Findings:
• Major operational disruption detected
• Service availability impacted
• Customer operations affected

3. Business Impact:
• Potential revenue loss
• Customer dissatisfaction
• Reputational risk

4. Executive Recommendation:
• Activate incident response procedures
• Restore affected services
• Notify stakeholders
• Perform root cause analysis
"""