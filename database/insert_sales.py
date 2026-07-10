import mysql.connector
import random
from datetime import datetime, timedelta

# -------------------------
# Database Connection
# -------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sales_forecasting"
)

cursor = conn.cursor()

# -------------------------
# Fetch Products
# -------------------------
cursor.execute("""
SELECT product_id, unit_price
FROM products
""")

products = cursor.fetchall()

product_price = {}

for pid, price in products:
    product_price[pid] = float(price)

# -------------------------
# Customer IDs
# -------------------------
cursor.execute("""
SELECT customer_id
FROM customers
""")

customer_ids = [row[0] for row in cursor.fetchall()]

# -------------------------
# Date Range
# -------------------------
start_date = datetime(2023, 1, 1)
end_date = datetime(2025, 12, 31)

days = (end_date - start_date).days

festival_months = [10, 11, 12]

sales_data = []

TOTAL_RECORDS = 20000

for i in range(TOTAL_RECORDS):

    sale_date = start_date + timedelta(days=random.randint(0, days))

    customer = random.choice(customer_ids)

    product = random.choice(list(product_price.keys()))

    price = product_price[product]

    weekday = sale_date.weekday()

    if weekday >= 5:
        quantity = random.randint(2, 8)
    else:
        quantity = random.randint(1, 5)

    if sale_date.month in festival_months:
        discount = random.choice([10, 15, 20, 25, 30])
    else:
        discount = random.choice([0, 5, 10, 15])

    total = quantity * price
    total = total - (total * discount / 100)

    sales_data.append(
        (
            sale_date.strftime("%Y-%m-%d"),
            customer,
            product,
            quantity,
            discount,
            round(total, 2)
        )
    )

    if (i + 1) % 5000 == 0:
        print(f"{i+1} records generated...")

query = """
INSERT INTO sales
(
sale_date,
customer_id,
product_id,
quantity,
discount,
total_sales
)
VALUES
(
%s,
%s,
%s,
%s,
%s,
%s
)
"""

cursor.executemany(query, sales_data)

conn.commit()

print("----------------------------------")
print(f"{cursor.rowcount} sales inserted.")
print("----------------------------------")

cursor.close()
conn.close()