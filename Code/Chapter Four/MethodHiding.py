class Student:
    def __init__(self, name, grade):
        self.name = name              # Public attribute
        self.__grade = grade          # Private (hidden) attribute

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Invalid grade!")

    def get_grade(self):
        return self.__grade

# Usage
s1 = Student("Piyush", 85)

print(s1.name)            # Output: Piyush
print(s1.get_grade())     # Output: 85

s1.set_grade(95)          # Modify safely using method
print(s1.get_grade())     # Output: 95

# Try to access directly (will cause error)
# print(s1.__grade)       # ❌ Error

# But can still access using name mangling (not recommended)
print(s1._Student__grade) # ⚠️ Output: 95
