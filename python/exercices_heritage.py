class Vehicle:
    def __init__(self, speed):
        self.speed = speed
        self.distance = 0
    def ride(self, temps):
        deplacement = temps * self.speed
        self.distance = self.distance + deplacement

class Train(Vehicle):
    def __init__(self, max_passengers):
        super().__init__(100)
        self.passengers = 0
        self.max_passengers = max_passengers
    def take_on_board(nouveau):
        self.passengers = self.passengers + nouveau
        if self.passengers > self.max_passengers:
            self.passengers = self.passengers

class TrainInterCity(Train):
    def __init__(self):
        super().__init__(100)
        self.profit_by_kilometer = 2.5
        self.profit = 0
    def ride(self, temps):
        deplacement = temps * self.speed
        self.distance = self.distance + deplacement
        self.profit = self.profit + (self.profit_by_kilometer*deplacement)
    def take_on_board(nouveau):
        self.passengers = self.passengers + nouveau
        if self.passengers > self.max_passengers:
            self.passengers = self.passengers

class FreightTrain(Train):
    def __init__(self):
        super().__init__(4)
        self.cargo = 0
    def load_cargo(new_cargo):
        self.cargo = self.cargo + new_cargo
    def take_on_board(nouveau):
        self.passengers = self.passengers + nouveau
        if self.passengers > self.max_passengers:
            self.passengers = self.passengers
