import os
import pygame, sys
from pygame.locals import *


####################################################################################
############### DEBUTANT EN PYTHON PROGRAMME DU PENTAGO BY ALEXIS ##################
####################################################################################


WIDTH=850    ##largeur
HEIGHT=600     ##hauteur
SIZE = 90

BLEUVERT = (0,152,128)
BLEUFOND = (1,111,254)
BLEUTROU = (23,95,188)
NOIR = (0,0,0)
BLANC = (255,255,255)
GRIS = (30,30,30)

maSurface1 = pygame.display.set_mode((WIDTH,HEIGHT))
maSurface2 = pygame.display.set_mode((800,650))  ##l'élément en noir 

pygame.display.set_caption('Jeu de Pentago by Alexis')

pygame.mixer.init(41200, -16, 2, 2048)

######## IMPORTS ###########

sonintro = pygame.mixer.Sound("intro.wav")
imgaccueil = pygame.image.load("accueil.png")
plateau6x6 = pygame.image.load("6x6.png")
plateau8x8 = pygame.image.load("8x8.png")
jouer = pygame.image.load("jouer.png")
charge = pygame.image.load("charger.png")
pion6 = pygame.image.load("pion6x6.png")
pion8 = pygame.image.load("pion8x8.png")
chargerplateau=pygame.image.load("chargerquoi.png")
son=pygame.image.load("sonon.png")
passon=pygame.image.load("sonoff.png")
aligne=pygame.image.load("pionaligner.png")
plateaualigne=pygame.image.load("plateau.png")
regles=pygame.image.load("regle.png")
reglesdujeu=pygame.image.load("regledujeu.jpg")
quitterjeu=pygame.image.load("quitter.png")
contrequi=pygame.image.load("iaounon.png")

    
def fond():                                 # AFFICHE LE FOND AVEC LE BOUTON JOUER
    maSurface1.blit(imgaccueil,(0,13))
    maSurface1.blit(jouer,(300,500))

##maSurface1.blit(plateau6x6,(0,13))
##maSurface1.blit(plateau8x8,(0,13))


def boutons ():                             # BOUTONS SOUS LE BOUTON JOUER
    maSurface1.blit(plateau6x6,(97,570))
    maSurface1.blit(plateau8x8,(300,570))
    maSurface1.blit(charge,(503,570))

def pasboutons():                           # AFFICHE LE FOND
    fond()

fond()
#boutons()
#maSurface1.blit(regles,(0,15))



sonintro.play()                             # JOUE LE SON
maSurface1.blit(passon,(750,25)) 

inProgress =True
affiche=False
bouge=False
clic=False
stock=False
suite=False
numero=0
clicfin=False

while inProgress: 
    for event in pygame.event.get():
        if event.type == QUIT:
            inProgress = False
            
         

                 
        if event.type == MOUSEBUTTONDOWN:   #BOUTON QUITTER
            X,Y = event.pos
            print(X,Y)
            
            if 0 < X < 200 and 90 < Y < 150:
                pygame.quit()
                 
                 
            
        if event.type == MOUSEMOTION:       # BOUTON REGLES DU JEU
            X,Y = event.pos
            print(X,Y)
            
            if 0 < X < 200 and 15 < Y < 75:
                 
                 maSurface1.blit(reglesdujeu,(200,150))
            
            else:
                fond()
                maSurface1.blit(regles,(0,15))
                maSurface1.blit(quitterjeu,(0,90))
                if stock==False:
                    maSurface1.blit(passon,(750,25))
                if stock==True:
                    maSurface1.blit(son,(750,25))  
                
                 
                 
                    

                
        if event.type == MOUSEBUTTONUP and stock==False:    #BOUTON DU SON
            X,Y = event.pos
            
            
            if 700 < X < 790 and 5 < Y < 50:
                 sonintro.stop()
                 pygame.draw.rect(maSurface1,(0,0,0),(750,25,18,18))
                 
                 maSurface1.blit(son,(750,25))
                 
                 stock=True
                 
        elif event.type == MOUSEBUTTONUP and stock==True :  #BOUTON DU SON
            X,Y = event.pos
            
            
            if 700 < X < 790 and 5 < Y < 50:
                 sonintro.play()
                 pygame.draw.rect(maSurface1,(0,0,0),(750,25,18,18))
                 maSurface1.blit(passon,(750,25))       
                 stock=False
                                 
        
        if event.type == MOUSEMOTION:                       #QUAND ON PASSE LE CURSEUR SUR JOUER QUE CA AFFICHE EN DESSOUS LES BOUTONS
            X,Y = event.pos
            
            
            if 300 < X < 500 and 500 < Y < 560: 
                boutons()
                affiche=True
                #numero=0
            
        
        if event.type == MOUSEMOTION and affiche==True :     #BOOLEEN POUR POUVOIR BOUGER
            X,Y = event.pos
            
            if 90 < X < 710 and 555 < Y < 630 or 300 < X < 500 and 500 < Y < 560:
                bouge=True
                affiche=True
                
                
                
            else:
                numero=0
                fond()
                pasboutons()
                maSurface1.blit(regles,(0,15))
                maSurface1.blit(quitterjeu,(0,90))
                affiche=False
                suite=False
                clicfin=False
                clic=False
                
                
        if event.type == MOUSEMOTION and bouge==True and affiche==True:     #BOUTON PLATEAU 8X8
            X,Y = event.pos
            
            if 300 < X < 501 and 555 < Y < 630:
                if numero==1 or numero==3 or numero==11 or numero == 33:
                    numero=0
                    suite=False
                    clicfin=False
                fond()
                
                maSurface1.blit(pion8,(300,570))
                maSurface1.blit(plateau6x6,(97,570))
                maSurface1.blit(charge,(503,570))
                maSurface1.blit(aligne,(120,500))
                maSurface1.blit(regles,(0,15))
                maSurface1.blit(quitterjeu,(0,90))
                
                
                clic=True
                
                
            if 97 < X < 301 and 560 < Y < 630:
                if numero==2 or numero ==22 or numero == 222 or numero==3 or numero==33:
                    numero=0
                    suite=False                 #BOUTON PLATEAU 6X6
                    clicfin=False
                fond()
                
                maSurface1.blit(pion6,(97,570))
                maSurface1.blit(plateau8x8,(300,570))
                maSurface1.blit(charge,(503,570))
                maSurface1.blit(aligne,(120,500))
                maSurface1.blit(regles,(0,15))
                maSurface1.blit(quitterjeu,(0,90))
                clic=True
                
            if 500 < X < 703 and 560 < Y < 630:
                global numero   # BOUTON CHARGE
                if numero==1 or numero==2 or numero ==11 or numero ==22 or numero ==222:
                    numero=0
                    suite=False
                    clicfin=False
                fond()
                
                maSurface1.blit(chargerplateau,(503,570))
                maSurface1.blit(plateau6x6,(97,570))
                maSurface1.blit(plateau8x8,(300,570))
                maSurface1.blit(plateaualigne,(530,500))
                maSurface1.blit(regles,(0,15))
                maSurface1.blit(quitterjeu,(0,90))
                
                clic=True
           
               
            

        if event.type == MOUSEBUTTONDOWN and clic==True and clicfin==False:      #LANER LE JEU QUAND ON CLIQUE AU BON ENDROIT
            X,Y=event.pos
            global numero
            if 97<X<191 and 571<Y<628:
                suite=True
                numero=1
                fond()
                maSurface1.blit(contrequi,(97,570))
                maSurface1.blit(plateau8x8,(300,570))
                maSurface1.blit(charge,(503,570))
                #maSurface1.blit(aligne,(120,500))
                maSurface1.blit(regles,(0,15))
                maSurface1.blit(quitterjeu,(0,90))
                
            if 198<X<295 and 571<Y<629:
                suite=True
                numero=11
                fond()
                maSurface1.blit(contrequi,(97,570))
                maSurface1.blit(plateau8x8,(300,570))
                maSurface1.blit(charge,(503,570))
                #maSurface1.blit(aligne,(120,500))
                maSurface1.blit(regles,(0,15))
                maSurface1.blit(quitterjeu,(0,90))
                
            if 300<X<364 and 571<Y<629:
                suite=True
                numero=2
                fond()
                maSurface1.blit(contrequi,(300,570))
                maSurface1.blit(plateau6x6,(97,570))
                maSurface1.blit(charge,(503,570))
                #maSurface1.blit(aligne,(120,500))
                maSurface1.blit(regles,(0,15))
                maSurface1.blit(quitterjeu,(0,90))
                
            if 368<X<430 and 571<Y<629:
                suite=True
                numero=22
                fond()
                maSurface1.blit(contrequi,(300,570))
                maSurface1.blit(plateau6x6,(97,570))
                maSurface1.blit(charge,(503,570))
                #maSurface1.blit(aligne,(120,500))
                maSurface1.blit(regles,(0,15))
                maSurface1.blit(quitterjeu,(0,90))
                
            if 434<X<500 and 571<Y<629:
                suite=True
                numero=222
                fond()
                maSurface1.blit(contrequi,(300,570))
                maSurface1.blit(plateau6x6,(97,570))
                maSurface1.blit(charge,(503,570))
                #maSurface1.blit(aligne,(120,500))
                maSurface1.blit(regles,(0,15))
                maSurface1.blit(quitterjeu,(0,90))
                
            if 506<X<599 and 571<Y<629:
                suite=True
                numero=3
                fond()
                maSurface1.blit(contrequi,(503,570))
                maSurface1.blit(plateau6x6,(97,570))
                maSurface1.blit(plateau8x8,(300,570))
                #maSurface1.blit(aligne,(120,500))
                maSurface1.blit(regles,(0,15))
                maSurface1.blit(quitterjeu,(0,90))
                
            if 606<X<698 and 571<Y<629:
                suite=True
                numero=33
                fond()
                maSurface1.blit(contrequi,(503,570))
                maSurface1.blit(plateau6x6,(97,570))
                maSurface1.blit(plateau8x8,(300,570))
                #maSurface1.blit(aligne,(120,500))
                maSurface1.blit(regles,(0,15))
                maSurface1.blit(quitterjeu,(0,90))
                
        
            clicfin=True
            #affiche=True
            print(numero)
        elif event.type == MOUSEBUTTONDOWN and suite==True and clicfin==True and clic==True :
            global numero
            posX,posY=event.pos
            global numero
            
                
            if 98<posX<194 and 570<posY<630 and numero==1 :
                sonintro.stop()
                exec(open("jeu6x64IA.py").read()) 
            if 199<posX<296 and 570<posY<630 and numero==1:
                sonintro.stop()
                exec(open("jeu6x64.py").read()) 

            if 98<posX<194 and 570<posY<630 and numero==11:
                sonintro.stop()
                exec(open("jeu6x65IA.py").read()) 
            if 199<posX<296 and 570<Y<630 and numero==11:
                sonintro.stop()
                exec(open("jeu6x65.py").read()) 
                
            if 300<posX<396 and 570<posY<630 and numero==2:
                sonintro.stop()
                exec(open("jeu8x85IA.py").read()) 
            if 400<posX<500 and 570<posY<630 and numero==2:
                sonintro.stop()
                exec(open("jeu8x85.py").read()) 
                
            if 300<posX<396 and 570<posY<630 and numero==22:
                sonintro.stop()
                exec(open("jeu8x86IA.py").read()) 
            if 400<posX<500 and 570<posY<630 and numero==22:
                sonintro.stop()
                exec(open("jeu8x86.py").read()) 

            if 300<posX<396 and 570<posY<630 and numero==222:
                sonintro.stop()
                exec(open("jeu8x87IA.py").read()) 
            if 400<posX<500 and 570<posY<630 and numero==222:
                sonintro.stop()
                exec(open("jeu8x87.py").read()) 
                
            if 504<posX<599 and 570<posY<630 and numero==3:
                sonintro.stop()
                exec(open("charge6x6IA.py").read())  
            if 607<posX<701 and 570<Y<630 and numero==3:
                sonintro.stop()
                exec(open("charge6x6.py").read()) 

            if 504<posX<599 and 570<posY<630 and numero==33:
                sonintro.stop()
                exec(open("charge8x8IA.py").read()) 
            if 607<posX<701 and 570<posY<630 and numero==33:
                sonintro.stop()
                exec(open("charge8x8.py").read())
                
     
        if numero==1:
            fond()
            maSurface1.blit(contrequi,(97,570))
            maSurface1.blit(plateau8x8,(300,570))
            maSurface1.blit(charge,(503,570))
            #maSurface1.blit(aligne,(120,500))
            maSurface1.blit(regles,(0,15))
            maSurface1.blit(quitterjeu,(0,90))
            
        elif numero==11:
            fond()
            maSurface1.blit(contrequi,(97,570))
            maSurface1.blit(plateau8x8,(300,570))
            maSurface1.blit(charge,(503,570))
            #maSurface1.blit(aligne,(120,500))
            maSurface1.blit(regles,(0,15))
            maSurface1.blit(quitterjeu,(0,90))
            
        elif numero==2:
            fond()
            maSurface1.blit(contrequi,(300,570))
            maSurface1.blit(plateau6x6,(97,570))
            maSurface1.blit(charge,(503,570))
            #maSurface1.blit(aligne,(120,500))
            maSurface1.blit(regles,(0,15))
            maSurface1.blit(quitterjeu,(0,90))
            
        elif numero==22:
            fond()
            maSurface1.blit(contrequi,(300,570))
            maSurface1.blit(plateau6x6,(97,570))
            maSurface1.blit(charge,(503,570))
            #maSurface1.blit(aligne,(120,500))
            maSurface1.blit(regles,(0,15))
            maSurface1.blit(quitterjeu,(0,90))
            
        elif numero==222:
            fond()
            maSurface1.blit(contrequi,(300,570))
            maSurface1.blit(plateau6x6,(97,570))
            maSurface1.blit(charge,(503,570))
            #maSurface1.blit(aligne,(120,500))
            maSurface1.blit(regles,(0,15))
            maSurface1.blit(quitterjeu,(0,90))
            
        elif numero==3:
            fond()
            maSurface1.blit(contrequi,(503,570))
            maSurface1.blit(plateau6x6,(97,570))
            maSurface1.blit(plateau8x8,(300,570))
            #maSurface1.blit(aligne,(120,500))
            maSurface1.blit(regles,(0,15))
            maSurface1.blit(quitterjeu,(0,90))
            
        elif numero==33:
            fond()
            maSurface1.blit(contrequi,(503,570))
            maSurface1.blit(plateau6x6,(97,570))
            maSurface1.blit(plateau8x8,(300,570))
            #maSurface1.blit(aligne,(120,500))
            maSurface1.blit(regles,(0,15))
            maSurface1.blit(quitterjeu,(0,90))
    
        
            
            
     
                                
                
#sonintro.stop()
#exec(open("charge8x8.py").read())                
                
                
                

        if event.type == QUIT:
            inProgress = False

        if event.type == KEYDOWN: # quitte aussi si tu appuies sur la touche ECHAP
            if event.key==K_ESCAPE:
                inProgress = False

    pygame.display.update()
    
pygame.quit()

