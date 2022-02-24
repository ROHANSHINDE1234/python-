class Employee:
    no_of_leaves = 8
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole


    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

harry = Employee("Harry", 455, "Instructor")
rohan = Employee("Rohan",344, "Student")

# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 344
# rohan.role = "Student"

print(rohan.printdetails())
print(harry.printdetails())

print(rohan.no_of_leaves)


