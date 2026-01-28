import streamlit as st

st.set_page_config(
    page_title="AI Clinic",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🤖 AI CLINIC – Preventive Health Platform")

if "logged_in" not in st.session_state:
    st.info("🔐 Please login to access AI Clinic features.")
