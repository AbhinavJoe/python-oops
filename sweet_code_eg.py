from abc import ABC, abstractmethod

# Abstractopm


class Employee(ABC):

    def __init__(self, name: str, salary: str):
        self.name = name
        self.salary = salary

    @abstractmethod
    def work(self):
        pass

# Inheritance 1


class Tester(Employee):

    def __init__(self, name: str, salary: str):
        super().__init__(name, salary)

    def test(self):
        print("{} is testing".format(self.name))

    def work(self):
        self.test()

#  Inheritance 2


class Developer(Employee):

    def __init__(self, name: str, salary: str):
        super().__init__(name, salary)

    def develop(self):
        print("{} is developing".format(self.name))

    def work(self):
        self.develop()

# Polymorphism 1


class Company:

    def __init__(self, name: str):
        self.name = name

    def work(self, employee: Employee):
        employee.work()


# Polymorphism 2
employees = [Developer("Abhinav", "85000"), Tester("Suman", "60000")]

for employee in employees:
    employee.work()
