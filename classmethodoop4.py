class Employee:
    no_of_leaves = 8
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole


    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary}" \
               f" and role is {self.role}"
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves


harry = Employee("Harry", 455, "Instructor")
rohan = Employee("Rohan",344, "Student")

Employee.no_of_leaves = 89
print(harry.no_of_leaves)