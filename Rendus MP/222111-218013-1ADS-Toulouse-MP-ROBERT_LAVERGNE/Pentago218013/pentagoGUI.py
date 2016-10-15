import random, sys, pygame, copy, os, time
from pygame.locals import *
pygame.init()

##################
#FONCTIONS CODEES#
##################

def NOUVEAUJEU(coorX,coorY,table):

    if coorX>770 and coorX<960 and coorY>90 and coorY<118 :
            
        table=[[["","",""],["","",""],["","",""]],[["","",""],["","",""],["","",""]],[["","",""],["","",""],["","",""]],[["","",""],["","",""],["","",""]]]
        click=1
        affichageBOUTON(click)
        affichage(table)
        return table

    else:
        return table

def QUIT(coordonX,coordonY):

    if coordonX>770 and coordonX<870 and coordonY>120 and coordonY<146:
        a=True
        return a
        
def rotate(table,cadre,position):

        if position==1:
            a=3
        elif position==0:
            a=1
	
        for i in range(0,a):
            template=[["","",""],["","",""],["","",""]]
            template[0][0]=table[cadre][2][0]
            template[2][0]=table[cadre][2][2]
            template[2][2]=table[cadre][0][2]
            template[0][2]=table[cadre][0][0]
		
            template[0][1]=table[cadre][1][0]
            template[1][0]=table[cadre][2][1]
            template[2][1]=table[cadre][1][2]
            template[1][2]=table[cadre][0][1]
		
            template[1][1]=table[cadre][1][1]
            
            table[cadre]=template
    

def convert(table):
        
	template=[["","","","","",""],["","","","","",""],["","","","","",""],["","","","","",""],["","","","","",""],["","","","","",""]]

	for a in range(0,6):
		for b in range(0,6):
			if b<3 and a<3:
				template[a][b]=table[0][a][b]
			if b>3 and a<3:
				template[a][b]=table[1][a][b-3]
			if b<3 and a>3:
				template[a][b]=table[2][a-3][b]
			if b>3 and a>3:
				template[a][b]=table[3][a-3][b-3]
				
	return template

def TOURDEJEU(joueur):
        
    if click==2:    
        if joueur==1:
            joueur=2

        elif joueur==2:
            joueur=1

        return joueur

    else:    
        return joueur


    
def POSITIONJOUEE(coordonX,coordonY,table,click):
        
    posel=0
    posec=0

    if click==1:
        
            if coordonX>=120.00 and coordonY>=90.00 and coordonX<420.00 and coordonY<390.00:
                cadre=0
                posel,posec=0, 0
                print(cadre)

            elif coordonX>420.00 and coordonY>=90.00 and coordonX<=720.00 and coordonY<390.00:
                cadre=1
                posel,posec=0, 1
                print(cadre)

            elif coordonX>=120.00 and coordonY>390.00 and coordonX<420.00 and coordonY<=690.00:
                cadre=2
                posel,posec=1,0
                print(cadre)

            elif coordonX>420.00 and coordonY>390.00 and coordonX<=720.00 and coordonY<=690.00:
                cadre=3
                posel,posec=1,1
                print(cadre)

            for i in range(0,3):
                for j in range(0,3):

                    if coordonX>=120+j*100+posec*300 and coordonX<220+j*100+posec*300 and coordonY>=90+i*100+posel*300 and coordonY<190+j*100+posel*300:
                        
                        table[cadre][i][j]=joueur
                        print(table)
                        break

            return table
    else:
            return table


def Chek(coordonX,coordonY,table,click):

    if click==2:
            
        if coordonX>=245 and coordonX<=310 and coordonY>=20 and coordonY<=85:
            rotate(table, 0, 1) 
                        
        elif coordonX>=725 and coordonX<=790 and coordonY>=210 and coordonY<=275:
            rotate(table,1, 1)

        elif coordonX>=540 and coordonX<=605 and coordonY>=695 and coordonY<=760:
            rotate(table, 2, 1)
                
        elif coordonX>=50 and coordonX<=110 and coordonY>=510 and coordonY<=575:
            rotate(table, 3, 1)
                
        elif coordonX>=50 and coordonX<=110 and coordonY>=210 and coordonY<=275:
            rotate(table, 0, 0)

        elif coordonX>=540 and coordonX<=605 and coordonY>=20 and coordonY<=85:
            rotate(table, 1, 0)

        elif coordonX>=725 and coordonX<=790 and coordonY>=510 and coordonY<=575:
            rotate(table, 2, 0)

        elif coordonX>=245 and coordonX<=310 and coordonY>=695 and coordonY<=760:
            rotate(table, 3, 0)


######################
#FONCTIONS GRAPHIQUES#
######################

def checkForQuit():
    for event in pygame.event.get((QUIT, KEYUP)):
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
                   
        

def affichage(table):
        table=convert(table)

        for i in range(0,6):
            for j in range(0,6):
        
                if table[i][j]== "":
                    pygame.draw.circle(maSurface, VERT,(170+j*100,140+i*100),25)

                elif table[i][j]==1:
                    pygame.draw.circle(maSurface, BLANC,(170+j*100,140+i*100),25)

                elif table[i][j]==2:
                    pygame.draw.circle(maSurface, NOIR,(170+j*100,140+i*100),25)


table=[[["","",""],["","",""],["","",""]],[["","",""],["","",""],["","",""]],[["","",""],["","",""],["","",""]],[["","",""],["","",""],["","",""]]]

joueur=1
click=1
coorX=0
coorY=0

BLANC    = (255, 255, 255)
NOIR     = (0, 0, 0)
BLEUFOND = (1, 111, 254)
VERT     = (0, 255, 0)
GRIS     = (30, 30, 30)

WIDTH  =1000 #Longueur de la fenêtre de jeux
HEIGHT =800  #Hauteur de la fenêtre de jeux

maSurface=pygame.display.set_mode((1000,800))               #Création de la Fenêtre
pygame.display.set_caption('TP PENTAGO')                    #Nom de la Fenêtre
maSurface.fill(BLEUFOND)                                    #Couleur de Fond de la Fenêtre
NouvellePartie = pygame.image.load("NEWGAME.png")           #Texte du menu
QuitterPartie = pygame.image.load("QUITTER.png")            #Texte du menu
Regles = pygame.image.load("REGLE.png")                     #Texte du menu
maSurface.blit(NouvellePartie,(750,50))                     #Position Texte du menu
maSurface.blit(QuitterPartie,(750,100))                     #Position Texte du menu
maSurface.blit(Regles,(750,150))                            #Position Texte du menu
pygame.draw.rect(maSurface, GRIS,(120,90,600,600))          #Plateau du jeu
pygame.draw.line(maSurface, NOIR,(420,90),(420,690),2)      #Delimitation des cadrants
pygame.draw.line(maSurface, NOIR,(120,390),(720,390),2)

def affichageBOUTON(click):

    if click==1:

        NouvellePartie = pygame.image.load("NEWGAME.png")           #Texte du menu
        QuitterPartie = pygame.image.load("QUITTER.png")            #Texte du menu
        Regles = pygame.image.load("REGLE.png")                     #Texte du menu
        maSurface.blit(NouvellePartie,(750,50))                     #Position Texte du menu
        maSurface.blit(QuitterPartie,(750,100))                     #Position Texte du menu
        maSurface.blit(Regles,(750,150))                            #Position Texte du menu
        pygame.draw.rect(maSurface, GRIS,(120,90,600,600))          #Plateau du jeu
        pygame.draw.line(maSurface, NOIR,(420,90),(420,690),2)      #Limites des cadres
        pygame.draw.line(maSurface, NOIR,(120,390),(720,390),2)

    if click==2:

        NouvellePartie = pygame.image.load("NEWGAME.png")           #Texte du menu
        QuitterPartie = pygame.image.load("QUITTER.png")            #Texte du menu
        Regles = pygame.image.load("REGLE.png")                     #Texte du menu
        maSurface.blit(NouvellePartie,(750,50))                     #Position Texte du menu
        maSurface.blit(QuitterPartie,(750,100))                     #Position Texte du menu
        maSurface.blit(Regles,(750,150))                            #Position Texte du menu
        pygame.draw.rect(maSurface, GRIS,(120,90,600,600))          #Plateau du jeu
        pygame.draw.line(maSurface, NOIR,(420,90),(420,690),2)      #Limites des cadres
        pygame.draw.line(maSurface, NOIR,(120,390),(720,390),2)

        fleche1=pygame.image.load("1b.png")                         #Affichage des différentes Flèches du jeu
        maSurface.blit(fleche1,(245,20))
        fleche2=pygame.image.load("4b.png")
        maSurface.blit(fleche2,(725,210))  
        fleche3=pygame.image.load("2a.png")
        maSurface.blit(fleche3,(540,695))
        fleche4=pygame.image.load("2b.png")
        maSurface.blit(fleche4,(50,510))
        fleche5=pygame.image.load("4a.png")
        maSurface.blit(fleche5,(50,210))
        fleche6=pygame.image.load("1a.png")
        maSurface.blit(fleche6,(540,20))
        fleche7=pygame.image.load("3a.png")
        maSurface.blit(fleche7,(725,510))
        fleche8=pygame.image.load("3b.png")
        maSurface.blit(fleche8,(245,695))


inProgress = True
while inProgress:

        
        for event in pygame.event.get():
                if event.type == QUIT:
                    inProgress = False
            
                if event.type == MOUSEBUTTONUP:
                    coordonX,coordonY=event.pos
                    print(coordonX, coordonY)
                          
                    Chek(coordonX,coordonY,table,click)
                    table=POSITIONJOUEE(coordonX,coordonY,table,click)
                    joueur=TOURDEJEU(joueur)
                    a=QUIT(coordonX,coordonY)
                    table=NOUVEAUJEU(coordonX,coordonY,table)

                    if a==True:
                        inProgress=False
                        
                    if click==1:
                        click=2
                        

                    else:
                        click=1
                        
                         
                           
                    affichageBOUTON(click)
                    affichage(table)
                         
    
        pygame.display.update()
pygame.quit()
        

pygame.quit()
sys.exit()
