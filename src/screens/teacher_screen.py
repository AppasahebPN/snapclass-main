import streamlit as st

from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard


def teacher_screen():
    style_background_dashboard()
    style_base_layout()

    header_dashboard()
    st.subheader('Teacher Portal')
    st.write('This is a frontend-only version of the teacher screen. All backend and session logic has been removed.')

    tab1, tab2, tab3 = st.columns(3)
    with tab1:
        st.button('Take Attendance', type='primary', width='stretch', icon=':material/ar_on_you:')
    with tab2:
        st.button('Manage Subjects', type='primary', width='stretch', icon=':material/book_ribbon:')
    with tab3:
        st.button('Attendance Records', type='primary', width='stretch', icon=':material/cards_stack:')

    st.divider()

    with st.expander('Take Attendance'):
        teacher_tab_take_attendance()

    with st.expander('Manage Subjects'):
        teacher_tab_manage_subjects()

    with st.expander('Attendance Records'):
        teacher_tab_attendance_records()

    footer_dashboard()


def teacher_tab_take_attendance():
    st.header('Take AI Attendance')
    st.write('This section is frontend-only. Attendance capture and storage are disabled.')
    st.file_uploader('Upload student photo', type=['png', 'jpg', 'jpeg'])
    st.button('Submit Attendance', type='primary')







def teacher_tab_manage_subjects():
    st.header('Manage Subjects')
    st.write('This section is frontend-only. Subject creation and listing are disabled.')
    st.text_input('Subject Name')
    st.text_input('Subject Code')
    st.text_input('Section')
    st.button('Create New Subject', type='primary', width='stretch')
    st.info('Subject cards are not available in frontend-only mode.')


def teacher_tab_attendance_records():
    st.header('Attendance Records')
    st.write('This section is frontend-only. Attendance records retrieval is disabled.')
    st.dataframe(
        {
            'Time': ['2026-06-22 10:00 AM', '2026-06-21 02:30 PM'],
            'Subject': ['Math', 'Science'],
            'Status': ['Pending', 'Pending'],
        },
        width='stretch',
        hide_index=True,
    )
