import streamlit as st

st.title("👨‍🎓 Register Student")

with st.form("register_form"):

    student_id = st.text_input("Student ID")
    student_name = st.text_input("Student Name")

    department = st.selectbox(
        "Department",
        ["CSE", "ISE", "ECE", "EEE", "MECH"]
    )

    photo = st.file_uploader(
        "Upload Photo",
        type=["jpg", "jpeg", "png"]
    )

    submit = st.form_submit_button("Register Student")

    if submit:
        st.success(
            f"{student_name} registered successfully!"
        )