# utils/intent_classifier.py

def detect_intent(user_input):
    """
    Detects the user's intent based on keywords.
    Returns one of the prompt categories.
    """

    message = user_input.lower()

    # Order Status
    if any(word in message for word in [
        "order", "tracking", "track", "delivery", "shipping"
    ]):
        return "order_status"

    # Refund
    elif any(word in message for word in [
        "refund", "return", "money back"
    ]):
        return "refund"

    # Billing
    elif any(word in message for word in [
        "bill", "billing", "payment", "charged", "invoice"
    ]):
        return "billing"

    # Technical Support
    elif any(word in message for word in [
        "error", "bug", "issue", "crash", "problem", "not working"
    ]):
        return "technical"

    # Account Recovery
    elif any(word in message for word in [
        "password", "login", "account", "forgot password"
    ]):
        return "account"

    # Default
    else:
        return "faq"
