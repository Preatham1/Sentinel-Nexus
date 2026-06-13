import google.generativeai as genai

from config import GEMINI_API_KEY

genai.configure(
    api_key=GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_action_plan(analysis):

    prompt = f"""
You are a Fortune 500 Chief Risk Officer.

Based on this incident analysis:

{analysis}

Generate:

1. Immediate Actions
2. Short-Term Actions
3. Long-Term Actions

Use bullet points.
Be concise.
"""

    try:

        response = model.generate_content(
            prompt
        )

        return response.text

    except Exception:

        return """
IMMEDIATE ACTIONS
• Escalate incident to leadership
• Activate incident response process
• Stabilize affected systems

SHORT-TERM ACTIONS
• Restore impacted services
• Notify stakeholders
• Investigate root cause

LONG-TERM ACTIONS
• Strengthen monitoring
• Improve security controls
• Review operational procedures
"""