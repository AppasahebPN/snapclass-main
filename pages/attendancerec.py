import streamlit as st
import pandas as pd

st.title("📊 Attendance Records")

data = {
    "ID": ["CSE101", "CSE102", "CSE103"],
    "Name": ["Rahul", "Priya", "Aman"],
    "Date": ["05-06-2026", "05-06-2026", "05-06-2026"],
    "Status": ["Present", "Present", "Absent"]
}

df = pd.DataFrame(data)

st.dataframe(
    df,
    use_container_width=True
)

st.download_button(
    "Download CSV",
    df.to_csv(index=False),
    file_name="attendance.csv",
    mime="text/csv"
)