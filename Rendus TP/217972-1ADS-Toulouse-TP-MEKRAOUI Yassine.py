## j'ai modifié mon code pour la ciqquième partie, normalement ca marche pour 6 lignes, 7 colonnes et 4 pions


#question2.1
#on commence par créer la liste pour le plateau
#modifié pour la question 5
def tailleplateau( ):
    plateau=[]
    ligne = int(input("entrez le nombre de ligne du plateau"))
    colonne = int(input("entrez le nombre de colonne du plateau"))
    for i in range(ligne):#on crée les lignes
        plateau.append([])
        for j in range(colonne):
            plateau[i].append(0)#on remplie els colonnes de chaque lignes avec des 0
    return plateau


#question 2.2
#on crée la fonction pour afficher le plateau

def afficheplateau(liste):
    for ligne in range(len(liste)):#double boucle for pour parcourir les cases du plateau
        print("|",end="")
        for colonne in range(len(liste[ligne])):#et on affiche sleon la valeur contenue
            if liste[ligne][colonne] == 1:
                print("x|",end="")
            if liste[ligne][colonne] == -1:
                print("o|",end="")
            if liste[ligne][colonne] == 0:
                print(" |",end="")
        print()
    for ligne in range(len(liste[0])):#les traits du bas
        print(" -",end="")
    print()
    for ligne in range(1,len(liste[0])+1):#numero des colonnes
        print(" {0}".format(ligne),end="")
    print()
    
#question2.3.1
def nbrpion(liste,numcol):
    nbpion=0#on crée un compteur
    for ligne in range(len(liste)):#boucle pour parcourir une colonne
        if liste[ligne][numcol] != 0:#il y a un pion quand c'est different de 0
            nbpion+=1  #on ajoute donce 1 au compteur
    return nbpion
#question2.3.2

def colpleine(liste,numcol):
    plein = True
    for ligne in range(len(liste)):#boucle pour parcourir une colonne
        if liste[ligne][numcol] == 0:#il y a un pion quand c'est different de 0
            plein = False  #on dit que la colonne n'est pas pleine
    return plein

#question2.3.3

def piondanscol(liste):
    nbcorrect = False #booléen pour verifier que le nombre est correct
    while nbcorrect == False: #on crée une boucle pour faire retaper le joueur si il rentre un nombre incorrect
        numcol = int(input("entrez votre numero de colonne"))
        if (numcol<1)and (numcol>7):#on verifie que c'est dans l'intervalle [1,7]
            print("numero de colonne invalide, recommencez!")
        if colpleine(liste,numcol)== True:#on verifie l'etat de la colonne
            print("cette colonne est pleine, recommencez!")
        if (numcol>=1)and (numcol<=7)and (colpleine(liste,numcol-1)== False):#on rajoute le -1 pour que colpleine fonctionne bien
            nbcorrect = True
    return numcol

#question2.3.4
from random import randint #on importe la fonction du module random
def IApiondanscol(liste):
    nbcorrect = False#pour verifier si la colonne est pleine
    while nbcorrect == False:
        numcol = randint(1,len(liste[0]))
        if colpleine(liste,numcol-1) == False: #on teste si la colonne est plein
            nbcorrect = True #si non on sort de la boucle
    return numcol





#question2.4.1 alignement horizontal
# variable globale pour question 5
global ptvictory
def alH (liste,numcol,joueur):
    ligne = len(liste)-1-nbrpion(liste,numcol-1) #oncommence par determiner la position du pion dans la colonne
    alignement = False
    cpt = 0        #on crée un compteur car la victoire se fait des 4 pions
    for i in range (0,len(liste[0])):
        if liste[ligne][i] != joueur: #on verifie les valeurs de la ligne
            cpt=0
        else:
            cpt+=1
    global ptvictory
    if cpt>=(ptvictory):
        alignement = True
    return alignement

#question2.4.2 alignement vertical

def alV(liste,numcol,joueur): #cette fois pas besoin de determiner la position
    alignement = False
    cpt = 0
    for i in range (0,len(liste)):
        if liste[i][numcol-1] != joueur: #on verifie les valeurs de la colonne
            cpt =0
        else:
            cpt+=1
    global ptvictory
    if cpt>=(ptvictory):
        alignement = True
    return alignement

#question2.4.3 alignement diagonale 1

def alD1(liste,numcol,joueur):
    cpt = 0
    alignement = False
    for i in range (0,len(liste)):
        if liste[len(liste)-1-i][i] != joueur: #on verifie les valeurs de la diagonale
            cpt=0
        else:
            cpt+=1
    global ptvictory
    if cpt>=(ptvictory):
        alignement = True
    return alignement

#question2.4.4 alignement diagonale 2

def alD2(liste,numcol,joueur):
    alignement = False
    cpt=0
    for i in range (0,len(liste)):
        if liste[i][len(liste)-1-i] != joueur: #on verifie les valeurs de la diagonale
            cpt=0
        else:
            cpt+=1
    global ptvictory
    if cpt>=(ptvictory):
        alignement = True
    return alignement

# question 2.4.5 coup gagnant

def coupgagnant(liste,numcol,joueur): # on teste les configurations du plateau avec les fonctions précédentes
    victoire = False
    if (alD2(liste,numcol,joueur)== True)or (alD1(liste,numcol,joueur)== True)or (alH(liste,numcol,joueur)== True)or (alV(liste,numcol,joueur)== True):
        victoire = True
    return victoire

# question 2.5 on lance le jeu
plateau=tailleplateau()
ptvictory = int(input(" la victoir en combiend  ejetons alignés ?"))
tour = 0
fin = False
while fin != True:
    afficheplateau(plateau)
    if tour%2 == 0:
        joueur = 1
        colonne = piondanscol(plateau) - 1  #important de rajouter le -1 pour modifier la liste qui represente le plateau
        print("vous jouez dans la colonne ",colonne+1)
    else:
        joueur = -1
        colonne =IApiondanscol(plateau) -1
        print("l'IA joue dans la colonne ",colonne+1)
#on a récupéré le numero de colonne joué et on sait qu'il est correct
# il faut maintenant modifier le plateau
    ligne = len(plateau)-1 #on commence par determiner la position du pion dans la colonne
    test = False
    while (test == False): #on verifie les cases de bas en haut jusqu'à ce qu'on tombe sur une case vide
        if plateau[ligne][colonne]== 0:
            plateau[ligne][colonne]= joueur #si la case est vide on la rempli
            test = True #et on quitte la boucle 
        else:
            ligne-=1 #sinon on passe a la case du dessus
    etat = coupgagnant(plateau,colonne+1,joueur) #on contrôle l'état de la partie, si victoire on sort de la boucle
    if etat == True:
        afficheplateau(plateau)
        print("fin de la partie")
        if joueur == 1:
            print("Vous avez gagné, bravo !")
        else:
            print("Victoire de l'IA, désole")
        fin = etat
    tour+=1
