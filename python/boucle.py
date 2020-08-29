from random import randint
d10 = randint(1, 10)
number1 = int(input("Devinne à quel nombre entre 1 et 10 je pense: "))
essai = 1
chance = 7
while number1 != d10 and essai < 7:
    print("Raté.")
    if number1 > d10:
        print("Trop grand.")
    else:
        print("Trop petit.")
    essai = essai + 1
    chance = chance - 1
    print("Il te reste " +str(chance)+ " essais.")
    number1 = int(input("Devinne à quel nombre entre 1 et 10 je pense: "))
print("Bravo! C'était bien " +str(d10)+".")
print("Ca t'as pris " +str(essai)+ " essai(s).")