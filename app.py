import streamlit as st
import pandas as pd

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="AI Clinic – Preventive Health",
    layout="wide"
)

# -------------------------------------------------
# LOAD KAGGLE DATASET
# -------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("diabetes_prediction_dataset.csv")

data = load_data()

# Dataset-based population baselines
AVG_GLUCOSE = data["blood_glucose_level"].mean()
AVG_HBA1C = data["HbA1c_level"].mean()

# -------------------------------------------------
# SESSION STATE
# -------------------------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# -------------------------------------------------
# LOGIN SCREEN
# -------------------------------------------------
if not st.session_state.logged_in:
    st.title("🧠 AI CLINIC – Preventive Health Platform")

    st.markdown("""
    **AI Clinic** is an AI-powered preventive healthcare system.

    It predicts a user's **current health risk**
    using **previous medical reports + lifestyle changes**
    without requiring new clinical tests.
    """)

    st.markdown("---")
    st.subheader("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username.strip() == "":
            st.error("Please enter a username")
        else:
            st.session_state.logged_in = True
            st.session_state.user = username
            st.success("Login successful!")
            st.rerun()

    st.stop()

# -------------------------------------------------
# MAIN APP
# -------------------------------------------------
st.success(f"Welcome, {st.session_state.user} 👋")

tab1, tab2, tab3 = st.tabs([
    "👤 Profile",
    "📄 Previous Report",
    "🧠 Health Prediction"
])

# -------------------------------------------------
# TAB 1: PROFILE
# -------------------------------------------------
with tab1:
    st.header("👤 User Profile")

    age = st.number_input("Age", 1, 120, 25)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    height = st.number_input("Height (cm)", 100, 220, 170)
    weight = st.number_input("Weight (kg)", 30, 200, 65)

    if st.button("Save Profile"):
        st.session_state.profile = {
            "age": age,
            "gender": gender,
            "height": height,
            "weight": weight
        }
        st.success("Profile saved successfully")

# -------------------------------------------------
# TAB 2: PREVIOUS REPORT
# -------------------------------------------------
with tab2:
    st.header("📄 Previous Diabetes Report")

    glucose = st.number_input("Previous Blood Glucose Level (mg/dL)", 50, 400, 110)
    hba1c = st.number_input("Previous HbA1c Level (%)", 3.0, 15.0, 5.5)
    days = st.slider("Days since last report", 1, 365, 30)

    if st.button("Save Report"):
        st.session_state.report = {
            "glucose": glucose,
            "hba1c": hba1c,
            "days": days
        }
        st.success("Report saved. You can now predict your health.")

# -------------------------------------------------
# TAB 3: AI HEALTH PREDICTION
# -------------------------------------------------
with tab3:
    st.header("🧠 AI Preventive Health Predictor")

    if "report" not in st.session_state:
        st.warning("Please save a previous report first.")
        st.stop()

    st.subheader("🍎 Lifestyle Since Last Report")

    diet = st.selectbox("Diet Quality", ["Poor", "Average", "Healthy"])
    exercise = st.selectbox("Exercise Frequency", ["None", "1–2 times/week", "3–5 times/week"])
    sleep = st.slider("Average Sleep (hours)", 3, 10, 7)
    stress = st.selectbox("Stress Level", ["Low", "Medium", "High"])

    # ---------------- RISK CALCULATION ----------------
    risk = 0

    # Kaggle dataset–based thresholds
    if st.session_state.report["glucose"] > AVG_GLUCOSE:
        risk += 20

    if st.session_state.report["hba1c"] > AVG_HBA1C:
        risk += 20

    # Lifestyle impact
    if diet == "Poor":
        risk += 15
    elif diet == "Average":
        risk += 8

    if exercise == "None":
        risk += 15
    elif exercise == "1–2 times/week":
        risk += 8

    if sleep < 6:
        risk += 10

    if stress == "High":
        risk += 15
    elif stress == "Medium":
        risk += 8

    # Time decay effect
    risk += min(st.session_state.report["days"] // 30 * 5, 20)

    risk = min(risk, 100)

    # ---------------- PREDICTION OUTPUT ----------------
    if st.button("🔮 Predict Current Health"):
        st.metric("Health Risk Score", f"{risk} / 100")

        if risk < 30:
            st.success("🟢 Low Risk – Your health appears stable.")
        elif risk < 60:
            st.warning("🟡 Moderate Risk – Lifestyle improvements recommended.")
        else:
            st.error("🔴 High Risk – Medical consultation advised.")

        st.markdown("""
        ### 🧠 Why this prediction?
        - Thresholds derived from **Kaggle Diabetes Dataset**
        - Previous glucose & HbA1c levels
        - Lifestyle changes
        - Time since last medical report

        ⚠️ This is a **preventive decision-support tool**, not a diagnosis.
        """)

        st.subheader("📊 Population Insight (Kaggle Data)")
        st.write("Average Blood Glucose (Dataset):", round(AVG_GLUCOSE, 2))
        st.write("Average HbA1c (Dataset):", round(AVG_HBA1C, 2))

        st.line_chart(data["blood_glucose_level"].sample(200))

# -------------------------------------------------
# LOGOUT
# -------------------------------------------------
st.markdown("---")
if st.button("🚪 Logout"):
    st.session_state.clear()
    st.rerun()

