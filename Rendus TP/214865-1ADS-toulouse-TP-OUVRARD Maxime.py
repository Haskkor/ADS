                                # Tp puissance 4#

# implémentation et affichage du plateau #

def puissance4():

    plateau=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

    for ligne in plateau:           # cette boucle for me permet d'afficher le plateau de manière graphique #
        col = "|"
        for element in ligne:
            if element == 0:        # cet élément correspond à la case vide #
                col=col+" |"
            elif element == 1:      # celui correspond à la valeur du joueur #
                col=col+" x"
            elif element == -1:     # et ce dernier à la valeur de l'ordinateur #
                col=col+" o"
        print(col)
    print(" -"*7)
    print(" 1 2 3 4 5 6 7")

puissance4()                        # c'est la représentation de la grille du puissance4 #

def Ftaille(plateau,Ncol):          # cette fonction retourne le nombre de pions dans la colonne en question #
    
    Ncol = int(input("Saisir un numéro de colonne: "))
    nbrpions = eval(input("Nombre de pions: "))
    Ncol == nbrpions
    return Ncol

Ftaille(Ncol)

def Fbool(plateau,Ncol):            # en principe, cela permet de savoir si une colonne est pleine ou pas #
    for i in range(8):  
        if Ncol>7:
            return(True)
        else:
            return(False)

Fbool(plateau,Ncol)

def Fpion(plateau,c):
    c = eval(input("saisir un numéro de colonne valide: "))


    
    
    
    



