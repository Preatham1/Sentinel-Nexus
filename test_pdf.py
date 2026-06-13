from pdf_report_generator import (
    generate_pdf_report
)

file = generate_pdf_report(
    "Critical security incident detected.",
    "Risk remains CRITICAL.",
    "High probability of future incidents."
)

print(file)