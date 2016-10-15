import pygame, sys
from pygame.locals import *
import marshal 
from random import randint
import copy

pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()


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

pygame.display.set_caption('Jeu de Pentago')

fleche1a = pygame.image.load("1a.png")  ##sens aiguille d'une montre
fleche2a = pygame.image.load("2a.png")
fleche3a = pygame.image.load("3a.png")
fleche4a = pygame.image.load("4a.png")

fleche1b = pygame.image.load("1b.png")  ##sens inverse
fleche2b = pygame.image.load("2b.png")
fleche3b = pygame.image.load("3b.png")
fleche4b = pygame.image.load("4b.png")


fleche1abis = pygame.image.load("1abis.png")
fleche2abis = pygame.image.load("2abis.png")
fleche3abis = pygame.image.load("3abis.png")
fleche4abis = pygame.image.load("4abis.png")

fleche1bbis = pygame.image.load("1bbis.png")  ##sens inverse
fleche2bbis = pygame.image.load("2bbis.png")
fleche3bbis = pygame.image.load("3bbis.png")
fleche4bbis = pygame.image.load("4bbis.png")

son=pygame.mixer.Sound("son.mp3")
passave = pygame.image.load("passave.png")
passauvegarde = pygame.image.load("passauvegarde.png")


#sonvictoire=pygame.mixer.Sound("son.mp3")



tourblanc = pygame.image.load("pions_blancs.png")
tournoir = pygame.image.load("pions_noirs.png")
victoireblanc = pygame.image.load("vic_blanc.png")
victoirenoir = pygame.image.load("vic_noir.png")
rejouer = pygame.image.load("Rejouer.png")
save=pygame.image.load("save.png")
quite=pygame.image.load("quitter.png")
tournerplateau=pygame.image.load("tournez.png")
menu=pygame.image.load("menu.png")
execoo=pygame.image.load("match_nul.png")
execoo=pygame.image.load("match_nul.png")

IA=pygame.image.load("iajoue.png")
vous=pygame.image.load("avous.png")



def passauvegarde2 ():
    maSurface2.blit(passave,(520,150))
def passauvegarde1():
    maSurface2.blit(passauvegarde,(570,150))
def debut():
    maSurface2.blit(vous,(150,550))
def tourdesblancs():
    maSurface2.blit(IA,(150,550))
def tourdesnoirs():
    maSurface2.blit(tournoir,(150,550))
def victoireblancs():
    maSurface2.blit(victoireblanc,(150,550))
def victoirenoirs():
    maSurface2.blit(victoirenoir,(150,550))
def imgrejouer():
    maSurface2.blit(rejouer,(580,230))
def sauvegarde1():
    maSurface2.blit(save,(575,150))
           
def sauvegardequibouge():
    y=570
    for i in range (1,10):
        y-=2
        maSurface2.blit(save,(y,150))
        pygame.display.update()

        fpsClock.tick(FPS)
    passauvegarde2 ()
    y=550
    for i in range (1,13):
        y+=2
        maSurface2.blit(save,(y,150))
        pygame.display.update()

        fpsClock.tick(FPS)
        
def quitt():
    maSurface2.blit(quite,(580,310))
def tournerplat():
    maSurface2.blit(tournerplateau,(150,550))
def imgmenu():
    maSurface2.blit(menu,(570,570))
def matchnul():
    maSurface2.blit(execoo,(150,550))
imgrejouer()    
imgmenu()  


def recommencer():
    global basta
    basta=1
    global c
    c=1
    pasfleche()
    global ligne
    ligne=3
    global nbrdedpion
    nbrdepion = 4
    global rotation
    global plateau1
    global plateau2
    global plateau3
    global plateau4
    plateau1=[]
    plateau2=[]
    plateau3=[]
    plateau4=[]
    tableau(plateau1,ligne)
    print(plateau1)
    tableau(plateau2,ligne)

    print(plateau2)
    tableau(plateau3,ligne)

    print(plateau3)
    tableau(plateau4,ligne)

    print(plateau4)


    graphplateau()
    global gagne
    gagne=False   
    global player
    player=2
    
    global joueur
    joueur = 1
    global fin
    fin=False
    global execo
    execo=False
    debut()

    affichepion()
    print()

def fleche():
    maSurface2.blit(fleche1a,(450,140))  ##a droite en haut
    maSurface2.blit(fleche2a,(340,450))  ##en bas a droite
    maSurface2.blit(fleche3a,(35,350))   ##a gauche en bas
    maSurface2.blit(fleche4a,(130,35))   ##en haut a gauche
    
    maSurface2.blit(fleche1b,(35,140))   ##a gauche en haut
    maSurface2.blit(fleche2b,(130,450))  ##en bas a gauche
    maSurface2.blit(fleche3b,(450,350))  ##a droite en bas
    maSurface2.blit(fleche4b,(340,35))   ##en haut a droite

def pasfleche():
    
    maSurface2.blit(fleche1abis,(450,140))  ##a droite en haut
    maSurface2.blit(fleche2abis,(340,450))  ##en bas a droite
    maSurface2.blit(fleche3abis,(30,350))   ##a gauche en bas
    maSurface2.blit(fleche4abis,(130,30))   ##en haut a gauche
    
    maSurface2.blit(fleche1bbis,(30,140))   ##a gauche en haut
    maSurface2.blit(fleche2bbis,(130,450))  ##en bas a gauche
    maSurface2.blit(fleche3bbis,(450,350))  ##a droite en bas
    maSurface2.blit(fleche4bbis,(340,30))   ##en haut a droite

##fleche()
##pasfleche()

def tableau(plateau,ligne):
    colonne=ligne
#    plateau=[]
    for i in range(ligne):
        plateau.append([])
        for j in range(colonne):
            plateau[i].append(0)

    return plateau

def afficheplateau(liste):
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            if liste[i][j] == 0:
                joueur=0
            if liste[i][j] == 1:
                joueur=1
            if liste[i][j] == 2:
                joueur=2
                
#plateau = tableau(plateau,ligne)
ligne=3
nbrdepion = 4
rotation=[]
plateau1=[]
plateau2=[]
plateau3=[]
plateau4=[]
tableau(plateau1,ligne)
afficheplateau(plateau1)
print(plateau1)
tableau(plateau2,ligne)
afficheplateau(plateau2)
print(plateau2)
tableau(plateau3,ligne)
afficheplateau(plateau3)
print(plateau3)
tableau(plateau4,ligne)
afficheplateau(plateau4)
print(plateau4)

##################################
##### On affiche le tableau  #####
##################################

def animvictoire():
    y=10
    w=0
    for i in range (1,40):
        y+=4
        w+=1
        pygame.draw.circle(maSurface2,NOIR,(275,275),y+5,0)
        pygame.draw.circle(maSurface2,BLANC,(275,275),y,0)
        
        fontObj = pygame.font.Font('freesansbold.ttf',(w))
        texteSurface3 = fontObj.render(" BRAVO T'AS",True,NOIR)
        texteSurface4 = fontObj.render("GAGNE !",True,NOIR)
        texteRect = texteSurface3.get_rect()
        texteRect.topleft = (135,220)
        maSurface2.blit(texteSurface3,texteRect)
        texteRect = texteSurface3.get_rect()
        texteRect.topleft = (180,270)
        maSurface2.blit(texteSurface4,texteRect)
        pygame.display.update()
        fpsClock.tick(FPS)
        
    
    
def animvictoire1():
    y=10
    w=0
    for i in range (1,40):
        y+=4
        w+=1
        pygame.draw.circle(maSurface2,BLANC,(275,275),y+5,0)
        pygame.draw.circle(maSurface2,NOIR,(275,275),y,0)
        
        fontObj = pygame.font.Font('freesansbold.ttf',(w))
        texteSurface3 = fontObj.render("VICTOIRE DE",True,BLANC)
        texteSurface4 = fontObj.render("  L'IA !",True,BLANC)
        texteRect = texteSurface3.get_rect()
        texteRect.topleft = (135,220)
        maSurface2.blit(texteSurface3,texteRect)
        texteRect = texteSurface3.get_rect()
        texteRect.topleft = (200,270)
        maSurface2.blit(texteSurface4,texteRect)
        pygame.display.update()
        fpsClock.tick(FPS)



def compteur(cptblanc,cptnoir):
    pascompteur()
    pygame.draw.rect(maSurface1,BLEUFOND,(90,555,50,50))
    pygame.draw.rect(maSurface1,BLEUFOND,(390,555,50,50))
    pygame.draw.circle(maSurface1,BLEUFOND,(116,580),18,0)
    pygame.draw.circle(maSurface2,BLANC,(116,580),15,0)
    pygame.draw.circle(maSurface2,NOIR,(416,580),15,0)

    cptblancs=str(cptblanc)
    cptnoirs=str(cptnoir)
    fontObj = pygame.font.Font('freesansbold.ttf',30)
    texteSurface3 = fontObj.render(cptblancs,True,BLANC)
    texteRect = texteSurface3.get_rect()
    texteRect.topleft = (108,610)
    maSurface2.blit(texteSurface3,texteRect)

    fontObj = pygame.font.Font('freesansbold.ttf',30)
    texteSurface3 = fontObj.render(cptnoirs,True,BLANC)
    texteRect = texteSurface3.get_rect()
    texteRect.topleft = (408,610)
    maSurface2.blit(texteSurface3,texteRect)
def pascompteur():
    pygame.draw.rect(maSurface2,NOIR,(90,612,400,40))
    

    

def afficheplateau(liste):
    for i in range(len(liste)):
        
        for j in range(len(liste[i])):
            if liste[i][j] == 0:
                print("0",sep="",end="")
            if liste[i][j] == 1:
                print("1",sep="",end="")
            if liste[i][j] == 2:
                print("2",sep="",end="")
        print()

        
def alV(temp,player):
    global nbrdepion
    
    for i in range (len(temp)):
        cpt=0
        
        
        for j in range (len(temp[i])):
            
            
            
            if temp[j][i]==player:
                
                
                cpt=cpt+1
                
            if cpt>=nbrdepion:
                return True
            
            if temp[j][i]!= player:
                cpt=0
    return False

def alh(temp,player):
    global nbrdepion
    
    for i in range (len(temp)):
        cpt=0
        
        
        for j in range (len(temp[i])):
            
            
            
            if temp[i][j]==player:
                
                
                cpt=cpt+1
                
            if cpt>=nbrdepion:
                return True
            
            if temp[i][j]!= player:
                cpt=0
    return False

##def joueur(joueur,temp):
##    if joueur==1:
##        if alh(temp,joueur):
##            return True
##        joueur=joueur%2+1
##        if alh(temp,joueur):
##
##            return True
def joueur2(joueur,temp):

    if joueur ==2:
        if alh(temp,joueur):
            print("JOUEUR 2 A GAGNE")

            global gagner
            gagner=False
            victoirenoirs()
            
            return True

def joueur1(joueur,temp):
    joueur=joueur%2+1
    if alh(temp,joueur):
        print("JOUEUR 1 A GAGNE")

        
        victoireblancs()
        
        global gagner
        gagner=True
        return True

##def joueurbis(joueur):
##    if joueur==1:
##        if alV(temp,joueur):
##            return True
##        joueur=joueur%2+1
##        if alV(temp,joueur):
##
##            return True
def joueur2bis(joueur,temp):

    if joueur ==2:
        if alV(temp,joueur):
            print("JOUEUR 2 A GAGNE")

            victoirenoirs()
            global gagner
            gagner=False
            return True

def joueur1bis(joueur,temp):
    joueur=joueur%2+1
    if alV(temp,joueur):
        print("JOUEUR 1 A GAGNE")

        
        victoireblancs()
        global gagner
        gagner=True
        return True

def diago(liste,player,temp):
    global nbrdepion
    
    taille=len(temp)
    for i in range (0,len(liste)-1):
        cpt=0
        for j in range (taille):
            #print(j)            
            #print(plateau[j][i+j])
        
            
            
            if liste[j][i+j]==player:
                cpt=cpt+1
            if cpt>=nbrdepion:
                
                return True
                
            if liste[j][i+j]!= player:
                cpt=0
        taille=taille-1

    return False





def rotations(temp,rotation):
    colone=[]
    ligne=[]

    for i in range (len(temp)):
        colone.append([])
        
        #ligne.append(plateau[i])      #ne sert apparament a rien
        for j in range (len(temp[i])):
            colone[i].append(temp[j][i])
            
    for i in range (len(colone)):
        

        rotation.append(colone[i])
        rotation[i].reverse()
    
    return rotation


def zero(joueur,temp):
    
    
    rotation=[]
    
    
    if diago(temp,joueur,temp):
        
        
        #print("gg")
        return True


def un (joueur,rotation1,temp):
    
    rotation=[]
    rotations(temp,rotation)
    rotation1.extend(rotation)
    
    rotation=[]
    
    
    if diago(rotation1,joueur,temp):
        
        
        #print("gg")
        return True
    
    



def deux(joueur,rotation1,rotation2,temp):
    
    rotation=[]
    rotations(rotation1,rotation)
    
    rotation2.extend(rotation)
    
    rotation=[]
    

    if diago(rotation2,joueur,temp):
        
        
        
        #print("gg")
        return True

   

def trois(joueur,rotation1,rotation2,rotation3,temp):
    
    rotation=[]
    rotations(rotation2,rotation)
    rotation3.extend(rotation)
    
    rotation=[]
    
    
 
    if diago(rotation3,joueur,temp):
        #print("gg")
        return True
      
def joueur1biss(joueur,temp):       
    rotation1=[]
    rotation2=[]
    rotation3=[]
    joueur=joueur%2+1
    if zero (joueur,temp) or  un (joueur,rotation1,temp) or  deux(joueur,rotation1,rotation2,temp) or trois(joueur,rotation1,rotation2,rotation3,temp):
        print ("joueur 1 gagne")
        victoireblancs()

        
        global gagner
        gagner=True
        return True
    
    
def joueur2biss(joueur,temp):
    rotation1=[]
    rotation2=[]
    rotation3=[]
    

    if joueur ==2:
        if zero (joueur,temp) or  un (joueur,rotation1,temp) or  deux(joueur,rotation1,rotation2,temp) or trois(joueur,rotation1,rotation2,rotation3,temp):
            print("joueur 2 gagne")
            
            victoirenoirs()
            global gagner
            gagner=False
            return True



     
    







def etend(temp,plateaufin):
    
    for i in range (len(temp)):

        temp[i].extend(plateaufin[i])

        
def reuni ():
    temp=[]
    
    case1=copy.deepcopy(plateau1)
    case2=copy.deepcopy(plateau2)
    case3=copy.deepcopy(plateau3)
    case4=copy.deepcopy(plateau4)
    
    etend (case1,case3)
    etend (case2,case4)
    temp.extend(case1)
    temp.extend(case2)
    print(temp)
    #temp1=copy.deepcopy(temp)
    player=2
    


    if joueur2(player,temp) and joueur1(player,temp) or joueur2(player,temp) and joueur2bis(player,temp) or joueur2(player,temp) and joueur1bis(player,temp) or joueur2(player,temp) and joueur2biss(player,temp) or joueur2(player,temp) and joueur1biss(player,temp):
        
        global execo
        execo=True
        return execo
    elif joueur1(player,temp) and joueur2(player,temp) or joueur1(player,temp) and joueur2bis(player,temp) or joueur1(player,temp) and joueur1bis(player,temp) or joueur1(player,temp) and joueur2biss(player,temp) or joueur1(player,temp) and joueur1biss(player,temp): 
        global execo
        execo=True
        return execo
    elif joueur2bis(player,temp) and joueur2(player,temp) or joueur2bis(player,temp) and joueur1(player,temp) or joueur2bis(player,temp) and joueur1bis(player,temp) or joueur2bis(player,temp) and joueur2biss(player,temp) or joueur2bis(player,temp) and joueur1biss(player,temp):
        global execo
        execo=True
        return execo
    elif joueur1bis(player,temp) and joueur2(player,temp) or joueur1bis(player,temp) and joueur1(player,temp) or joueur1bis(player,temp) and joueur2bis(player,temp) or joueur1bis(player,temp) and joueur2biss(player,temp) or joueur1bis(player,temp) and joueur1biss(player,temp):
        global execo
        execo=True
        return execo
    elif joueur2biss(player,temp) and joueur2(player,temp) or joueur2biss(player,temp) and joueur1(player,temp) or joueur2biss(player,temp) and joueur2bis(player,temp) or joueur2biss(player,temp) and joueur1bis(player,temp) or joueur2biss(player,temp) and joueur1biss(player,temp):
        global execo
        execo=True
        return execo
    elif joueur1biss(player,temp) and joueur2(player,temp) or joueur1biss(player,temp) and joueur1(player,temp) or joueur1biss(player,temp) and joueur2bis(player,temp) or joueur1biss(player,temp) and joueur1bis(player,temp) or joueur1biss(player,temp) and joueur2biss(player,temp):
        global execo
        execo=True
        return execo
    elif joueur2bis(player,temp) or joueur2biss(player,temp) or joueur2(player,temp) or joueur1biss(player,temp) or joueur1bis(player,temp) or joueur1(player,temp):
        print("gg")
        son.play()
        global fin
        fin=True
        return fin

        
       

    

def tourneplateau (plateau):
    for i in range (len(plateau)):
        plateau[i].reverse()
        tourne=plateau
    return plateau
    
def rotationgauche(plateau,rotation):
    colone=[]
    ligne=[]

    tourneplateau(plateau)
    for i in range (len(plateau)):
        
        colone.append([])
        
        
        ligne.append(plateau[i])      #ne sert apparament a rien
        for j in range (len(plateau[i])):
            colone[i].append(plateau[j][i])
            
    for i in range (len(colone)):
        

        rotation.append(colone[i])
        
    return rotation



#afficheplateau(plateau1)

def rotationdroite(plateau,rotation):
    colone=[]
    ligne=[]

    for i in range (len(plateau)):
        colone.append([])
        
        #ligne.append(plateau[i])      #ne sert apparament a rien
        for j in range (len(plateau[i])):
            colone[i].append(plateau[j][i])
            
    for i in range (len(colone)):
        

        rotation.append(colone[i])
        rotation[i].reverse()
    
    return rotation


def graphplateau():
## fond du plateau
    pygame.draw.rect(maSurface1,GRIS,(100,100,350,350))
    posy=140
    posx=140
    
##1ère case
    pygame.draw.rect(maSurface1,BLEUFOND,(110,110,160,160))
    posy=135
    posx=135

    for x in range (3):
        for y in range (3):          
            pygame.draw.circle(maSurface2,BLEUTROU,(posx,posy),17,0)
            posx+=55
        posy+=55
        posx=135
        
##2ème case
    pygame.draw.rect(maSurface1,BLEUFOND,(110,280,160,160))
    posy=305
    posx=135
    for x in range (3):
        for y in range (3):          
            pygame.draw.circle(maSurface2,BLEUTROU,(posx,posy),17,0)
            posx+=55
        posy+=55
        posx=135

##3ème case
    pygame.draw.rect(maSurface1,BLEUFOND,(280,110,160,160))
    posy=135
    posx=305

    for x in range (3):
        for y in range (3):          
            pygame.draw.circle(maSurface2,BLEUTROU,(posx,posy),17,0)
            posx+=55
        posy+=55
        posx=305

##4ème case
    pygame.draw.rect(maSurface1,BLEUFOND,(280,280,160,160))
    posy=305
    posx=305

    for x in range (3):
        for y in range (3):          
            pygame.draw.circle(maSurface2,BLEUTROU,(posx,posy),17,0)
            posx+=55
        posy+=55
        posx=305
        



def plateaufull(liste):
    s=0
    for i in range(3):
        if 0 not in liste[i] :
            s=s+1
    if s == 3:
        return True
    

            
def affichepion():
    for i in range(3):
        for j in range(3):
            if plateau1[j][i] == 0:
                pygame.draw.circle(maSurface2,BLEUTROU,(135+i*55,135+j*55),17,0)
            if plateau1[j][i] == 1:
                pygame.draw.circle(maSurface2,BLANC,(135+i*55,135+j*55),17,0)
            if plateau1 [j][i]==2:
                pygame.draw.circle(maSurface2,NOIR,(135+i*55,135+j*55),17,0)

            if plateau2[j][i] == 0:
                pygame.draw.circle(maSurface2,BLEUTROU,(135+i*55,305+j*55),17,0)
            if plateau2[j][i] == 1:
                pygame.draw.circle(maSurface2,BLANC,(135+i*55,305+j*55),17,0)
            if plateau2 [j][i]==2:
                pygame.draw.circle(maSurface2,NOIR,(135+i*55,305+j*55),17,0)
                

            if plateau3[j][i] == 0:
                pygame.draw.circle(maSurface2,BLEUTROU,(305+i*55,135+j*55),17,0)
            if plateau3[j][i] == 1:
                pygame.draw.circle(maSurface2,BLANC,(305+i*55,135+j*55),17,0)
            if plateau3 [j][i]==2:
                pygame.draw.circle(maSurface2,NOIR,(305+i*55,135+j*55),17,0)

            if plateau4[j][i] == 0:
                pygame.draw.circle(maSurface2,BLEUTROU,(305+i*55,305+j*55),17,0)
            if plateau4[j][i] == 1:
                pygame.draw.circle(maSurface2,BLANC,(305+i*55,305+j*55),17,0)
            if plateau4 [j][i]==2:
                pygame.draw.circle(maSurface2,NOIR,(305+i*55,305+j*55),17,0)
def plein(plateau1,plateau2,plateau3,plateau4):
    if plateaufull(plateau1) and plateaufull(plateau2) and plateaufull(plateau3) and plateaufull(plateau4):
        global execo
        execo=True
def tour (player):
    if player==1:
        tourdesblancs()
        
        print("AU TOUR DU JOUEUR 1")
    elif player==2:
        
        print("AU TOUR DU JOUEUR 2")

def acceuil():
       
    exec(open("accueil.py").read())
def sauvegarde():
    global plateau1
    global plateau2
    global plateau3
    global plateau4
    global cptnoir
    global cptblanc
    global joueur
    global nbrdepion
    
    marshal.dump(cptnoir, open("IAscptnoir", 'wb'))
    marshal.dump(cptnoir, open("IAscptblanc", 'wb'))
    marshal.dump(plateau1, open("IAsplateau1", 'wb'))
    marshal.dump(plateau2, open("IAsplateau2", 'wb'))
    marshal.dump(plateau3, open("IAsplateau3", 'wb'))
    marshal.dump(plateau4, open("IAsplateau4", 'wb'))
    marshal.dump(joueur, open("IAsjoueur", 'wb'))
    marshal.dump(nbrdepion, open("IAsnbrdepion", 'wb'))

basta=1
     
gagner=True              
inProgress =True
graphplateau()
gagne=False   
player=2
nbrdepion=4
joueur = 1
cptblanc=0
cptnoir=0
fin=False
execo=False
debut()
c=1
while inProgress:
    
    for event in pygame.event.get():
        
        if event.type == QUIT:
            inProgress = False

        if event.type == MOUSEBUTTONDOWN:
            X,Y = event.pos
            if 572 < X < 800 and 567 < Y < 631:
                print("pk")
                
                acceuil()
        
                
        
            #matchnul()   
        if gagne==False and fin==False and execo==False and joueur==1:
            sauvegarde1()
            #print("je suis au mauais endroit ")
            
            
            if event.type == MOUSEBUTTONDOWN and gagne==False and fin==False and execo==False and joueur==1:
                X,Y = event.pos
                if 592 < X < 800 and 149 < Y < 208:
                    print("sauvegarde")
                    sauvegardequibouge()
                    sauvegarde()
                if 580 < X < 800 and 230 < Y < 290:
                    print("je suis sur recommencer")
                    recommencer()
                
                if joueur==1:    
                    for i in range(3):
                        for j in range(3):                   
                            
                            if plateau1[j][i] == 0:                               
                                if (110+i*55) < X < (110+(i+1)*55) and (110+j*55) < Y < (110+(j+1)*55) and not plateaufull(plateau1):                            
                                    if joueur == 1:                                      
                                        plateau1[j][i] = 1
                                        
                                        affichepion()
                                        reuni()
                                        if fin==False:
                                            fleche()
                                            tournerplat()
                                        
                                            gagne=True                                
                                     

                                        
                            if plateau2[j][i] == 0:
                                if (110+i*55) < X < (110+(i+1)*55) and (280+j*55) < Y < (280+(j+1)*55) and not plateaufull(plateau2):
                                    if joueur == 1:                                
                                        plateau2[j][i] = 1
                                        affichepion()
                                        reuni()
                                        if fin==False:
                                            fleche()
                                            tournerplat()
                                            gagne=True 
                                   
                            if plateau3[j][i]==0:
                                if (280+i*55) < X < (280+(i+1)*55) and (110+j*55) < Y < (110+(j+1)*55) and not plateaufull(plateau3):
                                    if joueur == 1:
                                        plateau3[j][i] = 1
                                        affichepion()
                                        reuni()
                                        if fin==False:
                                            fleche()
                                            tournerplat()
                                            gagne=True 
                                    
                            if plateau4[j][i] == 0:
                                if (280+i*55) < X < (280+(i+1)*55) and (280+j*55) < Y < (280+(j+1)*55) and not plateaufull(plateau4):
                                    if joueur == 1:
                                        plateau4[j][i] = 1
                                        
                                        affichepion()
                                        reuni()
                                        if fin==False :
                                            fleche()
                                            tournerplat()
                                            gagne=True 
                                
        if joueur==2 and gagne==False and fin==False and execo==False:
            print("ca rentre la")
            a=randint(1,4)
            
            global basta
            basta=1
           
            
                    
            if a==1 and not plateaufull(plateau1):
                global basta
                while basta==1:
                    i=randint(0,2)
                    j = randint(0,2)
                    print(i)
                    print(j)
                    
                    if plateau1[j][i] == 0:
                        global basta
                        basta=2
                        plateau1[j][i] = 2
                                                
                        affichepion()
                        reuni()
                        print(fin)
                        if fin==False:
                            fleche()
                            tournerplat()
                            gagne=True
                            print(gagne)
                    else:
                        basta=1
            if a==2 and not plateaufull(plateau2):
                global basta
                while basta==1:
                    i=randint(0,2)
                    j = randint(0,2)
                    print(i)
                    print(j)
                    
                    if plateau2[j][i] == 0:
                        global basta
                        basta=2
                        plateau2[j][i] = 2
                                                
                        affichepion()
                        reuni()
                        print(fin)
                        if fin==False:
                            fleche()
                            tournerplat()
                            gagne=True
                            print(gagne)
                    else:
                        basta=1
            if a==3 and not plateaufull(plateau3):
                global basta
                while basta==1:
                    i=randint(0,2)
                    j = randint(0,2)
                    print(i)
                    print(j)
                    
                    if plateau3[j][i] == 0:
                        global basta
                        basta=2
                        plateau3[j][i] = 2
                                                
                        affichepion()
                        reuni()
                        print(fin)
                        if fin==False:
                            fleche()
                            tournerplat()
                            gagne=True
                            print(gagne)
                    else:
                        basta=1
            if a==4 and not plateaufull(plateau4):
                global basta
                while basta==1:
                    i=randint(0,2)
                    j = randint(0,2)
                    print(i)
                    print(j)
                    
                    if plateau4[j][i] == 0:
                        global basta
                        basta=2
                        plateau4[j][i] = 2
                                                
                        affichepion()
                        reuni()
                        print(fin)
                        if fin==False:
                            fleche()
                            tournerplat()
                            gagne=True
                            print(gagne)
                    else:
                        basta=1
            
                    
                    
                                                
                        
                                
        if gagne==True and fin==False and execo==False :
            
            if event.type == MOUSEBUTTONDOWN:
                X,Y = event.pos
                print(X,Y)
                if 592 < X < 800 and 149 < Y < 208:
                    print("test1")
                    passauvegarde1 ()
            if event.type == MOUSEBUTTONDOWN :
                X,Y = event.pos
                if 572 < X < 800 and 567 < Y < 631:
                    acceuil()
            
                
            if event.type == MOUSEBUTTONDOWN and joueur==1:
                
        
                posX,posY=event.pos
                print(posX,posY)
                if 580 < posX < 800 and 230 < posY < 290:
                    print("je suis sur recommencer")
                    recommencer()
                
                
                if 115 < posX < 210 and 45 < posY < 90: #fleche en haut à gauche
                    
                    rotation=[]
                    rotationdroite(plateau1,rotation)
                    plateau1=rotation                    
                    reuni()

                    
                    
                    plateau1=rotation                 
                    print("okay ca marche")
                    pasfleche()
                    affichepion()
                    if fin !=True:
                        if not plein(plateau1,plateau2,plateau3,plateau4):
                            global joueur
                            joueur=joueur%2+1
                            
                            tour (joueur)
                            gagne=False
                    
                if 41 < posX < 95 and 122 < posY < 217: #fleche à gauche en haut
                    
                    rotation=[]
                    rotationgauche(plateau1,rotation)
                    plateau1=rotation                    
                    reuni()
                    plateau1=rotation                                 
                    print("okay ca marche")
                    pasfleche()                    
                    affichepion()
                    if fin !=True:
                        if not plein(plateau1,plateau2,plateau3,plateau4):
                            global joueur
                            joueur=joueur%2+1
                            
                            tour (joueur)
                            gagne=False
                    
                if 42 < posX < 95 and 344 < posY < 431: #fleche en bas à gauche
                    
                    rotation=[]
                    rotationdroite(plateau2,rotation)
                    plateau2=rotation                    
                    reuni()
                    plateau2=rotation                    
                    print("okay ca marche")
                    pasfleche()                    
                    affichepion()
                    if fin !=True:
                        if not plein(plateau1,plateau2,plateau3,plateau4):
                            global joueur
                            joueur=joueur%2+1
                            
                            tour (joueur)
                            gagne=False
                    
                if 115 < posX < 223 and 459 < posY < 510: #fleche en bas à gauche
                    
                    rotation=[]
                    rotationgauche(plateau2,rotation)
                    plateau2=rotation                    
                    reuni()
                    plateau2=rotation                                                         
                    print("okay ca marche")
                    pasfleche()                    
                    affichepion()
                    if fin !=True:
                        if not plein(plateau1,plateau2,plateau3,plateau4):
                            global joueur
                            joueur=joueur%2+1
                            
                            tour (joueur)
                            gagne=False
                    
                if 324 < posX < 427 and 42 < posY < 90: #fleche en haut à droite
                    
                    rotation=[]
                    rotationgauche(plateau3,rotation)
                    plateau3=rotation                    
                    reuni()
                    plateau3=rotation                                                         
                    print("okay ca marche")
                    pasfleche()                    
                    affichepion()
                    if fin !=True:
                        if not plein(plateau1,plateau2,plateau3,plateau4):
                            global joueur
                            joueur=joueur%2+1
                            
                            tour (joueur)
                            gagne=False
                    
                if 456 < posX < 512 and 127 < posY < 226: #fleche à droite en haut 
                    
                    rotation=[]
                    rotationdroite(plateau3,rotation)
                    plateau3=rotation                    
                    reuni()
                    plateau3=rotation                                                         
                    print("okay ca marche")
                    pasfleche()                    
                    affichepion()
                    if fin !=True:
                        if not plein(plateau1,plateau2,plateau3,plateau4):
                            global joueur
                            joueur=joueur%2+1
                            
                            tour (joueur)
                            gagne=False
                    
                if 462 < posX < 514 and 337 < posY < 433: #fleche à droite en bas
                    
                    rotation=[]
                    rotationgauche(plateau4,rotation)
                    plateau4=rotation                    
                    reuni()
                    plateau4=rotation                                                        
                    print("okay ca marche")
                    pasfleche()                    
                    affichepion()
                    if fin !=True:
                        if not plein(plateau1,plateau2,plateau3,plateau4):
                            global joueur
                            joueur=joueur%2+1
                            
                            tour (joueur)
                            gagne=False
                    
                if 330 < posX < 432 and 461 < posY < 508: #fleche en bas à droite
                  
                    rotation=[]
                    rotationdroite(plateau4,rotation)
                    plateau4=rotation                    
                    reuni()
                    plateau4=rotation                                                         
                    print("okay ca marche")
                    pasfleche()
                    affichepion()
                    if fin !=True:
                        if not plein(plateau1,plateau2,plateau3,plateau4):
                            global joueur
                            joueur=joueur%2+1
                            
                            tour (joueur)

                            gagne=False
        if gagne==True and fin==False and execo==False and joueur==2:
            print("je sais pas quoi écrire")
        
            b=randint(1,8)
            if b==1: #fleche en haut à gauche
                
                rotation=[]
                rotationdroite(plateau1,rotation)
                plateau1=rotation                    
                reuni()

                
                
                plateau1=rotation                 
                print("okay ca marche")
                pasfleche()
                affichepion()
                if fin !=True:
                    if not plein(plateau1,plateau2,plateau3,plateau4):
                        joueur=joueur%2+1
                        
                        tour (joueur)
                        gagne=False
                
            if b==2: #fleche à gauche en haut
                
                rotation=[]
                rotationgauche(plateau1,rotation)
                plateau1=rotation                    
                reuni()
                plateau1=rotation                                 
                print("okay ca marche")
                pasfleche()                    
                affichepion()
                if fin !=True:
                    if not plein(plateau1,plateau2,plateau3,plateau4):
                        joueur=joueur%2+1
                        
                        tour (joueur)
                        gagne=False
                
            if b==3: #fleche en bas à gauche
                
                rotation=[]
                rotationdroite(plateau2,rotation)
                plateau2=rotation                    
                reuni()
                plateau2=rotation                    
                print("okay ca marche")
                pasfleche()                    
                affichepion()
                if fin !=True:
                    if not plein(plateau1,plateau2,plateau3,plateau4):
                        joueur=joueur%2+1
                        
                        tour (joueur)
                        gagne=False
                
            if b==4: #fleche en bas à gauche
                
                rotation=[]
                rotationgauche(plateau2,rotation)
                plateau2=rotation                    
                reuni()
                plateau2=rotation                                                         
                print("okay ca marche")
                pasfleche()                    
                affichepion()
                if fin !=True:
                    if not plein(plateau1,plateau2,plateau3,plateau4):
                        joueur=joueur%2+1
                        
                        tour (joueur)
                        gagne=False
                
            if b==5: #fleche en haut à droite
                
                rotation=[]
                rotationgauche(plateau3,rotation)
                plateau3=rotation                    
                reuni()
                plateau3=rotation                                                         
                print("okay ca marche")
                pasfleche()                    
                affichepion()
                if fin !=True:
                    if not plein(plateau1,plateau2,plateau3,plateau4):
                        joueur=joueur%2+1
                        
                        tour (joueur)
                        gagne=False
                
            if b==6: #fleche à droite en haut 
                
                rotation=[]
                rotationdroite(plateau3,rotation)
                plateau3=rotation                    
                reuni()
                plateau3=rotation                                                         
                print("okay ca marche")
                pasfleche()                    
                affichepion()
                if fin !=True:
                    if not plein(plateau1,plateau2,plateau3,plateau4):
                        
                        joueur=joueur%2+1
                        
                        tour (joueur)
                        gagne=False
                
            if b==7: #fleche à droite en bas
                
                rotation=[]
                rotationgauche(plateau4,rotation)
                plateau4=rotation                    
                reuni()
                plateau4=rotation                                                        
                print("okay ca marche")
                pasfleche()                    
                affichepion()
                if fin !=True:
                    if not plein(plateau1,plateau2,plateau3,plateau4):
                        
                        joueur=joueur%2+1
                        
                        tour (joueur)
                        gagne=False
                
            if b==8: #fleche en bas à droite
              
                rotation=[]
                rotationdroite(plateau4,rotation)
                plateau4=rotation                    
                reuni()
                plateau4=rotation                                                         
                print("okay ca marche")
                pasfleche()
                affichepion()
                if fin !=True:
                    if not plein(plateau1,plateau2,plateau3,plateau4):
                        
                        joueur=joueur%2+1
                        
                        tour (joueur)

                        gagne=False
            
        if fin==True:
            global c
            
             
            

            
            if gagner==True:
                if c ==1:
                    animvictoire()
                    global c
                    c=2
                victoireblancs()
                
                    
                
            if gagner==False:
                if c==1:
                    
                    animvictoire1()
                    global c
                    c=2
                victoirenoirs()
                
            if event.type == MOUSEBUTTONDOWN:
                X,Y = event.pos
                if 572 < X < 800 and 567 < Y < 631:
                    acceuil()
            if event.type == MOUSEBUTTONDOWN and gagner==True:
                
                posX,posY=event.pos
                print(posX,posY)
                if 580 < posX < 800 and 230 < posY < 290:
                    global cptblanc
                    global cptnoir
                    print(cptblanc)
                    cptblanc=cptblanc+1
                    print(cptblanc)
                    #sonvictoire.stop()
                    print("je suis sur recommencer")
                    compteur(cptblanc,cptnoir)
                    recommencer()
                    
                
            if event.type == MOUSEBUTTONDOWN and gagner==False:
                
        
                posX,posY=event.pos
                print(posX,posY)
                if 580 < posX < 800 and 230 < posY < 290:
                    #sonvictoire.stop()
                    print("je suis sur recommencer")
                    global cptnoir
                    global cptblanc
                    cptnoir=cptnoir+1
                    compteur(cptblanc,cptnoir)
                    recommencer()
                    
        if execo==True and fin==False:
            pasfleche()      
            matchnul()
            if event.type == MOUSEBUTTONDOWN:
                
        
                posX,posY=event.pos
                print(posX,posY)
                if 580 < posX < 800 and 230 < posY < 290:
                    print("je suis sur recommencer")
                    recommencer()            

                


    
        if event.type == QUIT:
            inProgress = False

        if event.type == KEYDOWN: # quitte aussi si tu appuies sur la touche ECHAP
            if event.key==K_ESCAPE:
                inProgress = False

    pygame.display.update()
    
pygame.quit()
