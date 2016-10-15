#2.2 Affichage du tableau

def affitableau(plateau):

#on définie les "pions" selon sa variable attribuée
    
    for ligne in plateau:
        for x in ligne:
            if x==0 :
                x=" "
            if x==1:
                x="x"
            if x==-1:
                x="o"
                
#on structure le tableau
                
            print(end="|")
            print(x,end="")
            print(end="|")
        print("\n")
    print(" -  -  -  -  -  -  -  ")
    print(" 1  2  3  4  5  6  7  ")


#2.3.1 Calcul de la hauteur d'une colonne

def hautcolo(plateau,c):
    affitableau(plateau)
    n=0
    if plateau[c]==1 :
        n=n+1
    if plateau[c]==-1:
        n=n+1
    return n


#2.3.2

def plein(plateau,c):
    hautcolo(plateau,c)
    z=0
    if n==7:
        z=1
    return z

#2.3.3

def pionjoueur(plateau,c):
    c=int(input("Choisissez une colonne : "))
    plein(plateau,c)
    while z==1:
        c=int(input("Choisir une autre colonne : "))
    return c


#2.3.4

def pionordi(plateau,c):
    c=randint(1,7)
    plein(plateau,c)
    while z==1:
        c=randint(1,7)
    return c




