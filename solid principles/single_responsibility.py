# MARK: Q. 1
"""
📌 Question:
Write a Python class Invoice that handles a list of items and computes the total.
Then, create a separate class to handle saving the invoice data to a file.
This forces you to split responsibilities: calculation vs. persistence.
"""


from typing import Dict


class Invoice:
    def __init__(self, items):
        self.items = items

    def total(self):
        return sum(self.items.values())


class InvoiceSaver:
    def save_to_file(self, invoice, filename="invoice.txt"):
        with open(filename, "w") as f:
            f.write(f"Items: {invoice.items}\n")
            f.write(f"Total: {invoice.total()}\n")
        return "Invoice Saved!"


# Usage
items = {"shampoo": 5, "chips": 10}
invoice = Invoice(items)
print(f"Total: {invoice.total()}")

saver = InvoiceSaver()
print(saver.save_to_file(invoice))

# MARK: Q. 2
"""
🚀 📝 Single Responsibility Principle problem
📌 The Problem
You are building a user management module for a simple app.
You start by writing a class like this:

python
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def validate_email(self):
        # checks if email has '@' and '.'
        pass

    def save_to_database(self):
        # code that connects to DB and saves user
        pass

    def send_welcome_email(self):
        # code to send email to self.email
        pass

❌ What’s wrong?
This class:

validates data

persists data

handles communication

It does way too much. If validation rules change, or database changes, or you switch to sending SMS instead of email — this class has multiple reasons to change.
It violates SRP.

🎯 Your task
👉 Refactor this into multiple classes, each with a single responsibility.
Try to separate:

user data,

validation,

persistence,

communication.

Use Python classes for each.
Show how the classes will work together.
"""


class User:
    def __init__(self, username, email):
        self._username = username
        self._email = email

    @property
    def username(self):
        return self._username

    @property
    def email(self):
        return self._email


class VaildateEmail:
    def validate_email(self, user: User):
        email = user.email
        if not email:
            return "Email is not valid!"
        return "Email is valid!"


class SaveToDB:
    def save_user(self, user: User):
        db = {}
        email = user.email
        if email not in db:
            db[email] = user
            return "User saved to database!"
        return "User already exists!"


class OnboardEmail:
    def welcome_email(self, user: User):
        email = user.email
        return f"Welcome {email} to the user management module"


user = User("john_doe", "john@example.com")

validator = VaildateEmail()
print(validator.validate_email(user))

repo = SaveToDB()
print(repo.save_user(user))

notifier = OnboardEmail()
print(notifier.welcome_email(user))
