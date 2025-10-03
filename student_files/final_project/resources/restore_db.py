"""

    Run this to create/recreate the database, as needed.

"""
import sqlite3
import sys

create_stmts = ['CREATE TABLE customers (customer_id INTEGER PRIMARY KEY AUTOINCREMENT, first_name VARCHAR(50) NOT NULL, last_name VARCHAR(50) NOT NULL, email VARCHAR(100) NOT NULL UNIQUE, phone_number VARCHAR(15), sign_up_date DATE NOT NULL, address VARCHAR(255), city VARCHAR(50), state VARCHAR(50), zip_code VARCHAR(10))',
                'CREATE TABLE customer_preferences (preference_id INTEGER PRIMARY KEY AUTOINCREMENT, customer_id INTEGER, preferred_contact_method VARCHAR(20), marketing_opt_in BOOLEAN, FOREIGN KEY (customer_id) REFERENCES customers(customer_id))',
                'CREATE TABLE customer_orders (order_id INTEGER PRIMARY KEY AUTOINCREMENT , customer_id INTEGER, order_date DATE NOT NULL, total_amount DECIMAL(10, 2) NOT NULL, order_status VARCHAR(20), FOREIGN KEY (customer_id) REFERENCES customers(customer_id))']

insert_stmt1 = """INSERT INTO customers (first_name, last_name, email, phone_number, sign_up_date, address, city, state, zip_code)
VALUES
('Alice', 'Johnson', 'alice.johnson@example.com', '555-0123', '2023-01-15', '123 Maple St', 'Springfield', 'IL', '62701'),
('Bob', 'Smith', 'bob.smith@example.com', '555-0456', '2023-02-20', '456 Oak St', 'Springfield', 'IL', '62702'),
('Carol', 'Williams', 'carol.williams@example.com', '555-0789', '2023-03-05', '789 Pine St', 'Springfield', 'IL', '62703'),
('David', 'Brown', 'david.brown@example.com', '555-1011', '2023-04-10', '321 Birch St', 'Springfield', 'IL', '62704'),
('Eve', 'Davis', 'eve.davis@example.com', '555-1213', '2023-05-15', '654 Cedar St', 'Springfield', 'IL', '62705')
"""

insert_stmt2 = """INSERT INTO customer_preferences (customer_id, preferred_contact_method, marketing_opt_in)
VALUES
(1, 'email', 1),
(2, 'phone', 0),
(4, 'email', 1),
(3, 'email', 0),
(1, 'phone', 1)
"""

insert_stmt3 = """INSERT INTO customer_orders (customer_id, order_date, total_amount, order_status)
VALUES
(1, '2023-10-01', 99.95, 'completed'),
(4, '2023-10-02', 19.99, 'completed'),
(3, '2023-10-03', 89.99, 'pending'),
(5, '2023-10-04', 79.96, 'completed'),
(2, '2023-10-05', 39.98, 'cancelled'),
(4, '2023-10-06', 22.88, 'completed'),
(1, '2023-10-06', 44.96, 'completed'),
(2, '2023-10-07', 11.99, 'pending'),
(3, '2023-10-08', 59.99, 'completed'),
(5, '2023-10-08', 64.27, 'pending'),
(1, '2023-10-08', 10.31, 'completed'),
(2, '2023-10-09', 79.99, 'completed'),
(3, '2023-10-10', 69.27, 'completed'),
(4, '2023-10-10', 53.79, 'completed')
"""

insert_stmts = [insert_stmt1, insert_stmt2, insert_stmt3]

db_file = 'customers.db'
tables = ['customers', 'customer_preferences', 'customer_orders']

try:
    with sqlite3.connect(db_file) as connection:
        print(f'Database connection opened.')
        cursor = connection.cursor()
        for idx, table in enumerate(tables):
            cursor.execute(f'DROP TABLE IF EXISTS {table}')
            print(f'--> {table} table dropped.')
            cursor.execute(create_stmts[idx])
            print(f'--> {table} table created')
            print(f'Inserting data into {table} table...')
            cursor.execute(insert_stmts[idx])
            print('Data inserted into table.')
except Exception as err:
    print('Warning: ', f'Data NOT loaded into {db_file}')
    print(f'Database Error (Type: {type(err)})\nError: {err}', file=sys.stderr)
finally:
    connection.close()
    print(f'Database connection on {db_file} closed')


# for the product.db database:
create_stmts = ['CREATE TABLE categories (category_id INTEGER PRIMARY KEY, name TEXT NOT NULL, description TEXT)',
                'CREATE TABLE products (product_id INTEGER PRIMARY KEY, name TEXT NOT NULL, description TEXT, category TEXT NOT NULL, price REAL NOT NULL, stock_quantity INTEGER NOT NULL, color TEXT, weight TEXT, dimensions TEXT)']

insert_stmt1 = """INSERT INTO categories (category_id, name, description) VALUES
(1, 'Electronics', 'Devices and gadgets for everyday use.'),
(2, 'Fitness', 'Equipment and accessories for fitness activities.'),
(3, 'Home & Kitchen', 'Products for home improvement and kitchen use.'),
(4, 'Bath', 'Bathroom prodcuts and accessories.')"""

insert_stmt2 = """INSERT INTO products (product_id, name, description, category, price, stock_quantity, color, weight, dimensions) VALUES
(2001, 'Wireless Mouse', 'Ergonomic wireless mouse with customizable buttons.', 'Electronics', 19.99, 150, 'Black', '100g', '4.5 x 2.5 x 1.5 inches'),
(2002, 'Mechanical Keyboard', 'High-quality mechanical keyboard with RGB lighting.', 'Electronics', 89.99, 75, 'RGB', '800g', '17.5 x 5.5 x 1.5 inches'),
(2003, 'Yoga Mat', 'Non-slip yoga mat for comfort and stability.', 'Fitness', 29.99, 200, 'Purple', '600g', '72 x 24 x 0.25 inches'),
(2004, 'Mechanical Keyboard', 'High-quality mechanical keyboard with RGB lighting.', 'Electronics', 89.99, 75, 'RGB', '800g', '17.5 x 5.5 x 1.5 inches'),
(2005, 'Shampoo', 'The best shampoo product you can use.', 'Bath', 8.99, 111, 'Pearl', '16oz', '1.5 x 6 x 1.5 inches'),
(2006, 'Soap', 'Bacterial Soap for everyday use.', 'Bath', 12.89, 200, 'Mint', '4oz', '3.5 x 2.5 x 1.5 inches'),
(2007, 'Shower Head', 'Multiform, easy-to-use shower head.', 'Bath', 29.99, 100, 'Chrome', '2lb', '7 x 5 x 6 inches'),
(2008, 'Mouse Pad', 'Durable mousepad suitable for numerous use cases.', 'Electronics', 14.99, 75, 'Blue/Black', '4oz', '9.5 x 7.5 x 0.5 inches'),
(2009, 'Basketball', 'Long lasting rubber indoor/outdoor basketball.', 'Fitness', 16.99, 120, 'Orange', '1lb', '9.5 inches'),
(2010, 'Baseball Glove', 'Large size, leather, durable.', 'Fitness', 19.79, 100, 'Brown', '10oz', '10.5 x 9 x 2 inches')"""

insert_stmts = [insert_stmt1, insert_stmt2]

db_file = 'product_data.db'
tables = ['categories', 'products']

try:
    with sqlite3.connect(db_file) as connection:
        print(f'Database connection opened.')
        cursor = connection.cursor()
        for idx, table in enumerate(tables):
            cursor.execute(f'DROP TABLE IF EXISTS {table}')
            print(f'--> {table} table dropped.')
            cursor.execute(create_stmts[idx])
            print(f'--> {table} table created')
            print(f'Inserting data into {table} table...')
            cursor.execute(insert_stmts[idx])
            print('Data inserted into table.')
except Exception as err:
    print('Warning: ', f'Data NOT loaded into {db_file}')
    print(f'Database Error (Type: {type(err)})\nError: {err}', file=sys.stderr)
finally:
    connection.close()
    print(f'Database connection on {db_file} closed')
