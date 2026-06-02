class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Woof Woof")

# Usage
animal = Animal()
animal.speak()  # Output: Animal speaks

dog = Dog()
dog.speak()  # Output: Woof Woof