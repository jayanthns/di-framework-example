import unittest

from src.container import DIContainer
from src.service.db import DatabaseService
from src.service.notification import NotificationService
from src.service.payment import PaymentService


class TestDIContainer(unittest.TestCase):
    def test_registration(self):
        container = DIContainer()
        container.register(DatabaseService)
        container.register(PaymentService)
        container.register(NotificationService)
        self.assertIn('DatabaseService', container.registry)
        self.assertIn('PaymentService', container.registry)
        self.assertIn('NotificationService', container.registry)

    def test_resolution(self):
        container = DIContainer()
        container.register(DatabaseService)
        container.register(PaymentService)
        container.register(NotificationService)
        payment_service = container.resolve(PaymentService)
        notification_service = container.resolve(NotificationService)
        self.assertIsInstance(payment_service, PaymentService)
        self.assertIsInstance(notification_service, NotificationService)
        self.assertIsInstance(payment_service.database_service, DatabaseService)
        self.assertIsInstance(notification_service.database_service, DatabaseService)

    def test_resolution_with_unregistered_class(self):
        container = DIContainer()
        with self.assertRaises(Exception) as cm:
            container.resolve(DatabaseService)
        self.assertEqual(str(cm.exception), "Class DatabaseService is not registered in the container.")

    def test_resolution_with_unresolved_dependency(self):
        class MyClass:
            def __init__(self, dependency):
                self.dependency = dependency

        container = DIContainer()
        container.register(MyClass)
        with self.assertRaises(Exception) as cm:
            container.resolve(MyClass)
        self.assertEqual(str(cm.exception), "Unable to resolve dependency for parameter 'dependency' in class 'MyClass'")

