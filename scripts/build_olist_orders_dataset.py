"""
Build the class version of the Olist orders dataset from the real, public
Kaggle dataset (olistbr/brazilian-ecommerce).

Downloads the full dataset via kagglehub, then derives a single flat table
with the columns used in class:

    order_id, customer_id, order_status, price,
    order_purchase_timestamp, order_delivered_customer_date,
    order_estimated_delivery_date

`price` is not a column on the raw orders table -- an order can contain
several line items, so it is the sum of `order_items.price` for that order
(i.e. the order's total merchandise value, excluding freight).

Usage:
    python scripts/build_olist_orders_dataset.py
"""

from pathlib import Path

import kagglehub
import pandas as pd

OUTPUT_PATH = Path(__file__).resolve().parent.parent / "data" / "olist_orders_dataset.csv"

TARGET_COLUMNS = [
    "order_id",
    "customer_id",
    "order_status",
    "price",
    "order_purchase_timestamp",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
]


def main():
    dataset_dir = Path(kagglehub.dataset_download("olistbr/brazilian-ecommerce"))
    print(f"Downloaded Kaggle dataset to: {dataset_dir}")

    orders = pd.read_csv(dataset_dir / "olist_orders_dataset.csv")
    order_items = pd.read_csv(dataset_dir / "olist_order_items_dataset.csv")

    order_totals = order_items.groupby("order_id", as_index=False)["price"].sum()

    orders_final = orders.merge(order_totals, on="order_id", how="left")[TARGET_COLUMNS]

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    orders_final.to_csv(OUTPUT_PATH, index=False)
    print(f"Wrote {len(orders_final):,} rows to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
