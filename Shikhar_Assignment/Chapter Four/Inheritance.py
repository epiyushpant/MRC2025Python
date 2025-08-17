# Single Inheritance
class Animal:
    def speak(self):
        print("Animal nakes sound")

class Dog(Animal):  # Single inheritance
    def bark(self):
        print("Dog barks")

# Multilevel Inheritance
class Puppy(Dog):
    def weep(self):
        print("Puppy weeps")

# Multiple Inheritance
class A:
    def method(self):
        print("Method A")

class B:
    def method(self):
        print("Method B")

class C(A, B):  # Multiple inheritance
    pass

# Hierarchical Inheritance
class Cat(Animal):
    def meow(self):
        print("Cat meows")

# Demonstration
d = Dog()
d.speak()  # Inherited
d.bark()

p = Puppy()
p.weep()
p.bark()  # Inherited from Dog
p.speak() # Inherited from Animal

c = C()
c.method()  # Uses A's method (first parent)

cat = Cat()
cat.speak()
cat.meow()