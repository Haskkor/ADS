#! /usr/bin/env python
# -*- coding:utf8-*-

from random import randint
"""S'occupe de l'affichage du plateau"""
"""Cette fonction est en relation avec la fonction initplateau"""
def affichplateau(liste):
    for i in liste:
        ligne = ""
        for j in i:
            if j == 0:
                ligne += "0 "
            elif j == 1:
                ligne += "1 "
            elif j == 2:
                ligne += "2 "
        print(ligne)
""""Génnère un plateau de N ligne et N colonne"""
def initPlateau(n):

    liste = [[randint(0,1)for j in range(n)]  for i in range(n)]
    return liste



