s = [[0 for i in range(6)]for i in range(6)]
def hor(j):                                                         # j designera le pion donc '1' ou '2'
    if j == s[0][0] == s[0][1] == s[0][2] == s[0][3] == s[0][4]:    # fonction pour lignes horizontale
        print(True)
    elif j == s[0][1] == s[0][2] == s[0][3] == s[0][4] == s[0][5]:
        print(True)
    elif j == s[1][1] == s[1][2] == s[1][3] == s[1][4] == s[1][5]:
        print(True)
    elif j == s[1][0] == s[1][1] == s[1][2] == s[1][3] == s[1][4]:
        print(True)
    elif j == s[2][1] == s[2][2] == s[2][3] == s[2][4] == s[2][5]:
        print(True)
    elif j == s[2][0] == s[2][1] == s[2][2] == s[2][3] == s[2][4]:
        print(True)
    elif j == s[3][1] == s[3][2] == s[3][3] == s[3][4] == s[3][5]:
        print(True)
    elif j == s[3][0] == s[3][1] == s[3][2] == s[3][3] == s[3][4]:
        print(True)
    elif j == s[4][1] == s[4][2] == s[4][3] == s[4][4] == s[4][5]:
        print(True)
    elif j == s[4][0] == s[4][1] == s[4][2] == s[4][3] == s[4][4]:
        print(True)
    elif j == s[5][1] == s[5][2] == s[5][3] == s[5][4] == s[5][5]:
        print(True)
    elif j == s[5][0] == s[5][1] == s[5][2] == s[5][3] == s[5][4]:
        print(True)
    else:
        print()



def ver(j):
    if j == s[0][0] == s[1][0] == s[2][0] == s[3][0] == s[4][0]:    # fonction pour lignes verticales
        print(True)
    elif j == s[1][0] == s[2][0] == s[3][0] == s[4][0] == s[5][0]:
        print(True)
    elif j == s[1][1] == s[2][1] == s[3][1] == s[4][1] == s[5][1]:
        print(True)
    elif j == s[0][1] == s[1][1] == s[2][1] == s[3][1] == s[4][1]:
        print(True)
    elif j == s[1][2] == s[2][2] == s[3][2] == s[4][2] == s[5][2]:
        print(True)
    elif j == s[0][2] == s[1][2] == s[2][2] == s[3][2] == s[4][2]:
        print(True)
    elif j == s[1][3] == s[2][3] == s[3][3] == s[4][3] == s[5][3]:
        print(True)
    elif j == s[0][3] == s[1][3] == s[2][3] == s[3][3] == s[4][3]:
        print(True)
    elif j == s[1][4] == s[2][4] == s[3][4] == s[4][4] == s[5][4]:
        print(True)
    elif j == s[0][4] == s[1][4] == s[2][4] == s[3][4] == s[4][4]:
        print(True)
    elif j == s[1][5] == s[2][5] == s[3][5] == s[4][5] == s[5][5]:
        print(True)
    elif j == s[0][5] == s[1][5] == s[2][5] == s[3][5] == s[4][5]:
        print(True)
    else:
        print()




def diag1(j):           # diagonales bas/gauche à haut/droite
    if j == s[0][4] == s[1][3] == s[2][2] == s[3][1] == s[4][0]:
        print(True)
    elif j == s[0][5] == s[1][4] == s[2][3] == s[3][2] == s[4][1]:
        print(True)
    elif j == s[5][0] == s[4][1] == s[3][2] == s[2][3] == s[1][4]:
        print(True)
    elif j == s[5][1] == s[4][2] == s[3][3] == s[2][4] == s[1][5]:
        print(True)
    else:
        print()



def diag2(j):           # diagonales haut/gauche à bas/droite
    if j == s[0][0] == s[1][1] == s[2][2] == s[3][3] == s[4][4]:
        print(True)
    elif j == s[1][1] == s[2][2] == s[3][3] == s[4][4] == s[5][5]:
        print(True)
    elif j == s[0][1] == s[1][2] == s[2][3] == s[3][4] == s[4][5]:
        print(True)
    elif j == s[1][0] == s[2][1] == s[3][2] == s[4][3] == s[5][4]:
        print(True)
    else:
        print()



