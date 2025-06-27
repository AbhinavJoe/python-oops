"""
📌 Question:
Design a Worker interface (or abstract base class in Python) with methods like work(), eat(), sleep().
Then create HumanWorker that does all these, and RobotWorker that should not be forced to implement eat() or sleep().
Refactor the interfaces so classes only implement what they need.
"""

from abc import ABC, abstractmethod


class Worker(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def work(self):
        pass


class WorkerNeeds(Worker, ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass


class HumanWorker(WorkerNeeds):
    def work(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass


class RobotWorker(Worker):
    def work(self):
        pass


human = HumanWorker()
robot = RobotWorker()
