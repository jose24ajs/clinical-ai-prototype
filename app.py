import streamlit as st

st.set_page_config(
    page_title="AI Clinic",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🧠 AI CLINIC – Preventive Health Platform")

st.markdown("""
Welcome to **AI Clinic**, an AI-powered preventive healthcare platform.

👉 Use the **left sidebar** to:
- 🔐 Login
- 👤 View your profile
- 📄 Select a health report
- 🧠 Predict your current health state
""")

if "logged_in" not in st.session_state:
    st.info("🔐 Please login to access AI Clinic features.")

