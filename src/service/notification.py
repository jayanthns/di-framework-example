import logging

from src.service.db import DatabaseService


class NotificationService:
    def __init__(self, database_service: DatabaseService):
        self.database_service = database_service

    def send_notification(self, message):
        # Simulate sending notifications
        try:
            self.database_service.fetch_data()
            logging.info(f"Sending notification: {message}")
        except Exception as e:
            logging.error(f"Notification failure due to the exception: {str(e)}")
