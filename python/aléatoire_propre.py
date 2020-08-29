from random import randint
d10 = randint(1, 10)

number1 = int(input("Devinne à quel nombre entre 1 et 10 je pense: "))
if number1 == d10:
    print("Bravo.")
else:
    if number1 < d10:
        print("Le nom est trop petit.")
    else:
        print("Le nom est trop grand.")
    number2 = int(input("Essaye encore: "))
    if number2 == d10:
        print("Bravo")
    else:
        if number2 < d10:
            print("Le nombre est trop petit.")
        else:
            print("Le nombre est trop grand.")
        number3 = int(input("Essaye une dernière fois."))
        if number3 == d10:
            print("Bravo.")
        else:
            print("Raté. Mon nombre était "+str(d10)+".")