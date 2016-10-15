import random, sys, pygame, time, copy, os, pickle
from pygame.locals import *
from fonction import *
  


table=[[["","",""],["","",""],["","",""]],[["","",""],["","",""],["","",""]],[["","",""],["","",""],["","",""]],[["","",""],["","",""],["","",""]]]
#table[cadrant][ligne][colonne]
#cadrants: 0|1
#          2|3



click=0             #Click incrémente les étapes de jeu : Si 0, fenetre d'acceuil du jeu, si 1 un joueur doit jouer, si 2 un joueur doit tourner un cadran
joueur=1            #Incrémentation du joueur(1 Blanc, 2 Noir)
coorX=0
coorY=0
check=0             #valeur return par les line/row/diag check
clickControle1=0    #Variable qui sert à vérifier si le joueur à cliqué sur un case libre pendant son tour(pour click=1)
clickControle2=0    #Variable qui sert à vérifier si le joueur à cliqué sur une flèche pendant le tour de rotation(pour click=2)


pygame.init()

#              R    G    B
WHITE      = (255, 255, 255)
BLACK      = (  0,   0,   0)
RED       = (  255, 25, 25)
RED2        = (  255,   0, 0)
GREY       = (176, 176, 176)

window_width = 1040     #Longueur de la fenêtre de jeux
window_height = 800     #Hauteur de la fenêtre de jeux
window = pygame.display.set_mode((window_width, window_height)) #Création Fenêtre
window.fill(GREY)                                               #Couleur Fond
pygame.display.set_caption('Pentago')                           #Nom Fenêtre
police=pygame.font.Font('freesansbold.ttf', 32)                 #Police Texte
texte3=police.render('Nouvelle Partie', True, BLACK, WHITE)
texte4=police.render('Sauvegarde Partie', True, BLACK, BLACK)
texteRect3 = texte3.get_rect()
texteRect4 = texte4.get_rect()
texteRect3.topleft=(150,470)
texteRect4.topleft=(620,470)
window.blit(texte3, texteRect3)
window.blit(texte4, texteRect4)




inProgress = True
while inProgress:
    if click==0:        #Affichage Graphique de l'acceuil

        fond1=pygame.image.load("FondStart.png")
        window.blit(fond1,(0,0))
        police=pygame.font.Font('freesansbold.ttf', 32)                 #Police Texte
        texte3=police.render('Nouvelle Partie', True, BLACK, WHITE)
        texte4=police.render('Sauvegarde Partie', True, BLACK, WHITE)
        texteRect3 = texte3.get_rect()
        texteRect4 = texte4.get_rect()
        texteRect3.topleft=(150,470)
        texteRect4.topleft=(600,470)
        window.blit(texte3, texteRect3)
        window.blit(texte4, texteRect4)
        pygame.draw.line(window, BLACK,(140,460),(408,460),3)
        pygame.draw.line(window, BLACK,(408,460),(408,508),3)
        pygame.draw.line(window, BLACK,(140,508),(408,508),3)
        pygame.draw.line(window, BLACK,(140,460),(140,508),3)
        
        pygame.draw.line(window, BLACK,(590,460),(903,460),3)
        pygame.draw.line(window, BLACK,(903,460),(903,508),3)
        pygame.draw.line(window, BLACK,(590,508),(903,508),3)
        pygame.draw.line(window, BLACK,(590,460),(590,508),3)
        
       
        
    if click==1:        #Affichage Graphique tour joueur doit poser un pion

        window.fill(GREY) 
        police=pygame.font.Font('freesansbold.ttf', 24)                 #Police Texte
        texte=police.render('Nouvelle Partie', True, BLACK, GREY)       #Texte 'Nouvelle Partie'
        texte2=police.render('Enregistrer Partie', True, BLACK, GREY)
        texte3=police.render('Quitter', True, BLACK, GREY)              #Texte 'Quitter'
        texteRect = texte.get_rect()            #Definition Encadrement Text
        texteRect2 = texte2.get_rect()
        texteRect3 = texte3.get_rect()
        texteRect.topleft=(770,92)              #Position Texte
        texteRect2.topleft=(770,122)
        texteRect3.topleft=(770,150)
        window.blit(texte, texteRect)           #Affichage du texte dans l'interface
        window.blit(texte2, texteRect2)
        window.blit(texte3,texteRect3)
        pygame.draw.rect(window, RED,(120,90,600,600))          #Plateau Pentago
        pygame.draw.line(window, GREY,(420,90),(420,690),2)     #Delimitation des cadrants
        pygame.draw.line(window, GREY,(120,390),(720,390),2)
        
        pygame.draw.rect(window, GREY,(245,20,65,65))           #Cache flèche pour placer le pion
        pygame.draw.rect(window, GREY,(725,210,65,65))
        pygame.draw.rect(window, GREY,(540,695,65,65))
        pygame.draw.rect(window, GREY,(50,510,65,65))
        pygame.draw.rect(window, GREY,(50,210,65,65))
        pygame.draw.rect(window, GREY,(540,20,65,65))
        pygame.draw.rect(window, GREY,(725,510,65,65))
        pygame.draw.rect(window, GREY,(245,695,65,65))

        pygame.draw.line(window, BLACK,(820,540),(961,540),3)
        pygame.draw.line(window, BLACK,(961,540),(961,601),3)
        pygame.draw.line(window, BLACK,(820,601),(961,601),3)
        pygame.draw.line(window, BLACK,(820,540),(820,601),3)
        
        affichage(table)
        affichageEcran(joueur,click,Vwin)
        
    if click==2:            #Affichage graphique tour joueur doit tourner un cadrant
            
        police=pygame.font.Font('freesansbold.ttf', 24)                 #Police Texte
        texte=police.render('Nouvelle Partie', True, BLACK, GREY)       #Texte 'Nouvelle Partie'
        texte2=police.render('Enregistrer Partie', True, BLACK, GREY)
        texte3=police.render('Quitter', True, BLACK, GREY)              #Texte 'Quitter'
        texteRect = texte.get_rect()                                    #Definition Encadrement Text
        texteRect2 = texte2.get_rect()
        texteRect3 = texte3.get_rect()
        texteRect.topleft=(770,92)                                      #Position Texte
        texteRect2.topleft=(770,122)
        texteRect3.topleft=(770,150)
        window.blit(texte, texteRect)           #Affichage du texte dans l'interface
        window.blit(texte2, texteRect2)
        window.blit(texte3, texteRect3)
        pygame.draw.rect(window, RED,(120,90,600,600))          #Plateau Pentago
        pygame.draw.line(window, GREY,(420,90),(420,690),2)     #Delimitation des cadrants
        pygame.draw.line(window, GREY,(120,390),(720,390),2)

        fond1=pygame.image.load("fleche1.jpg")                  #Postion/Affichage Flèche
        window.blit(fond1,(245,20))
        fond2=pygame.image.load("fleche2.jpg")
        window.blit(fond2,(725,210))  
        fond3=pygame.image.load("fleche3.jpg")
        window.blit(fond3,(540,695))
        fond4=pygame.image.load("fleche4.jpg")
        window.blit(fond4,(50,510))
        fond5=pygame.image.load("fleche5.jpg")
        window.blit(fond5,(50,210))
        fond6=pygame.image.load("fleche6.jpg")
        window.blit(fond6,(540,20))
        fond7=pygame.image.load("fleche7.jpg")
        window.blit(fond7,(725,510))
        fond8=pygame.image.load("fleche8.jpg")
        window.blit(fond8,(245,695))
        affichage(table)
        affichageEcran(joueur,click,Vwin)
        
    for event in pygame.event.get():
            if event.type == QUIT:
                inProgress = False
            
            if event.type == MOUSEBUTTONUP:
                    
                coorX,coorY=event.pos
                               #Toutes les fonctions si dessous sont apellées à chaque click, et chaque fonction s'éxecute selon le tour (le click) en cour, grace au "if" dans chacune des fonctions

                
                table,clickControle1=CCPJ(coorX,coorY,table,click,joueur)                                                                      #Check Click Position Jouée
                clickControle2=CCRC(coorX,coorY,table,click)                                                                            #Chek Click Rotation Cadrant
                Vwin=wincheck(table)                                                                                                    #Win Check (Vwin = Variable Win)
                joueur=TDJ(joueur,click,clickControle2,Vwin)                                                                                 #Tour De Jeux                                                                                                                                     
                a=Quit(coorX,coorY)                                                                                                     #Bouton Quitter
                table,click,joueur,clickControle1,clickControle2=NewGame(coorX,coorY,table,click,joueur,clickControle1,clickControle2)  #Nouvelle Partie
                Sauvegarde(table,click,coorX,coorY)                                                                                     #Enregistrer la partie
                table,click=JouerSauvegarde(table,click,coorX,coorY)                                                                    #Jouer les Sauvegarde
                print(table)

                if a==True:       #Test du bouton Quitter pour fermeture de la fenêtre
                    inProgress=False

                #Sert à changer les tours (les clicks) avec vérification du tour jouer    
                if click==1:
                    if clickControle1==1:
                        click=1
                        affichageEcran(joueur,click,Vwin)
                        
                    else:
                        click=2
                        affichageEcran(joueur,click,Vwin)
                  
                else:
                    if clickControle2==2:
                        click=2
                        clickControle=0
                        

                    else: 
                        click=1
                       
                       
                         
                affichage(table)
                         
    
    pygame.display.update()
        
pygame.quit()
        

pygame.quit()
sys.exit()


