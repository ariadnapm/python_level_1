from fighters  import fighter1, fighter2
from random import randint, choice
attaque = ["Pied: ", "Poing: ", "Morsure: "]
while fighter1["Vie restante: "]>0 and fighter2["Vie restante: "]>0:
    #attaque fighter1
    attaque_choisie = choice(attaque)
    valeur_attaque = fighter1[attaque_choisie]
    damage = valeur_attaque - fighter2["Points de défense restants: "]
    if damage < 0: #damage = max(damage, 0)
        damage = 0
    fighter2["Vie restante: "] = fighter2["Vie restante: "] - damage
    print(fighter1["Nom: "]+" utilise "+attaque_choisie+": " +str(damage))

    #attaque fighter12
    attaque_choisie = choice(attaque)
    valeur_attaque = fighter2[attaque_choisie]
    damage = valeur_attaque - fighter1["Points de défense restants: "]
    if damage < 0: #damage = max(damage, 0)
        damage = 0
    fighter1["Vie restante: "] = fighter1["Vie restante: "] - damage
    print(fighter2["Nom: "]+" utilise "+attaque_choisie+": " +str(damage))

if fighter1["Vie restante: "]>0:
    print(fighter1["Nom: "]+" a gagné.")
elif fighter2["Vie restante: "]>0:
    print(fighter2["Nom: "]+" a gagné.")
else:
    print("Double K.O")