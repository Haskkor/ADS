import os

def partiewin(joueur,liste):
    for i in liste:
        if i[0] == joueur and i[1] == joueur and i[2] == joueur:
            return True
    for i in range(len(liste)):
        if liste[0][i] == joueur and liste[1][i] == joueur and liste[2][i] == joueur:
            return True
    if liste[0][0] == joueur and liste[1][1] == joueur and liste[2][2] == joueur:
        return True
    if liste[0][2] == joueur and liste[1][1] == joueur and liste[2][0] == joueur:
        return True
    return False

def jouercase(joueur,liste):
    ligne = eval(input("Saisissez un numero de ligne (1-3) : ")) - 1
    colonne = eval(input("Saisissez un numero de colonne (1-3) : ")) - 1
    while liste[ligne][colonne] != 0:
        ligne = eval(input("Saisissez un numero de ligne (1-3) : ")) - 1
        colonne = eval(input("Saisissez un numero de colonne (1-3) : ")) - 1
    liste[ligne][colonne] = joueur

def casevide(liste):
    for i in liste:
        for j in i:
            if j == 0:
                return True
    return False

def affichplateau(liste):
    for i in liste:
        ligne = ""
        for j in i:
            if j == 0:
                ligne += ". "
            elif j == 1:
                ligne += "x "
            elif j == 2:
                ligne += "o "
        print(ligne)

plateau = [[0] * 3 for i in range(3)]
joueur = 1
affichplateau(plateau)
print("Tour du joueur 1.")
while casevide(plateau):
    jouercase(joueur,plateau)
    affichplateau(plateau)
    if partiewin(joueur,plateau):
        break
    if joueur == 1:
        joueur = 2
        print("Tour du joueur 2.")
    else:
        joueur = 1
        print("Tour du joueur 1.")
if partiewin(joueur,plateau):
    print("Le joueur " + str(joueur) + " a gagne !")
    affichplateau(plateau)
else:
    print("Match nul !")
    affichplateau(plateau)
    
os.system("pause")
