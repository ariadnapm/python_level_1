from random import randint

def bravo():
    print("Bravo!")

def ask_number():
    number = input("Devinne à quel nombre entre 1 et 10 je pense: ")
    number = int(number)
    while number>10 or number<1:
        print("Chiffre non-valide.")
        number = input("Devinne à quel nombre entre 1 et 10 je pense: ")
        number = int(number)
    return number

def bingo(number, d10):
    if number > d10:
        print("Trop grand.")
        return False
    if number < d10:
        print("Trop petit.")
        return False
    return True 

d10 = randint(1, 10)
number = ask_number

if number == d10:
    bravo()
else:
    number = ask_number()
    if number == d10:
        bravo()
    else:
        bingo(number, d10)
        number = ask_number()
        if number == d10:
            bravo()
        else:
            bingo(number, d10)
            number = ask_number()
            if number == d10:
                bravo()
            else:
                print("Raté. Mon nombre était "+str(d10)+".")