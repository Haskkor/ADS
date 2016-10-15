##Variables

n=6  #Nombre de lignes et de colonnes du plateau
p=5  #Nombre de pions de la même couleur alignés déterminant la victoire

# plateau : tableau à deux dimensions de taille n
# o : valeur qui sera égale à 1 ou 2 (1 pion blanc, 2 pion noir)


#Test de l'alignement horizontal

def alignementHorizontal(plateau,o):
    alignement = False   #Par défaut alignement est égal à False, car rien n'est aligné à la base

    for i in range(n): #pour tester sur n'importe quelle ligne

        if plateau[i][0] == o and plateau[i][0] == plateau[i][1] and plateau[i][0] == plateau[i][2] and plateau[i][0] == plateau[i][3] and plateau[i][0] == plateau[i][4] :
        #on vérifie que c'est le bon pion choisi

            alignement = True

        elif plateau[i][1] == o and plateau[i][1] == plateau[i][2] and plateau[i][1] == plateau[i][3] and plateau[i][1] == plateau[i][4] and plateau[i][1] == plateau[i][5] :


            alignement = True

    #On fini par un return de "alignement" qui renverra False s'il n'y a pas d'alignement et True s'il y en a un

    return alignement


#Test alignement verticale

def alignementVertical(plateau,o):
    alignement = False    #Par défaut alignement est égal à False, car rien n'est aligné à la base

    for j in range(n): #pour tester sur n'importe quelle colonne

        if plateau[0][j]== o and plateau[0][j] == plateau[1][j] and plateau[0][j] == plateau[2][j] and plateau[0][j] == plateau[3][j] and plateau[0][j] == plateau[4][j] :

            alignement = True

        elif plateau[1][j] == o and plateau[1][j] == plateau[2][j] and plateau[1][j] == plateau[3][j] and plateau[1][j] == plateau[4][j] and plateau[1][j] == plateau[5][j] :

            alignement = True

    #On fini par un return de "alignement" qui renverra False s'il n'y a pas d'alignement et True s'il y en a un

    return alignement



def alignementDiagonale(plateau,o):
    alignement = False

    #Alignement haut gauche bas droite

    if plateau[0][0]== o and plateau[0][0] == plateau[1][1] and plateau[0][0] == plateau[2][2] and plateau[0][0] == plateau[3][3] and plateau[0][0] == plateau[4][4] :

        alignement = True

    elif plateau[1][1] == o and plateau[1][1] == plateau[2][2] and plateau[1][1] == plateau[3][3] and plateau[1][1] == plateau[4][4] and plateau[1][1] == plateau[5][5] :

        alignement = True


    #Alignment Haut droite bas gauche

    elif plateau[0][5] == o and plateau[0][5] == plateau[1][4] and plateau[0][5] == plateau[2][3] and plateau[0][5] == plateau[3][2] and plateau[0][5] == plateau[4][1] :

        alignement = True

    elif plateau[1][4] == o and plateau[1][4] == plateau[2][3] and plateau[1][4] == plateau[3][2] and plateau[1][4] == plateau[4][1] and plateau[1][4] == plateau[5][0] :

        alignement = True


    #Alignement des petites diagonales haut gauche bas droite

    elif plateau[0][1] == o and plateau[0][1] == plateau[1][2] and plateau[0][1] == plateau[2][3] and plateau[0][1] == plateau[3][4] and plateau[0][1] == plateau[4][5] :

        alignement=True

    elif plateau[1][0] == o and plateau[1][0] == plateau[2][1] and plateau[1][0] == plateau[3][2] and plateau[1][0] == plateau[4][3] and plateau[1][0] == plateau[5][4] :

        alignement=True


    #Alignement des petites diagonales haut droite bas gauche

    elif plateau[0][4] == o and plateau[0][4] == plateau[1][3] and plateau[0][4] == plateau[2][2] and plateau[0][4] == plateau[3][1] and plateau[0][4] == plateau[4][0] :

        alignement=True

    elif plateau[1][5] == o and plateau[1][5] == plateau[2][4] and plateau[1][5] == plateau[3][3] and plateau[1][5] == plateau[4][2] and plateau[1][5] == plateau[5][1] :

        alignement=True


    return alignement










