#! /usr/bin/env python
# -*- coding:utf8-*-


def alignementLigne(n, listes, p, j):
    cpt = 0
    for liste in listes:
        cpt = 0
        for elem in liste:
            if elem == j:
                cpt += 1
            else :
                cpt = 0
            if cpt == p:
                return True
        
def alignementColonne(n, listes, p, j):            
    """alignmentVerticale"""
    cpt = 0
    numColum = 0
    while numColum < n:
        cpt = 0
        for liste in listes:
            if liste[numColum] == j:
                cpt += 1
            else :
                cpt = 0
            if cpt == p:
                return True

        numColum += 1
        
def aligneBasGaucheVersHautDroit(n, listes, p, j):    
    """alignementDiagonaleBgVbD"""
    z = 5
    a = 0
    cpt = 0
            
    while z != -1:
        if listes[z][a] == j:
            cpt += 1
            if cpt == p:
               return True
            
        else:
            cpt = 0
            
        z -= 1
        a += 1
 
def pouriture(n, listes, p, j):
    
    """alignementDiagonaleHgVbD"""
    a = 0
    z = 0
    cpt = 0
    while a != 6:
        if listes[z][a] == j:
            cpt += 1
            if cpt == p:
                return True
            
        else:
            cpt = 0
            
        z += 1
        a += 1

def ensemble(n, listes, p, j):
        if alignementLigne(n, listes, p, j) == True:
            print("Gagné")
        if alignementColonne(n, listes, p, j) == True:
            print("Gagnee")
        if aligneBasGaucheVersHautDroit(n, listes, p, j) == True:
            print("Gagnéee")
        if pouriture(n, listes, p, j) == True:
            print("Gagnéeee")
    
listes = [[1,1,1,0,0,1],
          [1,1,1,0,0,1],
          [0,0,1,0,0,1],
          [0,0,1,1,0,0],
          [0,1,0,0,0,0],
          [1,0,0,0,0,0]]

"""alignementColonne(6, listes, 3, 1)"""


    
