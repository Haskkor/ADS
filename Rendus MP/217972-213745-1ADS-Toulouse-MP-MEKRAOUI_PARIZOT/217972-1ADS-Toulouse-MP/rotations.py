from bases import *


def rotationDroite(m,liste):
    newliste = getListe(m)
    for i in range(m):
        for j in range(m):
            newliste[j][m-i-1]= liste[i][j]
    return newliste

def rotationGauche(m,liste):
    newliste = getListe(m)
    
    for i in range(m):
        for j in range(m):
            newliste[m-j-1][i]= liste[i][j]
    return newliste

def getQuad(m,plateau,quad):
    liste =[]
    if quad == 1:
        for i in range(m//2):
            liste.append([])
            for j in range(m//2):
                liste[i].append(plateau[i][j])
    if quad == 2:
        for i in range(m//2):
            liste.append([])
            for j in range(m//2):
                liste[i].append(plateau[i+m//2][j])
    if quad == 3:
        for i in range(m//2):
            liste.append([])
            for j in range(m//2):
                liste[i].append(plateau[i][j+m//2])
    if quad == 4:
        for i in range(m//2):
            liste.append([])
            for j in range(m//2):
                liste[i].append(plateau[i+m//2][j+m//2])
    return liste

def rotationQuad(plateau,m,quad,sens):
    liste = getQuad(m,plateau,quad)
    if sens == True:
        liste = rotationGauche(m//2,liste)
    if sens == False:
        liste = rotationDroite(m//2,liste)
    if quad == 1:
        for i in range(m//2):
            for j in range(m//2):
                plateau[i][j] = liste[i][j]
    if quad == 2:
        for i in range(m//2):
            for j in range(m//2):
                plateau[i+m//2][j] = liste[i][j]
    if quad == 3:
        for i in range(m//2):
            for j in range(m//2):
                plateau[i][j+m//2] = liste[i][j]
    if quad == 4:
        for i in range(m//2):
            for j in range(m//2):
                plateau[i+m//2][j+m//2] = liste[i][j]
    return plateau



    
