import streamlit as st

st.set_page_config(
    page_title="AI Clinic",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---- FORCE SIDEBAR ----
with st.sidebar:
    st.title("🤖 AI CLINIC")
    st.markdown("### Pages")
    st.markdown(
        """
        Use the **Pages menu above** ☝️  
        to navigate through the app.
        """
    )

# ---- MAIN PAGE ----
st.title("🧠 AI CLINIC – Preventive Health Platform")

st.markdown("""
Welcome to **AI Clinic**, an AI-powered preventive healthcare platform.

👉 **Steps to use this app:**
1. Open the **left sidebar**
2. Click **1_Login**
3. Login with your username
4. Navigate to Profile, Report Select, and Predictor
""")

if "logged_in" not in st.session_state:
    st.warning("🔐 Please login to access AI Clinic features.")
