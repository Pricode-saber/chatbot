from utils.database import load_csv


def get_refund_by_order(order_id: str):
    df = load_csv("refunds.csv")
    return df[df["order_id"] == order_id]


def get_refund_status(order_id: str):
    result = get_refund_by_order(order_id)
    if result.empty:
        return "No refund found"
    return result.iloc[0]["status"]
