
######################
### LE JEU DE PING ###
######################

# 1. Demande à l'utilisateur de fournir un nombre de lignes et un nombre de
# colonnes pour le plateau de jeu

def tailleplateau():
    lignes = 0
    colonnes = 0
    while lignes <= 0 and colonnes <=0:
        lignes = eval(input("Saisir un nombre de lignes : "))
        colonnes = eval(input("Saisir un nombre de colonnes : "))
    return lignes, colonnes

# 2. Crée un plateau de jeu de x lignes et de y colonnes

def creerplateau(lignes, colonnes):
    return [[True] * colonnes for i in range(lignes)]

# 3. Affiche le plateau de jeu

def afficheplateau(plateau):
    for ligne in plateau:
        for colonne in ligne:
            if colonne:
                print("O", end=" ")
            else:
                print("X", end=" ")
        print("")

# 4. Demande à l'utilisateur de sélectionner une case sur le plateau

def jouercase(lignes, colonnes):
    xcase = 0
    ycase = 0
    while (xcase < 1 or xcase > colonnes) or (ycase < 1 or ycase > colonnes):
        ycase = eval(input("Saisir un numéro de lignes : "))
        xcase = eval(input("Saisir un numéro de colonnes : "))
    return xcase - 1, ycase - 1

# 5. Retourne les cases avoisinantes à la case passée en paramètre

def retournercases(ligne, colonne, plateau):
    for i in range(ligne-1, ligne+2):
        for j in range(colonne-1, colonne+2):
            if i == ligne and j == colonne:
                continue
            elif i < 0 or i > len(plateau) - 1 or j < 0 or j > len(plateau[i]) - 1:
                continue
            else:
                plateau[i][j] = not plateau[i][j]

# 6. Controle si la partie est terminée (toutes les cases valent False)

def partiegagnee(plateau):
    for ligne in plateau:
        for colonne in ligne:
            if colonne:
                return False
    print("Félicitations !")
    return True

# 7. Indique si l'utilisateur veut continuer à jouer ou non

def continuerpartie():
    continuer = eval(input("Saisir 0 pour arrêter et 1 pour continuer : "))
    while continuer < 0 or continuer > 1:
        continuer = eval(input("Saisir 0 pour arrêter et 1 pour continuer : "))
    if continuer == 0:
        print("")
        print("Vous êtes trop impatient...")
        return False
    else:
        print("")
        return True

# 8. Procédure principale exécutant le jeu

def jeudeping():
    lignes, colonnes = tailleplateau()
    plateau = creerplateau(lignes,colonnes)
    continuer = True
    print("")
    afficheplateau(plateau)
    print("")
    gagne = partiegagnee(plateau)
    while not gagne:
        colonne, ligne = jouercase(lignes,colonnes)
        retournercases(ligne, colonne, plateau)
        print("")
        afficheplateau(plateau)
        print("")
        gagne = partiegagnee(plateau)
        if not gagne:
            continuerpartie()

###########################
### LE JEU DE SOLITAIRE ###
###########################

# 1. Crée une liste à 2 dimensions dont tous les éléments sont à False comportant n lignes et
# m colonnes

def creerplato(lignes, colonnes):
    return [[False] * colonnes for i in range(lignes)]

# 2. Place des étoiles sur le plateau sur les coordonnées fournies par le joueur

def placeretoiles(plateau):
    nbretoiles = eval(input("Saisissez un nombre d'étoiles : "))
    while nbretoiles < 1:
        nbretoiles = eval(input("Saisissez un nombre d'étoiles : "))
    print("")
    for i in range(nbretoiles):
        print("Coordonnées de l'étoile ", i + 1)
        print("")
        line = eval(input("Saisissez un numéro de ligne : ")) - 1
        col = eval(input("Saisissez un numéro de colonne : ")) - 1
        while line < 0 or col <0 or line > len(plateau) - 1 or col > len(plateau[0]) - 1 or plateau[line][col] :
            line = eval(input("Saisissez un numéro de ligne : ")) - 1
            col = eval(input("Saisissez un numéro de colonne : ")) - 1
        plateau[line][col] = True
        print("")

# 3. Affiche le plateau de jeu

def afficheplateau(plateau):
    for ligne in plateau:
        for colonne in ligne:
            if colonne:
                print("*", end=" ")
            else:
                print(".", end=" ")
        print("")

# 4. Controle si la partie est terminée (toutes les cases valent False)

def partiegagne(plateau):
    for indligne in range(len(plateau)):
        for indcol in range(len(plateau[indligne])):
            compteur = 0
            for i in range(indligne-1, indligne+2):
                for j in range(indcol-1, indcol+2):
                    if i == indligne and j == indcol:
                        continue
                    elif i < 0 or i > len(plateau) - 1 or j < 0 or j > len(plateau[i]) - 1:
                        continue
                    else:
                        if plateau[i][j]:
                            compteur += 1
            if compteur % 2 == 0:
                print("Dommage ...")
                return False
    print("Félicitations !")
    return True

# 5. Procédure principale exécutant le jeu

def jeudesolitaire():
    lignes = 0
    colonnes = 0
    while lignes <= 0 and colonnes <=0:
        lignes = eval(input("Saisir un nombre de lignes : "))
        colonnes = eval(input("Saisir un nombre de colonnes : "))
    print("")
    plateau = creerplato(lignes,colonnes)
    afficheplateau(plateau)
    print("")
    placeretoiles(plateau)
    print("")
    afficheplateau(plateau)
    print("")
    partiegagne(plateau)

##########################
### EXECUTION DES JEUX ###
##########################

choix = eval(input("Choisissez un jeu. 1 - Jeu de Ping, 2 - Jeu Solitaire : "))
while choix < 1 or choix > 2:
    choix = eval(input("Choisissez un jeu. 1 - Jeu de Ping, 2 - Jeu Solitaire : "))
if choix == 1:
    jeudeping()
else:
    jeudesolitaire()
