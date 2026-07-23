import streamlit as st


def render_cards(on_select):
    cards = [
        ("📦 Track my Order", "Where is my order ORD1001?"),
        ("💰 Request Refund", "I need help with a refund request."),
        ("🔧 Technical Issue", "I am facing a technical issue with my device."),
        ("🔐 Reset Password", "I need help resetting my account password."),
    ]

    cols = st.columns(2)
    for idx, (label, prompt) in enumerate(cards):
        with cols[idx % 2]:
            if st.button(label, use_container_width=True, key=f"card_{idx}"):
                if label == "📦 Track my Order":
                    st.session_state.awaiting_order_id = True
                    st.rerun()
                else:
                    on_select(prompt)
