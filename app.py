import streamlit as st

st.set_page_config(
    page_title="AI Clinic",
    layout="wide"
)

st.title("🧠 AI CLINIC – Preventive Health Platform")

st.markdown("""
Welcome to **AI Clinic**, an AI-powered preventive healthcare platform.

This system predicts a user's **current health state**
using previous reports and lifestyle data.
""")

st.markdown("## 🚀 Get Started")

st.markdown(
    """
    <a href="/1_Login" target="_self">
        <button style="
            background-color:#2563eb;
            color:white;
            padding:14px 30px;
            font-size:18px;
            border:none;
            border-radius:10px;
            cursor:pointer;
        ">
        🔐 Go to Login
        </button>
    </a>
    """,
    unsafe_allow_html=True
)

st.markdown("---")
st.info("After login, you can access Profile, Reports, and Prediction modules.")

