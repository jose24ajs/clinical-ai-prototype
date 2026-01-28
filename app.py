import streamlit as st

st.set_page_config(
    page_title="AI Clinic",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🤖 AI CLINIC")
st.sidebar.markdown("### Navigation")

st.sidebar.page_link("pages/1_Login.py", label="🔐 Login")
st.sidebar.page_link("pages/2_Profile.py", label="👤 Profile")
st.sidebar.page_link("pages/3_Report_Select.py", label="📄 Select Report")
st.sidebar.page_link("pages/4_Predictor.py", label="🧠 Predict Health")

# ---------------- MAIN ----------------
st.title("🧠 AI CLINIC – Preventive Health Platform")

st.markdown(
    """
    Welcome to **AI Clinic**, an AI-powered preventive healthcare platform.

    👉 Use the **left sidebar** to navigate:
    - Login to your account
    - View previous reports
    - Select a health domain
    - Predict your current health state
    """
)

if "logged_in" not in st.session_state:
    st.warning("🔐 Please login to access AI Clinic features.")
