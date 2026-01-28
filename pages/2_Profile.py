import streamlit as st

if "logged_in" not in st.session_state:
    st.warning("Please login first.")
    st.stop()

st.title("👤 Patient Profile")

st.subheader(f"Welcome, {st.session_state['user']}")

st.markdown("### 📁 Previous Medical Reports")

reports = {
    "👁 Eye": "Normal vision, mild strain",
    "❤️ Heart": "Slight BP elevation",
    "🩸 Blood Sugar": "Pre-diabetic range"
}

for r, v in reports.items():
    st.info(f"{r} Report: {v}")

st.markdown("---")

st.success("Current Health Status: 🟡 Moderate Risk (last prediction)")
