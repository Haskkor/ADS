###########################
####### TP PYTHON  ########
###########################


# 2.2 Affichage du plateau


# On définit une procrédure prenant un paramètre un plateau

plateau = [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,-1,0,1,0,0,0], [0,1,1,-1,0,0,-1]]

# On définit une procrédure prenant en paramètre un plateau et qui en réalise l'affichage.
# Avec les conventions suivantes : 0 = ' ', 1 = 'x', -1 = 'o'.

def game():
    
# On commence par rentrer dans les deux liste grace au boucle for.
# Et on definit les barres qui seront entre les pions.

    for ligne in plateau:
        barre = "|"                
        for x in ligne:

# Pour chaque cas, on affiche la valeur qui lui est attribué dans la convention.
# Malheureusement je n'ai pas su bien les positionner.

            if x == 0:      
                barre=barre+" |"
            elif x == 1:                
                barre=barre+" x"
            elif x == -1:               
                barre=barre+" o"
        print(barre)

# Puis on affiche les barres, ainsi que les numéros en dessous des colonnes.

    print("","-","-","-" ,"-" ,"-" ,"-" ,"-" )  
    print("",1,2,3,4,5,6,7)

game()


# 2.3.1 Calcul de la hauteur d'une colonne


def retourpion(plateau,c):
    c = eval(input( " Saisir un nombre de colonne :  "))

# On rentre dans la boucle on se positionne à la colonne demander,
# Si la valeur que l'on rencontre est égale à 1 ou -1 on compte +1.

    for ligne in plateau:
        for c in ligne:
            if c == 1 or c == -1:
                count +=1
    return somme

retourpion(plateau,1)


# 2.3.2 Une colonne est-elle pleine

def retourplein(plateau,c):
    c=eval(input(" Saisir un nombre de colonne : "))

# On determine si chaque case est égale à 1 ou -1 pour la colonne demander.
# Si c'est le cas on retourne Vrai sinon c'est Faux.

    for ligne in plateau:
        for c in ligne:
            if c == 1 or c == -1:
                return True
            else:
                return False    


# 2.3.3 Pose d'un pion par le joueur

c =eval(input(" Saisir la colonne que vous voulez jouer : "))
def pionjoueur(plateau,c):
    while c < 0
