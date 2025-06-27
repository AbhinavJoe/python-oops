# class people:
#     def __init__(self, name: str, age: int) -> None:
#         self.name: str = name
#         self.__age: int = age #__age is a private class variable

#     def test(self):
#         self.name
#         pass

#     # Getter
#     def getName(self):
#         return self.__age

#     #Setter
#     def setName(self, value):
#         self.__age = value


# if (__name__ == "__main__"):
#     person1 = people("Abhinav", 21)
#     person2 = people("Josef", 20)
#     person3 = people("Someone", 20)

#     print()


from abc import ABC, abstractmethod


class people:
    def _init_(self, name: str, age: int) -> None:
        self.__name: str = name
        self.__age: int = age  # __age is a private class variable

    def getName(self):
        return self.__name

    def setName(self, value):
        self.__name = value

# Inheritance
# Animal is an abstract class. ABC defines it as an abstract class and then we need to define each method inside the class as an abstract method


class Animal(ABC):
    @abstractmethod
    def _init_(self, name, age) -> None:
        self.name = name
        self.age = age
        super()._init_()

    @abstractmethod
    def speak(self):
        pass

# The dog and Cat classes are normal classes that are using the abstract class, basically using a common strucutre from that class using super()


class Dog(Animal):
    def _init_(self, name, age, breed) -> None:
        super()._init_(name, age)
        self.breed = breed

    def speak(self):
        print("BARK!")


class Cat(Animal):
    def _init_(self, name, age) -> None:
        super()._init_(name, age)

    def speak(self):
        print("MEOW!")


if (__name__ == "__main__"):
    person1 = people("Abhinav", 500)
    person2 = people("Josef", 20)

    person1.setName("Liba")
    print(person1.getName())
