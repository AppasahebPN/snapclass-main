import streamlit as st

st.title("📸 Take Attendance")

st.info("Start camera for face recognition")

if st.button("Start Camera"):
    st.success("Camera Started")

    st.image(
        "https://via.placeholder.com/800x400.png?text=Camera+Feed"
    )

    st.subheader("Detected Student")

    st.write("Name : Rahul Kumar")
    st.write("ID : CSE101")

    if st.button("Mark Attendance"):
        st.success("Attendance Marked")