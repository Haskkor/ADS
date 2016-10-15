import pygame
from pygame.locals import *
#opérations sur la table


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
    

def convert(liste):
    #Renvoie une table à deux dimensions [ligne][colonne] à partir de la table à cadrants
        
        tampon=[["","","","","",""],["","","","","",""],["","","","","",""],["","","","","",""],["","","","","",""],["","","","","",""]]
    
        for v in range(0,6):
                for w in range(0,6):
                        
                        if w<3 and v<3:
                                tampon[v][w]=liste[0][v][w]
                        if w>=3 and v<3:
                                tampon[v][w]=liste[1][v][w-3]
                        if w<3 and v>=3:
                                tampon[v][w]=liste[2][v-3][w]
                        if w>=3 and v>=3:
                                tampon[v][w]=liste[3][v-3][w-3]
		    			
        return tampon


def linecheck(table,line):
    check=0
    
    if table[line][0]==table[line][1] and table[line][0]==table[line][2] and table[line][0]==table[line][3] and table[line][0]==table[line][4] and table[line][0]!="":
        check=table[line][0]
		
    elif table[line][1]==table[line][2] and table[line][1]==table[line][3] and table[line][1]==table[line][4] and table[line][1]==table[line][5] and table[line][1]!="":
    	check=table[line][1]
		
    return check


def rowcheck(table, row):#copy of above for now
    
	if table[row][0]==table[row][1] and table[row][0]==table[row][2] and table[row][0]==table[row][3] and table[row][0]==table[row][4] and table[row][0]!="":
		check=table[row][0]
		
	elif table[row][1]==table[row][2] and table[row][1]==table[row][3] and table[row][1]==table[row][4] and table[row][1]==table[row][5] and table[row][1]!="":
		check=table[row][1]
		
def diagcheck(table, diag):
    
	#valeur de diag:
	#deux diagonales sont plus grandes que 5: les plus grandes et celles juste à coté (petites)
	#pour les diagonales partant en haut à gauche: la grande est 1, la petite inférieure est 2 et la petite supérieure est 3
	#pour les diagonales partant en bas à droite: la grande est 4, la petite inférieure est 5 et la petite supérieure est 6
	
	check=0
	if diag==1:
		if table[0][0]==table[1][1] and table[0][0]==table[2][2] and table[0][0]==table[3][3] and table[0][0]==table[4][4] and table[0][0]!="":
			check=table[0][0]
			
		elif table[5][5]==table[1][1] and table[5][5]==table[2][2] and table[5][5]==table[3][3] and table[5][5]==table[4][4] and table[5][5]!="":
			check=table[5][5]
	
	elif diag==2:
		if table[1][0]==table[2][1] and table[1][0]==table[3][2] and table[1][0]==table[4][3] and table[1][0]==table[5][4] and table[1][0]!="":
			check=table[1][0]
			
	elif diag==3:
		if table[0][1]==table[1][2] and table[0][1]==table[2][3] and table[0][1]==table[3][4] and table[0][1]==table[4][5] and table[0][1]!="":
			check=table[0][1]
			
	elif diag==4:
		if table[0][5]==table[1][4] and table[0][5]==table[2][3] and table[0][5]==table[3][2] and table[0][5]==table[4][1] and table[0][5]!="":
			check=table[0][0]
			
		elif table[5][0]==table[1][4] and table[5][0]==table[2][3] and table[5][0]==table[3][2] and table[5][0]==table[4][1] and table[5][0]!="":
			check=table[5][5]
	
	elif diag==5:
		if table[1][5]==table[2][4] and table[1][5]==table[3][3] and table[1][5]==table[4][2] and table[1][5]==table[5][1] and table[1][5]!="":
			check=table[1][5]
			
	elif diag==6:
		if table[0][4]==table[1][3] and table[0][4]==table[2][2] and table[0][4]==table[3][1] and table[0][4]==table[4][0] and table[0][4]!="":
			check=table[0][4]
			
	return check


def wincheck(table):
	#input table à 3 dimensions
	#output la valeur ju joueur gagnant ou 3 si ex-equo ou 4 si plateau plein sans vainqueur
    
	wincount=0
	win1=0
	win2=0
	extra=0
	tampon=convert(table)
	for i in range(6):
		if linecheck(tampon,i)!=0:
			wincount=wincount+1
			
			if wincount<2 and win1==0:
				win1=linecheck(tampon,i)
				
			elif wincount==2 and win1!=linecheck(tampon,i):
				win2=linecheck(tampon,i)
				
	for i in range(6):
		if rowcheck(tampon,i)!=0:
			wincount=wincount+1
			
			if wincount<2 and win1==0:
				win1=rowcheck(tampon,i)
				
			elif wincount==2 and win1!=rowcheck(tampon,i):
				win2=rowcheck(tampon,i)
	for i in range(6):
		if diagcheck(tampon,i)!=0:
			wincount=wincount+1
			
			if wincount<2 and win1==0:
				win1=diagcheck(tampon,i)
				
			elif wincount==2 and win1!=diagcheck(tampon,i):
				win2=diagcheck(tampon,i)
				
	if win1!=0 and win2==0:
		return win1
	elif win1!=0 and win2!=0:
		return 3
	for i in range(6):
		for j in range(6):
			if tampon[i][j]=="":
				extra=1
	if extra==1:
		return 0
	else:
		return 4


def convert(liste):
    #Renvoie une table à deux dimensions [ligne][colonne] à partir de la table à cadrants
        
        tampon=[["","","","","",""],["","","","","",""],["","","","","",""],["","","","","",""],["","","","","",""],["","","","","",""]]
    
        for v in range(0,6):
                for w in range(0,6):
                        
                        if w<3 and v<3:
                                tampon[v][w]=liste[0][v][w]
                        if w>=3 and v<3:
                                tampon[v][w]=liste[1][v][w-3]
                        if w<3 and v>=3:
                                tampon[v][w]=liste[2][v-3][w]
                        if w>=3 and v>=3:
                                tampon[v][w]=liste[3][v-3][w-3]
		    			
        return tampon

def rotate(table,liste,cadrant,sens):
        #tourne un cadrant un sens
        #sens trigo=1
        #sens anti trigo=0
        
	
        if sens==1:
            a=3
        elif sens==0:
            a=1
	
        for i in range(0,a):
            tampon=[["","",""],["","",""],["","",""]]
            tampon[0][0]=liste[cadrant][2][0]
            tampon[2][0]=liste[cadrant][2][2]
            tampon[2][2]=liste[cadrant][0][2]
            tampon[0][2]=liste[cadrant][0][0]
		
            tampon[0][1]=liste[cadrant][1][0]
            tampon[1][0]=liste[cadrant][2][1]
            tampon[2][1]=liste[cadrant][1][2]
            tampon[1][2]=liste[cadrant][0][1]
		
            tampon[1][1]=liste[cadrant][1][1]
            
            table[cadrant]=tampon




def CCPJ(coorX,coorY,table,click,joueur):    #Check Click Position Joué
    clickControle1=1        #Variable qui sert à vérifié si le joueur à cliqué sur un case libre pendant son tour(pour click=1)
    posel=0
    posec=0

    if click==1:  #Check de la position joué 
        
            if coorX>=120.00 and coorY>=90.00 and coorX<420.00 and coorY<390.00:
                cadrant=0
                posel,posec=0, 0
                print(cadrant)
                

            elif coorX>420.00 and coorY>=90.00 and coorX<=720.00 and coorY<390.00:
                cadrant=1
                posel,posec=0, 1
                print(cadrant)

            elif coorX>=120.00 and coorY>390.00 and coorX<420.00 and coorY<=690.00:
                cadrant=2
                posel,posec=1,0
                print(cadrant)

            elif coorX>420.00 and coorY>390.00 and coorX<=720.00 and coorY<=690.00:
                cadrant=3
                posel,posec=1,1
                print(cadrant)
                print(posel," ",posec)

            else:
                return table, 1

            for i in range(0,3):
                for j in range(0,3):     #Place le pion du joueur dans la case clické

                    if table[cadrant][i][j]=="": 
                        if coorX>=120+j*100+posec*300 and coorX<220+j*100+posec*300 and coorY>=90+i*100+posel*300 and coorY<190+i*100+posel*300:
        
                            table[cadrant][i][j]=joueur
                            clickControle1=0
                            print(table)
                            break
                        

            return table, clickControle1
    else:
            return table, clickControle1


def CCRC(coorX,coorY,table,click):    #Check Click Rotation Cadrant
        clickControle2=0      #Variable qui sert à vérifié si le joueur à cliqué sur une flèche pendant le tour de rotation(pour click=2)
        liste=table
        if click==2:
        
            if coorX>=245 and coorX<=310 and coorY>=20 and coorY<=85:
                rotate(table,liste, 0, 1)
                return 0
                        
            elif coorX>=725 and coorX<=790 and coorY>=210 and coorY<=275:
                rotate(table,liste,1, 1)
                return 0

            elif coorX>=540 and coorX<=605 and coorY>=695 and coorY<=760:
                rotate(table,liste, 3, 1)
                return 0
                
            elif coorX>=50 and coorX<=110 and coorY>=510 and coorY<=575:
                rotate(table,liste, 2, 1)
                return 0
                
            elif coorX>=50 and coorX<=110 and coorY>=210 and coorY<=275:
                rotate(table,liste, 0, 0)
                return 0

            elif coorX>=540 and coorX<=605 and coorY>=20 and coorY<=85:
                rotate(table,liste, 1, 0)
                return 0
            
            elif coorX>=725 and coorX<=790 and coorY>=510 and coorY<=575:
                rotate(table,liste, 3, 0)
                return 0

            elif coorX>=245 and coorX<=310 and coorY>=695 and coorY<=760:
                rotate(table,liste, 2, 0)
                return 0
            
            else:
                clickControle2=2
                print("totoclick")
                return clickControle2
            
        return 0

def checkForQuit():
    for event in pygame.event.get((QUIT, KEYUP)):
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
                   
        

def affichage(table):
    #On test les valeurs des cases dans notre liste pour mettre la couleur correspondante
        table=convert(table)
        
        for i in range(0,6):            #Affichage Rond Plateau
            for j in range(0,6):
        
                if table[i][j]== "":
                    pygame.draw.circle(window, RED2,(170+j*100,140+i*100),25)

                elif table[i][j]==1:
                    pygame.draw.circle(window, WHITE,(170+j*100,140+i*100),25)

                elif table[i][j]==2:
                    pygame.draw.circle(window, BLACK,(170+j*100,140+i*100),25)



def affichageEcran(joueur, click,Vwin):
    #Cette fonction s'occupe de l'affichage dans l'écran à droite
    
    #print("Vwin base : ", Vwin)
    if click==1 and joueur==1:                              #Tour des blancs
        police=pygame.font.Font('freesansbold.ttf', 22)
        texteB=police.render('Au tour des', True, BLACK,GREY)
        texteB2=police.render('Blanc',True,BLACK,GREY)
        texteRectB=texteB.get_rect()
        texteRectB2=texteB2.get_rect()
        texteRectB.topleft=(830,550)
        texteRectB2.topleft=(860,572)
        window.blit(texteB, texteRectB)
        window.blit(texteB2,texteRectB2)

    if click==1 and joueur==2:                              #Tour des noirs
        police=pygame.font.Font('freesansbold.ttf', 22)
        texteN=police.render('Au tour des', True, BLACK,GREY)
        texteN2=police.render('Noir',True,BLACK,GREY)
        texteRectN=texteN.get_rect()
        texteRectN2=texteN2.get_rect()
        texteRectN.topleft=(830,550)
        texteRectN2.topleft=(865,572)
        window.blit(texteN, texteRectN)
        window.blit(texteN2,texteRectN2)

    if click==2:                                            #Tournez un cadran
        police=pygame.font.Font('freesansbold.ttf', 22)
        texteC=police.render('Tournez un ',True,BLACK,GREY)
        texteC2=police.render('Cadran',True,BLACK,GREY)
        texteRectC=texteC.get_rect()
        texteRectC2=texteC2.get_rect()
        texteRectC.topleft=(830,550)
        texteRectC2.topleft=(849,572)
        window.blit(texteC,texteRectC)
        window.blit(texteC2,texteRectC2)

    if Vwin==1:                                             #Victoire des blanc
        #print("Vwin : ",Vwin)
        police=pygame.font.Font('freesansbold.ttf', 22)
        texteWB1=police.render(' Les blanc ',True,BLACK,GREY)
        texteWB2=police.render('Gagnent ',True,BLACK,GREY)
        texteRectWB1=texteWB1.get_rect()
        texteRectWB2=texteWB2.get_rect()
        texteRectWB1.topleft=(840,550)
        texteRectWB2.topleft=(845,572)
        window.blit(texteWB1, texteRectWB1)
        window.blit(texteWB2,texteRectWB2)
        
    if Vwin==2:                                             #Victoire des noirs
        #print("Vwin : ",Vwin)
        police=pygame.font.Font('freesansbold.ttf', 22)
        texteWN1=police.render(' Les noirs  ',True,BLACK,GREY)
        texteWN2=police.render('Gagnent  ',True,BLACK,GREY)
        texteRectWN1=texteWN1.get_rect()
        texteRectWN2=texteWN2.get_rect()
        texteRectWN1.topleft=(840,550)
        texteRectWN2.topleft=(843,572)
        window.blit(texteWN1, texteRectWN1)
        window.blit(texteWN2,texteRectWN2)

    if Vwin==3:                                             #Match Nul(Les deux gagnent)
        #print("Vwin : ",Vwin)
        police=pygame.font.Font('freesansbold.ttf', 22)
        texteNul1=police.render(' Match ',True,BLACK,GREY)
        texteNul2=police.render(' Nul ',True,BLACK,GREY)
        texteRectNul1=texteNul1.get_rect()
        texteRectNul2=texteNul2.get_rect()
        texteRectNul1.topleft=(840,550)
        texteRectNul2.topleft=(845,572)
        window.blit(texteNul1, texteRectNul1)
        window.blit(texteNul2,texteRectNul2)
                                                            
    if Vwin==4:                                             #Aucun Gagnant
        police=pygame.font.Font('freesansbold.ttf', 22)
        texteAG1=police.render(' Aucun ',True,BLACK,GREY)
        texteAG2=police.render('Gagnant ',True,BLACK,GREY)
        texteRectAG1=texteAG1.get_rect()
        texteRectAG2=texteAG2.get_rect()
        texteRectAG1.topleft=(840,550)
        texteRectAG2.topleft=(845,572)
        window.blit(texteAG1, texteRectAG1)
        window.blit(texteAG2,texteRectAG2)
        

def Sauvegarde(table,click,coorX,coorY):    #Permet d'enregistrer la partie
    stockT=[[["","",""],["","",""],["","",""]],[["","",""],["","",""],["","",""]],[["","",""],["","",""],["","",""]],[["","",""],["","",""],["","",""]]]
    stockC=0
    
    if coorX>=770 and coorX<=950 and coorY>=122 and coorY<=147:
        
        if click==1:
            FST=open(SauvegardeT.py, 'wb')              #Fichier Stock Table
            FST.write(str(table))
            FST.close()

            FSC=open('SauvegardeC.txt', 'w')            #Fichier Stock Click
            FSC.write("2")#     <------- si click=1 on met click=2 dans la Sauvergarde, car lorsqu'on va apellé la Sauvegarde, les clics vont s'intervertir dans le While InProgress
            FSC.close()#                                                                                                                            et on reviendra à 1                            
            
            
        elif click==2:
            FST=open('SauvegardeT.py', 'w')
            FST.write(str(table))
            FST.close()

            FSC=open('SauvegardeC.txt', 'w')
            FSC.write("1")#     <------ Même chose ici
            FSC.close
            
        if click==2:
            click=1

        else:
            click=2


def JouerSauvegarde(table,click,coorX,coorY):   #Permet de jouer la partie enregistrée
    
    if click==0:
        
        if coorX>=590 and coorX<=903 and coorY>=460 and coorY<=508:
            FST=open('SauvegardeT.py', 'r')
            table=FST.read()
            FST.close()

            FSC=open('SauvegardeC.txt', 'r')
            click=FSC.read()
            FSC.close()
            
            window.fill(GREY)
            print
            return table, click
        else:
            return table, click
    else:
        return table,click

def NewGame(coorX,coorY,table,click,joueur,clickControle1,clickControle2): #Initialisation les variables pour nouvelle partie
    
    if click==0: #Click=0 signifie que l'on est sur la page de démarage avec ecrit Pentago

        if coorX>=140 and coorX<=408 and coorY>=460 and coorY<=508:     #Check Position Button Nouvelle Partie

            table=[[["","",""],["","",""],["","",""]],[["","",""],["","",""],["","",""]],[["","",""],["","",""],["","",""]],[["","",""],["","",""],["","",""]]]
            affichage(table)
            joueur=1
             
            return table,click,joueur,0,0

        else:
            return table,click,joueur,0,0

    else:
    
        if coorX>770 and coorX<960 and coorY>90 and coorY<118 :     #Check position button Nouvelle partie en jeu
            
            table=[[["","",""],["","",""],["","",""]],[["","",""],["","",""],["","",""]],[["","",""],["","",""],["","",""]],[["","",""],["","",""],["","",""]]]
            click=2
            joueur=1
            affichage(table)
            return table,click,joueur,1,0

        else:
            return table,click,joueur,clickControle1,clickControle2


def Quit(coorX,coorY):

    if coorX>770 and coorX<870 and coorY>150 and coorY<176:
        a=True
        return a
    
        

def TDJ(joueur,click,clickControle2,Vwin):    #Tour De Jeux
        
    if click==2:    
        if joueur==1:
            
            if clickControle2==2:
                return joueur
            
            else:
                joueur=2
                affichageEcran(joueur,click,Vwin)
                return joueur

        elif joueur==2:
            if clickControle2==2:
                return joueur
            
            else:
                joueur=1
                affichageEcran(joueur,click,Vwin)

                return joueur

    else:    
        return joueur
    
    affichageEcran(joueur,click)
