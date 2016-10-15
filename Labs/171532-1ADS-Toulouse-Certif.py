import sys
import random
import copy
import pygame

__author__ = "Jérémy Farnault - 171532"

####################
### 2.1 LA FORET ###
####################

# Prend deux entiers n et m et retourne une liste à 2 dimensions de
# n lignes et m colonnes dont toutes les valeurs sont égales à 0
def createForest(n, m):
    forest = [[0 for col in range(m)] for row in range(n)]
    return forest

# Prend une liste, ses dimensions et une probabilité et
# place aléatoirement des arbres dans la forêt
def placeTrees(forest, n, m, p):
    for i in range(len(forest)):
        for j in range(len(forest[i])):
            # Si le nombre aléatoire est inférieure à la probabilité on place un arbre
            if random.randint(0,100) < p:
                forest[i][j] = 1

# Prend une liste et ses dimensions puis met le feu à un arbre au hasard
def setFire(forest, n, m):
    x = random.randint(0,n - 1)
    y = random.randint(0,m - 1)
    # Tant que la case choisie ne contient pas un arbre on continue
    while forest[x][y] != 1:
        x = random.randint(0,n - 1)
        y = random.randint(0,m - 1)
    forest[x][y] = 2

# Prend une liste et ses dimensions et retourne la proportion d'arbres dans la forêt
def proporTrees(forest, n, m):
    trees = 0
    for i in forest:
        for j in i:
            if j == 1:
                trees += 1
    # Retourne un pourcentage
    propor = (trees / (n * m)) * 100
    return propor

# Prend une liste et ses dimensions et affiche la forêt dans la console
# 0 -> '.' ; 1 -> 'A' ; 2 -> 'F' ; 3 -> 'C'
def printForest(forest, n, m):
    for i in forest:
        line = ""
        for j in i:
            if j == 0:
                line += ". "
            elif j == 1:
                line += "A "
            elif j == 2:
                line += "F "
            elif j == 3:
                line += "C "
        print(line)
        
#################################
### 2.2 LA PROPAGATION DU FEU ###
#################################

# Prend une liste, ses dimensions et les coordonnées d'une case et renvoie un
# booléen indiquant la présence d'un arbre en feu à proximité de la case
def nearFire(forest, n, m, i, j):
    # Vérifie que l'on ne sorte pas des bornes du tableau et contrôle les
    # cases situées au Nord, au Sud, à l'Ouest et à l'Est
    if i - 1 >= 0:
        if forest[i - 1][j] == 2:
            return True
    if i + 1 < n:
        if forest[i + 1][j] == 2:
            return True
    if j - 1 >= 0:
        if forest[i][j - 1] == 2:
            return True
    if j + 1 < m:
        if forest[i][j + 1] == 2:
            return True
    return False

# Prend une liste et ses dimensions et modifie la forêt pour la faire passer
# à la génération suivante
def nextGeneration(forest, n, m):
    # Copie la liste dans une liste temporaire
    tempForest = copy.deepcopy(forest)
    for i in range(len(forest)):
        for j in range(len(forest[i])):
            # Si la case est vide
            if forest[i][j] == 0:
                tempForest[i][j] = 0
            # Si la case est un arbre (contrôle la proximité d'arbres en feu)
            elif forest[i][j] == 1:
                if nearFire(forest, n, m, i, j):
                    tempForest[i][j] = 2
                else:
                    tempForest[i][j] = 1
            # Si la case est un arbre en feu
            elif forest[i][j] == 2:
                tempForest[i][j] = 3
            # Si la case est un arbre en cendres
            elif forest[i][j] == 3:
                tempForest[i][j] = 3
    return tempForest

# Suivi de l'évolution d'une forêt nouvellement créée sur plusieurs générations
# avec l'affichage dans la console
def mainConsole(forest, iterations, n, m):
    # Pour le nombre d'itérations souhaitée
    for i in range(iterations):
        # Calcul de la proportion d'arbres
        propor = proporTrees(forest, n, m)
        # Affichage de la forêt
        printForest(forest, n, m)
        # Affichage de la proportion d'arbres
        print()
        print("Proportion d'arbres : " + str("%.2f" % propor))
        print()
        # Passage à la prochaine génération
        forest = nextGeneration(forest, n, m)

###################################    
### 2.3 UNE INTERFACE GRAPHIQUE ###
###################################

# Suivi de l'évolution d'une forêt nouvellement créée sur plusieurs générations
# avec l'affichage graphique
def graphicDisplay(forest, iterations, n, m):
    # Définition d'un timer
    clock = pygame.time.Clock()
    # Définition des couleurs utilisées
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    # Définition de la fenêtre d'affichage
    screen = pygame.display.set_mode((n + 200, m + 200))
    screen.fill((200, 200, 200))
    pygame.display.set_caption('Evolution incendie de foret')
    # Pour le nombre d'itérations souhaitées
    for i in range(iterations):
        for i in range(len(forest)):
            for j in range(len(forest[i])):
                if forest[i][j] == 0:
                    screen.set_at((i + 100,j + 100), WHITE)
                elif forest[i][j] == 1:
                    screen.set_at((i + 100,j + 100), GREEN)
                elif forest[i][j] == 2:
                    screen.set_at((i + 100,j + 100), RED)
                elif forest[i][j] == 3:
                    screen.set_at((i + 100,j + 100), BLACK)
        # Passage à la prochaine génération, mise à jour de l'affichage
        forest = nextGeneration(forest, n, m) 
        pygame.display.update()
        clock.tick(30)
            
###########################
### FONCTION PRINCIPALE ###
###########################

def main():
    choice = 0
    # Propose le mode graphique ou le mode console à l'utilisateur
    print("Voulez-vous lancer le mode graphique ou le mode console ?")
    while choice > 2 or choice < 1:
        choice = eval(input("[ 1 - Console ; 2 - Graphique ] : "))
    # Demande la hauteur et la largeur de forêt souhaitée
    n = eval(input("Saisissez une hauteur de foret : "))
    m = eval(input("Saisissez une largeur de foret : "))
    forest = createForest(n, m)
    prob = 0
    # Demande la probabilité d'arbres souhaitée
    while prob <= 0:
        prob = eval(input("Saisissez une probabilite d'arbres : "))
    placeTrees(forest, n, m, prob)
    setFire(forest, n, m)
    iterations = 0
    # Demande le nombre d'itérations souhaitées
    while iterations <= 1:
        iterations = eval(input("Saisissez un nombre d'iterations : "))
    # Lance le programme dans le mode choisi
    if choice == 1:
        print("")
        mainConsole(forest, iterations, n, m)
    elif choice == 2:
        graphicDisplay(forest, iterations, n, m)

main()















    
    
