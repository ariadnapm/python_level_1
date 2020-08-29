from random import randint
class Fighters:
    def __init__(self, vie, defense, minus, mega):
        self.vie = vie
        self.vie_max = vie
        self.defense = defense
        self.damage = 0
        self.minus = minus
        self.mega = mega
    def attack(self, other_fighter):
        self.damage = randint(self.minus, self.mega)
        self.damage = self.damage - other_fighter.defense
        self.damage = max(0, self.damage)
        other_fighter.vie = other_fighter.vie - self.damage

class Tomate(Fighters):
    def __init__(self):
        super().__init__(10, 1, 4, 6)

class Broccoli(Fighters):
    def __init__(self):
        super().__init__(10, 2, 1, 4)
        self.vie_moitie = self.vie_max/2
        if self.vie < self.vie_moitie:
            self.damage = self.damage * 2

class Carotte(Fighters):
    def __init__(self):
        super().__init__(8, 1, 3, 5)
        if self.damage == 5 and self.vie < self.vie_max:
            self.vie = self.vie + 1

class Ring:
    def __init__(self, veg_1, veg_2):
        self.veg_1 = veg_1
        self.veg_2 = veg_2 
    def change_vegetables(self, veg_1, veg_2):
        self.veg_1 = veg_1
        self.veg_2 = veg_2
    def fight_round(self):
        self.veg_1.attack(self.veg_2)
        if self.veg_2.vie <= 0:
            return self.veg_1
        self.veg_2.attack(self.veg_1)
        if self.veg_1.vie <= 0:
            return self.veg_2
        return None