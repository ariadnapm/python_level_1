#abbreviations
a = a + 1
a+ = 1

a = a - 1
a- = 1

a = a*3
a* = 3

a = a/4
a/ = 4

#division entière: sans virgule
5//2 = 2

#modulo: reste d'une division entière
5%2 = 1

#les fstring
name = "Thomas"
age = 38
print("Je m'appelle "+name+" et j'ai "+str(age)+" ans.")
print(f"Je m'appelle {name} et j'ai {age} ans.")

#ordonner

def bebble_sort(list_to_sort)
    ok = False
    while (ok==False):
        ok==True
    for index in range(0, len(list_to sort)-1):
        x = list_to_sort[index]
        y = list_to_sort[index + 1]

        if x > y:
            x, y = y, x
        list_to_sort[index] = x
        list_to_sort[index + 1] = y
        return list_to_stop
print(bubble_sort([4,6,82,22,75,17]))