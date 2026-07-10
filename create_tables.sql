CREATE DATABASE sales_forecasting;

USE sales_forecasting;

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    unit_price DECIMAL(10,2)
);

CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100),
    city VARCHAR(50),
    age INT,
    gender VARCHAR(10)
);

CREATE TABLE sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    sale_date DATE,
    customer_id INT,
    product_id INT,
    quantity INT,
    discount DECIMAL(5,2),
    total_sales DECIMAL(10,2),

    FOREIGN KEY(customer_id)
        REFERENCES customers(customer_id),

    FOREIGN KEY(product_id)
        REFERENCES products(product_id)
);

CREATE TABLE predictions (
    prediction_id INT AUTO_INCREMENT PRIMARY KEY,
    prediction_date DATE,
    predicted_sales DECIMAL(10,2),
    model_name VARCHAR(100)
);

select * from products;

SELECT COUNT(*) FROM customers;

SELECT COUNT(*) FROM sales;

SELECT * FROM sales LIMIT 10;


SELECT
s.sale_date,
c.customer_name,
p.product_name,
s.quantity,
s.discount,
s.total_sales
FROM sales s
JOIN customers c
ON s.customer_id = c.customer_id
JOIN products p
ON s.product_id = p.product_id
LIMIT 10;




