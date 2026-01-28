import streamlit as st
import pandas as pd
import time

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="AI Clinic – Preventive Health",
    layout="wide"
)

# -------------------------------------------------
# CUSTOM CSS (VISUAL MAGIC ✨)
# -------------------------------------------------
st.markdown("""
<style>
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}

.fade-in {
    animation: fadeIn 1.2s ease-in-out;
}

.glass {
    background: rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 25px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.25);
    backdrop-filter: blur(10px);
}

.big-title {
    font-size: 48px;
    font-weight: 800;
}

.subtitle {
    font-size: 18px;
    color: #d1d5db;
}

.metric-box {
    background: linear-gradient(135deg,#2563eb,#9333ea);
    padding: 20px;
    border-radius: 16px;
    color: white;
    text-align: center;
    font-size: 20px;
}

button[kind="primary"] {
    border-radius: 12px !important;
    padding: 10px 24px !important;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# LOAD DATASET
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
# LOGIN SCREEN
# -------------------------------------------------
if not st.session_state.logged_in:
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)

    st.markdown('<div class="big-title">🧠 AI CLINIC</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Preventive Health Intelligence Platform</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="glass fade-in">
    <h3>Why AI Clinic?</h3>
    <ul>
        <li>📊 Uses real-world Kaggle medical data</li>
        <li>🧠 Predicts health risk without new tests</li>
        <li>🛡️ Focused on prevention, not diagnosis</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🔐 Secure Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("🚀 Enter AI Clinic", type="primary"):
        if username.strip():
            st.session_state.logged_in = True
            st.session_state.user = username
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Username required")

    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# -------------------------------------------------
# MAIN DASHBOARD
# -------------------------------------------------
st.markdown('<div class="fade-in">', unsafe_allow_html=True)
st.success(f"👋 Welcome, {st.session_state.user}")

tab1, tab2, tab3 = st.tabs([
    "👤 Profile",
    "📄 Previous Report",
    "🧠 AI Prediction"
])

# -------------------------------------------------
# PROFILE TAB
# -------------------------------------------------
with tab1:
    st.markdown('<div class="glass fade-in">', unsafe_allow_html=True)
    st.header("👤 Personal Health Profile")

    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", 1, 120, 25)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    with col2:
        height = st.number_input("Height (cm)", 100, 220, 170)
        weight = st.number_input("Weight (kg)", 30, 200, 65)

    if st.button("💾 Save Profile"):
        st.session_state.profile = {
            "age": age,
            "gender": gender,
            "height": height,
            "weight": weight
        }
        st.success("Profile saved")

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------
# REPORT TAB
# -------------------------------------------------
with tab2:
    st.markdown('<div class="glass fade-in">', unsafe_allow_html=True)
    st.header("📄 Previous Diabetes Report")

    glucose = st.number_input("Blood Glucose (mg/dL)", 50, 400, 110)
    hba1c = st.number_input("HbA1c (%)", 3.0, 15.0, 5.5)
    days = st.slider("Days since last test", 1, 365, 30)

    if st.button("📥 Save Report"):
        st.session_state.report = {
            "glucose": glucose,
            "hba1c": hba1c,
            "days": days
        }
        st.success("Report saved")

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------
# PREDICTION TAB
# -------------------------------------------------
with tab3:
    if "report" not in st.session_state:
        st.warning("Please save a report first.")
    else:
        st.markdown('<div class="glass fade-in">', unsafe_allow_html=True)
        st.header("🧠 AI Preventive Health Prediction")

        diet = st.selectbox("🍎 Diet Quality", ["Poor", "Average", "Healthy"])
        exercise = st.selectbox("🏃 Exercise", ["None", "1–2/week", "3–5/week"])
        sleep = st.slider("😴 Sleep (hours)", 3, 10, 7)
        stress = st.selectbox("🧘 Stress Level", ["Low", "Medium", "High"])

        if st.button("🔮 Run AI Prediction", type="primary"):
            with st.spinner("Analyzing health signals..."):
                time.sleep(1.5)

            risk = 0
            if st.session_state.report["glucose"] > AVG_GLUCOSE: risk += 20
            if st.session_state.report["hba1c"] > AVG_HBA1C: risk += 20
            if diet == "Poor": risk += 15
            if exercise == "None": risk += 15
            if sleep < 6: risk += 10
            if stress == "High": risk += 15
            risk += min(st.session_state.report["days"] // 30 * 5, 20)
            risk = min(risk, 100)

            st.progress(risk / 100)

            st.markdown(f"""
            <div class="metric-box fade-in">
            Health Risk Score<br><strong>{risk} / 100</strong>
            </div>
            """, unsafe_allow_html=True)

            if risk < 30:
                st.success("🟢 Low Risk – Keep going!")
            elif risk < 60:
                st.warning("🟡 Moderate Risk – Improve habits")
            else:
                st.error("🔴 High Risk – Medical consultation advised")

            with st.expander("🧠 How did AI decide this?"):
                st.markdown("""
                - Kaggle population baselines  
                - Previous glucose & HbA1c  
                - Lifestyle patterns  
                - Time-based risk decay  
                """)

        st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------
# LOGOUT
# -------------------------------------------------
st.markdown("---")
if st.button("🚪 Logout"):
    st.session_state.clear()
    st.rerun()
