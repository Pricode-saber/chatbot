import streamlit as st

from chatbot import chatbot
from components.message_card import render_message
from components.quick_actions import render_quick_actions
from components.hero_section import render_hero


def handle_send(prompt):
    if not prompt:
        return

    st.session_state.messages.append({"role": "user", "content": prompt})
    render_message("user", prompt)

    render_message("assistant", "", is_typing=True)
    with st.spinner(""):
        response = chatbot(prompt)

    st.session_state.messages.append({"role": "assistant", "content": response})

    st.session_state.last_response = response


def render_chat_window():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "current_page" not in st.session_state:
        st.session_state.current_page = "support"

    if st.session_state.current_page == "support":
        render_hero()

        if not st.session_state.messages:
            render_quick_actions(handle_send)

        for message in st.session_state.messages:
            render_message(message["role"], message["content"])

        prompt = st.chat_input("Ask anything...")
        if prompt:
            handle_send(prompt)
            st.rerun()

    elif st.session_state.current_page == "home":
        st.title("🏠 Home")
        st.write("Welcome to TechNova AI support.")

    elif st.session_state.current_page == "dashboard":
        st.title("📊 Dashboard")
        st.info("Support metrics and insights will appear here.")

    elif st.session_state.current_page == "test_cases":
        st.title("🧪 Test Cases")
        st.code("Where is my order ORD1001?\nI need a refund.\nMy device is not working.", language="text")

    elif st.session_state.current_page == "about":
        st.title("ℹ About")
        st.write("TechNova AI is a smart customer support assistant powered by Gemini.")
