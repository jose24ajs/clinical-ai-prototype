import streamlit as st

st.set_page_config(
    page_title="AI Clinic",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🤖 AI CLINIC")
st.sidebar.markdown("### Navigation")

page = st.sidebar.radio(
    "Go to:",
    ["🏠 Home", "🔐 Login", "👤 Profile", "📄 Select Report", "🧠 Predict Health"]
)

# ---------------- PAGE ROUTING ----------------
if page == "🔐 Login":
    st.switch_page("pages/1_Login.py")

elif page == "👤 Profile":
    st.switch_page("pages/2_Profile.py")

elif page == "📄 Select Report":
    st.switch_page("pages/3_Report_Select.py")

elif page == "🧠 Predict Health":
    st.switch_page("pages/4_Predictor.py")

# ---------------- HOME PAGE ----------------
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
