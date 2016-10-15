# la grille innitiale
grille = [ [ 0,0,0,0,0,0,0 ],
           [ 0,0,0,0,0,0,0 ],
           [ 0,0,0,0,0,0,0 ],
           [ 0,0,0,0,0,0,0 ],
           [ 0,0,0,0,0,0,0 ],
           [ 0,0,0,0,0,0,0 ] ]
colonne = 0
joueur = 0
for ligne in grille:
    line = "|"
    for element in ligne:
        if element == 0:
            line = line + " |"
        elif element == 1:
            line = line + "X|"
        elif element == -1:
            line = line + "O|"
    print ( line )
print ( " -" * 7 )
print ( " 1 2 3 4 5 6 7" )
#fonction qui verifie la colonne

def verif_colonne ( grille,colonne ):
    somme = 0
    for i in range ( 6 ):
        if grille[ i ][ colonne - 1 ] == 0:
            somme = somme + 1
    return somme


verif_colonne ( grille,5 )

#fonction qui verifie si la colonne est pleine
def verif_colonne_pleine ( grille,colonne ):
    somme = 0
    for i in range ( 6 ):
        if grille[ i ][ colonne - 1 ] == 0:
            somme = somme + 1
    if somme == 0:
        return True
    else:
        return False

#fonction de la pose du joueur
def pose ( grille ):
    colonne = int ( input ( "veuillez saisir un numero de colonne compis entre 1 et 7" ) )
    while colonne > 7 or colonne < 1 or verif_colonne_pleine ( grille,colonne ) == True:
        colonne = int ( input ( "veuillez saisir un numero de colonne compis entre 1 et 7" ) )
    grille[verif_colonne(grille,colonne )-1][colonne] = 1
    for ligne in grille:
        line = "|"
        for element in ligne:
                if element == 0:
                    line = line + " |"
                elif element == 1:
                    line = line + "X|"
                elif element == -1:
                    line = line + "O|"
        print ( line )
    print ( " -" * 7 )
    print ( " 1 2 3 4 5 6 7" )
#fonction de la pose de l'odinateur
pose ( grille )
import random


def pose_ordi ( grille ):
    colonne = random.randint ( 1,7 )
    while colonne == verif_colonne_pleine ( grille,colonne ) == True:
        colonne = random.randint ( 1,7 )
    return colonne

#fonction de la verification horizontal
def horizontal ( grille,colonne,joueur ):
    if joueur == 1:
        check = 0
        for i in range ( 0,6 ):
            if grille[ i ].count ( 1 ) >= 4:
                check = check + 1
            else:
                check = check
        if check == 1:
            return True
        else:
            return False
    elif joueur == -1:
        check = 0
        for i in range ( 0,6 ):
            if grille[ i ].count ( -1 ) >= 4:
                check = check + 1
            else:
                check = check
        if check == 1:
            return True
        else:
            return False
#fontion pour la verification verical

def vertical ( grille,colonne,joueur ):
    if joueur == 1:
        check = 0
        for i in range ( 0,6 ):
            if grille[ i ][ colonne ] == 1:
                check = check + 1
            else:
                check = check
        if check >= 4:
            return True
        else:
            return False
    elif joueur == -1:
        check = 0
        for i in range ( 0,6 ):
            if grille[ i ][ colonne ] == -1:
                check = check + 1
            else:
                check = check
        if check >= 4:
            return True
        else:
            return False

#fontion pour la premiere verification diagonal
def diagonal1 ( grille,colonne,joueur ):
    if joueur == 1:
        ligne = 0
        for colonne in range ( 3,7 ):
            check = 0
            for j in range ( 0,colonne ):
                if grille[ ligne + j ][ colonne - j ] == 1:
                    check = check + 1
            print ( check )
            if check >= 4:
                return True
        ligne = 5
        for colonne in range ( -7,-2,1 ):
            check = 0
            for j in range ( 0,int ( -colonne ) ):
                if grille[ ligne - j ][ colonne + j ] == 1:
                    check = check + 1
            if check >= 4:
                return True
            else:
                return False
    if joueur == -1:
        ligne = 0
        for colonne in range ( 3,7 ):
            check = 0
            for j in range ( 0,colonne ):
                if grille[ ligne + j ][ colonne - j ] == -1:
                    check = check + 1
            if check >= 4:
                return True
        ligne = 5
        for colonne in range ( -7,-2,1 ):
            check = 0
            for j in range ( 0,int ( -colonne ) ):
                if grille[ ligne - j ][ colonne + j ] == -1:
                    check = check + 1
            if check >= 4:
                return True
            else:
                return False

#fontion pour la deuxiemme verification diagonal
def diagonal2 ( grille,colonne,joueur ):
    if joueur == 1:
        ligne = 5
        for colonne in range ( 3,7 ):
            check = 0
            for j in range ( colonne ):
                if grille[ ligne - j ][ colonne - j ] == 1:
                    check = check + 1
            if check >= 4:
                return True
            else:
                return False
        ligne = 0
        for colonne in range ( -1,-7,-1 ):
            check = 0
            for j in range ( 0,-colonne ):
                if grille[ ligne + j ][ colonne + j ] == 1:
                    check = check + 1
            if check >= 4:
                return True
            else:
                return False
        if joueur == -1:
            ligne = 5
        for colonne in range ( 3,7 ):
            check = 0
            for j in range ( colonne ):
                if grille[ ligne - j ][ colonne - j ] == -1:
                    check = check + 1
            if check >= 4:
                return True
            else:
                return False
        ligne = 0
        for colonne in range ( -1,-7,-1 ):
            check = 0
            for j in range ( 0,-colonne ):
                if grille[ ligne + j ][ colonne + j ] == -1:
                    check = check + 1
            if check >= 4:
                return True
            else:
                return False
pose ( grille )