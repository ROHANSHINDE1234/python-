class Parent():
    def assign_name(self,name):
        self.name = name
    def show_name(self):
        return self.name

class Child(Parent):
    def assign_age(self,age):
        self.age = age
    def show_age(self):
        return self.age

class Grandchild(Child):
    def assign_gender(self,gender):
        self.gender = gender
    def show_gender(self):
        return self.gender
p1 = Grandchild()
p1.assign_name("Rohan")
p1.assign_age(21)
p1.assign_gender("male")

print(p1.show_name())
print(p1.show_age())
print(p1.show_gender())