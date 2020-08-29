from bike_heritage import Bike, Car, Vehicle

bike = Bike()
car = Car()

bike.ride(2)
car.ride(2)
print(bike.distance)
print(car.distance)
print(bike.ride)
print(car.ride)
car.fill_tank(15)
print(car.fuel)