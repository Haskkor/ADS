import os
import random

def quigagne(joueur):
    if joueur:
        print("JOUEUR VAINQUEUR !!!")
    else:
        print("ORDINATEUR VAINQUEUR !!!")

def jouejoueur():
    nbrallum = 0
    while nbrallum < 1 or nbrallum > 3:
        nbrallum = eval(input("Combien prenez-vous d'allumettes ? : "))
    return nbrallum

def joueordi():
    nbrallum = random.randint(1,3)
    print("L'ordinateur a pris " + str(nbrallum) + " allumette(s).")
    return nbrallum

def dessineallum(nbr):
    print("Il reste " + str(nbr) + " allumette(s) : ")
    dessin = ""
    for i in range(nbr):
        dessin += "| "
    print(dessin)

def quicommence():
    commence = 0
    while commence != 1 and commence != 2:
        commence = eval(input("Voulez vous commencer (1) ou que l'ordinateur commence (2) : "))
    if commence == 1:
        return True
    else:
        return False
    
def jeuallum(nbr):
    joueur = quicommence()
    while nbr > 0:
        dessineallum(nbr)
        if joueur:
            nbr = nbr - jouejoueur()
        else:
            nbr = nbr - joueordi()
        joueur = not joueur
    quigagne(joueur)

nbr = 0

while nbr < 1 or nbr % 2 == 0:
    nbr = eval(input("Saisissez un nombre impair d'allumettes : "))

jeuallum(nbr)

os.system("pause")
