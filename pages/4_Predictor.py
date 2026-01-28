import streamlit as st

if "logged_in" not in st.session_state:
    st.error("Please login first.")
    st.stop()

st.title("🧠 AI Preventive Health Predictor")

if "report" not in st.session_state:
    st.warning("Please select a health report first.")
    st.stop()

st.subheader("🍎 Lifestyle Since Last Report")

diet = st.selectbox("Diet Quality", ["Poor", "Average", "Healthy"])
exercise = st.selectbox("Exercise Frequency", ["None", "1–2 times/week", "3–5 times/week"])
sleep = st.slider("Average Sleep (hours)", 3, 10, 7)
stress = st.selectbox("Stress Level", ["Low", "Medium", "High"])

# ---------------- AI LOGIC (RULE-BASED PREDICTION) ----------------
risk = 0

if diet == "Poor":
    risk += 20
elif diet == "Average":
    risk += 10

if exercise == "None":
    risk += 20
elif exercise == "1–2 times/week":
    risk += 10

if sleep < 6:
    risk += 15

if stress == "High":
    risk += 20
elif stress == "Medium":
    risk += 10

days = st.session_state.report["days"]
risk += min(days // 10, 20)

st.markdown("---")

if st.button("🔮 Predict Current Health"):
    st.subheader("📈 Prediction Result")

    st.metric("Health Risk Score", f"{risk} / 100")

    if risk < 30:
        st.success("🟢 Stable – Maintain your current lifestyle.")
    elif risk < 60:
        st.warning("🟡 Moderate Risk – Improve diet, sleep, and exercise.")
    else:
        st.error("🔴 High Risk – Medical consultation recommended.")

    st.markdown("""
    ### 🧠 Why this prediction?
    This prediction is based on:
    - Previous medical report  
    - Time since last report  
    - Lifestyle changes  
    - Preventive AI rules  

    ⚠️ This is **not a diagnosis**, but a **preventive insight tool**.
    """)
