from utils.database import load_csv


def get_support_tickets(customer_id: str):
    df = load_csv("support_tickets.csv")
    return df[df["customer_id"] == customer_id]


def get_latest_ticket_status(customer_id: str):
    result = get_support_tickets(customer_id)
    if result.empty:
        return "No tickets found"
    return result.iloc[0]["status"]
