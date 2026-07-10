import random
from faker import Faker
import mysql.connector

fake = Faker("en_IN")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sales_forecasting"
)

cursor = conn.cursor()

cities = [
    "Hyderabad","Bangalore","Chennai","Mumbai",
    "Delhi","Pune","Kolkata","Ahmedabad",
    "Jaipur","Lucknow","Visakhapatnam",
    "Coimbatore","Kochi","Nagpur","Indore"
]

genders = ["Male","Female"]

customers = []

for _ in range(1000):

    customers.append(

        (
            fake.name(),
            random.choice(cities),
            random.randint(18,70),
            random.choice(genders)
        )

    )

query = """
INSERT INTO customers
(customer_name, city, age, gender)
VALUES (%s,%s,%s,%s)
"""

cursor.executemany(query, customers)

conn.commit()

print(f"{cursor.rowcount} customers inserted successfully!")

cursor.close()
conn.close()