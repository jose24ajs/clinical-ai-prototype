import streamlit as st

st.set_page_config(
    page_title="AI Clinic",
    layout="wide",
    initial_sidebar_state="expanded"  # FORCE sidebar open
)

# ---------- SIDEBAR CONTENT (IMPORTANT) ----------
st.sidebar.title("🤖 AI CLINIC")
st.sidebar.markdown("### Navigation")
st.sidebar.info("Use the pages below ⬇️")

# ---------- MAIN PAGE ----------
st.title("🧠 AI CLINIC – Preventive Health Platform")

st.markdown(
    """
    Welcome to **AI Clinic**, an AI-powered preventive healthcare platform.

    👉 Use the **left sidebar** to:
    - Login
    - View your profile
    - Select a health report
    - Predict your current health state
    """
)

if "logged_in" not in st.session_state:
    st.warning("🔐 Please login to access AI Clinic features.")
