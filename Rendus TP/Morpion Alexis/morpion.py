import pygame, sys
from pygame.locals import *
pygame.init()
WIDTH=400
HEIGHT=328
maSurface = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Morpion')
imagegrenouille = pygame.image.load("grenouillemorpion.png")
imagesmiley = pygame.image.load("smiley.gif")
SIZE = 90

##### Jérémy ##### 
# Bouton recommencer
# Si tu le mets dans ta boucle de jeu, il recrée la police, le bouton et
# compagnie à chaque passage. Ca consomme des ressources pour rien.
fontObj = pygame.font.Font('freesansbold.ttf',14)
texteSurface = fontObj.render('Recommencer',True,(255,255,255),(0,0,0))
texteRect = texteSurface.get_rect()
texteRect.topleft = (295,30)
maSurface.blit(texteSurface,texteRect)

###############################
##### On fait un tableau  #####
###############################

def tableau():
    ligne=3
    colonne=3
    plateau=[]
    for i in range(ligne):
        plateau.append([])
        for j in range(colonne):
            plateau[i].append(0)

    return plateau

def afficheplateau(liste):
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            if plateau[i][j] == 0:
                joueur=0
            if plateau[i][j] == 1:
                joueur=1
            if plateau[i][j] == 2:
                joueur=2
                
plateau = tableau()       

afficheplateau(plateau)


##################################
##### On affiche le tableau  #####
##################################

joueur = 1          #le joueur 1 commence

inProgress = True

def graphplateau():
    pygame.draw.rect(maSurface,(255,255,255),(10,10,278,278))
    posy=13
    posx=13

    pygame.draw.rect(maSurface,(255,255,255),(10,10,278,278))
    posy=13
    posx=13

    for x in range (3):
        for y in range (3):          
            pygame.draw.rect(maSurface,(0,0,0),(posx,posy,90,90))
            posx+=91
        posy+=91
        posx=13
graphplateau()

########################
##### qui gagne ?  #####
########################

def quigagne (joueur, plateau):       
    for i in range(3):
        if plateau[0][i] == joueur and plateau[1][i] == joueur and plateau[2][i] == joueur:
            fontObj = pygame.font.Font('freesansbold.ttf',14)
            texteSurface = fontObj.render("joueur "+str(joueur)+" a gagné",True,(255,255,255),(0,0,0))
            texteRect = texteSurface.get_rect()
            texteRect.topleft = (15,310)
            maSurface.blit(texteSurface,texteRect)
            ##### Jérémy #####
            # J'ai transformé ta suite de if en elif pour que le programme ne
            # teste pas tous les cas. Si il recontre un cas valable, il sort.
            # De même, j'ai retourné un booléen. True si le joueur a gagné,
            # False à la fin, si le joueur n'a pas gagné
            return True
        elif plateau[i][0] == joueur and plateau[i][1] == joueur and plateau[i][2] == joueur:
            fontObj = pygame.font.Font('freesansbold.ttf',14)
            texteSurface = fontObj.render("joueur "+str(joueur)+" a gagné",True,(255,255,255),(0,0,0))
            texteRect = texteSurface.get_rect()
            texteRect.topleft = (15,310)
            maSurface.blit(texteSurface,texteRect)
            return True
        elif plateau[0][0] == joueur and plateau[1][1] == joueur and plateau[2][2] == joueur:
            fontObj = pygame.font.Font('freesansbold.ttf',14)
            texteSurface= fontObj.render("joueur "+str(joueur)+" a gagné",True,(255,255,255),(0,0,0))
            texteRect = texteSurface.get_rect()
            texteRect.topleft = (15,310)
            maSurface.blit(texteSurface,texteRect)
            return True
        elif plateau[0][2] == joueur and plateau[1][1] == joueur and plateau[2][0] == joueur:
            fontObj = pygame.font.Font('freesansbold.ttf',14)
            texteSurface = fontObj.render("joueur "+str(joueur)+" a gagné",True,(255,255,255),(0,0,0))
            texteRect = texteSurface.get_rect()
            texteRect.topleft = (15,310)
            maSurface.blit(texteSurface,texteRect)
            return True
        return False
           
########################
##### case vide ?  #####
########################
    
##def casevide(liste):       # ne sert apparament a rien 
##    for i in range (len(liste)):
##        for j in range (i):
##            if j == 0:
##                return True
##    return False
##  

##### Jérémy #####
# Booléen pour contrôler si un joueur a gagné. Voir plus bas.
gagne = False

while inProgress:
    
#############################
##### image pour jouer  #####
#############################

    for x1 in range(len(plateau)):
        for y1 in range(len(plateau)):
            if plateau[x1][y1] == 1:
                maSurface.blit(imagegrenouille,(y1*90+13+7,x1*90+13+2))
            elif plateau[x1][y1] == 2:
                maSurface.blit(imagesmiley,(y1*90+13+5,x1*90+13+4))
   
####################################
##### bouton pour recommencer  #####
####################################
    
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:            
            poseX, poseY = event.pos

######################
##### qui joue?  #####
######################
            
            y = int((poseX - 13) // SIZE)
            x = int((poseY - 13) // SIZE)

            ##### Jérémy #####
            # Ajout du booléen de contrôle de victoire. Si un joueur a gagné,
            # on ne peut plus ajouter de case.
            if x>=0 and x <len(plateau) and not gagne:
                if y>=0 and y <len(plateau[x]):

                    ##### Jérémy #####
                    # Ici tu faisais un "if quigagne(joueur,plateau):
                    #                       break"
                    # Ta fonction quigagne ne renvoie rien. Donc le if ne
                    # fonctionnait pas. De plus, ici le break ne sert à rien.
                    # Un break te sert à sortir de la boucle et la boucle que
                    # tu parcours est la boucle des évènements. Pas utile donc.
                    # Si tu regardes ta fonction quigagne, je retourne
                    # maintenant un booléen. Je le met dans une variable qui
                    # contrôle si un joueur à gagné.
                    
                    if joueur == 1 and plateau[x][y]==0:
                        plateau[x][y] = 1
                        gagne = quigagne(joueur,plateau)
                        joueur = 2
                    elif joueur == 2 and plateau[x][y]==0:
                        plateau[x][y] = 2
                        gagne = quigagne(joueur,plateau)
                        joueur = 1
    
######################################
##### appuyer bouton recommencer #####
######################################

            if poseX > texteRect.left and poseX < texteRect.right and poseY > texteRect.top and poseY < texteRect.bottom:
                pygame.draw.rect(maSurface,(255,255,255),(10,10,278,278))
                posy=13
                posx=13
                ##### Jérémy ######
                # Remise à zéro du booléen de contrôle de victoire et du joueur
                gagne = False
                joueur = 1                

################################
##### afficher cadrillage  #####
################################

                for x in range (3):
                    for y in range (3):          
                        pygame.draw.rect(maSurface,(0,0,0),(posx,posy,90,90))
                        posx+=91
                    posy+=91
                    posx=13
                
                plateau=tableau()

                ##### Jérémy #####
                # Ici j'ai supprimé le code qui recréait le bouton recommencer.
                # Il manquait une parenthèse qui faisait que tu ne pouvais
                # recommencer qu'une seule fois. De plus comme j'ai déjà
                # sorti ce code de la boucle (voir plus haut), pas besoin de le
                # remettre là.

##### Jérémy #####
# Ici j'ai suprimé la ligne "for event in pygame.event.get():"
# Tu parcours déjà la liste des évènements un peu plus haut. Pas besoin de le
# faire plusieurs fois. 
    
        if event.type == QUIT:
            inProgress = False

    pygame.display.update()
    
pygame.quit()
