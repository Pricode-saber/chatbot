import streamlit as st


def sidebar():
    """Render the left navigation sidebar and return the selected page."""

    if "sidebar_page" not in st.session_state:
        st.session_state.sidebar_page = "🏠 Home"

    with st.sidebar:
        st.markdown(
            """
            <div style='display:flex;align-items:center;gap:12px;padding:12px 8px;'>
                <div style='width:44px;height:44px;border-radius:10px;display:flex;align-items:center;justify-content:center;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.06);'>
                    <span style='font-size:20px;'>🤖</span>
                </div>
                <div style='line-height:1;'>
                    <div style='font-weight:700;font-size:16px;'>TechNova AI</div>
                    <div style='color:#A3A3A3;font-size:12px;margin-top:2px;'>Customer Support</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("<div style='margin:10px 8px;'><hr style='border:none;height:1px;background:rgba(255,255,255,.03)'/></div>", unsafe_allow_html=True)

        if st.button("➕  New Chat", use_container_width=True, key="new_chat"):
            st.session_state.messages = []
            st.session_state.sidebar_page = "🏠 Home"
            st.rerun()

        # Navigation items
        nav_items = [
            ("🏠 Home", "Home"),
            ("💬 Customer Support", "Customer Support"),
            ("📊 Dashboard", "Dashboard"),
            ("🧪 Test Cases", "Test Cases"),
            ("ℹ️ About", "About"),
        ]

        for label, _ in nav_items:
            selected = st.session_state.sidebar_page == label
            btn_key = f"nav_{label}"
            if selected:
                st.markdown(f"<div class='nav-button' style='border:1px solid rgba(255,255,255,.18);box-shadow:0 6px 20px rgba(0,0,0,.45);'>{label}</div>", unsafe_allow_html=True)
            else:
                if st.button(label, key=btn_key, use_container_width=True):
                    st.session_state.sidebar_page = label
                    st.rerun()

        st.markdown("<div style='margin:14px 8px;'><hr style='border:none;height:1px;background:rgba(255,255,255,.03)'/></div>", unsafe_allow_html=True)

        # Model card
        st.markdown("### AI Model")
        st.markdown(
            """
            <div class='model-card'>
                <div style='display:flex;align-items:center;gap:10px;'>
                    <div style='width:34px;height:34px;border-radius:8px;background:rgba(255,255,255,.04);display:flex;align-items:center;justify-content:center;'>🧠</div>
                    <div>
                        <div style='font-weight:700;'>Gemini 2.5 Flash</div>
                        <div style='font-size:12px;color:#A3A3A3;'>BETA • Online</div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("<div style='margin:14px 8px;'><hr style='border:none;height:1px;background:rgba(255,255,255,.03)'/></div>", unsafe_allow_html=True)

        # Chat stats
        total = len(st.session_state.get("messages", []))
        st.markdown("### Chat Statistics")
        c1, c2 = st.columns(2)
        c1.metric("Chats", total)
        c2.metric("Status", "Online")

        st.markdown("<div style='margin:14px 8px;'><hr style='border:none;height:1px;background:rgba(255,255,255,.03)'/></div>", unsafe_allow_html=True)

        return st.session_state.sidebar_page
