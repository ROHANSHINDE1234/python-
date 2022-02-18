# f = open("rohan1.txt", "w")
# a = f.write("Rohan is smart\n")
# print(a)
# f.close()
#
# f = open("rohan2.txt", "a")
# a = f.write("Rohan is smart\n")
# print(a)
# f.close()

#handle read and write boath
f = open("rohan1.txt","r+")
print(f.read())
f.write("Thank you")
