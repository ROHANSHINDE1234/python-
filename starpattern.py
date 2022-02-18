n = int(input("Enter number of rows of star: "))
B = bool(int(input("Enter True or False")))
if B == 1:
    for i in range(n+1):
        print(i*"*")
elif B == 0:
    for i in range(n+1):
        print((n-i)*"*")