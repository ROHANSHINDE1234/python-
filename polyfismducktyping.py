class Pycharm:
    def execute(self):
        print("Compiling")
        print("Running")

class Mycompiler:
    def execute(self):
        print("Compiling2")
        print("Running2")


class Laptop:
    def code(self,ide):
        ide.execute()

ide = Pycharm()
ide = Mycompiler()

lap1 = Laptop()
lap1.code(ide)


