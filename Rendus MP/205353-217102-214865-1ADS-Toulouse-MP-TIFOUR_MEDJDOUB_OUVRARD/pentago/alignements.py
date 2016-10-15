from bases import *
# fontion pour verifier si il y'a une allignements horizental de p elements
check = 0
def align_hor(n,plateau,p,j):
    check = 0
    for i in range (0,n):
        check = 0
        for k in range(0,n-1):
            if plateau[ i ][ k ] == j and plateau[ i ][ k + 1 ] == j:
                check = check + 1
            else:
                check = 0
            if check >= p-1:
                return True
    return False
# fontion pour verifier si il y'a une allignements vertical de p elements
def align_ver(n,plateau,p,j):
    check = 0
    for i in range (0,n):
        check = 0
        for k in range(0,n-1):
            if plateau[ k ][ i ] == j and plateau[ k+1 ][ i ] == j:
                check = check + 1
            else:
                check = 0
            if check >= p-1:
                return True
            elif k+2 == n:
                break
    return False
# fontion pour verifier si il y'a un allignement diagonal de bas gauche a haut droite de p elements
def align_diag1(n,plateau,p,j):
    check = 0
    for i in range(0,n):
        check = 0
        for k in range(0,i):
            if plateau[k][i-k] == j and plateau[k+1][i-k-1] == j:
                check += 1
            else:
                check = 0
            if check >= p-1:
                return True
            elif k+1 == i or i-k == 0:
                break
    check = 0
    for i in range(0,n):
        check = 0
        for k in range(n-1,i-1,-1):
            if plateau[k][i-(k+1)] == j and plateau[k-1][i+1-(k+1)] == j:
                check += 1
            else:
                check = 0
            if check >= p-1:
                return True
    else:
        return False
# fontion pour verifier si il y'a un allignement diagonal de haut gauche a bas droite de p elements
def align_diag2(n,plateau,p,j):
    check = 0
    for i in range(0,n-1):
        check = 0
        for k in range(0,n-1-i):
            if plateau[k+1][i+k+1] == j and plateau[k][i+k] == j:
                check+=1
            else:
                check=0
            if check >= p-1:
                return True
    check = 0
    for i in range(0,n-1):
        check = 0
        for k in range(n-1,i,-1):
            if plateau[k][k-i] == j and  plateau[k-1][k-i-1] == j:
                    check+=1
            else:
                check=0
            if check >= p-1:
                return True
    else:
        return False
#   fontion pour verifier si il y'a un alignenment quelconque de p elements
def check(n,plateau,p,j):
    if align_ver(n,plateau,p,j) or align_hor(n,plateau,p,j) or align_diag1(n,plateau,p,j) or align_diag2(n,plateau,p,j):
        check = 0
        return True
    else:
        check = 0
        return False

grille = [[0,0,0,0,0,2],
          [1,1,0,0,2,1],
          [0,1,0,0,0,0],
          [0,2,2,1,0,1],
          [0,2,0,2,0,0],
          [1,1,2,0,0,1]]
print(check(5,grille,4,2))
affichage(grille)

# coded by amir tifour, rachid medjoub and maxime ouvrard