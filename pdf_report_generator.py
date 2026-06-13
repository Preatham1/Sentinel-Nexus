from datetime import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def generate_pdf_report(
    analysis,
    trend,
    prediction,
    action_plan
):

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = (
        f"Sentinel_Nexus_Report_{timestamp}.pdf"
    )

    pdf = SimpleDocTemplate(
        filename
    )

    styles = getSampleStyleSheet()

    content = [

        Paragraph(
            "Sentinel Nexus Executive Report",
            styles["Title"]
        ),

        Spacer(1, 20),

        Paragraph(
            "Executive Briefing",
            styles["Heading2"]
        ),

        Paragraph(
            analysis,
            styles["BodyText"]
        ),

        Spacer(1, 15),

        Paragraph(
            "Trend Intelligence",
            styles["Heading2"]
        ),

        Paragraph(
            trend,
            styles["BodyText"]
        ),

        Spacer(1, 15),

        Paragraph(
            "Predictive Intelligence",
            styles["Heading2"]
        ),

        Paragraph(
            prediction,
            styles["BodyText"]
        ),

        Spacer(1, 15),

        Paragraph(
            "Executive Copilot Action Plan",
            styles["Heading2"]
        ),

        Paragraph(
            action_plan,
            styles["BodyText"]
        )

    ]

    pdf.build(content)

    return filename