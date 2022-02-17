i = 0
while(True):

    if i+1<5:
        i = i+1
        continue

    print(i+1, end=" ")
    if(i == 44):
        break
    i = i+1

while(True):
    a = float(input("Enter a number: \n"))
    if a>100:
        print("Congrats no is greater than 100\n")
        break
    else:
        print("Try again!!!\n")
        continue
