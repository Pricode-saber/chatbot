import streamlit as st


def apply_theme():
    st.session_state.setdefault("theme", "dark")

    if st.session_state.theme == "dark":
        st.markdown(
            """
            <style>
            .theme-toggle { color: #F5F5F5; }
            </style>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <style>
            .theme-toggle { color: #111111; }
            </style>
            """,
            unsafe_allow_html=True,
        )
