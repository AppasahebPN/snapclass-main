import streamlit as st

from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard


def student_screen():
    style_background_dashboard()
    style_base_layout()

    header_dashboard()
    st.subheader('Student Portal')
    st.write('This is a frontend-only version of the student screen. Backend logic and session state handling have been removed.')

    with st.expander('Your Enrolled Subjects'):
        st.write('This section is frontend-only. Enrolled subject data is not loaded.')
        st.dataframe(
            {
                'Subject': ['Math', 'Science'],
                'Status': ['Enrolled', 'Enrolled'],
                'Next Class': ['Tomorrow', 'Friday'],
            },
            width='stretch',
            hide_index=True,
        )

    st.divider()

    with st.expander('Enrollment'):
        st.write('Use the controls below to simulate enrollment UI without backend actions.')
        st.text_input('Join Code')
        st.button('Enroll in Subject', type='primary', width='stretch', icon=':material/add_circle:')

    footer_dashboard()
