import streamlit as st

if "logged_in" not in st.session_state:
    st.warning("Please login first.")
    st.stop()

st.title("🗂 Select Health Report")

choice = st.radio(
    "Choose a report:",
    ["👁 Eye Health", "❤️ Heart Health", "🩸 Blood Sugar"]
)

st.session_state["selected_report"] = choice

if st.button("Predict Current State"):
    st.switch_page("pages/4_Predictor.py")
