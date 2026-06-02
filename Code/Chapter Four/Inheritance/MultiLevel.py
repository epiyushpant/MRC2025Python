class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def show_employee(self):
        print(f"Employee ID: {self.employee_id}")

class Manager(Employee):
    def __init__(self, name, age, employee_id, team_size):
        super().__init__(name, age, employee_id)
        self.team_size = team_size

    def show_manager(self):
        print(f"Manages a team of {self.team_size} people")

# Usage
mgr = Manager("Alice", 35, "E123", 10)
mgr.show_person()     # From Person class
mgr.show_employee()   # From Employee class
mgr.show_manager()    # From Manager class
