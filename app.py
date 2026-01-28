import streamlit as st

st.set_page_config(
    page_title="AI Clinic",
    layout="wide"
)

# ---------------- LOGIN STATE ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- LOGIN PAGE ----------------
if not st.session_state.logged_in:
    st.title("🧠 AI CLINIC – Preventive Health Platform")

    st.markdown("""
    Welcome to **AI Clinic**, an AI-powered preventive healthcare system.

    This platform predicts your **current health state**
    using previous medical reports and lifestyle data.
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

# ---------------- MAIN APP AFTER LOGIN ----------------
with st.sidebar:
    st.title("🤖 AI CLINIC")
    st.markdown("### Navigation")

    if st.button("👤 Profile"):
        st.switch_page("pages/2_Profile.py")

    if st.button("📄 Health Report"):
        st.switch_page("pages/3_Report_Select.py")

    if st.button("🧠 Predict Health"):
        st.switch_page("pages/4_Predictor.py")

    st.markdown("---")
    if st.button("🚪 Logout"):
        st.session_state.clear()
        st.rerun()

st.title("🧠 AI CLINIC – Dashboard")
st.success(f"Welcome, {st.session_state.user} 👋")

st.markdown("""
### 🚀 What can you do here?
- View your health profile  
- Select a previous medical report  
- Predict your current health state **without new tests**  

👉 Use the **left sidebar** to continue.
""")
