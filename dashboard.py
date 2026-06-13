# dashboard.py
import streamlit as st
import pandas as pd
from portfolio_agent import analyze_portfolio
from semantic_retriever import find_relevant_projects
from executive_chat import ask_executive_copilot

st.set_page_config(
    page_title="Sentinel Nexus",
    layout="wide"
)

st.title(" Sentinel Nexus Command Center")

st.markdown(
    "Enterprise Intelligence Operating System"
)

projects = analyze_portfolio()

total_projects = len(projects)

high_risk = len(
    [p for p in projects if p["status"] == "HIGH RISK"]
)

medium_risk = len(
    [p for p in projects if p["status"] == "MEDIUM RISK"]
)

low_risk = len(
    [p for p in projects if p["status"] == "LOW RISK"]
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Projects",
    total_projects
)

col2.metric(
    "High Risk",
    high_risk
)

col3.metric(
    "Medium Risk",
    medium_risk
)

col4.metric(
    "Low Risk",
    low_risk
)

st.subheader("Project Portfolio")

for project in projects:

    status = project["status"]

    if status == "HIGH RISK":

        st.error(
            f"{project['project']} | Score: {project['score']} | {status}"
        )

    elif status == "MEDIUM RISK":

        st.warning(
            f"{project['project']} | Score: {project['score']} | {status}"
        )

    else:

        st.success(
            f"{project['project']} | Score: {project['score']} | {status}"
        )

st.subheader("Executive Summary")

highest_risk = projects[0]

st.write(
    f"Immediate attention required: {highest_risk['project']}"
)
chart_data = pd.DataFrame(
    {
        "Project": [
            p["project"]
            for p in projects
        ],
        "Risk Score": [
            p["score"]
            for p in projects
        ]
    }
)

st.subheader("Risk Distribution")

st.bar_chart(
    chart_data.set_index("Project")
)
st.divider()

st.subheader(" Ask Sentinel Nexus")

question = st.text_input(
    "Ask a question about your project portfolio"
)

if st.button("Analyze"):

    if question:

        results = find_relevant_projects(question)

        st.subheader("Results")

        for item in results:

            if item["status"] == "HIGH RISK":

                st.error(
                    f"{item['project']} - {item['status']}"
                )

            elif item["status"] == "MEDIUM RISK":

                st.warning(
                    f"{item['project']} - {item['status']}"
                )

            else:

                st.success(
                    f"{item['project']} - {item['status']}"
                )
st.divider()
st.subheader("Executive Chat Copilot")

question = st.chat_input(
    "Ask Sentinel Nexus..."
)

if question:

    answer = ask_executive_copilot(
        question
    )

    st.write(answer)
