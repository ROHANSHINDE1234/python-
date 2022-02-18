a = 9
b = 8
c = sum((a,b))#built in function
print(c)

def function(a, b):
    print("Hello you are in Function", a+b)
def function1(a,b):
    """This is a function which return average of two numbers"""
    average = (a+b)/2
    print(average)
    return average

v = function1(5,7)
print(v)
print(function1.__doc__)

