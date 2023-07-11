import sqlite3
import logging


class DatabaseService:
    def __init__(self):
        self.connection = sqlite3.connect(":memory:")
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price REAL
            )
        """)
        self.connection.commit()

    def fetch_data(self):
        self.cursor.execute("SELECT * FROM products")
        data = self.cursor.fetchall()
        data_list = []
        for row in data:
            data_list.append(
                {
                    "product_id": row[0],
                    "name": row[1],
                    "price": row[2]
                }
            )
            logging.info("fetched data succesfully")

    def add_product(self, name, price):
        self.cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
        self.connection.commit()
        logging.info("Product added successfully")

    def close_connection(self):
        self.connection.close()
