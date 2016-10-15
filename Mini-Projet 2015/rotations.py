""" Rotations de listes à deux dimentions. """

##############################
### ROTATION D'UN QUADRANT ###
##############################

import bases

def rotate_clockwise(m,board):
    """ Réalise la rotation de 90 degrés dans le sens des aiguilles d'une
    montre d'une liste de m lignes et m colonnes. """
    temp_list = bases.create_list(m)
    for i in range(len(board)):
        for j in range(len(board[i])):
            temp_list[j][m-(i+1)] = board[i][j]
    return temp_list

def rotate_counterclockwise(m,board):
    """ Réalise la rotation de 90 degrés dans le sens contraire des aiguilles
    d'une montre d'une liste de m lignes et m colonnes. """
    temp_list = bases.create_list(m)
    for i in range(len(board)):
        for j in range(len(board[i])):
            temp_list[m-(j+1)][i] = board[i][j]
    return temp_list

def quadrant_rotate(n,board,num,rotate_cw):
    """ Réalise le tableau complet après avoir demandé une rotation de 90 degrés
    selon le sens passé en paramètre du quadrant passé lui aussi en paramètre. """
    if num == 1:
        return redo_board(board,0,n//2,0,n//2, \
                          find_rotation_direction(n,board,0,n//2,0,n//2,rotate_cw))
    elif num == 2:
        return redo_board(board,0,n//2,n//2,n, \
                           find_rotation_direction(n,board,0,n//2,n//2,n,rotate_cw))
    elif num == 3:
        return redo_board(board,n//2,n,0,n//2, \
                           find_rotation_direction(n,board,n//2,n,0,n//2,rotate_cw))
    elif num == 4:
        return redo_board(board,n//2,n,n//2,n, \
                           find_rotation_direction(n,board,n//2,n,n//2,n,rotate_cw))

def find_rotation_direction(n,board,x_start,x_end,y_start,y_end,rotate_cw):
    """ Renvoie le quadrant spécifié après avoir effectué la rotation indiquée. """
    if rotate_cw:
        return rotate_clockwise(n//2,find_quadrant(x_start,x_end,y_start,y_end,board,n//2))
    else:
        return rotate_counterclockwise(n//2,find_quadrant(x_start,x_end,y_start,y_end, \
                                                          board,n//2))

def redo_board(board,x_start,x_end,y_start,y_end,quad_rotate):
    """ Reconstitue le tableau complet en concaténant le plateau avec le quadrant
    après rotation. """
    x,y = 0,0
    for i in range(x_start,x_end):
        for j in range(y_start,y_end):
            board[i][j] = quad_rotate[x][y]
            y += 1
        x += 1
        y = 0
    return board

def find_quadrant(x_start,x_end,y_start,y_end,board,n):
    """ Renvoie le quadrant recherché dans la liste globale en se basant
    sur le numéro de la première et de la dernière ligne ainsi que le
    numéro de la première et de la dernière colonne. """
    temp_board = bases.create_list(n)
    x,y = 0,0
    for i in range(x_start,x_end):
        for j in range(y_start,y_end):
            temp_board[x][y] = board[i][j]
            y += 1
        x += 1
        y = 0
    return temp_board
        
            
    
    
    
