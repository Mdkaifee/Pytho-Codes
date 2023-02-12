class vehicle:
    def __init__(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost
    def show_vehicle_details(self):
        print("Mileage is:",self.mileage)
        print("Cost is:",self.cost)
v1=vehicle(300,500)
v1.show_vehicle_details()

class Car(vehicle):
    def show_car_details(self):
        print("I am a car")
c1=Car(250,555)
c1.show_car_details()