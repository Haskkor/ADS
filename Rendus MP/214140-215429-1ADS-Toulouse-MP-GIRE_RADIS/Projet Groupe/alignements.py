win = 0


def VérifLignes(plateau):
    win = 0
    if plateau[0][0] == plateau[0][1] == plateau[0][2] == plateau[0][3] == plateau[0][4]:
        if plateau[0][0] == 1:
            win = 1
        elif plateau[0][0] == 2:
            win = 2
    elif plateau[0][1] == plateau[0][2] == plateau [0][3] == plateau[0][4] == plateau[0][5]:
        if plateau[0][1] == 1:
            win =1
        elif plateau[0][1] == 2:
            win =2
    elif plateau[1][0] == plateau[1][1] == plateau[1][2] == plateau[1][3] == plateau[1][4]:
        if plateau[1][0] == 1:
            win =1
        elif plateau[1][0] == 2:
            win = 2
    elif plateau[1][1] == plateau[1][2] == plateau [1][3] == plateau[1][4] == plateau[1][5]:
        if plateau[1][1] == 1:
            win = 1
        elif plateau[1][1] == 2:
            win = 2
    elif plateau[2][0] == plateau[2][1] == plateau [2][2] == plateau[2][3] == plateau[2][4]:
        if plateau[2][0] == 1:
            win = 1
        elif plateau[2][0] == 2:
            win = 2
    elif plateau[2][1] == plateau[2][2] == plateau [2][3] == plateau[2][4] == plateau[2][5]:
        if plateau[2][1] == 1:
            win = 1
        elif plateau[2][1] == 2:
            win = 2
    elif plateau[3][0] == plateau[3][1] == plateau [3][2] == plateau[3][3] == plateau[3][4] :
        if plateau[3][0] == 1:
            win =1
        elif plateau[3][0] == 2:
            win = 2
    elif plateau[3][1] == plateau[3][2] == plateau [3][3] == plateau[3][4] == plateau[3][5]:
        if plateau[0][0] == 1:
            win = 1
        elif plateau[0][0] == 2:
            win = 2
    elif plateau[4][0] == plateau[4][1] == plateau [4][2] == plateau[4][3] == plateau[4][4]:
        if plateau[0][0] == 1:
            win = 1
        elif plateau[0][0] == 2:
            win = 2
    elif plateau[4][1] == plateau[4][2] == plateau [4][3] == plateau[4][4] == plateau[4][5] :
        if plateau[0][0] == 1:
            win = 1
        elif plateau[0][0] == 2:
            win = 2
    elif plateau[5][0] == plateau[5][1] == plateau [5][2] == plateau[5][3] == plateau[5][4]:
        if plateau[0][0] == 1:
            win = 1
        elif plateau[0][0] == 2:
            win = 2
    elif plateau[5][1] == plateau[5][2] == plateau [5][3] == plateau[5][4] == plateau[5][5]:
        if plateau[0][0] == 1:
            win = 1
        elif plateau[0][0] == 2:
            win = 2
    return win



def VérifColonnes(plateau):
    win = 0
    if plateau[0][0] == plateau[1][0] == plateau[2][0] == plateau[3][0] == plateau[4][0]:
        if plateau[0][0] == 1:
            win =1
        elif plateau[0][0] == 2:
            win =2
    elif plateau[0][0] == plateau[2][0] == plateau[3][0] == plateau[4][0] == plateau[5][0]:
        if plateau[0][0] == 1:
            win =1
        elif plateau[0][0] == 2:
            win =2
    elif plateau[0][0] == plateau[1][1] == plateau[2][1] == plateau[3][1] == plateau[4][1]:
        if plateau[0][0] == 1:
            win =1
        elif plateau[0][0] == 2:
            win =2
    elif plateau[0][0] == plateau[2][1] == plateau[3][1] == plateau[4][1] == plateau[5][1]:
        if plateau[0][0] == 1:
            win =1
        elif plateau[0][0] == 2:
            win =2
    elif plateau[0][0] == plateau[1][2] == plateau[2][2] == plateau[3][2] == plateau[4][2]:
        if plateau[0][0] == 1:
            win =1
        elif plateau[0][0] == 2:
            win =2
    elif plateau[0][0] == plateau[2][2] == plateau[3][2] == plateau[4][2] == plateau[5][2]:
        if plateau[0][0] == 1:
            win =1
        elif plateau[0][0] == 2:
            win =2
    elif plateau[0][0] == plateau[1][3] == plateau[2][3] == plateau[3][3] == plateau[4][3]:
        if plateau[0][0] == 1:
            win =1
        elif plateau[0][0] == 2:
            win =2
    elif plateau[0][0] == plateau[2][3] == plateau[3][3] == plateau[4][3] == plateau[5][3]:
        if plateau[0][0] == 1:
            win =1
        elif plateau[0][0] == 2:
            win =2
    elif plateau[0][0] == plateau[1][4] == plateau[2][4] == plateau[3][4] == plateau[4][4]:
        if plateau[0][0] == 1:
            win =1
        elif plateau[0][0] == 2:
            win =2
    elif plateau[0][0] == plateau[2][4] == plateau[3][4] == plateau[4][4] == plateau[5][4]:
        if plateau[0][0] == 1:
            win =1
        elif plateau[0][0] == 2:
            win =2
    elif plateau[0][0] == plateau[1][5] == plateau[2][5] == plateau[3][5] == plateau[4][5]:
        if plateau[0][0] == 1:
            win =1
        elif plateau[0][0] == 2:
            win =2
    elif plateau[0][0] == plateau[2][5] == plateau[3][5] == plateau[4][5] == plateau[5][5]:
        if plateau[0][0] == 1:
            win =1
        elif plateau[0][0] == 2:
            win =2
    return win

def VérifDiagonales(plateau):
    win = 0
    if plateau[0][0] == plateau[1][1] == plateau[2][2] == plateau[3][3] == plateau[4][4]:
        if plateau[0][0] == 1:
            win = 1
        elif plateau[0][0] == 2:
            win =2
    if plateau[5][5] == plateau[1][1] == plateau[2][2] == plateau[3][3] == plateau[4][4] :
        if plateau[0][0] == 1:
            win =1
        elif plateau[0][0] == 2:
            win =2
    if plateau[1][0] == plateau[2][1] == plateau[3][2] == plateau[4][3] == plateau[5][4] :
        if plateau[0][0] == 1:
            win =1
        elif plateau[0][0] == 2:
            win =2
    if plateau[0][1] == plateau[1][2] == plateau[2][3] == plateau[3][4] == plateau[4][5] :
        if plateau[0][0] == 1:
            win =1
        elif plateau[0][0] == 2:
            win =2
    if plateau[0][5] == plateau[1][4] == plateau[2][3] == plateau[3][2] == plateau[4][1] :
        if plateau[0][0] == 1:
            win =1
        elif plateau[0][0] == 2:
            win =2
    if plateau[1][4] == plateau[2][3] == plateau[3][2] == plateau[4][1] == plateau[5][0] :
        if plateau[0][0] == 1:
            win =1
        elif plateau[0][0] == 2:
            win =2
    if plateau[0][4] == plateau[1][3] == plateau[2][2] == plateau[3][1] == plateau[4][0] :
        if plateau[0][0] == 1:
            win =1
        elif plateau[0][0] == 2:
            win =2
    if plateau[5][1] == plateau[4][3] == plateau[3][2] == plateau[2][1] == plateau[1][0] :
        if plateau[0][0] == 1:
            win =1
        elif plateau[0][0] == 2:
            win =2
    return win


def check (plateau):
    VérifDiagonales(plateau)
    VérifColonnes(plateau)
    VérifLignes(plateau)
    if win == 1:
        joueur1 = 1
    elif win == 2:
        joueur2 = 1
