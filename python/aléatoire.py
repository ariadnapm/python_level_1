from random import randint
d10 = randint(1, 10)

number1 = int(input("Devinne à quel nombre entre 1 et 10 je pense: "))
if number1 == d10:
    print("Bravo.")
elif number1 > d10:
    print("Ce nombre est trop grand.")
    number2 = int(input("Devinne à quel nombre je pense: "))
    if number2 == d10:
        print("Bravo.")
    elif number2 > d10:
        print("Ce nombre est trop grand.")
        number3 = int(input("Devinne à quel nombre je pense: "))
        if number3 == d10:
            print("Bravo.")
        else:
            print("Perdu. Mon chiffre était " +str(d10)+".")
    else:
        print("Ce nombre est trop petit.")
        number3 = int(input("Devinne à quel nombre je pense: "))
        if number3 == d10:
            print("Bravo.")
        else:
            print("Perdu. Mon chiffre était " +str(d10)+".")
else:
    print("Ce nombre est trop petit.")
    number2 = int(input("Devinne à quel nombre je pense: "))
    if number2 == d10:
        print("Bravo.")
    elif number2 > d10:
        print("Ce nombre est trop grand.")
        number3 = int(input("Devinne à quel nombre je pense: "))
        if number3 == d10:
            print("Bravo.")
        else:
            print("Perdu. Mon chiffre était " +str(d10)+".")
    else:
        print("Ce nombre est trop petit.")
        number3 = int(input("Devinne à quel nombre je pense: "))
        if number3 == d10:
            print("Bravo.")
        else:
            print("Perdu. Mon chiffre était " +str(d10)+".")