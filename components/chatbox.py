import streamlit as st


def render_chatbox(messages):
    for message in messages:
        role = message["role"]
        content = message["content"]
        if role == "user":
            st.markdown(
                f"""
                <div style="margin:10px 0;padding:12px 14px;background:#2F6FED;border-radius:14px;color:white;max-width:78%;margin-left:auto;">
                    <div style="font-size:13px;font-weight:600;">You</div>
                    <div style="margin-top:4px;white-space:pre-wrap;">{content}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"""
                <div style="margin:10px 0;padding:12px 14px;background:#181A20;border-radius:14px;color:#F5F5F5;border:1px solid #2A2D35;max-width:85%;">
                    <div style="font-size:13px;font-weight:600;color:#8AB4F8;">TechNova AI</div>
                    <div style="margin-top:4px;white-space:pre-wrap;">{content}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
