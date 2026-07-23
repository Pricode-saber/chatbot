import streamlit as st


def render_message(role, content, is_typing=False):
    if role == "user":
        st.markdown(
            f"""
            <div style="margin:12px 0;padding:14px 16px;background:#2F6FED;border-radius:16px;color:white;max-width:78%;margin-left:auto;box-shadow:0 0 10px rgba(47,111,237,0.18);">
                <div style="font-size:14px;font-weight:600;">You</div>
                <div style="margin-top:6px;white-space:pre-wrap;">{content}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div style="margin:12px 0;padding:16px 18px;background:#181A20;border-radius:16px;color:#F5F5F5;max-width:85%;border:1px solid #2A2D35;box-shadow:0 0 10px rgba(255,255,255,0.04);">
                <div style="font-size:14px;font-weight:600;color:#8AB4F8;">TechNova AI</div>
                <div style="margin-top:8px;white-space:pre-wrap;">{content}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    if is_typing:
        st.markdown(
            """
            <div style="margin:12px 0;padding:12px 14px;background:#181A20;border-radius:16px;color:#B0B7C3;max-width:50%;border:1px solid #2A2D35;">
                TechNova AI is typing...
                <div style="margin-top:6px;font-size:20px;letter-spacing:4px;">● ● ●</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
