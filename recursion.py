def print2(str1):
    print("this is " + str1)

print2("rohan")

def factorial_itrative(n):
    fac = 1
    for i in range(n):
        fac = fac*(i+1)
    return fac


    pass
number = int(input("Enter a number: "))
print("Factorial using iteration",factorial_itrative(number))

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n*factorial_recursive(n-1)
number = int(input("Enter a number: "))
print("Factorial using recursive",factorial_recursive(number))
# Quiz

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
number = int(input("Enter a number: "))
print(fibonacci(number))

