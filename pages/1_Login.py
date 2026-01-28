import streamlit as st

st.set_page_config(page_title="AI Clinic Login", layout="centered")

st.markdown(
    """
    <h1 style='text-align:center;'>🤖 AI CLINIC</h1>
    <h3 style='text-align:center;'>Preventive Health Intelligence</h3>
    """,
    unsafe_allow_html=True
)

st.image(
    "https://images.unsplash.com/photo-1581093588401-22d39b2d4f9b",
    use_container_width=True
)

st.markdown("---")

username = st.text_input("👤 Username")
password = st.text_input("🔒 Password", type="password")

if st.button("Login"):
    if username:
        st.session_state["logged_in"] = True
        st.session_state["user"] = username
        st.success("Login successful! Use the sidebar to navigate ➡")
    else:
        st.error("Please enter username")
