from utils.database import load_csv


def get_billing_by_customer(customer_id: str):
    df = load_csv("billing.csv")
    return df[df["customer_id"] == customer_id]


def get_billing_status(customer_id: str):
    result = get_billing_by_customer(customer_id)
    if result.empty:
        return "No billing found"
    return result.iloc[0]["status"]
