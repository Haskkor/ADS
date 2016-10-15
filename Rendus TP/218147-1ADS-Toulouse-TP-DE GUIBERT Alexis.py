from random import randint

def jeux_ordi (i,colone,plateau):
    if i == 1:
        if plateau[5][i-1]==0:
            plateau[5][i-1]= -1
        elif plateau[4][i-1]== 0:
             plateau[4][i-1]= -1
        elif plateau[3][i-1]== 0:
             plateau[3][i-1]= -1
        elif plateau[2][i-1]== 0:
              plateau[2][i-1]= -1
        elif plateau[1][i-1]== 0:
             plateau[1][i-1]= -1
        elif plateau[0][i-1]== 0:
             plateau[0][i-1]= -1

    if i == 2:
        if plateau[5][i-1]==0:
             plateau[5][i-1]= -1
        elif plateau[4][i-1]== 0:
             plateau[4][i-1]= -1
        elif plateau[3][i-1]== 0:
             plateau[3][i-1]= -1
        elif plateau[2][i-1]== 0:
             plateau[2][i-1]= -1
        elif plateau[1][i-1]== 0:
             plateau[1][i-1]= -1
        elif plateau[0][i-1]== 0:
             plateau[0][i-1]= -1
    if i == 3:
        if plateau[5][i-1]==0:
             plateau[5][i-1]= -1
        elif plateau[4][i-1]== 0:
             plateau[4][i-1]= -1
        elif plateau[3][i-1]== 0:
             plateau[3][i-1]= -1
        elif plateau[2][i-1]== 0:
             plateau[2][i-1]= -1
        elif plateau[1][i-1]== 0:
             plateau[1][i-1]= -1
        elif plateau[0][i-1]== 0:
             plateau[0][i-1]= -1
    if i == 4:
        if plateau[5][i-1]==0:
             plateau[5][i-1]= -1
        elif plateau[4][i-1]== 0:
             plateau[4][i-1]= -1
        elif plateau[3][i-1]== 0:
             plateau[3][i-1]= -1
        elif plateau[2][i-1]== 0:
             plateau[2][i-1]= -1
        elif plateau[1][i-1]== 0:
             plateau[1][i-1]= -1
        elif plateau[0][i-1]== 0:
             plateau[0][i-1]= -1

    if i == 5:
        if plateau[5][i-1]==0:
             plateau[5][i-1]= -1
        elif plateau[4][i-1]== 0:
             plateau[4][i-1]= -1
        elif plateau[3][i-1]== 0:
             plateau[3][i-1]= -1
        elif plateau[2][i-1]== 0:
             plateau[2][i-1]= -1
        elif plateau[1][i-1]== 0:
             plateau[1][i-1]= -1
        elif plateau[0][i-1]== 0:
             plateau[0][i-1]= -1

    if i == 6:
        if plateau[5][i-1]==0:
             plateau[5][i-1]= -1
        elif plateau[4][i-1]== 0:
             plateau[4][i-1]= -1
        elif plateau[3][i-1]== 0:
             plateau[3][i-1]= -1
        elif plateau[2][i-1]== 0:
             plateau[2][i-1]= -1
        elif plateau[1][i-1]== 0:
             plateau[1][i-1]= -1
        elif plateau[0][i-1]== 0:
             plateau[0][i-1]= -1

    if i == 7:
        if plateau[5][i-1]==0:
             plateau[5][i-1]= -1
        elif plateau[4][i-1]== 0:
             plateau[4][i-1]= -1
        elif plateau[3][i-1]== 0:
             plateau[3][i-1]= -1
        elif plateau[2][i-1]== 0:
             plateau[2][i-1]= -1
        elif plateau[1][i-1]== 0:
             plateau[1][i-1]= -1
        elif plateau[0][i-1]== 0:
             plateau[0][i-1]= -1

#permet d'afficher un cadrillage propre 
    
    for lignes_de_jeu in plateau:
        lignes = ""
        for pion in lignes_de_jeu:
            if pion == (0):
                lignes += "| "
            elif pion == (1):
                lignes += "|X"
            elif pion ==(-1):
                lignes +="|O"
            else:
                affichage_du_plateau (ligne, colone)

        #on affiche le tableau  
        print (lignes)
        
        #on affiche la numérotation dessous ainsi que l'interface graphique
        
    print ("","-","-","-","-","-","-","-")  
    print ("",1,2,3,4,5,6,7)

    print ("l'adversaire à joué a vous de jouer")
    joue_joueur(colone)


#cela permet de retourner une case lorsque je joueur joue 
def jeux (i,colone,plateau):
    if i == 1:
        if plateau[5][i-1]==0:
            plateau[5][i-1]= 1
        elif plateau[4][i-1]== 0:
             plateau[4][i-1]= 1
        elif plateau[3][i-1]== 0:
             plateau[3][i-1]= 1
        elif plateau[2][i-1]== 0:
              plateau[2][i-1]= 1
        elif plateau[1][i-1]== 0:
             plateau[1][i-1]= 1
        elif plateau[0][i-1]== 0:
             plateau[0][i-1]= 1

    if i == 2:
        if plateau[5][i-1]==0:
             plateau[5][i-1]= 1
        elif plateau[4][i-1]== 0:
             plateau[4][i-1]= 1
        elif plateau[3][i-1]== 0:
             plateau[3][i-1]= 1
        elif plateau[2][i-1]== 0:
             plateau[2][i-1]= 1
        elif plateau[1][i-1]== 0:
             plateau[1][i-1]= 1
        elif plateau[0][i-1]== 0:
             plateau[0][i-1]= 1
    if i == 3:
        if plateau[5][i-1]==0:
             plateau[5][i-1]= 1
        elif plateau[4][i-1]== 0:
             plateau[4][i-1]= 1
        elif plateau[3][i-1]== 0:
             plateau[3][i-1]= 1
        elif plateau[2][i-1]== 0:
             plateau[2][i-1]= 1
        elif plateau[1][i-1]== 0:
             plateau[1][i-1]= 1
        elif plateau[0][i-1]== 0:
             plateau[0][i-1]= 1
    if i == 4:
        if plateau[5][i-1]==0:
             plateau[5][i-1]= 1
        elif plateau[4][i-1]== 0:
             plateau[4][i-1]= 1
        elif plateau[3][i-1]== 0:
             plateau[3][i-1]= 1
        elif plateau[2][i-1]== 0:
             plateau[2][i-1]= 1
        elif plateau[1][i-1]== 0:
             plateau[1][i-1]= 1
        elif plateau[0][i-1]== 0:
             plateau[0][i-1]= 1

    if i == 5:
        if plateau[5][i-1]==0:
             plateau[5][i-1]= 1
        elif plateau[4][i-1]== 0:
             plateau[4][i-1]= 1
        elif plateau[3][i-1]== 0:
             plateau[3][i-1]= 1
        elif plateau[2][i-1]== 0:
             plateau[2][i-1]= 1
        elif plateau[1][i-1]== 0:
             plateau[1][i-1]= 1
        elif plateau[0][i-1]== 0:
             plateau[0][i-1]= 1

    if i == 6:
        if plateau[5][i-1]==0:
             plateau[5][i-1]= 1
        elif plateau[4][i-1]== 0:
             plateau[4][i-1]= 1
        elif plateau[3][i-1]== 0:
             plateau[3][i-1]= 1
        elif plateau[2][i-1]== 0:
             plateau[2][i-1]= 1
        elif plateau[1][i-1]== 0:
             plateau[1][i-1]= 1
        elif plateau[0][i-1]== 0:
             plateau[0][i-1]= 1

    if i == 7:
        if plateau[5][i-1]==0:
             plateau[5][i-1]= 1
        elif plateau[4][i-1]== 0:
             plateau[4][i-1]= 1
        elif plateau[3][i-1]== 0:
             plateau[3][i-1]= 1
        elif plateau[2][i-1]== 0:
             plateau[2][i-1]= 1
        elif plateau[1][i-1]== 0:
             plateau[1][i-1]= 1
        elif plateau[0][i-1]== 0:
             plateau[0][i-1]= 1
            

        
        #on affiche la numérotation dessous ainsi que l'interface graphique
        
    print ("","-","-","-","-","-","-","-")  
    print ("",1,2,3,4,5,6,7)
        
    joue_ordi(colone)
    

def joue_ordi (colone):
#permet de rentrer un nombre aléatoire entre 1 et 7
    i=randint(1,7)
    jeux_ordi (i,colone,plateau)


def joue_joueur(colone):
    i = 0
#permet de demander au joueur de rentrer un nombre entre 1 et 7
    while i < 1 or i > 7:
        i = eval(input("entre la colone dans laquelle vous voulez jouer: "))

    
    jeux (i,colone,plateau)


    #cela devrait permettre de pouvoir calculer le nombre de 0 dans une colone mais cela ne marche pas 

##def nombre_de_pion_colone (plateau,ligne,colone):
 #   somme = 0
  #  for colone in plateau:
   #     somme = somme + plateau.count(0)
    #    print (somme)

        


def qui_joue():
    n=0
    while n!=1 and n!=2:
        n=eval(input("choisis 1 pour commencer ou 2 pour laisser l'ordi commencer "))
    if n==1:
        joue_joueur(colone)
    if n==2:
        joue_ordi (colone)
    


    
    

#on va travailler l'affichage du plateau
def affichage_du_plateau (ligne, colone):
    lignes_de_jeu=[]
    
    #dans cette partie on travaille sur le plateau, on va donc faire que
    #chaque ligne prennent a valeur 0 au départ
    
    for i in range (0,ligne):
        for j in range (0,colone):
            lignes_de_jeu.append(0)
            
        #le plateau va donc jouter les lignes 
        # pour ainsi procéder a un affichage
        
        plateau.append(lignes_de_jeu)
        lignes_de_jeu=[]
        
    #on va afficher les lignes pour ainsi crééer un pseudo affichage graphique
    #chaque ligne prendra la valeur O X ou rien suivant si le plateau comporte
    #un 0 un 1 ou un -1 et on affiche une barre pour rendre cela plus graphique
        
    for lignes_de_jeu in plateau:
        lignes = ""
        for pion in lignes_de_jeu:
            if pion == (0):
                lignes += "| "
            elif pion == (1):
                lignes += "|X"
            elif pion ==(-1):
                lignes +="|O"
            else:
                affichage_du_plateau (ligne, colone)

        #on affiche le tableau  
        print (lignes)
        
        #on affiche la numérotation dessous ainsi que l'interface graphique
        
    print ("","-","-","-","-","-","-","-")  
    print ("",1,2,3,4,5,6,7)
    
    qui_joue()
    #je met en explication ce qu'il y a ci dessous car cela ne marche pas

    
# nombre_de_pion_colone (plateau,ligne,colone)







#on initie le plateau pour le rendre vide
plateau=[]
  
# on initialise le nombre de lignes et de colones (on met une colone de plus 
ligne=6 
colone=8
affichage_du_plateau (ligne, colone)

print (plateau)


#le programmer permet de faire jouer un ordinateur aléatoirement ainsi qu'un joueur
#a tour de role mais je n'ai pas eus le temps de faire un compteur qui marche pour réussir
#à voir qui gagne 



