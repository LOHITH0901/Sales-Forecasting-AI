import mysql.connector

# -------------------------------
# Database Connection
# -------------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",      # Change if your MySQL has a password
    database="sales_forecasting"
)

cursor = conn.cursor()

# -------------------------------
# Products Data
# -------------------------------

products = [

# Electronics (20)
("Laptop","Electronics",65000),
("Gaming Laptop","Electronics",95000),
("Smartphone","Electronics",30000),
("Flagship Smartphone","Electronics",70000),
("Tablet","Electronics",22000),
("Smart Watch","Electronics",12000),
("Wireless Earbuds","Electronics",3500),
("Bluetooth Speaker","Electronics",2800),
("Monitor","Electronics",15000),
("Keyboard","Electronics",1200),
("Mechanical Keyboard","Electronics",3500),
("Mouse","Electronics",800),
("Gaming Mouse","Electronics",2200),
("Printer","Electronics",9000),
("Webcam","Electronics",2500),
("Power Bank","Electronics",1800),
("External Hard Drive","Electronics",4500),
("USB Flash Drive","Electronics",700),
("Router","Electronics",2500),
("Projector","Electronics",35000),

# Furniture (15)
("Office Chair","Furniture",6500),
("Study Table","Furniture",8500),
("Dining Table","Furniture",22000),
("Coffee Table","Furniture",4500),
("Bookshelf","Furniture",6000),
("Bed","Furniture",28000),
("Wardrobe","Furniture",24000),
("Sofa","Furniture",35000),
("TV Unit","Furniture",8500),
("Recliner Chair","Furniture",12000),
("Computer Desk","Furniture",7000),
("Plastic Chair","Furniture",700),
("Wooden Stool","Furniture",900),
("Shoe Rack","Furniture",2500),
("Bean Bag","Furniture",3200),

# Grocery (15)
("Rice 10kg","Grocery",850),
("Wheat Flour 5kg","Grocery",320),
("Sugar 5kg","Grocery",280),
("Cooking Oil 1L","Grocery",180),
("Tea Powder","Grocery",240),
("Coffee Powder","Grocery",420),
("Milk 1L","Grocery",60),
("Butter","Grocery",55),
("Cheese","Grocery",180),
("Eggs Pack","Grocery",90),
("Biscuits","Grocery",40),
("Chocolate","Grocery",120),
("Soft Drink","Grocery",90),
("Fruit Juice","Grocery",110),
("Pasta","Grocery",95),

# Clothing (15)
("T-Shirt","Clothing",700),
("Jeans","Clothing",1800),
("Shirt","Clothing",1400),
("Jacket","Clothing",3200),
("Sweater","Clothing",2100),
("Hoodie","Clothing",2200),
("Track Pant","Clothing",1200),
("Shorts","Clothing",650),
("Saree","Clothing",3500),
("Kurta","Clothing",1200),
("Leggings","Clothing",650),
("Shoes","Clothing",3500),
("Sandals","Clothing",1800),
("Cap","Clothing",350),
("Socks","Clothing",180),

# Sports (10)
("Cricket Bat","Sports",2800),
("Football","Sports",1200),
("Basketball","Sports",1400),
("Volleyball","Sports",900),
("Badminton Racket","Sports",1800),
("Tennis Racket","Sports",4200),
("Gym Bag","Sports",1700),
("Yoga Mat","Sports",900),
("Skipping Rope","Sports",350),
("Dumbbells","Sports",2200),

# Books (10)
("Python Programming","Books",850),
("Java Programming","Books",900),
("SQL Guide","Books",700),
("Machine Learning","Books",1200),
("Data Science","Books",1100),
("Artificial Intelligence","Books",1400),
("Novel","Books",450),
("Dictionary","Books",650),
("Notebook","Books",90),
("Story Book","Books",350),

# Beauty (10)
("Face Wash","Beauty",220),
("Shampoo","Beauty",280),
("Conditioner","Beauty",320),
("Perfume","Beauty",1500),
("Body Lotion","Beauty",420),
("Lipstick","Beauty",550),
("Face Cream","Beauty",390),
("Hair Oil","Beauty",240),
("Sunscreen","Beauty",480),
("Soap Pack","Beauty",180),

# Home Appliances (5)
("Mixer Grinder","Home Appliances",3500),
("Microwave Oven","Home Appliances",9000),
("Electric Kettle","Home Appliances",1800),
("Vacuum Cleaner","Home Appliances",8500),
("Ceiling Fan","Home Appliances",2800)
]

# -------------------------------
# Insert Query
# -------------------------------

query = """
INSERT INTO products(product_name, category, unit_price)
VALUES (%s,%s,%s)
"""

cursor.executemany(query, products)

conn.commit()

print(f"{cursor.rowcount} products inserted successfully.")

cursor.close()
conn.close()


