class Vehicle:
    def __init__(self,cost,mileage):
        self.cost = cost
        self.mileage = mileage
    def show_details(self):
        print("This is a vehicle")
        print(f"Cost of this vehicle is {self.cost} rs.")
        print(f"It runs {self.mileage} km in 1 liter.")
v1 = Vehicle(200,15)
# v1.show_details()

class Car(Vehicle):
    def show_car(self):
        print("This is inherted class")
        print(f"Cost of this vehicle is {self.cost} rs.")
        print(f"It runs {self.mileage} km in 1 liter.")

v2 = Car(300,5)
# v2.show_details()
v2.show_car()

