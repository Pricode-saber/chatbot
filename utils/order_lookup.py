import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ORDERS = pd.read_csv(os.path.join(BASE_DIR, "database", "orders.csv"))


def get_order(order_id):
    order_id = str(order_id or "").upper().strip()

    if "OrderID" in ORDERS.columns:
        result = ORDERS[ORDERS["OrderID"].astype(str).str.upper() == order_id]
    elif "order_id" in ORDERS.columns:
        result = ORDERS[ORDERS["order_id"].astype(str).str.upper() == order_id]
    else:
        return None

    if result.empty:
        return None

    row = result.iloc[0].to_dict()

    if "OrderID" not in row and "order_id" in row:
        row["OrderID"] = row["order_id"]
    if "Product" not in row and "product" in row:
        row["Product"] = row["product"]
    if "Status" not in row and "status" in row:
        row["Status"] = row["status"]
    if "DeliveryDate" not in row and "order_date" in row:
        row["DeliveryDate"] = row["order_date"]

    if row.get("DeliveryDate") is None and "order_date" in row:
        row["DeliveryDate"] = row["order_date"]

    return row
