import streamlit as st

st.set_page_config(
    page_title="AI Clinic",
    layout="wide"
)

st.title("🧠 AI CLINIC – Preventive Health Platform")

st.markdown(
    "Predict your current health state using previous reports and lifestyle data."
)

st.markdown("---")

# ---------------- LOGIN ----------------
if "logged_in" not in st.session_state:
    st.subheader("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username:
            st.session_state["logged_in"] = True
            st.session_state["user"] = username
            st.success("Login successful! Use the left sidebar to continue.")
        else:
            st.error("Please enter a username")

    st.stop()

# ---------------- AFTER LOGIN ----------------
st.success(f"Welcome, {st.session_state['user']} 👋")

st.markdown("### 🚀 What would you like to do?")

st.markdown(
    """
    👉 Use the **left sidebar** to:
    - 👤 View Profile  
    - 📄 Select Health Report  
    - 🧠 Predict Current Health  
    """
)
