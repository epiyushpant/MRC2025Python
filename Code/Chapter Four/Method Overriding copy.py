class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        super().speak()      # Call the parent class method
        print("Dog barks")   # Child class behavior

# Create Dog object
d = Dog()
d.speak()
