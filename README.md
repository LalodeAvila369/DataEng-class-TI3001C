# Data Engineering Class (TI3001C)

Course materials for the Data Engineering class: notebooks, scripts, and
datasets used in lectures and labs.

**Professor:** Eduardo de Avila-Armenta | eduardo.deavila@tec.mx

## Repository structure

```
.
├── data/                              # Datasets used in class (see below)
├── notebooks/                         # Class notebooks
├── scripts/                           # Scripts to build/refresh datasets
├── requirements.txt
├── LICENSE
└── README.md
```

## Setup

```bash
pip install -r requirements.txt
```

## Datasets

### `data/diabetes_patients.csv`

**Synthetic data.** Every row was artificially generated for teaching
purposes and does not correspond to real patients.

> ⚠️ Do not use this dataset for clinical decision-making, medical
> research, predictive modeling of real health outcomes, or any use
> beyond classroom exercises. It exists only to practice data-wrangling
> techniques on a table shaped like health data.

### `data/olist_orders_dataset.csv`

Derived from the real, public **Olist Brazilian E-Commerce dataset**
([Kaggle: olistbr/brazilian-ecommerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)).
It joins the `orders` and `order_items` tables from the original dataset
into one flat file with these columns:

| column | source |
|---|---|
| `order_id`, `customer_id`, `order_status`, `order_purchase_timestamp`, `order_delivered_customer_date`, `order_estimated_delivery_date` | `olist_orders_dataset` |
| `price` | sum of `olist_order_items_dataset.price` per `order_id` (an order's total merchandise value, excluding freight) |

To regenerate it from the latest source data:

```bash
python scripts/build_olist_orders_dataset.py
```

The script downloads the full dataset via `kagglehub` and rebuilds
`data/olist_orders_dataset.csv`. The original dataset has more tables
(customers, products, sellers, reviews, payments, geolocation) than are
used here — download it directly from Kaggle if a lesson needs them.

## License

This work is licensed under [CC BY 4.0](LICENSE) — you're free to share and
adapt it, including for commercial use, as long as you give appropriate
credit. See the [LICENSE](LICENSE) file for details.
