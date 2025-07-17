class Father:
    def skills(self):
        print("Gardening, Programming")

class Mother:
    def skills(self):
        print("Cooking, Art")

class Child(Father, Mother):
    def skills(self):
        Father.skills(self)  # Call Father's skills
        Mother.skills(self)  # Call Mother's skills
        print("Sports")

c = Child()
c.skills()
