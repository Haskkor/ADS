import os

# ATTENTION : il y a ici, 2 solutions de proposées pour le même problème

def trouvoccu(elem,liste):
    for i in range(len(liste)):
        if liste[i] == elem:
            return i
    return -1

def trouvoccu2(elem,liste):
    if elem in liste:
        return liste.index(elem)
    else:
        return -1

liste = ["a","b","c","d","e","e","e","b","a"]
elem = input("Saisissez un element : ")

print(trouvoccu(elem,liste))

os.system("pause")
