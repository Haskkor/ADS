import pygame
import managerPlateau
import rotation
import alignement
from pygame.locals import *
#Couleur

WHITE = (255,255,255)
Blue  = (0  , 0 ,255)
GREEN = (255,255,255)
RED   = (255, 0 , 0 )
BLACK = (0  , 0 , 0 )
cCercle= (110,110,110) 
n = BLACK
pygame.init()


#Ouverture de la fenêtre Pygame

fenetre = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption('PENTAGO')

pygame.draw.rect(fenetre, Blue, (500,468,700,500))
pygame.draw.line(fenetre, n, (870,968),(870,470), 5)
pygame.draw.line(fenetre, n, (500,730),(1196,730), 5)

fond = pygame.image.load("fond.jpg").convert()
#fenetre.blit(fond, (200,250,))

fondP = pygame.image.load("fondT.jpg").convert()
fenetre.blit(fondP, (0,0))
fondPlateau = pygame.image.load("fondPlateau.jpg").convert_alpha()
#fenetre.blit(fondPlateau, (700,500,))
#Chargement et collage du fond


plateauT = managerPlateau.initPlateau(6)
managerPlateau.affichplateau(plateauT)
j = 1
n = 0

exp = "fondPion1.jpg"
tr = "perso.png"
fondCadran = "fondCadran.png"
fondPion2 = "fondPion2.png"
fond_Pion= exp
perso = pygame.image.load(exp).convert_alpha()
position_perso = perso.get_rect()
pygame.display.flip()
#BOUCLE INFINIE

while True:
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        
              
                if event.type == MOUSEBUTTONDOWN and event.button == 1: 
                        event.pos[1]
                        event.pos[0]
                        pion(j)
                        if j == 1:
                                j = 2
                                
                                print(event.pos[0], event.pos[1])
                                           
                        elif j == 2:
                               
                                j = 1
                                print(event.pos[0], event.pos[1])
                                        
                
                #if event.type == MOUSEBUTTONDOWN and event.button == 3 and event.pos[1] < 100:
                        #pygame.draw.circle(fenetre, RED, (150,130),10)
                #if event.type == MOUSEBUTTONDOWN and event.button == 3 and event.pos[1] < 200:
                        #pygame.draw.circle(fenetre, RED, (630,397),10)
        
                
#GRAPHISME
        
        def cercle_a(n, color, m, e, i):
                while n < 3 :
                        if n != 3:
                                q = 0
                                while q != 6:
                                
                                        pygame.draw.circle(fenetre, color, (m,e),i)
                                        q += 1
                                        e += 89                
                        m += 130
                        e = 490
                        n += 1


        def cercle_b(n, color, m, e, i):
                while n < 3 :
                        if n != 3:
                                q = 0
                                while q != 6:
                                
                                        pygame.draw.circle(fenetre, color, (m,e),i)
                                        q += 1
                                        e += 89                      
                        m += 130
                        e = 490
                        n += 1
        def pion(color):
                pygame.draw.circle(fenetre, color, (550,490),10)

        
        def fondCadrann(fondCadran, x, y):
                perso = pygame.image.load(fondCadran).convert_alpha()
                position_perso = perso.get_rect()
                i = 0
                while i < 2:
                        perso = pygame.image.load(fondCadran).convert_alpha()
                        position_perso = perso.get_rect()
                        position_perso = position_perso.move(x,y)
                        fenetre.blit(perso, position_perso)
                        i += 1
                        y += 220
                        
                x = 810
                y = 250
                z = 0
                while z < 2:
                        
                        perso = pygame.image.load(fondCadran).convert_alpha()
                        position_perso = perso.get_rect()
                        position_perso = position_perso.move(x,y)
                        fenetre.blit(perso, position_perso)
                        z += 1
                        
                        y += 220
        def affiche(moitie, listes1,x,y,j):
                listeTs2 = [[0] * 3 for i in range(3)]
                for i in range(moitie):
                        for j in range(moitie):
                                if listes1[i][j] == 1:
                                        perso = pygame.image.load(tr).convert_alpha()
                                        position_perso = perso.get_rect()
                                        position_perso = position_perso.move(x,y)
                                        fenetre.blit(perso, position_perso)
                                        y += 70
                for i in range(moitie):
                        for j in range(moitie):
                                if listes1[i][j] == 0:
                                        perso = pygame.image.load(fondPion2).convert_alpha()
                                        position_perso = perso.get_rect()
                                        position_perso = position_perso.move(x,y)
                                        fenetre.blit(perso, position_perso)
                                        y += 200
                                                 
                                                                
        def dessinPion(exp,tr,x,y,j, listes, numCadran, boole):
                i = 0
                t = 0
                
                m = 6
                moitie = int (m / 2)
    
                listeCadran= [[0] * 3 for i in range(moitie)]
                if numCadran == 1:
                        for i in range(moitie):
                            for j in range(moitie):
                                listeCadran[i][j] = listes[i][j]
                                colonnePion(x,y,j, listes,numCadran)

                if numCadran == 2:
                            t = 0
                            for i in range(moitie, n):
                                u = 0
                                for j in range(moitie):
                                    listeCadran[t][u] = listes[i][j]
                                    u = u + 1
                                t = t + 1
                                affiche(3, listeCadran, x, y,j)
       
                if numCadran == 3:
                        t = 0
                        for i in range(moitie, n):
                                u = 0
                                for j in range(moitie, n):
                                        listeCadran[t][u] = listes[i][j]
                                        u += 1
                                t += 1
                                affiche(3, listeCadran, x, y,j)
                if numCadran == 4:
                        t = 0
                        for i in range(moitie):
                                u = 0
                                for j in range(moitie, n):
                                        listeCadran[t][u] = listes[i][j]
                                        u += 1
                                t += 1
                                affiche(3, listeCadran, x, y,j)
                
                
 
        
                        
        def lignePion(n,j, x, y, fond_Pion): 
                n = 0
                while n < 2:
                        if n == 0:
                                n = 0 
                                while n < 3:
                                        fond_Pion = tr
                                        colonnePion(n,j,x,y, fond_Pion)
                                        y+= 75
                                        n += 1
                        if x <= 1023 and y <= 625:
                                fond_Pion = exp                
                        y = 475
                        if n == 1:
                                n = 0
                                while n < 3:
                                        colonnePion(n,j,x,y, fond_Pion)
                                        y+= 75
                                        n+=1
                        n+=1
                n = 0
                
                while n < 2:
                        if n == 0:
                                n = 0 
                                while n < 3:
                                        colonnePion(n,j,x,y, fond_Pion)
                                        y+= 75
                                        n += 1
                                        
                        x = 529
                        if n == 1:
                                n = 0
                                while n < 3:
                                        colonnePion(n,j,x,y, fond_Pion)
                                        y+= 75
                                        n+=1
                        n+=1
                                        
        def colonnePion(n,j,x,y, fond_Pion):
                n = 0
                while n < 3:
                        if n == 0:
                                i = 0
                                while i < 3:
                                        image(j,x,y, fond_Pion)
                                        i += 1
                                        x += 100
                        if n == 1:
                                i = 0
                                while i < 3:
                                        image(j,x,y, fond_Pion)
                                        i += 1
                                        x += 100
                        n +=1
                n = 0
                
                
        def image(j,x,y, fond_Pion):
                perso = pygame.image.load(fond_Pion).convert_alpha()
                position_perso = perso.get_rect()
                position_perso = position_perso.move(x,y)
                fenetre.blit(perso, position_perso)
                test = position_perso
                print(test)
# PLACEMENT DE PION
       
       
        def casevide(liste):
            for i in liste:
                for j in i:
                    if j == 0:
                        return True
                    return False


        #Rafraichissement
               
        fenetre.blit(fondP, (0,0))
        fondCadrann(fondCadran, 505, 250)
        #testvoir(exp,tr,523,257,j, plateauT)
        lignePion(n, j, 523, 257, fond_Pion)
        #lignePion(0,exp,tr,523,320,j, listes)
        #fenetre.blit(fond, (200,250))
        #pygame.draw.rect(fenetre, Blue, (500,468,700,500))
        #fenetre.blit(fondPlateau, (700,500,))
        #pygame.draw.line(fenetre, n, (870,968),(870,470), 5)
        #pygame.draw.line(fenetre, n, (500,730),(1196,730), 5)
        #dessinPion(exp, tr, 523, 257,j, listes)
     
        pygame.display.update()
        
        
