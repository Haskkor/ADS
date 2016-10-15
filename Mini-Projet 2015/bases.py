""" Définition des listes et affichage. """

##########################
### 3.1 INITIALISATION ###
##########################

def create_list(n):
    """ Crée une liste à deux dimensions de n lignes et n colonnes dont
    toutes les valeurs valent 0. """
    return [[0] * n for i in range(n)]

def print_list(board):
    """ Affiche les valeurs d'une liste à deux dimensions. """
    for line in board:
        for elem in line:
            print(elem,end=' ')
        print("")

def is_full(board):
    """ Indique si il reste une case de libre ou non sur le plateau. """
    for line in board:
        for item in line:
            if item == 0:
                return False
    return True
