#ETAPE 1
class Bike:
    def __init__(self):
        self.speed = 15
        self.distance = 0
    def ride(self, temps):
        deplacement = self.speed * temps
        self.distance = self.distance + deplacement

class Car:
    def __init__(self):
        self.speed = 100
        self.distance = 0
    def ride(self, temps):
        deplacement = self.speed * temps
        self.distance = self.distance + deplacement

#ETAPE2
class Bike:
    def __init__(self, speed):
        self.speed = speed
        self.distance = 0
    def ride(self, temps):
        deplacement = self.speed * temps
        self.distance = self.distance + deplacement

class Car:
    def __init__(self, speed):
        self.speed = speed
        self.distance = 0
    def ride(self, temps):
        deplacement = self.speed * temps
        self.distance = self.distance + deplacement

class Vehicle:
    def __init__(self, speed):
        self.speed = speed
        self.distance = 0
    
    def ride(self, temps):
        deplacement = temps * self.speed
        self.distance = self.distance + deplacement

#ETAPE3
class Bike(Vehicle):
    def __init__(self):
        super().__init__(15)


class Car(Vehicle):
    def __init__(self):
        super().__init__(100)

#ETAPE4
class Car(Vehicle):
    def __init__(self):
        super().__init__(100)
        self.fuel = 100
        self.consumption = 0.05
    
    def ride(self, duration):
        super().ride(duration)
        self.fuel= self.fuel - (self.consumption * duration * self.speed)
    
    def fill_tank(self, fuel_volume):
        self.fuel = self.fuel + fuel_volume 