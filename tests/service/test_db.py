import unittest

from src.service.db import DatabaseService

class TestDatabaseService(unittest.TestCase):
    def setUp(self):
        self.database_service = DatabaseService()

    def tearDown(self):
        self.database_service.close_connection()

    def test_fetch_data(self):
        self.database_service.add_product("Product 1", 10.99)
        self.database_service.add_product("Product 2", 19.99)
        expected_output = "fetched data succesfully"
        with self.assertLogs(level="INFO") as cm:
            self.database_service.fetch_data()
            self.assertIn(expected_output, cm.output[0])

    def test_add_product(self):
        expected_output = "Product added successfully"
        with self.assertLogs(level="INFO") as cm:
            self.database_service.add_product("New Product", 24.99)
            self.assertIn(expected_output, cm.output[0])

        expected_output = "fetched data succesfully"
        with self.assertLogs(level="INFO") as cm:
            self.database_service.fetch_data()
            self.assertIn(expected_output, cm.output[0])
