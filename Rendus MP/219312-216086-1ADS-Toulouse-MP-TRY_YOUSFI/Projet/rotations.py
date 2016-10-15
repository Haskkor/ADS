##############################################

#Fonction pour la rotation de la matrice.

##############################################

#/!\ #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#* /!\

from bases import *
import random, sys, pygame, time, copy
import pygame

Num = 3

def rotation_90(Num, tableau):

    resultat = [[0]*Num for _ in range(Num)]

    for x in range(Num):

        for y in range(Num):

            resultat[y][Num-1-x] = tableau[x][y]

    return resultat

print (rotation_90(3,table)) 

# Fontions pour la rotation



def rotation (carre, direction,quadrant):

    n = len(carre)


#CARRE 1

    if quadrant == 1:

        l1 = []

        for i in range (0,n//2):
            l1.append(carre[i][0:n//2])

#Changement de direction

        if direction == True:
            dessin(rotation_90(Num, l1))

        else:
            dessin(rotation_90(Num, rotation_90(Num, rotation_90(Num, l1))))

#Re-insertion de la liste dans la matrice après rotation.

        for i in range (0,n//2):

            carre[i][0:n//2] = l1[0:n//2]


#CARRE 2

    if quadrant == 2:
        l2 = []

        for i in range (n//2,n):
            l2.append(carre[i][0:n//2])

        if direction == True:
            dessin(rotation_90(Num, l2))

        else:
            dessin(rotation_90(Num, rotation_90(Num, rotation_90(Num, l2))))

        for i in range (0,n//2):

            carre[i][0:n//2] = l2[0:n//2]

#/!\ #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#* /!\

#CARRE 3


    if quadrant == 3:
        l3 = []

        for i in range (n//2,n):
            l3.append(carre[i][n//2:n])

        if direction == True:
            dessin(rotation_90(Num, l3))

        else:
            dessin(rotation_90(Num, rotation_90(Num, rotation_90(Num, l3))))

        for i in range (0,n//2):

            carre[i][0:n//2] = l3[0:n//2]

#/!\ #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#* /!\


#CARRE 4

    if quadrant == 4:
        l4 = []

        for i in range (0,n//2):
            l4.append(carre[i][n//2:n])

        if direction == True:
            dessin(rotation_90(Num, l4))

        else:
            dessin(rotation_90(Num, rotation_90(Num, rotation_90(Num, l4))))

        for i in range (0,n//2):

            carre[i][0:n//2] = l4[0:n//2]


###*********************************************************************
##
##
### Affichage de test, pense à l'enlever
##
##
###*********************************************************************
##
##print("")
##print("****************************************************************")
##print("")
##print("Affichage d'un carré de test APRES rotation et APRES réinsertion")
##print("")
##print("****************************************************************")
##print("")
##
##rotation(table,True,4)
