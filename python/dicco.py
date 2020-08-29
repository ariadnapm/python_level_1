name = input("Donne un nom à ton personnage: ")
#power = int(input("Quel est le niveau de pouvoir de ton héros? "))
regles = {"name": name, "puissance" : 10, "magie" : 5, "défense" : 3}
#premis = {name: power}
for key, value in regles.items():
    print(key + ":" + str(value))
for v in regles.values():
    print(v)
