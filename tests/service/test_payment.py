import unittest

from src.service.payment import PaymentService

class MockDatabaseService:
    def fetch_data(self):
        print("Mock fetch_data method called.")

class MockDatabaseServiceRaisesError():
    def fetch_data(self):
        print("Mock fetch_data method called.")
        raise Exception("payment error")

class TestPaymentService(unittest.TestCase):

    def test_process_payment_with_success_scenario(self):
        self.mock_database_service = MockDatabaseService()
        self.payment_service = PaymentService(self.mock_database_service)

        expected_output = "Processing payment of 100... Payment processed successfully!"
        with self.assertLogs(level="INFO") as cm:
            self.payment_service.process_payment(100)
            self.assertIn(expected_output, cm.output[0])

    def test_process_payment_with_error_scenario(self):
        self.mock_database_service = MockDatabaseServiceRaisesError()
        self.payment_service = PaymentService(self.mock_database_service)

        expected_output = "Payment process failed due to the exception: payment error"
        with self.assertLogs(level="ERROR") as cm:
            self.payment_service.process_payment(100)
            self.assertIn(expected_output, cm.output[0])
