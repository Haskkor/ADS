import pygame #permet d'importer pygame
from rotations import *
from Convertliste import *
from alignements import *
pygame.init()
maSurface = pygame.display.set_mode((1300,800))
maSurface.fill((200,200,200))
pygame.display.set_caption('Pentago')
tour = 0
tourCtrl = 0
joueur1 = 0
joueur2 = 0

plateau = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]


def Plateau(maSurface,plateau):
    Table = pygame.draw.rect(maSurface,(0,0,0),(195,95,605,605))
    quadrant1 = Quadrant(200,100)
    quadrant2 = Quadrant(500,100)
    quadrant4 = Quadrant(200,400)
    quadrant3 = Quadrant(500,400)
    return quadrant1,quadrant2,quadrant3,quadrant4


def Quadrant(x,y):
    Quadrant1 = pygame.draw.rect(maSurface,(200,0,0),(x,y,295,295))

Plateau(maSurface,plateau)


def PoserPion(posex,posey,plateau,tour,tourCtrl):
    for lignes in range(0,6):
        for cases in range(0,6):
            if (225 + cases* 100)<posex<(275 + cases*100)and (125 + lignes* 100)<posey<(175 + lignes*100):
                if plateau[lignes][cases] == 0:
                    if tour == 0:
                        joueurBlancimage = pygame.image.load('joueurBlanc.bmp')
                        maSurface.blit(joueurBlancimage,(1000,100))
                        plateau[lignes][cases] = 1
                        tourCtrl = 1

                    elif tour == 2:
                        joueurNoirimage = pygame.image.load('joueurNoir.bmp')
                        maSurface.blit(joueurNoirimage,(1000,100))
                        plateau[lignes][cases] = 2
                        tourCtrl = 3

    return plateau,tourCtrl


def Couleurs(plateau):
    for lignes in range(0,6):
        for cases in range(0,6):
            if plateau[lignes][cases] == 1:
                pygame.draw.circle(maSurface,(255,255,255),(250+cases*100,150+lignes*100),25)
            elif plateau[lignes][cases] == 2:
                pygame.draw.circle(maSurface,(0,0,0),(250+cases*100,150+lignes*100),25)
            elif plateau[lignes][cases] == 0 :
                    pygame.draw.circle(maSurface,(150,0,0),(250+cases*100,150+lignes*100),25)





def Rotate(posex,posey,plateau):
    liste = ConvertListe(plateau)
    flecheBas = pygame.image.load('flechebas.png')
    flecheGaucheInverse = pygame.image.load('flechegaucheinverse.png')
    maSurface.blit(flecheBas,(325,25))
    maSurface.blit(flecheBas,(625,25))
    maSurface.blit(flecheBas,(325,725))
    maSurface.blit(flecheBas,(625,725))
    maSurface.blit(flecheGaucheInverse,(850,215))
    maSurface.blit(flecheGaucheInverse,(100,215))
    maSurface.blit(flecheGaucheInverse,(850,515))
    maSurface.blit(flecheGaucheInverse,(100,515))

    if 325<posex<425 and 25<posey<100:
        RotationsQuadrant(0,True,liste)
    elif 625<posex<725 and 25<posey<100:
        RotationsQuadrant(1,True,liste)
    elif 325<posex<425 and 725<posey<825:
        RotationsQuadrant(3,True,liste)
    elif 625<posex<725 and 725<posey<825:
        RotationsQuadrant(2,True,liste)

    elif 850<posex<930 and 215<posey<315:
        RotationsQuadrant(1,False,liste)
    elif 100<posex<188 and 215<posey<315:
        RotationsQuadrant(0,False,liste)
    elif 850<posex<930 and 515<posey<815:
        RotationsQuadrant(3,False,liste)
    elif 100<posex<188 and 515<posey<815:
        RotationsQuadrant(2,False,liste)
    stockage2 = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
    for h in range(0,6):
        for g in range(0,6):
            if g<3 and h<3:
                stockage2[h][g] = liste[0][h][g]
            if g>=3 and h>=3:
                stockage2[h][g] = liste[3][h-3][g-3]
            if g<3 and h>=3:
                stockage2[h][g] = liste[2][h-3][g]
            if g>=3 and h<3:
                stockage2[h][g] = liste[1][h][g-3]
    plateau = stockage2
    return plateau





inProgress = True
while inProgress:
    for event in pygame.event.get():
        if tour == 0:
            joueurBlancimage = pygame.image.load('joueurBlanc.bmp')
            maSurface.blit(joueurBlancimage,(1000,100))
        elif tour == 1:
            TournerunCadran = pygame.image.load('Tourner un cadran.bmp')
            maSurface.blit(TournerunCadran,(1000,100))
            tourCtrl = 2
        elif tour == 2 :
            joueurNoirimage = pygame.image.load('joueurNoir.bmp')
            maSurface.blit(joueurNoirimage,(1000,100))
        elif tour == 3:
            TournerunCadran = pygame.image.load('Tourner un cadran.bmp')
            maSurface.blit(TournerunCadran,(1000,100))
            tourCtrl = 4
        Couleurs(plateau)

        if event.type == pygame.MOUSEBUTTONUP:
            posex,posey = event.pos
            check(plateau)
            plateau,tourCtrl = PoserPion(posex,posey,plateau,tour,tourCtrl)
            if tour == 0 and tourCtrl == 1:
                tour = 1
            elif tour == 1 and tourCtrl == 2:
                tour = 2
            elif tour == 2 and tourCtrl == 3 :
                tour = 3
            elif tour == 3 and tourCtrl == 4:
                tour = 0
            Couleurs(plateau)
            plateau = Rotate(posex,posey,plateau)

            if joueur1 == 1:
                WIN1 = pygame.image.load('WIN1.bnp')
                maSurface.blit(WIN1,(1300,800))


        if event.type == pygame.QUIT:
            inProgress = False
    pygame.display.update()



