import streamlit as st

st.set_page_config(
    page_title="AI Preventive Health Predictor",
    layout="centered"
)

st.title("🧠 AI Preventive Health Predictor")
st.markdown(
    "Predict your **current health state** using your **last medical report** "
    "and **lifestyle habits after that report**, without taking a new test."
)

st.divider()

# ===================== PREVIOUS REPORT =====================
st.subheader("🧾 Previous Medical Report")

bp = st.number_input(
    "Blood Pressure (Systolic, mmHg)",
    min_value=80,
    max_value=200,
    value=120
)

sugar = st.number_input(
    "Blood Sugar Level (mg/dL)",
    min_value=60,
    max_value=300,
    value=110
)

days = st.slider(
    "Days since last medical report",
    1, 90, 15
)

st.divider()

# ===================== LIFESTYLE =====================
st.subheader("🍽 Lifestyle After Report")

diet = st.selectbox(
    "Food intake pattern",
    ["Balanced", "High Sugar", "High Fat", "Mostly Junk Food"]
)

exercise = st.selectbox(
    "Exercise frequency",
    ["Daily", "3–4 times/week", "Rarely", "Never"]
)

sleep = st.slider(
    "Average sleep per day (hours)",
    3, 9, 7
)

stress = st.selectbox(
    "Stress level",
    ["Low", "Medium", "High"]
)

st.divider()

# ===================== AI LOGIC =====================
risk = 0
reasons = []

# Base medical risk
if bp > 140:
    risk += 25
    reasons.append("Previously high blood pressure")

if sugar > 140:
    risk += 25
    reasons.append("Previously high blood sugar")

# Time factor
if days > 30:
    risk += 10
    reasons.append("Long gap since last medical check")

# Lifestyle impact
if diet in ["High Sugar", "Mostly Junk Food"]:
    risk += 20
    reasons.append("Unhealthy food intake")

if exercise in ["Rarely", "Never"]:
    risk += 15
    reasons.append("Lack of physical activity")

if sleep < 6:
    risk += 10
    reasons.append("Insufficient sleep")

if stress == "High":
    risk += 15
    reasons.append("High stress level")

# ===================== HEALTH STATUS =====================
if risk >= 70:
    status = "🔴 High Health Risk"
elif risk >= 40:
    status = "🟡 Moderate Risk"
else:
    status = "🟢 Stable"

# ===================== RESULTS =====================
st.subheader("📊 Predicted Current Health State")
st.metric("Health Risk Score", f"{risk} / 100", status)

st.divider()

# ===================== EXPLANATION =====================
st.subheader("🧠 Why this prediction?")
if reasons:
    for r in reasons:
        st.write(f"• {r}")
else:
    st.write("• No major negative indicators detected")

st.divider()

# ===================== FUTURE WARNING =====================
st.subheader("🔮 Future Health Outlook")

if status == "🔴 High Health Risk":
    st.error(
        "If current habits continue, there is a **high chance of health deterioration**. "
        "A medical consultation is strongly recommended."
    )
elif status == "🟡 Moderate Risk":
    st.warning(
        "Your health may worsen over time if lifestyle factors are not improved."
    )
else:
    st.success(
        "Your health is likely to remain stable if current habits continue."
    )

st.divider()

# ===================== PREVENTIVE ACTIONS =====================
st.subheader("✅ AI-Suggested Preventive Actions")

if status == "🔴 High Health Risk":
    st.write("- Reduce sugar and junk food immediately")
    st.write("- Start light daily exercise")
    st.write("- Manage stress through relaxation techniques")
    st.write("- Schedule a medical check-up soon")

elif status == "🟡 Moderate Risk":
    st.write("- Improve diet balance")
    st.write("- Increase physical activity")
    st.write("- Maintain regular sleep schedule")

else:
    st.write("- Continue healthy habits")
    st.write("- Regular health monitoring recommended")

st.divider()

st.caption(
    "⚠ This tool provides **health awareness and prevention guidance only**. "
    "It does not replace professional medical diagnosis."
)
