grocery = ["harpic", "vim", "deodrant", "bhindi",
           "lollypop"]
print(grocery[1])
numbers = [2, 7, 9, 11, 3]


print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()

print(numbers[0:5])
print(numbers[:5])
print(numbers[0:])
print(numbers[::2])
print(len(numbers))
print(max(numbers))
print(min(numbers))
numbers.append(71)

#numbers.insert(1,67)
#mutable can change
#immutable cannot change
tp = (1, 2, 3)
print(tp)
a = 1
b = 8
a, b = b, a
print(a,b)



