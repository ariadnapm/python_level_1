from random import randint
def dice_simulation(): 
    dice = randint(1, 6) 
    return dice
result = dice_simulation() 
print("Résultat du dé: " + str(result))

def weird_function():
    result = randint(1,6)    
    return result 
    print("Texte qui ne sera jamais afficher.") 