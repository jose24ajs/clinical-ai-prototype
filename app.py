import streamlit as st

st.set_page_config(
    page_title="AI Clinic",
    layout="wide"
)

# ---------------- SESSION INIT ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- LOGIN SCREEN ----------------
if not st.session_state.logged_in:
    st.title("🧠 AI CLINIC – Preventive Health Platform")

    st.markdown("""
    **AI Clinic** is an AI-powered preventive healthcare system.

    It predicts your **current health condition**
    using previous medical reports and lifestyle data —
    without requiring new hospital visits.
    """)

    st.markdown("---")
    st.subheader("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username.strip():
            st.session_state.logged_in = True
            st.session_state.user = username
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Please enter a username")

    st.stop()

# ---------------- MAIN APP ----------------
st.success(f"Welcome, {st.session_state.user} 👋")

tab1, tab2, tab3 = st.tabs([
    "👤 Profile",
    "📄 Previous Report",
    "🧠 Health Prediction"
])

# ================= TAB 1: PROFILE =================
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
        st.success("Profile saved")

# ================= TAB 2: REPORT =================
with tab2:
    st.header("📄 Previous Medical Report")

    report_type = st.selectbox(
        "Select report type",
        ["Blood Pressure", "Blood Sugar", "Heart Health"]
    )

    bp = sugar = heart = None

    if report_type == "Blood Pressure":
        bp = st.number_input("Previous BP (Systolic)", 80, 200, 120)

    elif report_type == "Blood Sugar":
        sugar = st.number_input("Previous Sugar Level (mg/dL)", 50, 300, 110)

    elif report_type == "Heart Health":
        heart = st.selectbox("Heart Status", ["Normal", "At Risk", "Critical"])

    days = st.slider("Days since report", 1, 180, 30)

    if st.button("Save Report"):
        st.session_state.report = {
            "type": report_type,
            "bp": bp,
            "sugar": sugar,
            "heart": heart,
            "days": days
        }
        st.success("Report saved")

# ================= TAB 3: PREDICTOR =================
with tab3:
    st.header("🧠 AI Preventive Health Predictor")

    if "report" not in st.session_state:
        st.warning("Please save a previous report first.")
        st.stop()

    diet = st.selectbox("Diet Quality", ["Poor", "Average", "Healthy"])
    exercise = st.selectbox("Exercise Frequency", ["None", "1–2/week", "3–5/week"])
    sleep = st.slider("Average Sleep (hours)", 3, 10, 7)
    stress = st.selectbox("Stress Level", ["Low", "Medium", "High"])

    risk = 0

    if diet == "Poor":
        risk += 20
    elif diet == "Average":
        risk += 10

    if exercise == "None":
        risk += 20
    elif exercise == "1–2/week":
        risk += 10

    if sleep < 6:
        risk += 15

    if stress == "High":
        risk += 20
    elif stress == "Medium":
        risk += 10

    risk += min(st.session_state.report["days"] // 10, 20)

    if st.button("🔮 Predict Health"):
        st.metric("Health Risk Score", f"{risk} / 100")

        if risk < 30:
            st.success("🟢 Stable – Keep your lifestyle")
        elif risk < 60:
            st.warning("🟡 Moderate Risk – Improve habits")
        else:
            st.error("🔴 High Risk – Consult a doctor")

        st.markdown("""
        ### Why this prediction?
        - Previous medical report
        - Time since report
        - Lifestyle habits
        - Preventive AI logic

        ⚠️ This is not a diagnosis.
        """)

# ---------------- LOGOUT ----------------
st.markdown("---")
if st.button("🚪 Logout"):
    st.session_state.clear()
    st.rerun()
