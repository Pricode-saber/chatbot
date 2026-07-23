import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DB_DIR = os.path.join(BASE_DIR, "database")

CUSTOMERS = pd.read_csv(os.path.join(DB_DIR, "customers.csv"))
ORDERS = pd.read_csv(os.path.join(DB_DIR, "orders.csv"))
REFUNDS = pd.read_csv(os.path.join(DB_DIR, "refunds.csv"))
BILLING = pd.read_csv(os.path.join(DB_DIR, "billing.csv"))
SUPPORT = pd.read_csv(os.path.join(DB_DIR, "support_tickets.csv"))


def get_customer_by_id(customer_id: str):
    return CUSTOMERS[CUSTOMERS["customer_id"] == customer_id]
