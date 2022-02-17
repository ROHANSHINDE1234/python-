
var1 = 6
var2 = 56

var3 = int(input())

if var3>var2:
    print("Greater")
elif var3==var2:
    print("equal")
else:
    print("Lesser")

list1 = [5, 7, 6]
print(5 not in list1)
if 5 in list1:
    print("yes in list")

#Quiz
print("What is your age?")
age = int(input())
if 7<=age<=70:

    if age<18:
        print("You cannot drive")
    elif age==18:
        print("we cannot decide")
    else:
        print("you can drive")
else:
    print("Age out of range")
