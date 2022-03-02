class Phone:
    def set_color(self,color):
        self.color = color

    def set_cost(self,cost):
        self.cost=cost

    def show_color(self):
        return self.color

    def show_cost(self):
        return self.cost

    def make_call(self):
        print("Making a call")

    def play_games(self):
        print("Playing games")

p1 = Phone()
p1.make_call()
p1.play_games()
p2 = Phone()
p2.set_color("Blue")
p2.set_cost(5000)
print(p2.show_color())
print(p2.show_cost())
p2.make_call()