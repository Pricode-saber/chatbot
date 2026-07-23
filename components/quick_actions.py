import streamlit as st


def render_quick_actions(on_select):
    st.markdown("<div style='display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin:16px 0;'>", unsafe_allow_html=True)

    cards = [
        ("📦 Track my Order", "Where is my order ORD1001?"),
        ("💰 Request Refund", "I want to request a refund for my recent purchase."),
        ("🔧 Technical Issue", "I am facing a technical issue with my device."),
        ("🔐 Reset Password", "I need help resetting my account password."),
    ]

    for label, prompt in cards:
        if st.button(label, key=f"quick_{label}", use_container_width=True):
            if label == "📦 Track my Order":
                st.session_state.awaiting_order_id = True
                st.rerun()
            else:
                on_select(prompt)

    st.markdown("</div>", unsafe_allow_html=True)
