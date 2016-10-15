import os

# ATTENTION : il y a ici, 2 solutions de proposées pour le même problème

def pluspetit(liste):
    temp = liste[0]
    for x in liste:
        if x < temp:
            temp = x
    return temp

def pluspetit2(liste):
    return min(liste)

liste = [5,62,7,9,356,2,165,48,6,651,3,1]

print(pluspetit(liste))

os.system("pause")
