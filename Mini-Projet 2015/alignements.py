""" Vérification de l'alignement potentiel de pions sur le plateau de jeu. """

################################
### 3.3 TEST D'UN ALIGNEMENT ###
################################

def line_align(n,board,p,j):
    """ Fonction prenant en paramètre un entier n, une liste à deux dimensions
    de n lignes et n colonnes, un entier p et un entier j. Cette fonction
    retournera True si dans au moins une des lignes est présent un alignement
    de p valeurs consécutives égales à j. """
    occu = 0
    for line in board:
        for elem in line:
            if elem == j:
                occu += 1
            else:
                occu = 0
            if occu == p:
                return True
        occu = 0
    return False

def column_align(n,board,p,j):
    """ Fonction prenant en paramètre un entier n, une liste à deux dimensions
    de n lignes et n colonnes, un entier p et un entier j. Cette fonction
    retournera True si dans au moins une des colonnes est présent un alignement
    de p valeurs consécutives égales à j. """
    occu = 0
    for x in range(n-1):
        for y in range(n-1):
            if board[y][x] == j:
                occu += 1
            else:
                occu = 0
            if occu == p:
                return True
        occu = 0
    return False

def diag_bottop_align(n,board,p,j):
    """ Contrôle l'alignement potentiel de pions sur la diagonale allant du
    bas à gauce vers le haut à droite. """
    occu = 0
    for x in range(n):
        for y in range(n):
            if x + y == n - 1:
                if board[x][y] == j:
                    occu += 1
                else:
                    occu = 0
            if occu == p:
                return True
    return False
    
    
def diag_topbot_align(n,board,p,j):
    """ Contrôle l'alignement potentiel de pions sur la diagonale allant du
    haut à gauce vers le bas à droite. """
    occu = 0
    for x in range(n):
        for y in range(n):
            if x == y:
                if board[x][y] == j:
                    occu += 1
                else:
                    occu = 0
            if occu == p:
                return True
    return False

def is_align(n,board,p,j):
    """ Fonction prenant en paramètre un entier n, une liste à deux dimensions de
    n lignes et n colonnes, un entier p et un entier j. Cette fonction
    retournera True si dans au moins une des quatre directions est présent un
    alignement de p valeurs consécutives égales à j. """
    if line_align(n,board,p,j) or column_align(n,board,p,j) or \
       diag_bottop_align(n,board,p,j) or diag_topbot_align(n,board,p,j):
        return True
    else:
        return False
    




