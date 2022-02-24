class Employee:
    no_of_leaves = 8
    pass

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 344
rohan.role = "Student"

print(rohan.no_of_leaves)

print(rohan.__dict__)

Employee.no_of_leaves = 9

print(harry.no_of_leaves)
print(Employee.__dict__)

