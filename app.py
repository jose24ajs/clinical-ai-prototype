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

# ===================== SUBMIT BUTTON =====================
submitted = st.button("🔍 Predict My Current Health")

if not submitted:
    st.info("👆 Enter your details and click **Predict My Current Health** to see the result.")

# ===================== AI LOGIC =====================
if submitted:
    risk = 0
    reasons = []

    # Medical history impact
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
        reasons.append("Low physical activity")

    if sleep < 6:
        risk += 10
        reasons.append("Insufficient sleep")

    if stress == "High":
        risk += 15
        reasons.append("High stress level")

    # ===================== STATUS =====================
    if risk >= 70:
        status = "🔴 High Health Risk"
    elif risk >= 40:
        status = "🟡 Moderate Risk"
    else:
        status = "🟢 Stable"

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

    # ===================== FUTURE OUTLOOK =====================
    st.subheader("🔮 Future Health Outlook")

    if status.startswith("🔴"):
        st.error(
            "If current habits continue, your health may **worsen significantly**. "
            "Preventive action is strongly advised."
        )
    elif status.startswith("🟡"):
        st.warning(
            "Your health may decline gradually if lifestyle improvements are not made."
        )
    else:
        st.success(
            "Your health is expected to remain **stable** if current habits continue."
        )

    st.divider()

    # ===================== ACTIONS =====================
    st.subheader("✅ AI-Suggested Preventive Actions")

    if status.startswith("🔴"):
        st.write("- Reduce sugar and junk food immediately")
        st.write("- Start daily light exercise")
        st.write("- Improve sleep consistency")
        st.write("- Consider medical consultation")

    elif status.startswith("🟡"):
        st.write("- Improve diet balance")
        st.write("- Increase physical activity")
        st.write("- Manage stress proactively")

    else:
        st.write("- Continue healthy habits")
        st.write("- Regular monitoring recommended")

    st.divider()

    st.caption(
        "⚠ This tool provides **health awareness and prevention guidance only**. "
        "It does not replace professional medical advice."
    )
