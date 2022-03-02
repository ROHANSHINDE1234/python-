class Employee:
    def __init__(self,name,age,salary,gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def employee_details(self):
        print("Name of Employee is: ",self.name)
        print("Age of Employee is: ", self.age)
        print("Salary of Employee is: ", self.salary)
        print("Gender of Employee is: ", self.gender)

e1 = Employee("Rohan",21,300000,"Male")
e2 = Employee("Nihal",22,350000,"Male")

e2.employee_details()
e1.employee_details()