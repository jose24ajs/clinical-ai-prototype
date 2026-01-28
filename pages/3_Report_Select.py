import streamlit as st

if "logged_in" not in st.session_state:
    st.error("Please login first.")
    st.stop()

st.title("📄 Select Previous Health Report")

report_type = st.selectbox(
    "Choose report type",
    ["Blood Pressure", "Blood Sugar", "Heart Health", "General Checkup"]
)

st.subheader("📊 Previous Report Values")

bp = sugar = heart = None

if report_type == "Blood Pressure":
    bp = st.number_input("Previous BP (Systolic)", 80, 200, 120)

elif report_type == "Blood Sugar":
    sugar = st.number_input("Previous Sugar Level (mg/dL)", 50, 300, 110)

elif report_type == "Heart Health":
    heart = st.selectbox("Heart Condition", ["Normal", "At Risk", "Critical"])

days = st.slider("Days since report", 1, 180, 30)

if st.button("Save Report"):
    st.session_state.report = {
        "type": report_type,
        "bp": bp,
        "sugar": sugar,
        "heart": heart,
        "days": days
    }
    st.success("Report saved. You can now predict your health.")
