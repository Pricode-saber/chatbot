def evaluate_response(user_message: str, response: str) -> dict:
    return {
        "user_message": user_message,
        "response_length": len(response),
        "contains_helpful_language": "help" in response.lower() or "support" in response.lower(),
    }
