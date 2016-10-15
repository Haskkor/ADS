import os
from alignements import *
from bases import *
from rotations import *
import pygame,sys 
import traceback 
from pygame.locals import *
pygame.init()

###***COLORS*******************

BLACK =(0,0,0)
WHITE=(255,255,255)
gold =(218,165, 32)
clr= (47,79,79)
Redclr=(142,35,35)
Bois=(139,131,120)	
bordered=(209,146,117)	
beige=(245,245,220)	
Gris=(193,205,193)	


fenetre = pygame.display.set_mode((1400,780))
pygame.display.set_caption('PentaGOT - PENTAGO EDITION GAME OF THRONES -')
Fond= pygame.image.load('Playgot.jpg').convert()
fenetre.blit(Fond,(0,0))

joueur=1
inProgress=True
procéd1=True
procéd2=True

son=pygame.mixer.Sound("Game_Of_Thrones_Opening_-_Main_Theme.wav") 
continuer = 1
joue = 0 

while continuer:
    for event in pygame.event.get(): 
        if event.type==QUIT:
            continuer=0

        if event.type == MOUSEMOTION and joue==0:

            son.play()
            joue = 1

#########[DESSIN DU PLATEAU] ###########

#Dessin d'1 quad
def quad(table,fenetre,i,j,épaisseur):
    pygame.draw.rect(fenetre,Redclr,(120+(épaisseur*j),55 +(épaisseur*i) ,340,340),10)
    for u in range (3):
        for v in range (3): 
            pygame.draw.rect(fenetre,WHITE,(340*j+ 129 + 110*v,340*i +110*u+69, 100,100) ,5)
            if table[3*j+v] [3*i+u] ==0 :
                pygame.draw.circle(fenetre,Gris,(340*j+180+110*v,340*i+115+110*u), 50,0)
           
            if table[3*j+v] [3*i+u] ==1 :
                
                pygame.draw.circle(fenetre,WHITE,(340*j+180+110*v,340*i+115+110*u), 50,0)
                playjoueur1= pygame.image.load('Pion1.jpg').convert()
                fenetre.blit(playjoueur1,(340*j+ 129 + 110*v,340*i +110*u+69))
                

            if table[3*j+v] [3*i+u] ==2 :
                #pygame.draw.circle(fenetre,gold,(340*j+180+110*v,340*i+115+110*u), 50,0)
                playjoueur2= pygame.image.load('Pion2.jpg').convert()
                fenetre.blit(playjoueur2,(340*j+ 129 + 110*v,340*i +110*u+65))
            
######Dessin du plateau de jeu 
                
def dessin1(plateau, surface): 
    for i in range (0,2):
        for j in range (0,2):
            quad(table,fenetre,i,j,340)


####Pour mon changement de joueur
def next(player):
    if player == 1:
        return 2
    if player ==2 : 
        return 1

####Fonction pour la pose d'un pion

def pion(plateau,surface,joueur):
    for event in pygame.event.get():

        if event.type== MOUSEBUTTONDOWN and event.button == 1:
            for i  in range (0,2):
                for j in range (0,2):
                    for u in range (3):
                        for v in range(3):
                            if table[3*j+v][3*i+u]==0:
                                
                                if 340*j+130+110*v<event.pos [0]<340*j+230+110*v and 340*i+65+110*u<event.pos[1] <340*i+165+110*u :
                                    if joueur ==1 :
                                        table [3*j+v][3*i+u]=1
                                        Tour1= pygame.image.load('Tourjoueur1.jpg').convert()
                                        fenetre.blit(Tour1,(900,75))
                                    if joueur==2:
                                        table [3*j+v][3*i+u]=2
                                        Tour2= pygame.image.load('Tourjoueur2.jpg').convert()
                                        fenetre.blit(Tour2,(900,75))
                                    joueur= next (joueur) 

                                    return True 

        return False 



#### Affichage de flèches
def Arrows(surface):
    Fleche1= pygame.image.load('fleche1.png').convert()
    fenetre.blit(Fleche1,(55,65))

    Fleche2= pygame.image.load('fleche2.png').convert()
    fenetre.blit(Fleche2,(130,10))

    Fleche3= pygame.image.load('fleche3.png').convert()
    fenetre.blit(Fleche3,(690,10))

    Fleche4= pygame.image.load('fleche4.png').convert()
    fenetre.blit(Fleche4,(830,65))

    Fleche5= pygame.image.load('fleche5.png').convert()
    fenetre.blit(Fleche5,(830,625))

    Fleche6= pygame.image.load('fleche6.png').convert()
    fenetre.blit(Fleche6,(690,740))

    Fleche7= pygame.image.load('fleche7.png').convert()
    fenetre.blit(Fleche7,(130,740))

    Fleche8= pygame.image.load('fleche8.png').convert()
    fenetre.blit(Fleche8,(55,625))


            
def click(table,fenetre): 
       
    for event in pygame.event.get():

        if event.type== MOUSEBUTTONDOWN and event.button == 1:
            if 130<event.pos[0]<230 and 10<event.pos[1]<45:#2
                    rotation (table,True,1)
                    return dessin1(table,fenetre) 
            
            if 55<event.pos[0] < 90 and 65<event.pos[1]<165 :
                    rotation (table,False,1)
                    return dessin1(table,fenetre)

      

            if 55<event.pos[0]< 90 and 625<event.pos[1]<725 :
                    rotation (table, True ,2)
                    return False

            
            if 130<event.pos[0]<230 and 740<event.pos[1]<775:
                    rotation (table, False ,2)
                    return False
            
            if 690<event.pos[0]<710 and 740<event.pos[1]<775:
                    rotation (table, True ,3)
                    return False
            
            if 830<event.pos[0]< 865 and 625<event.pos[1]<725:
                    rotation (table, False ,3)
                    return False
            
            if 830<event.pos[0]<865 and 65<event.pos[1]<165 :#4
                    rotation (table, True ,4)
                    return False
            
            if 690<event.pos[0]<710 and 10<event.pos[1]<45:#3
                    rotation (table, False ,4)
                    return False


inProgress=True
while inProgress:
    dessin1(table,fenetre)
                   
    if pion(table,fenetre,joueur): 
        joueur=next(joueur)
        Arrows(fenetre)

        if click(table,fenetre):

            quad(table,fenetre)
            dessin1(table,fenetre)

   

    pygame.display.update

    for event in pygame.event.get(): 
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()    
    pygame.display.update()

pygame.quit()


