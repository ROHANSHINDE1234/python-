f = open("rohan.txt", "rt")
print(f.readlines())



print(f.readline())
print(f.readline())
print(f.readline())

content = f.read()
for line in f:
    print(line, end="")

print(content)
content = f.read(3)
print("1",content)

content = f.read(883)
print("2",content)

f.close()