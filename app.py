import streamlit as st

st.set_page_config(
    page_title="AI Clinic",
    layout="wide"
)

st.title("🤖 AI CLINIC – Preventive Health Platform")

st.markdown(
    """
    Welcome to **AI Clinic**, an AI-powered preventive healthcare platform.

    👉 Please use the **sidebar** to:
    - Login
    - View your profile
    - Select a report
    - Predict your current health state
    """
)

# Safety redirect
if "logged_in" not in st.session_state:
    st.info("🔐 Please login to access AI Clinic features.")
