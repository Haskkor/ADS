import random

#1 - Création du plateau de jeu. ***************************

        #1.a - Définitions de la taille du plateau de jeu, on demande ici de saisir des nombres entiers.

LIGNES = eval(input("Combien de lignes de jeu voulez vous?"))

COLONNES = eval(input("Combien de colonnes de jeu voulez vous ?"))

CHOIX = eval(input("Dans quelle colonne voulez vous jouer?"))

        #1.b - Traitement des données afin d'afficher un plateau, avec les valeurs saisies par le joueur humain.

plateau = [['']*COLONNES for i in range(0, LIGNES)]
plateau[CHOIX] = CHOIX
for ligne in plateau:
    
        for x in ligne:
            
            print('|', x,'', end='|  ')
            
        print('\n ')



        #1.c - Gestion de l'affichage du nombre de colonnes. ( Situées en bas de chaque colonnes. )
    
NUMEROTATION = 0

for NUMEROTATION in range (0,COLONNES):
    
        print(' ', NUMEROTATION+1,' ', end=' ')





    




