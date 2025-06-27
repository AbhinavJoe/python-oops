"""
📌 Question:
Write a Report class that depends on an Output abstraction to print data.
Create two implementations of Output: ConsoleOutput and FileOutput.
Make sure Report depends on the abstraction, not the concrete classes.
(Demonstrate with constructor injection or setter injection.)
"""

from abc import ABC, abstractmethod


class Output(ABC):
    @abstractmethod
    def print_data(self):
        pass


class ConsoleOutput(Output):
    def print_data(self):
        print("Print data to console")


class FileOutput(Output):
    def print_data(self):
        filename = 'file_output.txt'
        with open(filename, "w") as f:
            f.write("Print data to file")
        print(f"Data written to {filename}")


class Report:
    def __init__(self, output_strategy: Output):
        self.output_strategy = output_strategy

    def print_output_data(self):
        self.output_strategy.print_data()


outputs = [ConsoleOutput(), FileOutput()]
for output in outputs:
    report = Report(output)
    report.print_output_data()
