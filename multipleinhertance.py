class Parent1:
    def assign_string1(self,str1):
        self.str1 = str1
    def show_string1(self):
        return self.str1

class Parent2:
    def assign_string2(self,str2):
        self.str2 = str2
    def show_string2(self):
        return self.str2

class Derived(Parent1,Parent2):
    def assign_string3(self,str3):
        self.str3 = str3
    def show_string3(self):
        return self.str3

c1 = Derived()
c1.assign_string1("one")
c1.assign_string2(2)
c1.assign_string3("Three")
print(c1.show_string1())
print(c1.show_string2())
print(c1.show_string3())

