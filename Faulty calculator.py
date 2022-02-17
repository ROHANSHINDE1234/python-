#design a calculator which will correctly solve all tghe problems except the folloing
#45*3 = 555, 56*9=77, 56/6=4
#your code should take operator and two numbers as input from the user and then return the result
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = ["+", "-", "*", "/"]
print("+ indicates addition,- indicates subtraction,/ indicates division, * indicates multiplication  ")
print(operation)
c = input("operator required: ")
faulty_numbers = [45,3,56,9,56,6]
if c == "+":
    print(a+b)
elif c == "-":
    print(a-b)
elif c == "*":
    if (a == 45) & (b == 3):
        print("555")
    elif (a == 56) & (b == 9):
        print("77")
    else:
        print(a*b)
else:
    if (a == 56) & (b == 6):
        print("4")
    else:
        print(a/b)


