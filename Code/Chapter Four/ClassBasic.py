# write code in python to explain self and init keyword 
# This script demonstrates the use of `self` and `__init__` in Python classes.

class Person:
    def __init__(self, name, age):
# Initialize a new Person instance with a name and age.
        self.name = name 
        self.age = age    

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
# Example usage

if __name__ == "__main__":
    person1 = Person("Alice", 30)
    print(person1.greet())  
    
    person2 = Person("Bob", 25)
    print(person2.greet())  #



