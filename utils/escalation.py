def should_escalate(user_message: str, intent: str) -> bool:
    message = user_message.lower()
    if "angry" in message or "fraud" in message or "threat" in message:
        return True
    if intent == "billing" and "refund" in message and "immediately" in message:
        return True
    return False
