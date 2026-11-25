# Data Dictionary

- `customers.csv`: one row per customer; `customer_id` is the key.
- `products.csv`: one row per product; includes unit cost and selling price.
- `orders.csv`: order-line records; an order may have a customer, product, date, quantity, price, and status.
- `returns.csv`: return records linked to an order ID.

The data intentionally contains a few quality issues such as a duplicate order row,
missing values, inconsistent capitalization, a zero quantity, and an unknown customer ID.
Discover them through analysis rather than assuming their locations.
