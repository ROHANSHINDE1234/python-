# classes - Template
#object - instance of the class
# DRY - Do not repeat your self
# get_no_of_films()

class Student:
    pass
harry = Student()
rohan = Student()

harry.name = "Harry"
harry.std = 12
harry.section = 1

rohan.std = 9
rohan.subjects = ["hindi", "english"]
print(harry.name, rohan.std)
