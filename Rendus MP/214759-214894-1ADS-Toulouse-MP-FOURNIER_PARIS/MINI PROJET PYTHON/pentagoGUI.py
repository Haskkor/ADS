#Initialisation et paramètre de la fenêtre de jeu

import pygame, sys
from pygame.locals import *
pygame.init()

maSurface = pygame.display.set_mode((1024,768))

FPS=30
fpsClock = pygame.time.Clock()

pygame.display.set_caption('Pentago')

#Mise en place de toutes les fonctions de bases

#################################################################################################################################################
#################################################################################################################################################
#################################################################################################################################################
#################################################################################################################################################

def baseplateau(n,plateau):
    #fonction de mise en place de la liste à deux dimensions
    plateau=[[0 for i in range (n)] for j in range (n)]
    return plateau

def afficheplateau(plateau):
    for ligne in plateau:
        ligne = map(str, ligne)
        print(' '.join(ligne))
    return plateau

#########################################################################

def alignementHorizontal(plateau,o):
    alignement = False   #Par défaut alignement est égal à False, car rien n'est aligné à la base

    for i in range(n): #pour tester sur n'importe quelle ligne

        if plateau[i][0] == o and plateau[i][0] == plateau[i][1] and plateau[i][0] == plateau[i][2] and plateau[i][0] == plateau[i][3] and plateau[i][0] == plateau[i][4] :
        #on vérifie que c'est le bon pion choisi

            alignement = True

        elif plateau[i][1] == o and plateau[i][1] == plateau[i][2] and plateau[i][1] == plateau[i][3] and plateau[i][1] == plateau[i][4] and plateau[i][1] == plateau[i][5] :


            alignement = True

    #On fini par un return de "alignement" qui renverra False s'il n'y a pas d'alignement et True s'il y en a un

    return alignement


#Test alignement verticale

def alignementVertical(plateau,o):
    alignement = False    #Par défaut alignement est égal à False, car rien n'est aligné à la base

    for j in range(n): #pour tester sur n'importe quelle colonne

        if plateau[0][j]== o and plateau[0][j] == plateau[1][j] and plateau[0][j] == plateau[2][j] and plateau[0][j] == plateau[3][j] and plateau[0][j] == plateau[4][j] :

            alignement = True

        elif plateau[1][j] == o and plateau[1][j] == plateau[2][j] and plateau[1][j] == plateau[3][j] and plateau[1][j] == plateau[4][j] and plateau[1][j] == plateau[5][j] :

            alignement = True

    #On fini par un return de "alignement" qui renverra False s'il n'y a pas d'alignement et True s'il y en a un

    return alignement



def alignementDiagonale(plateau,o):
    alignement = False

    #Alignement haut gauche bas droite

    if plateau[0][0]== o and plateau[0][0] == plateau[1][1] and plateau[0][0] == plateau[2][2] and plateau[0][0] == plateau[3][3] and plateau[0][0] == plateau[4][4] :

        alignement = True

    elif plateau[1][1] == o and plateau[1][1] == plateau[2][2] and plateau[1][1] == plateau[3][3] and plateau[1][1] == plateau[4][4] and plateau[1][1] == plateau[5][5] :

        alignement = True


    #Alignment Haut droite bas gauche

    elif plateau[0][5] == o and plateau[0][5] == plateau[1][4] and plateau[0][5] == plateau[2][3] and plateau[0][5] == plateau[3][2] and plateau[0][5] == plateau[4][1] :

        alignement = True

    elif plateau[1][4] == o and plateau[1][4] == plateau[2][3] and plateau[1][4] == plateau[3][2] and plateau[1][4] == plateau[4][1] and plateau[1][4] == plateau[5][0] :

        alignement = True


    #Alignement des petites diagonales haut gauche bas droite

    elif plateau[0][1] == o and plateau[0][1] == plateau[1][2] and plateau[0][1] == plateau[2][3] and plateau[0][1] == plateau[3][4] and plateau[0][1] == plateau[4][5] :

        alignement=True

    elif plateau[1][0] == o and plateau[1][0] == plateau[2][1] and plateau[1][0] == plateau[3][2] and plateau[1][0] == plateau[4][3] and plateau[1][0] == plateau[5][4] :

        alignement=True


    #Alignement des petites diagonales haut droite bas gauche

    elif plateau[0][4] == o and plateau[0][4] == plateau[1][3] and plateau[0][4] == plateau[2][2] and plateau[0][4] == plateau[3][1] and plateau[0][4] == plateau[4][0] :

        alignement=True

    elif plateau[1][5] == o and plateau[1][5] == plateau[2][4] and plateau[1][5] == plateau[3][3] and plateau[1][5] == plateau[4][2] and plateau[1][5] == plateau[5][1] :

        alignement=True


    return alignement

#########################################################################






#Fonction choisissant un quadrant (liste à 2D) depuis le plateau (liste à 2D) et l'amenant à choisir une rotation horaire ou antihoraire

#Le numéro des cadrants est disposé de telle sorte :

#####
#1#4#
#2#3#
#####



def rotationPlateau(plateau,n,q,v):

    if n%2==0:  #vérification de n pair

        #Quadrant 1

        if q==1:

            if v is True:
                for i in range(m):
                   for j in range(m):
                       quadrant[i][j] = plateau[i][j]
                for i in range(m):
                    for j in range(m):
                        tampon[i][j]=quadrant[m-j-1][i]
                for i in range(m):
                    for j in range(m):
                        plateau[i][j]=tampon[i][j]

            if v is False:
                for i in range(m):
                   for j in range(m):
                       quadrant[i][j] = plateau[i][j]
                for i in range(m):
                    for j in range(m):
                        tampon[i][j]=quadrant[j][m-i-1]
                for i in range(m):
                    for j in range(m):
                        plateau[i][j]=tampon[i][j]

        #Quadrant 2

        if q==2:

            if v is True:

                for i in range(m):
                   for j in range(m):
                       quadrant[i][j] = plateau[i+m][j]
                for i in range(m):
                    for j in range(m):
                        tampon[i][j]=quadrant[m-j-1][i]
                for i in range(m):
                    for j in range(m):
                        plateau[i+m][j]=tampon[i][j]

            if v is False:

                for i in range(m):
                   for j in range(m):
                       quadrant[i][j] = plateau[i+m][j]
                for i in range(m):
                    for j in range(m):
                        tampon[i][j]=quadrant[j][m-i-1]
                for i in range(m):
                    for j in range(m):
                        plateau[i+m][j]=tampon[i][j]

        #Quadrant 3

        if q==3:

            if v is True:
                for i in range(m):
                   for j in range(m):
                       quadrant[i][j] = plateau[i+m][j+m]
                for i in range(m):
                    for j in range(m):
                        tampon[i][j]=quadrant[m-j-1][i]
                for i in range(m):
                    for j in range(m):
                        plateau[i+m][j+m]=tampon[i][j]

            if v is False:
                for i in range(m):
                   for j in range(m):
                       quadrant[i][j] = plateau[i+m][j+m]
                for i in range(m):
                    for j in range(m):
                        tampon[i][j]=quadrant[j][m-i-1]
                for i in range(m):
                    for j in range(m):
                        plateau[i+m][j+m]=tampon[i][j]

        #Quadrant 4

        if q==4:

            if v is True:

                for i in range(m):
                   for j in range(m):
                       quadrant[i][j] = plateau[i][j+m]
                for i in range(m):
                    for j in range(m):
                        tampon[i][j]=quadrant[m-j-1][i]
                for i in range(m):
                    for j in range(m):
                        plateau[i][j+m]=tampon[i][j]

            if v is False:

                for i in range(m):
                   for j in range(m):
                       quadrant[i][j] = plateau[i][j+m]
                for i in range(m):
                    for j in range(m):
                        tampon[i][j]=quadrant[j][m-i-1]
                for i in range(m):
                    for j in range(m):
                        plateau[i][j+m]=tampon[i][j]


#################################################################################################################################################
#################################################################################################################################################
#################################################################################################################################################
#################################################################################################################################################

#on load toutes les images et on met en place le fond

fond=pygame.image.load("fond.png")
maSurface.blit(fond,(0,0))
#les fleches

fleche1=pygame.image.load("fleche1.png")
fleche2=pygame.image.load("fleche2.png")
fleche3=pygame.image.load("fleche3.png")
fleche4=pygame.image.load("fleche4.png")
fleche5=pygame.image.load("fleche5.png")
fleche6=pygame.image.load("fleche6.png")
fleche7=pygame.image.load("fleche7.png")
fleche8=pygame.image.load("fleche8.png")

#les points

pionblanc=pygame.image.load("pionblanc.png")
pionnoir=pygame.image.load("pionnoir.png")

#autres images

noirgagne=pygame.image.load("noirgagne.png")
blancgagne=pygame.image.load("blancgagne.png")
poseblanc=pygame.image.load("poseblanc.png")
posenoir=pygame.image.load("posenoir.png")
quittez=pygame.image.load("quittez.png")
rejouez=pygame.image.load("rejouez.png")
tournercadrant=pygame.image.load("tournercadrant.png")





#Variables
n=6
m=(int(n/2))
tampon=[[None for i in range(m)]for j in range(m)]
quadrant=[[None for i in range(m)]for j in range(m)]
plateau=[[0 for i in range (n)] for j in range (n)]
# o est la variable déterminant le pion, 0 pour vide, 1 pour blanc, 2 pour noir
#On va utiliser une variable b permettant de déterminer quel joueur joue.
#b est d'abord égal à 0, à chaque tour, b sera égal à b+1
#Quand b est paire, les blancs jouent, quand b est impair, les noirs jouent
b=0

#Fonction affichant les pions sur le plateau


def affichagePion(plateau):
    for i in range(3):
        for j in range(3):
            if plateau[i][j]==1:
                maSurface.blit(pionblanc,(140+j*78,163+i*78))
            elif plateau[i][j]==2:
                maSurface.blit(pionnoir,(140+j*78,163+i*78))

    for i in range(3,6):
        for j in range(3):

            if plateau[i][j]==1:
                maSurface.blit(pionblanc,(140+j*78,163+i*82))
            elif plateau[i][j]==2:
                maSurface.blit(pionnoir,(140+j*78,163+i*82))

    for i in range(3):
        for j in range(3,6):
            if plateau[i][j]==1:
                maSurface.blit(pionblanc,(140+j*82,163+i*78))
            elif plateau[i][j]==2:
                maSurface.blit(pionnoir,(140+j*82,163+i*78))

    for i in range(3,6):
        for j in range(3,6):
            if plateau[i][j]==1:
                maSurface.blit(pionblanc,(140+j*82,163+i*82))
            elif plateau[i][j]==2:
                maSurface.blit(pionnoir,(140+j*82,163+i*82))



def affichageImagePose(b):
    if b==1:
        maSurface.blit(poseblanc,(747,90))
    elif b==2:
        maSurface.blit(posenoir,(747,90))


#TEST#

plateau=[[0 for i in range(n)]for j in range(n)]
afficheplateau(plateau)
b=1

inProgress = True


while inProgress:
    rejouer = True
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            x, y=event.pos


        #Quadrant 1
            for i in range(3):
                for j in range(3):
                    if plateau[i][j]==0:
                        if (140+j*78)<x<(140+(j+1)*78) and (163+i*78)<y<(163+(i+1)*78):
                            if b==1:
                                plateau[i][j]=1

                            elif b==2:
                                plateau[i][j]=2


        #Quadrant 2
            for i in range(3,6):
                for j in range(3):
                    if plateau[i][j]==0:
                        if (140+j*78)<x<(140+(j+1)*78) and (163+i*82)<y<(163+(i+1)*82):
                            if b==1:
                                plateau[i][j]=1

                            elif b==2:
                                plateau[i][j]=2


        #Quadrant 3
            for i in range(3,6):
                for j in range(3,6):
                    if plateau[i][j]==0:
                        if  (140+j*82)<x<(140+(j+1)*82) and (163+i*82)<y<(163+(i+1)*82):
                            if b==1:
                                plateau[i][j]=1

                            elif b==2:
                                plateau[i][j]=2


        #Quadrant 4
            for i in range(3):
                for j in range(3,6):
                    if plateau[i][j]==0:
                        if  (140+j*82)<x<(140+(j+1)*82) and (163+i*78)<y<(163+(i+1)*78):
                            if b==1:
                                plateau[i][j]=1

                            elif b==2:
                                plateau[i][j]=2




            maSurface.blit(fleche1,(208,60))
            maSurface.blit(fleche2,(444,60))
            maSurface.blit(fleche3,(632,232))
            maSurface.blit(fleche4,(632,464))
            maSurface.blit(fleche5,(452,658))
            maSurface.blit(fleche6,(204,658))
            maSurface.blit(fleche7,(38,466))
            maSurface.blit(fleche8,(38,234))

            if 208<x<276 and 60<y<110:
                maSurface.blit(fond,(0,0))
                rotationPlateau(plateau,n,1,True)

            elif 444<x<508 and 60<y<110:
                maSurface.blit(fond,(0,0))
                rotationPlateau(plateau,n,4,False)

            elif 632<x<678 and 232<y<302:
                maSurface.blit(fond,(0,0))
                rotationPlateau(plateau,n,4,True)

            elif 634<x<678 and 464<y<520:
                maSurface.blit(fond,(0,0))
                rotationPlateau(plateau,n,3,False)

            elif 452<x<520 and 658<y<704:
                maSurface.blit(fond,(0,0))
                rotationPlateau(plateau,n,3,True)

            elif 204<x<274 and 658<y<704:
                maSurface.blit(fond,(0,0))
                rotationPlateau(plateau,n,2,False)

            elif 38<x<82 and 466<y<534:
                maSurface.blit(fond,(0,0))
                rotationPlateau(plateau,n,2,True)

            elif 38<x<82 and 234<y<302:
                maSurface.blit(fond,(0,0))
                rotationPlateau(plateau,n,1,False)

            if b==1:
                b=2
            elif b==2:
                b=1









#Test des alignement

            if alignementDiagonale(plateau,1)is True or alignementVertical(plateau,1) is True or alignementHorizontal(plateau,1) is True:
                maSurface.blit(blancgagne,(725,182))
                rejouer=False
            elif alignementDiagonale(plateau,2)is True or alignementVertical(plateau,2) is True or alignementHorizontal(plateau,2) is True:
                maSurface.blit(noirgagne,(725,182))
                rejouer = False

            affichagePion(plateau)

#Bouton rejouer et quitter

            if rejouer is False:
                maSurface.blit(rejouez,(760,346))
                maSurface.blit(quittez,(759,433))
                if event.type == MOUSEBUTTONDOWN:
                    x, y=event.pos
                    if 760<x<914 and 345<y<395 :
                        rejouer = True
                        plateau=[[0 for i in range(n)]for j in range(n)]
                        maSurface.blit(fond,(0,0))
                    elif 759<x<914 and  432<y<473 :
                        inProgress= False




    if event.type == QUIT:
        inProgress = False

    pygame.display.update()
pygame.quit()







