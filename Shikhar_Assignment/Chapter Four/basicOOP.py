# Class and Object demonstration
class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Create objects
dog1 = Dog("Buddy", 5)
dog2 = Dog("Milo", 3)

# Access attributes and methods
print(dog1.description())
print(dog2.speak("Woof!"))
print(f"All dogs are {Dog.species}")