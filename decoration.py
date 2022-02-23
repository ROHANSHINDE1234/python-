def function1():
    print("Subscribe now")

func2 = function1
del function1
func2()

def funcret(num):
    if num == 0:
        return print
    if num == 1:
        return sum

a = funcret(1)
print(a)

def executer(func):
    func("this")

executer(print)
import time
def dec1(func1):
    def nowexec():
        print("Executing now")
        time.sleep(2)
        func1()
        print("Ececuted")
    return nowexec
@dec1
def who_is_rohan():
    print("Rohan is a good boy")

# who_is_rohan = dec1(who_is_rohan) [= @dec1]

who_is_rohan()

