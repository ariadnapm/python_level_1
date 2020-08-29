from random import randint
class Tomate:
    def __init__(self):
        self.vie = 10
        self.vie_max = 10
        self.defense = 1
    def attack(self, other_fighter):
        damage = randint(4, 6)
        damage = damage - other_fighter.defense
        damage = max(0, damage)
        other_fighter.vie = other_fighter.vie - damage

class Broccoli:
    def __init__(self):
        self.vie = 10
        self.vie_max = 10
        self.defense = 2
    def attack(self, other_fighter):
        damage = randint(1,4)
        self.vie_moitie = self.vie_max/2
        if self.vie < self.vie_moitie:
            damage = damage * 2
        damage = damage - other_fighter.defense
        damage = max(0, damage)
        other_fighter.vie = other_fighter.vie - damage

class Carotte:
    def __init__(self):
        self.vie = 8
        self.vie_max = 8
        self.defense = 1
    def attack(self, other_fighter):
        damage = randint(3, 5)
        if damage == 5 and self.vie < self.vie_max:
            self.vie = self.vie + 1
        damage = damage - other_fighter.defense
        damage = max(0, damage) 
        other_fighter.vie = other_fighter.vie - damage

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