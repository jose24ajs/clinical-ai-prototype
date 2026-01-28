import streamlit as st
import pandas as pd

st.set_page_config(page_title="Clinical Trial AI Platform", layout="wide")

st.title("🧠 AI-Powered Clinical Trial Risk Dashboard")

# Load data
edc = pd.read_csv("data/edc_data.csv")
lab = pd.read_csv("data/lab_data.csv")
monitor = pd.read_csv("data/monitoring_logs.csv")

risk_scores = {}

for site in edc['site_id'].unique():
    risk = 0

    if len(edc[(edc.site_id == site) & (edc.form_complete == "No")]) > 0:
        risk += 30

    if len(lab[(lab.site_id == site) & (lab.lab_value.isna())]) > 0:
        risk += 40

    delay = monitor[monitor.site_id == site].days_delayed.values[0]
    if delay > 7:
        risk += 30

    deviation = monitor[monitor.site_id == site].protocol_deviation.values[0]
    if deviation == "Yes":
        risk += 40

    risk_scores[site] = risk

risk_df = pd.DataFrame.from_dict(risk_scores, orient='index', columns=['Risk Score'])
risk_df['Status'] = risk_df['Risk Score'].apply(
    lambda x: "🔴 High" if x >= 70 else "🟡 Medium" if x >= 40 else "🟢 Low"
)

st.subheader("📊 Site Risk Overview")
st.dataframe(risk_df)

st.subheader("🚨 AI Alerts & Recommendations")
for site, score in risk_scores.items():
    if score >= 70:
        st.error(f"{site}: High operational risk detected. Immediate monitoring recommended.")
    elif score >= 40:
        st.warning(f"{site}: Moderate risk detected. Follow-up suggested.")
