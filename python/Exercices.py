#EXERCICES

#Exo1#Exo2
a=3
print(str(a))
b=3
print(str(a+b))

#Exo3#Exo4
name = "Brutor"
print("II le retour de "+name)
number=10
print(str(number)+" "+name)

#Exo5#Exo6#Exo7
keyboard = input("Saisissez un mot: ")
print(keyboard)
print("Saisie clavier: "+keyboard)
other_keyboard = input("Saisissez un autre mot: ")
print(keyboard+ " "+other_keyboard)

#Exo8#Exo9#Exo10
number = input("Saisissez un nombre: ")
print(number)
if int(number) > 10 :
    print("Ce nombre est plus grand que 10.")
else:
    print("Ce nombre est plus petit ou égal à dix.")

#Exo11
variable1 = int(input("Saisissez un nombre: "))
if variable1<4 and variable1>3:
    print("Boum")
else:
    print("Rien ne se passe.")
    
#Exo12
from random import randint
variable2 = randint(1,6)
print(str(variable2))

#Exo13
variable3 = randint(1,10)
if variable3 > 9:
    print("Score maximum.")
elif variable3 > 5:
    print("Bon score.")
else:
    print("Score correct.")

#Exo14
pts_vie = 30
attaque = randint(5,10)
vie_totale = pts_vie - attaque #pts_vie-=attaque
print("Le monstre a encore "+str(vie_totale)+" points de vie.")

#Exo15
pts_vie = 30
attaque = randint(5,10)
vie_totale = pts_vie - (attaque*3)
print("Il reste "+str(vie_totale)+" points de vie au monstre.")

#Exo16
vie_totale = 30
attaque = randint(5,10)
while vie_totale > 0:
    vie_totale = vie_totale - attaque
    print("Le monstre a encore "+str(vie_totale)+" points de vie.")
print("Le monstre est mort.")

#Exo17
variable4 = [0,1,2,3,4,5] #list(range(6))
for i in variable4:
    print(str(i))

#Exo18
d10 = randint(0,10)
list_nombres = []
while d10 != 0:
    list_nombres.append(d10)
    d10 = randint(0,10)
for m in list_nombres:
    print(str(m))
print("Ca a pris "+str(len(list_nombres))+" essais.")

#Exo19
d10 = randint(0,10)
list_nombres = []
old_d10 = None
while d10 not in old_d10:
    list_nombres.append(d10)
    old_d10 = d10
    d10 = randint(0,10)
print("")
for m in list_nombres:
    print(str(m))
print("Ca a pris "+str(len(list_nombres))+" essais.")

#Exo20
from random import randint
mots = input("Saisi un mot: ")
mots_pris = []
while mots != "end":
    mots_pris.append(mots)
    mots = input("Saisi un autre mot: ")
print(mots_pris[::-1]) #for w in mots_pris[len(mots_pris)-1::-1]  print(w)
#for index in range(len(mots_pris)-1,-1,-1):    print(mots_pris[index])

#Exo21
entiers = int(input("Saisissez des nombres au choix: "))
entiers_liste = []
maximum = entiers
minimum = entiers
while entiers != 0:
    if entiers > maximum:
        maximum = entiers
    if number < minimum:
        minimum = entiers
    entiers = int(input("Saisissez un nombre: "))
print("Le nombre proposé le plus petit est "+str(minimum))
print("Le nombre proposé le plus grand est "+str(maximum))

#Exo22
user_non=[]
while len(user_non)<5: 
    user = int(input("Saisissez un nombre: "))
    if user > 10 or user < 1:
        user = int(input("Saisissez un nombre: "))
        print("Nombre non accepté.")
    else:
        user_non.append(user)
print(user_non)