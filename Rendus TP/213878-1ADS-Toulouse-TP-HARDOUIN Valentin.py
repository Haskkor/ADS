                             #TP Puissance 4 en python






def plateau():        #affichage du plateau
    plateau = [[" |"]*7  for i in range(6)]
    posepion()
    for ligne in plateau:
        for i in ligne:
            print(i," ",end="")
        print("\n")
    print("-  -   -   -   -   -   -  ")
    print("0  1   2   3   4   5   6  ")
    
def posepion() :      #pose d'un pion par le joueur 
        

    print("choisir la case voulut : ")
    ligne=int(input("numéro de colonne : "))
    colonne=int(input("numéro de ligne : "))
    plateau[colonne][ligne]=("x|")
    print("\n")
    

def coupIA():         #pose d'un pion par l'ordinateur
    ligne=[randint(0,6)]
    colonne=[randint(0,6)]


def sommecol() :        #hauteur d'une colonne
    col=[colonne][ligne-1]
    


    
plateau()


