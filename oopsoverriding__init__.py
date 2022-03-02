class Vehicle:
    def __init__(self,cost,mileage):
        self.cost = cost
        self.mileage = mileage

    def show_details(self):
        print("This is parent class!")
        print("This is a vehicle")
        print(f"Cost of this vehicle is {self.cost} rs.")
        print(f"It runs {self.mileage} km in 1 liter.")

class Car(Vehicle):
    def __init__(self,cost,mileage,tyre,color):
        super().__init__(cost,mileage)
        self.tyre = tyre
        self.color = color

    def show_car_details(self):
        print("This is a Inhereted class!")
        print(f"This vehicle has {self.tyre} tyres.")
        print(f"It is {self.color} in colour.")

c1 = Car(30000,5,4,"Blue")
c1.show_details()
print("\n")
c1.show_car_details()