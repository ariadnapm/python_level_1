from random import randint

def dices(number, faces=6, additionnal=0):
    print(str(number)+"d"+str(faces)+"+"+str(additionnal))
    result = 0
    for n in range(number):
        result = result + randint(1, faces)
    return result + additionnal

print(dices(2))
print(dices(3,4))
print(dices(1,8,3))