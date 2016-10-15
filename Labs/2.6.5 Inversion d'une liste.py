import os

# ATTENTION : il y a ici, 2 solutions de proposées pour le même problème

def inverseliste(liste):
    for i in range(len(liste) // 2):
        liste[i], liste[-(i+1)] = liste[-(i+1)], liste[i]

def inverseliste2(liste):
    liste.reverse()

liste = [4,2,3,7,8]

inverseliste(liste)
print(liste)

os.system("pause")
