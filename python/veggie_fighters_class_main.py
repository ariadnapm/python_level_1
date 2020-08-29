from veggie_fighters_class import Carotte, Tomate, Broccoli, Ring

tomato = Tomate()
carotte = Carotte()
broccoli = Broccoli()

matchs = [
    (tomato, carotte), (carotte, tomato),
    (broccoli, carotte), (carotte, broccoli),
    (broccoli, tomato), (tomato, broccoli)
]

score= {tomato : 0, carotte : 0, broccoli : 0}

for veg_1, veg_2 in matchs:
    veg_1.vie = veg_1.vie_max
    veg_2.vie = veg_2.vie_max
    
    ring = Ring(veg_1, veg_2)
    winner = ring.fight_round()
    while winner is None:
        winner = ring.fight_round()

    score[winner] = score[winner] + 1

print("La tomate a "+str(score[tomato])+" points. La carotte a "+str(score[carotte])+" points. Le broccoli a "+str(score[broccoli])+" points.")