####################################################

#Fonction pour construire le tableau.

####################################################

import pygame
import random, sys, pygame, time, copy


def tableau(n):
    return [[0]*n for i in range(n)]



table = tableau(6)

##table[3][3]= 1
##print (table) 
####table[0][1]= 2
##table[1][0]= 3
#table[0][0]= 1
##
##for i in range(2):
##    for j in range (2):
##        print (table[i][j]) 




#*********************************************************************

#Fonction pour afficher le tabeau, et supprimer les ponctuations inutiles.

#*********************************************************************

def dessin (plateau):

    for ligne in plateau:

        line = ""

        for elem in ligne:

            if elem == 0:

                line += "0 "

            elif elem == 1:

                line += "1 "

            elif elem == 2:

                line += "2 "

        print(line)

dessin(table)


