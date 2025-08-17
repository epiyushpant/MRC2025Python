# Polymorphism
class Bird:
    def fly(self):
        print("Some birds can fly")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies fast")

class Penguin(Bird):
    def fly(self):
        print("Penguins can't fly")

# Data Hiding (Name Mangling)
class SecureData:
    def __init__(self):
        self.__secret = "12345"  # Private variable

    def get_secret(self):  # Getter method
        return self.__secret[-2:]  # Only show last 2 digits

    def set_secret(self, new_secret):  # Setter method
        if len(new_secret) >= 5:
            self.__secret = new_secret

# Demonstration
birds = [Sparrow(), Penguin()]
for bird in birds:
    bird.fly()  # Same method, different behaviors

data = SecureData()
print("Partial secret:", data.get_secret())  # "45"
data.set_secret("67890")
print("Updated partial:", data.get_secret())  # "90"
# print(data.__secret)  # Error: AttributeError