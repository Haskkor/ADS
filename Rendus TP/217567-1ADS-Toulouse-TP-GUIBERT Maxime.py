from random import *


#2.1
    
listeligne=[]
listep=[]       #Liste Plateau

for i in range(1, 7):
    
    for i in range(1, 8):
        listeligne.append(0)      #Création d'une ligne
        
    listep.append(listeligne)     #Ajout de la ligne dans le plateau final
    listeligne=[]            #Reinitialisation de la liste qui sert a créer les ligne


for v in range(1, 7):   #2.2
    for w in range(1, 8):        #Double boucle For pour testé toute les cases

        print("|", end="")       #Design plateau
        if listep[v-1][w-1]==0:
                print(" ", end="")

        elif listep[v-1][w-1]==1:
                print("x", end="")
                
        else:
            print("o", end="")
           
    print("|","")       
print(" - - - - - - -") #Design plateau
print(" 1 2 3 4 5 6 7")
print("\n") #Pour espacée l'affichage dans la console



def npc(listep, colonne):     #Nombre Pions Colonne (2.3.1)
    
    
    compteur=0
    
    for i in range(1, 7):
        
        if listep[i-1][colonne-1]==1 or listep[i-1][colonne-1]==-1:     #Colonne-1 car l'homme compte de 1 à 7 et la machine de 0 à 6
            compteur += 1

    return compteur


def pleine(listep, colonne):

    compteur=0
    
    for i in range(1, 7):
        
        if listep[i-1][colonne-1]==1 or listep[i-1][colonne-1]==-1:
            compteur += 1

    if compteur==6:
         return True

    else:
        return False


def tour_joueur(listep): #2.3.3
    
    colonnej=0      #Colonne Jouée
    
    while colonnej<1 or colonnej>7 or a==True:
        colonnej=int(input("Choisissez la colonne à jouer : "))
        a=pleine(listep, colonnej)

    return colonnej


def tour_ordi(listep):  #2.3.4

    colonnej=0
    
    while colonnej<1 or colonnej>7 or a==True:
        colonnej=randint(1,7)
        a=pleine(listep, colonnej)

    return colonnej





#2.4.1
def align_horiz(listep, colonnej, play): #listep = plateau, colonnej = la colonne joué, play = le dernier joueur à avoir joué

    count=0
    gg=0
    ggg=0
    
    for i in range(1, 7):
        if listep[i-1][colonnej-1]==1 or listep[i-1][colonnej-1]==-1:
            count += 1      #Ce compteur sert à savoir sur quelle ligne a était joué le dernier pion (nous connaissons deja la colonne)


    if colonnej<4:  #Cas où on est à gauche du milieu, on verifie vers la droite
    
        for j in range(1,5):
            
            if listep[count][j-1]==play:
                gg += 1

                
    elif colonnej>4: #Cas où on est à droite du milieu, on verifie vers la gauche
        
        for v in range(5,1,-1):
            
            if listep[count][v-1]==play:
                gg += 1


    else:       #Cas où on est au milieu, on verifie dans les deux directions
        
        for j in range(1,5):
            
            if listep[count][j-1]==play:
                gg += 1


        for v in range(5,1,-1):
            
            if listep[count][v-1]==play:
                ggg += 1
                   
#J'isole tout les cas car si on est a gauche du milieu et qu'on vérifie vers la gauche, la console va nous affiché "out of range"   
    

    if gg==4 or ggg==4:
        victoire = True

    else:
        victoire = False

    return victoire





def align_verti(listep, colonnej, play): #2.4.2

    count=0
    gg=0
    
    for i in range(1, 7):
        
        if listep[i-1][colonnej-1]==1 or listep[i-1][colonnej-1]==-1:
            count += 1


    for i in range(count, 7-count):
        
        if listep[i-1][colonnej-1]==play:
            gg += 1


    if gg==4:
        victoire = True

    else:
        victoire = False

    return victoire





def align_diag1(listep, colonnej, play): #2.4.3

    count=0
    gg=0
    
    for i in range(1, 7):
        
        if listep[i-1][colonnej-1]==1 or listep[i-1][colonnej-1]==-1:
            count += 1

    for v in range(1,5):
        if listep[5-count][colonnej-1]==play: #Je sais pas trop comment expliqué [5-count] et [colonnej-1] sans schéma
            gg += 1
            
        count += 1
        colonnej += 1

    if gg==4:
        victoire = True
        
    else:
        victoire = False
        
    return victoire
        




def align_diag2(listep, colonnej, play): #2.4.4

    count=0
    gg=0
    
    for i in range(1, 7):
        
        if listep[i-1][colonnej-1]==1 or listep[i-1][colonnej-1]==-1:
            count += 1

    for i in range(1, 5):

        if listep[5-count][5-count]==play:
            gg += 1

    if gg==4:
        victoire = True

    else:
        victoire = False

    return victoire
            

def coup_gagnant(listep, colonnej, play): #2.4.5
    
    a=align_horiz(listep, colonnej, play)
    b=align_verti(listep, colonnej, play)
    c=align_diag1(listep, colonnej, play)
    d=align_diag2(listep, colonnej, play)

    if a==True or b==True or c==True or d==True:
        victoire = True

    else:
        victoire = False

    return victoire





#Début de la partie

play = 1
victoire = 0
count=0


while victoire != True:
    count=0
    if play==1:
        colonnej=tour_joueur(listep)
        
        for i in range(1, 7):
        
            if listep[i-1][colonnej-1]==1 or listep[i-1][colonnej-1]==-1:
                count += 1
        listep[5-count][colonnej-1]=1
        
        play = -1
        
    else:
        colonnej=tour_ordi(listep)
        
        print("L'ordinateur à joué : ", str(colonnej), "\n")
        
        
        for i in range(1, 7):
        
            if listep[i-1][colonnej-1]==1 or listep[i-1][colonnej-1]==-1:
                count += 1
        listep[5-count][colonnej-1]=-1
        
        
        play=1

    for v in range(1, 7):   #2.2
        for w in range(1, 8):        #Double boucle For pour testé toute les cases

            print("|", end="")       #Design plateau
            if listep[v-1][w-1]==0:
                print(" ", end="")

            elif listep[v-1][w-1]==1:
                print("x", end="")
                
            else:
                print("o", end="")
           
        print("|","")       
    print(" - - - - - - -") #Design plateau
    print(" 1 2 3 4 5 6 7")
    print("\n") #Pour espacée l'affichage dans la console


    victoire = coup_gagnant(listep, colonnej, play)

print("Vous avez Gg")















    



