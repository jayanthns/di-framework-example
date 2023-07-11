# Custom Dependency Injection Framework

This project implements a custom Dependency Injection (DI) framework in Python and demonstrates its usage in a simple e-commerce system.

## Objective

The objective of this project is to develop a custom DI framework from scratch and apply it to manage dependencies in an e-commerce system.

## Features

- Custom Dependency Injection framework (`DIContainer`) for managing dependencies.
- Registration mechanism for classes and interfaces along with their dependencies.
- Resolution mechanism to resolve dependencies when classes or interfaces are requested.
- Infrastructure classes for the e-commerce system:
  - `DatabaseService` to simulate database interactions.
  - `PaymentService` to simulate payment processing.
  - `NotificationService` to simulate sending notifications.

## Usage

1. Clone the repository:

```bash
git clone https://github.com/jayanthns/di-framework-example.git
cd di-framework-example
```

2. Create a virtualenvironment

   1. On Windows
      ```bash
      python3 -m venv venv
      venv/Scripts/activate
      ```
   2. On Linux/Mac
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Run the tests to ensure the DI framework and infrastructure classes are functioning correctly:

```bash
python -m unittest
```

5. How to use the DIContainer with `register` and `resolve`.

```python
container = DIContainer()
container.register(DatabaseService)
container.register(PaymentService)
container.register(NotificationService)

# Resolve instances from the container
db_service = container.resolve(DatabaseService)
payment_service = container.resolve(PaymentService)  # Get the payment service instance
notification_service = container.resolve(NotificationService)  # Get the notification service instance

# Use the resolved instances
db_service.fetch_data()
payment_service.process_payment(100)
notification_service.send_notification("Payment successful")
```
