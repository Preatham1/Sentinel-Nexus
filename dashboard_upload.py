# dashboard_upload.py
import streamlit as st
import pandas as pd
from agent_orchestrator import run_orchestrator
from executive_chat import ask_executive_copilot
from pdf_report_generator import generate_pdf_report
from ai_document_analyzer import analyze_document
from incident_database import save_incident, get_incidents
from trend_analyzer import analyze_trends
from prediction_engine import predict_next_risk
from executive_copilot import generate_action_plan
from timeline_engine import get_risk_timeline
from risk_score_engine import calculate_risk_score
from agent_formatter import (
    format_operations,
    format_risk,
    format_executive
)

st.set_page_config(
    page_title="Sentinel Nexus Upload Center",
    layout="wide"
)

st.title("Sentinel Nexus Document Intelligence")

uploaded_file = st.file_uploader(
    "Upload Enterprise Document",
    type=["txt"]
)

if uploaded_file:
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Document uploaded successfully.")

    if st.button("Analyze Document"):
        analysis = analyze_document(uploaded_file.name)
        st.session_state["analysis"] = analysis

        if "Critical" in analysis:
            risk = "CRITICAL"
        elif "High" in analysis:
            risk = "HIGH"
        elif "Medium" in analysis:
            risk = "MEDIUM"
        else:
            risk = "LOW"

        save_incident(uploaded_file.name, risk)

if "analysis" in st.session_state:
    analysis = st.session_state["analysis"]

    st.subheader("Executive Briefing")
    st.write(analysis)
    st.info(
        """
        Agent Orchestration Flow

        Upload → Operations Agent →
        Risk Agent →
        Executive Agent →
        Executive Decision
        """
    )

    # --- Multi-Agent Intelligence Section ---
    st.divider()
    st.subheader("Multi-Agent Intelligence")

    results = run_orchestrator(analysis)

    operations_findings = results["operations"]
    risk_assessment = results["risk"]
    executive_summary = results["executive"]

    st.write("Operations Agent Assessment")
    for item in format_operations(operations_findings):
        st.markdown(item)

    st.write("Risk Agent Assessment")
    st.text(format_risk(risk_assessment))

    st.write("Executive Agent Summary")
    st.text(format_executive(executive_summary))

    st.divider()
    st.subheader("Executive Copilot")

    action_plan = generate_action_plan(analysis)
    st.write(action_plan)

    st.divider()
    st.subheader("Executive Report")

    if st.button("Generate PDF Report"):
        pdf_file = generate_pdf_report(
            analysis,
            analyze_trends(),
            predict_next_risk(),
            action_plan
        )

        st.success(f"Report generated: {pdf_file}")

        with open(pdf_file, "rb") as file:
            st.download_button(
                label="📥 Download Report",
                data=file,
                file_name=pdf_file,
                mime="application/pdf"
            )

# --- Executive Dashboard Metrics ---
st.divider()
st.subheader("Executive Dashboard")

incidents = get_incidents()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Risk Score", calculate_risk_score())

with col2:
    st.metric("Incidents", len(incidents))

with col3:
    st.metric("Trend", analyze_trends())

with col4:
    st.metric("Prediction", predict_next_risk())

# --- Risk Score Section ---
st.divider()
st.subheader("Enterprise Risk Score")

score = calculate_risk_score()

if score >= 80:
    st.error(f"{score} / 100")
elif score >= 50:
    st.warning(f"{score} / 100")
else:
    st.success(f"{score} / 100")

timeline = get_risk_timeline()
if timeline:
    timeline_df = pd.DataFrame(timeline)
    st.subheader("Enterprise Risk Trend")
    timeline_df["timestamp"] = pd.to_datetime(timeline_df["timestamp"])
    st.line_chart(timeline_df.set_index("timestamp"))

# --- Incident History Section ---
st.subheader("Incident History")

incidents = get_incidents()
if incidents:
    df = pd.DataFrame(incidents)

    st.subheader("Incident Database")
    st.dataframe(df, use_container_width=True)

    st.subheader("Risk Analytics")
    risk_counts = df["risk"].value_counts().sort_index()
    st.bar_chart(risk_counts, height=300)

    st.subheader("Trend Intelligence")
    trend = analyze_trends()
    if "CRITICAL" in trend:
        st.error(trend)
    elif "HIGH" in trend:
        st.warning(trend)
    else:
        st.info(trend)

    st.subheader("Predictive Intelligence")
    prediction = predict_next_risk()
    if "critical" in prediction.lower():
        st.error(prediction)
    elif "high" in prediction.lower():
        st.warning(prediction)
    else:
        st.success(prediction)

    st.subheader("Incident Feed")
    for incident in reversed(incidents):
        risk = incident["risk"]
        time_value = incident.get("timestamp", incident.get("date", "Unknown"))
        message = f"{time_value} | {incident['file']} → {risk}"

        if risk == "CRITICAL":
            st.error(message)
        elif risk == "HIGH":
            st.warning(message)
        elif risk == "MEDIUM":
            st.info(message)
        else:
            st.success(message)

    # --- Executive Chat Copilot Section ---
    st.divider()
    st.subheader("Executive Chat Copilot")

    chat_question = st.chat_input(
        "Ask about incidents, risks, policies, or projects..."
    )

    if chat_question:
        answer = ask_executive_copilot(chat_question)
        st.write(answer)

else:
    st.info("No incidents analyzed yet.")
