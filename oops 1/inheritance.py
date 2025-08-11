class Person:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    def get_details(self):
        return {"Name": self.__name, "Email": self.__email}


class Intern(Person):
    def do_task(self):
        return f"{self.get_details()['Name']} is an intern and is doing the assigned tasks."


class Employee(Intern):
    def submit_report(self):
        return f"{self.get_details()['Name']} is a full-time employee and has submitted the report."


class Manager(Employee):
    def assign_task(self):
        return f"{self.get_details()['Name']} is a manager and has assigned tasks to the team."


class Director(Manager):
    def make_decision(self):
        return f"{self.get_details()['Name']} is a director and has made a strategic decision."


# Example usage
if __name__ == "__main__":
    director = Director("Abhinav Joshi", "abhinav@example.com")
    print(director.get_details())
    print(director.make_decision())
    print(director.assign_task())
    print(director.do_task())
    print(director.submit_report())
