import unittest

from src.service.notification import NotificationService

class MockDatabaseService:
    def fetch_data(self):
        print("Mock fetch_data method called.")

class MockDatabaseServiceRaisesError:
    def fetch_data(self):
        print("Mock fetch_data method called.")
        raise Exception("notification error")


class TestNotificationService(unittest.TestCase):
    def setUp(self):
        self.mock_database_service = MockDatabaseService()
        self.notification_service = NotificationService(self.mock_database_service)

    def test_send_notification_with_success_scenario(self):
        self.mock_database_service = MockDatabaseService()
        self.notification_service = NotificationService(self.mock_database_service)

        expected_output = "Sending notification: Test message"
        with self.assertLogs(level="INFO") as cm:
            self.notification_service.send_notification("Test message")
        self.assertIn(expected_output, cm.output[0])

    def test_send_notification_with_exception_scenario(self):
        self.mock_database_service = MockDatabaseServiceRaisesError()
        self.notification_service = NotificationService(self.mock_database_service)
        expected_output = "Notification failure due to the exception: notification error"
        with self.assertLogs(level="ERROR") as cm:
            self.notification_service.send_notification("Test message")
        self.assertIn(expected_output, cm.output[0])


