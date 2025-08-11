"""
Better Polymorphism Challenge

Scenario:
You are building a payment processing system for an e-commerce platform.
Different payment methods (Credit Card, PayPal, Crypto) have different rules for:

- Processing the payment (process_payment(amount))

- Generating a payment receipt (generate_receipt(transaction_id))

- The core payment system:

    Should only interact with an abstract PaymentMethod interface/base class.

    Must be able to add new payment methods in the future without modifying existing code (hint: polymorphism + Open/Closed Principle).

    The checkout() function should accept any payment method instance and process it without knowing its concrete type.

Requirements:

- PaymentMethod (abstract base class/interface) defines process_payment(amount) and generate_receipt(transaction_id).

Implement:

- CreditCardPayment

- PayPalPayment

- CryptoPayment

Write a checkout(payment_method, amount) function that:

- Calls process_payment

- Calls generate_receipt

- Show usage with a list of mixed payment methods.

Example behavior:

Processing credit card payment of $500...
Receipt generated for credit card transaction: TXN123
Processing PayPal payment of $200...
Receipt generated for PayPal transaction: TXN124
Processing crypto payment of $1000...
Receipt generated for crypto transaction: TXN125


This makes you:

- Apply polymorphism in a business-relevant context.

- Design an extensible architecture where you can add ApplePayPayment later without changing checkout().

- Understand why we don’t do if type == "creditcard" checks in good OOP design.
"""
