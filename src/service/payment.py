import unittest
import logging

from src.service.db import DatabaseService

class PaymentService:
    def __init__(self, database_service: DatabaseService):
        self.database_service = database_service

    def process_payment(self, amount):
        # Perform payment processing
        try:
            self.database_service.fetch_data()
            logging.info(f"Processing payment of {amount}... Payment processed successfully!")
        except Exception as e:
            logging.error(f"Payment process failed due to the exception: {str(e)}")
