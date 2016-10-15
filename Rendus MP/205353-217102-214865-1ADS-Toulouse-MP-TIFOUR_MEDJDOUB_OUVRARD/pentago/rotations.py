from bases import *
# fonction pour pivoter une matrice dans le sens horaire
def rotation1(m):
    couches = len (m) // 2
    taille = len (m) - 1
    for couche in range(couches):
        for i in range (couche, taille - couche):
            temp = m[couche][i]
            m[couche][i] = m[taille - i][couche]
            m[taille - i][couche] = m[taille - couche][taille - i]
            m[taille - couche][taille - i] = m[i][taille - couche]
            m[i][taille - couche] = temp
    return m
# fonction pour pivoter une matrice contre le sens horaire
def rotation2(m):
    couches = len (m) // 2
    taille = len (m) - 1
    for couche in range (couches):
        for i in range (couche, taille - couche):
            temp = m[couche][i]
            m[couche][i] = m[i][taille - couche]
            m[i][taille - couche] = m[taille - couche][taille - i]
            m[taille - couche][taille - i] = m[taille - i][couche]
            m[taille - i][couche] = temp
    return m
# fontion pour pivoter qu'un quandrant
def rotat(n,plateau,quad,sens):
    if quad == 1:
        list1 = []
        for i in range(0,n//2):
            list1.append(plateau[i][0:n//2])
        if sens == True:
            rotation1(list1)
        else:
            rotation2(list1)
        for i in range(0,n//2):
            plateau[i][0:n//2] = list1[i][0:n//2]
    if quad == 2:
        list2 = []
        for i in range(n//2,n):
            list2.append(plateau[i][0:n//2])
        if sens == True:
            rotation1(list2)
        else:
            rotation2(list2)
        for i in range(n//2,n):
            plateau[i][0:n//2] = list2[i-n//2][0:n//2]
    if quad == 3:
        list3 = []
        for i in range(n//2,n):
            list3.append(plateau[i][n//2:n])
        if sens == True:
            rotation1(list3)
        else:
            rotation2(list3)
        for i in range(n//2,n):
            plateau[i][n//2:n] = list3[i-n//2][0:n//2]
    if quad == 4:
        list4 = []
        for i in range(0,n//2):
            list4.append(plateau[i][n//2:n])
        if sens == True:
            rotation1(list4)
        else:
            rotation2(list4)
        for i in range(0,n//2):
            plateau[i][n//2:n] = list4[i][0:n//2]
grille = [[0,0,0,0,0,2],
          [1,1,0,0,2,1],
          [0,1,0,0,0,0],
          [0,2,2,1,0,1],
          [0,2,0,2,0,0],
          [1,1,2,0,0,1]]
affichage(grille)
print("----------------------")
rotat(len(grille),grille,3,True)
affichage(grille)
# coded by amir tifour, rachid medjoub and maxime ouvrard