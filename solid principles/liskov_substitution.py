"""
📌 Question:
Implement a Bird class with a fly() method.
Then create a Penguin class.
Show how violating Liskov Substitution can break code expecting any Bird, and then adjust your design to satisfy Liskov, e.g., 
via interfaces or separating flying vs. non-flying birds.
"""

# Below will violate Liskov Substitution


class Bird:
    def __init__(self):
        pass

    def fly(self):
        print("Bird is Flying")


class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly :(")


birds = [Bird(), Penguin()]
for bird in birds:
    bird.fly()


# Following Liskov Substitution

class CanFly:
    def __init__(self):
        pass

    def fly(self):
        print("It is a flying bird")


class CannotFly:
    def __init__(self):
        pass

    def fly(self):
        print("It is a non flying bird")


class Bird2(CanFly):
    def fly(self):
        return super().fly()


class Penguin2(CannotFly):
    def fly(self):
        return super().fly()


birds2 = [Bird2(), Penguin2()]
for bird in birds2:
    bird.fly()
