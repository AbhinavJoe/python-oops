"""
Question:
Create a BankAccount class where the account balance cannot be directly modified from outside the class.

The balance should only change through deposit(amount) and withdraw(amount) methods.

The withdrawal method should not allow overdrafts.

Include a method to check the current balance safely.
"""


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit_money(self, amount: int) -> int | None:
        if amount <= 0:
            print("Deposit amount must be positive!")
            return None

        self.__balance += amount
        return self.__balance

    def withdraw_money(self, amount: int) -> int | None:
        if amount > self.__balance:
            print("Insufficient funds")
            return None

        self.__balance -= amount
        return self.__balance


bank_instance = BankAccount(2000)
print(bank_instance.get_balance())
print(bank_instance.deposit_money(1000))
print(bank_instance.withdraw_money(2000))
