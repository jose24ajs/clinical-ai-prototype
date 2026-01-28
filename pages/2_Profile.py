import streamlit as st

if "logged_in" not in st.session_state:
    st.error("Please login first.")
    st.stop()

st.title("👤 User Profile")

st.markdown(f"""
**Username:** {st.session_state.user}

This profile stores your baseline health information
used for predictive analysis.
""")

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
    st.success("Profile saved successfully!")
