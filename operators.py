#Operators in python
#
# #Arthematic operator
print("5 + 6 = ", 5+6)
print("5 - 6 = ", 5-6)
print("5 / 6 = ", 5/6)
print("5 // 6 = ", 5//6)
print("5 % 6 = ", 5%6)

#Assignment operator
print("#Assignment operator")
x = 5
x +=1
x /=2

x -=1
print(x)

#Comparision operator
i = 53
print(i == 5)
print(i<=3)

#Logical operator
a = True
b = False
print(a and b)
print(a or b )

#Identity operator
print(a is b)
print(a is not b)
print(5 is not 0)

#Membership operator
list = [3, 34 ,345, 234 ,43, 32 ]
print(32 in list)
print(324 in list)
print(324 not in list)

#Bitwise operator
# 0 - 00
# 1 - 01
# 2 - 10
# 3 - 11

print(0 & 1)
print(1 | 2)
print(2 |1)
print(3 & 0)