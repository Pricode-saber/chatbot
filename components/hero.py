import streamlit as st


def hero():
    st.markdown(
        """
        <div class="hero">
            <div class="hero-icon">🤖</div>
            <h1 class="hero-title gradient">AI Customer Support Assistant</h1>
            <p class="hero-subtitle">
                Fast. Intelligent. Reliable.
                <br>
                Get instant help with orders, refunds, billing,
                technical issues, and account support.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
