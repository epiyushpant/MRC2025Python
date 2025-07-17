
# write code in python to explain single inheritance in python

class Animal:
    def __init__(self, species):
        self.species = species  
    def make_sound(self):
        return "Some sound"
    
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__("Dog")  # Call the parent class constructor    
        self.name = name  
        self.age = age   

    def make_sound(self):
        return "Woof Woof"      
    
# Example usage 
if __name__ == "__main__":
    # Create a new Dog instance
    dog1 = Dog("Buddy", 5)
    
    # Call the make_sound method
    print(f"{dog1.name} says: {dog1.make_sound()}")  # Output: Buddy says: Woof Woof
    
    # Print the species of the dog
    print(f"{dog1.name} is a {dog1.species}.")  # Output: Buddy is a Dog.
    
    # Print the age of the dog
    print(f"{dog1.name} is {dog1.age} years old.")  # Output: Buddy is 5 years old. 
