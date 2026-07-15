import streamlit as st

st.title("🏠 Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Students", "120")

with col2:
    st.metric("Today's Attendance", "85")

with col3:
    st.metric("Attendance %", "70.8")

st.markdown("---")

st.subheader("System Overview")

st.write("""
This system automates attendance using face recognition.
Students can be registered and attendance can be marked automatically.
""")