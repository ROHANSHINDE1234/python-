l = 10 #global
def function1(n):
    #l = 5 #local
    global l
    l = l +45
    m = 8 #local
    print(l,m)
    print(n, "I have printed")
function1("I am rohan")
print(l)
x = 89
def harry():
    x = 20
    def rohan():
        global x
        x = 88
    print("Before calling rohan", x)
    rohan()
    print("after calling rohan", x)
harry()
print(x)
#quiz

