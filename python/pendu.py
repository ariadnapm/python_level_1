from random import randint
mots = ["chat", "chien", "poisson", "cheval", "canard", "lézard"]
mot = mots[randint(0, len(mots)-1)]

cache = "-"*len(mot)
essais_joueur = []

print("Mot à trouver: "+ cache)

while mot != cache:
    lettre = input("Propose une lettre: ")
    essais_joueur.append(lettre)
    cache=""
    for index in mot:
        if index in essais_joueur:
            cache = cache + index
        else:
            cache = cache + "-"
    print("Mot à trouver: " + cache)