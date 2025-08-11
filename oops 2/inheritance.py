"""
Question:
Create a base class Vehicle with common attributes like make, model, and year.

Create two subclasses: Car and Motorcycle that inherit from Vehicle.

Add specific attributes for each (e.g., number_of_doors for Car, type_of_handlebar for Motorcycle).

Demonstrate creating instances and calling both inherited and subclass-specific methods.
"""


class Vehicle:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def start(self) -> str:
        return f"{self.year} {self.make} {self.model} has started."


class Car(Vehicle):
    def __init__(self, make: str, model: str, year: int, number_of_doors: int, engine: str):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors
        self.engine = engine

    def start(self) -> str:
        return f"{super().start()} It has {self.number_of_doors} doors and a {self.engine} engine."


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str, year: int, handlebar_width: int, super_bike: bool):
        super().__init__(make, model, year)
        self.handlebar_width = handlebar_width
        self.super_bike = super_bike

    def start(self) -> str:
        bike_type = "superbike" if self.super_bike else "regular bike"
        return f"{super().start()} It has a {self.handlebar_width}-inch handlebar and is a {bike_type}."


instances = [
    Car("Honda", "Civic", 2020, 4, "V8"),
    Motorcycle("Kawasaki", "Ninja", 2025, 10, True)
]

for instance in instances:
    print(instance.start())
