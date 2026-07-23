import streamlit as st


def render_hero():
    st.markdown(
        """
        <div style="padding:20px 0 10px 0;">
            <h1 style="color:white;margin-bottom:8px;">🤖 AI Customer Support Assistant</h1>
            <p style="color:#CBD5E1;font-size:16px;">How can I help you today?</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
