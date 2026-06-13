import streamlit as st

st.set_page_config(page_title="Sentinel Nexus")

page = st.sidebar.selectbox(
    "Select Module",
    [
        "Command Center",
        "Document Intelligence"
    ]
)

if page == "Command Center":
    exec(open("dashboard.py").read())

elif page == "Document Intelligence":
    exec(open("dashboard_upload.py").read())