import streamlit as st

st.set_page_config(
    page_title="AI Clinical Trial Health Predictor",
    layout="centered"
)

st.title("🧠 AI Clinical Trial Health Predictor")
st.markdown(
    "This system evaluates the **current operational health** of a clinical trial site "
    "and suggests **future preventive actions** to avoid data quality issues and delays."
)

st.divider()

# ---------------- USER INPUTS ----------------
st.subheader("📥 Enter Current Site State")

delay_days = st.slider("⏱ Reporting Delay (days)", 0, 20, 3)
missing_data = st.slider("📉 Missing Data (%)", 0, 50, 10)
protocol_deviation = st.selectbox("⚠ Protocol Deviation Observed?", ["No", "Yes"])
query_rate = st.slider("❓ Open Queries (%)", 0, 40, 8)
workload = st.selectbox("👥 Site Workload", ["Low", "Medium", "High"])

st.divider()

# ---------------- AI RISK LOGIC ----------------
risk_score = 0
reasons = []

if delay_days > 7:
    risk_score += 25
    reasons.append("Delayed data reporting")

if missing_data > 20:
    risk_score += 30
    reasons.append("High missing data rate")

if protocol_deviation == "Yes":
    risk_score += 25
    reasons.append("Protocol deviation detected")

if query_rate > 15:
    risk_score += 10
    reasons.append("High number of unresolved queries")

if workload == "High":
    risk_score += 10
    reasons.append("High site workload")

# ---------------- RISK CATEGORY ----------------
if risk_score >= 70:
    status = "🔴 Critical Risk"
elif risk_score >= 40:
    status = "🟡 Warning"
else:
    status = "🟢 Healthy"

# ---------------- RESULTS ----------------
st.subheader("📊 AI Health Assessment")
st.metric("Overall Risk Score", f"{risk_score} / 100", status)

st.divider()

# ---------------- EXPLAINABILITY ----------------
st.subheader("🧠 Why this assessment?")
if reasons:
    for r in reasons:
        st.write(f"• {r}")
else:
    st.write("• No major risk factors detected")

st.divider()

# ---------------- FUTURE PREDICTION ----------------
st.subheader("🔮 Future Health Prediction (Next 30 Days)")

if status == "🔴 Critical Risk":
    st.error(
        "If current conditions continue, this site is likely to cause **database lock delays**, "
        "**audit findings**, and **increased monitoring cost**."
    )
elif status == "🟡 Warning":
    st.warning(
        "If unmanaged, this site may gradually move into a **high-risk state**, "
        "affecting trial timelines."
    )
else:
    st.success(
        "Site is expected to remain **stable** if current performance is maintained."
    )

st.divider()

# ---------------- PREVENTIVE ACTIONS ----------------
st.subheader("✅ AI-Suggested Preventive Actions")

if status == "🔴 Critical Risk":
    st.write("🔧 **Immediate Actions Required:**")
    st.write("- Conduct urgent remote or onsite monitoring")
    st.write("- Allocate additional data entry support")
    st.write("- Trigger protocol deviation review")
    st.write("- Daily data review until stabilized")

elif status == "🟡 Warning":
    st.write("🛠 **Recommended Actions:**")
    st.write("- Weekly data quality review")
    st.write("- Site refresher training")
    st.write("- Automated reminders for data entry")
    st.write("- Monitor workload distribution")

else:
    st.write("✅ **Maintenance Actions:**")
    st.write("- Continue current monitoring strategy")
    st.write("- Monthly performance review")
    st.write("- Encourage best practices")

st.divider()

st.caption(
    "⚠ This is a decision-support prototype. It does not replace clinical judgment."
)
