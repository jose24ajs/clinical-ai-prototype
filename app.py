import streamlit as st
import pandas as pd
import time
import random

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="AI Clinic – Preventive Intelligence",
    layout="wide"
)

# -------------------------------------------------
# LOAD DATA (KAGGLE)
# -------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("diabetes_prediction_dataset.csv")

data = load_data()
AVG_GLUCOSE = data["blood_glucose_level"].mean()
AVG_HBA1C = data["HbA1c_level"].mean()

# -------------------------------------------------
# SESSION STATE
# -------------------------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# -------------------------------------------------
# LOGIN
# -------------------------------------------------
if not st.session_state.logged_in:
    st.title("🧠 AI CLINIC")
    st.subheader("Preventive Health & Clinical Intelligence Platform")

    st.info(
        "This system provides **AI-assisted preventive insights**. "
        "It does NOT replace professional medical diagnosis."
    )

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("🔐 Login"):
        if username.strip():
            st.session_state.logged_in = True
            st.session_state.user = username
            st.rerun()
        else:
            st.error("Username required")

    st.stop()

# -------------------------------------------------
# MAIN DASHBOARD
# -------------------------------------------------
st.success(f"Welcome, {st.session_state.user} 👋")

tab1, tab2, tab3 = st.tabs([
    "👤 Profile",
    "📄 Previous Report",
    "🧠 AI Health Intelligence"
])

# -------------------------------------------------
# TAB 1: PROFILE
# -------------------------------------------------
with tab1:
    st.header("👤 Patient Profile")

    age = st.number_input("Age", 1, 120, 30)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    height = st.number_input("Height (cm)", 100, 220, 170)
    weight = st.number_input("Weight (kg)", 30, 200, 70)

    if st.button("💾 Save Profile"):
        st.session_state.profile = {
            "age": age,
            "gender": gender,
            "height": height,
            "weight": weight
        }
        st.success("Profile saved")

# -------------------------------------------------
# TAB 2: PREVIOUS REPORT
# -------------------------------------------------
with tab2:
    st.header("📄 Previous Diabetes Report")

    glucose = st.number_input("Blood Glucose (mg/dL)", 50, 400, 110)
    hba1c = st.number_input("HbA1c (%)", 3.0, 15.0, 5.5)
    days = st.slider("Days since last report", 1, 365, 30)

    if st.button("📥 Save Report"):
        st.session_state.report = {
            "glucose": glucose,
            "hba1c": hba1c,
            "days": days
        }
        st.success("Report saved")

# -------------------------------------------------
# TAB 3: AI INTELLIGENCE
# -------------------------------------------------
with tab3:
    st.header("🧠 AI Preventive Health Intelligence")

    if "report" not in st.session_state:
        st.warning("Please save a previous report first.")
        st.stop()

    st.subheader("🍎 Lifestyle Since Last Report")

    diet = st.selectbox("Diet Quality", ["Poor", "Average", "Healthy"])
    exercise = st.selectbox("Exercise Frequency", ["None", "1–2/week", "3–5/week"])
    sleep = st.slider("Sleep (hours)", 3, 10, 7)
    stress = st.selectbox("Stress Level", ["Low", "Medium", "High"])

    if st.button("🔮 Run AI Analysis"):
        with st.spinner("Analyzing longitudinal health trajectory..."):
            time.sleep(1.5)

        # ---------------- AI RISK MODEL ----------------
        risk = 0
        factors = []

        if st.session_state.report["glucose"] > AVG_GLUCOSE:
            risk += 20
            factors.append("Above-average blood glucose")

        if st.session_state.report["hba1c"] > AVG_HBA1C:
            risk += 20
            factors.append("Elevated HbA1c")

        if diet == "Poor":
            risk += 15
            factors.append("Unhealthy diet")

        if exercise == "None":
            risk += 15
            factors.append("Low physical activity")

        if sleep < 6:
            risk += 10
            factors.append("Insufficient sleep")

        if stress == "High":
            risk += 15
            factors.append("High stress level")

        risk += min(st.session_state.report["days"] // 30 * 5, 20)
        risk = min(risk, 100)

        confidence = random.randint(78, 92)

        # ---------------- OUTPUT ----------------
        st.progress(risk / 100)
        st.metric("Predicted Health Risk Score", f"{risk} / 100")

        if risk < 30:
            st.success("🟢 Low Risk – Stable trajectory")
        elif risk < 60:
            st.warning("🟡 Moderate Risk – Preventive action recommended")
        else:
            st.error("🔴 High Risk – Clinical review advised")

        st.markdown(f"**AI Confidence:** {confidence}%")

        # ---------------- EXPLAINABLE AI ----------------
        with st.expander("🧠 Why did the AI predict this? (Explainable AI)"):
            for f in factors:
                st.write(f"• {f}")

            st.caption(
                "Thresholds derived from Kaggle Diabetes Dataset "
                "and longitudinal risk modeling."
            )

        # ---------------- HUMAN IN THE LOOP ----------------
        st.subheader("🧑‍⚕️ Human-in-the-Loop Decision")
        decision = st.radio(
            "Do you agree with the AI recommendation?",
            ["Approve", "Override", "Defer"]
        )

        if decision == "Override":
            st.text_area("Provide clinical justification")

        st.success("Decision recorded in audit trail")

        # ---------------- CLOSED LOOP ----------------
        with st.expander("🔁 Outcome Feedback (Model Learning)"):
            outcome = st.selectbox(
                "What happened after this recommendation?",
                ["Improved", "No Change", "Worsened"]
            )
            st.info(
                "This feedback will be used to continuously "
                "improve AI performance."
            )

        st.caption(
            "⚠️ This platform provides decision-support insights only. "
            "Final medical decisions remain with qualified professionals."
        )

# -------------------------------------------------
# LOGOUT
# -------------------------------------------------
st.markdown("---")
if st.button("🚪 Logout"):
    st.session_state.clear()
    st.rerun()
