import streamlit as st

if "logged_in" not in st.session_state:
    st.warning("Please login first.")
    st.stop()

st.title("🧠 AI Health Prediction")

report = st.session_state.get("selected_report", "Health")
st.subheader(f"Selected Report: {report}")

diet = st.selectbox("🍽 Diet", ["Balanced", "High Sugar", "Junk Food"])
exercise = st.selectbox("🏃 Exercise", ["Daily", "Occasional", "None"])
sleep = st.slider("😴 Sleep (hours)", 3, 9, 6)
stress = st.selectbox("😰 Stress Level", ["Low", "Medium", "High"])

if st.button("Run Prediction"):
    risk = 0
    reasons = []

    if diet != "Balanced":
        risk += 20; reasons.append("Poor diet")
    if exercise == "None":
        risk += 20; reasons.append("No exercise")
    if sleep < 6:
        risk += 15; reasons.append("Low sleep")
    if stress == "High":
        risk += 20; reasons.append("High stress")

    st.markdown("---")

    if risk >= 60:
        st.error("🔴 High Risk Detected")
    elif risk >= 30:
        st.warning("🟡 Moderate Risk")
    else:
        st.success("🟢 Stable Health")

    st.markdown("### 🧠 Why?")
    for r in reasons:
        st.write(f"- {r}")
