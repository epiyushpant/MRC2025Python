class Employee:
    def salary(self):
        print("Base salary")

class Manager(Employee):
    def salary(self):
        print("Manager salary with bonus")

m = Manager()
m.salary()  # Output: Manager salary with bonus