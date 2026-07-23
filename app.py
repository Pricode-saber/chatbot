import streamlit as st

from chatbot import chatbot
from components.sidebar import sidebar
from styles import load_css
from utils.order_lookup import get_order

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="TechNova AI Support",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# THEME — Dark Mode Only
# -----------------------------

if "awaiting_order_id" not in st.session_state:
    st.session_state.awaiting_order_id = False

st.markdown(load_css(), unsafe_allow_html=True)

# -----------------------------
# SIDEBAR (component)
# -----------------------------

page = sidebar()

# -----------------------------
# CHAT HISTORY
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# MAIN PAGE
# -----------------------------

st.markdown(
    """
    <div class="hero">
        <div class="hero-icon">🤖</div>
        <h1 class="hero-title">AI <span class="gradient">Customer Support</span> Assistant</h1>
        <p class="hero-subtitle">Your intelligent customer support companion for orders, refunds, technical issues, and password recovery.</p>
        <div class="divider-line"></div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("### How can I help you today?")

# -----------------------------
# QUICK ACTIONS
# -----------------------------

st.markdown("<div class='quick-actions-wrap'><div class='quick-actions'>", unsafe_allow_html=True)

# Desktop: 5 columns of cards; Streamlit will wrap on small screens
cols = st.columns([1,1,1,1,1], gap="large")

prompts = [
    ("📦\n\nTrack my Order\n\nTrack an existing order\nusing Order ID", "Track my order", "quick_track"),
    ("💰\n\nRequest Refund\n\nStart a refund request\nfor a recent order", "I want a refund", "quick_refund"),
    ("🔧\n\nTechnical Issue\n\nResolve a technical\nproblem quickly", "Technical issue", "quick_technical"),
    ("💳\n\nBilling Issue\n\nGet help with payments\nand invoices", "Billing issue", "quick_billing"),
    ("🔐\n\nReset Password\n\nRecover access to\nyour account", "Forgot password", "quick_password"),
]

for i, (label, prompt_text, key) in enumerate(prompts):
    with cols[i]:
        if st.button(label, use_container_width=True, key=key):
            if key == "quick_track":
                st.session_state.awaiting_order_id = True
                st.rerun()

            st.session_state.messages.append({"role": "user", "content": prompt_text})
            with st.spinner("Thinking..."):
                response = chatbot(prompt_text)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()

st.markdown("</div></div>", unsafe_allow_html=True)

st.divider()

# -----------------------------
# DISPLAY CHAT
# -----------------------------

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# CHAT INPUT
# -----------------------------

if st.session_state.awaiting_order_id:
    st.info("📦 Enter your Order ID")

    order_id = st.text_input("Order ID", placeholder="ORD1001")

    if st.button("Track Order"):
        if not order_id or not order_id.strip():
            st.warning("⚠️ Please enter a valid Order ID.")
        else:
            order = get_order(order_id)

            if order:
                # Build a friendly order summary for the user
                order_summary = f"""✅ **📦 Order Found**

| Field | Details |
|-------|---------|
| **Order ID** | {order['OrderID']} |
| **Product** | {order['Product']} |
| **Status** | {order['Status']} |
| **Delivery Date** | {order['DeliveryDate']} |
"""
                # Save user message to chat history
                st.session_state.messages.append(
                    {"role": "user", "content": f"Track my order {order_id}"}
                )

                # Save the order summary as assistant response
                st.session_state.messages.append(
                    {"role": "assistant", "content": order_summary}
                )

                # Generate a conversational AI response explaining the order
                prompt = f"""
You are a professional customer support executive.

Explain this order to the customer in a warm, conversational tone.

Order Details:
- Order ID: {order['OrderID']}
- Product: {order['Product']}
- Status: {order['Status']}
- Delivery Date: {order['DeliveryDate']}
"""
                with st.spinner("Preparing support response..."):
                    response = chatbot(prompt)

                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )
            else:
                st.session_state.messages.append(
                    {"role": "user", "content": f"Track my order {order_id}"}
                )
                st.session_state.messages.append(
                    {"role": "assistant", "content": f"❌ **Order not found.**\n\nI couldn't find any order with ID `{order_id}`. Please check the Order ID and try again."}
                )

        st.session_state.awaiting_order_id = False
        st.rerun()
else:
    prompt = st.chat_input("Ask anything...")

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = chatbot(prompt)
                st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

