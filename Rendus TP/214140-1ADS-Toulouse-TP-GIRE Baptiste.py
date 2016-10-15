pion = input("Entrer joueur(1) ou ordinateur(2)")#on décide ici le nombre retourné par le programme en fonction du joueur
nbLignes = 6# On défini le nombre de lignes
nbColonnes = 7# on défini le nombre de colonnes

def Plateau():#On défini le plteau de jeu
    plateau = []# On initialise le plateau
    colonnes = nbColonnes
    for j in range(nbLignes):
        for i in range(colonnes):# Cette boucle sert a rajouter les chiffres dans le plateau
            if pion == "1":
                plateau.append(1)# On remplace les 0 par des 1 si c'est un joueur
            elif pion == "2":
                plateau.append(-1)# On remplace les 0 par des -1 si c'est l'ordinateur
            else:
                plateau.append(0)# Sinon on laisse les 0
            colonnes -= 1

        return plateau

def Affichage(Plateau):   #Cette fonction gère l'affichage du plateau
    for i in range(nbLignes):
        if pion == "1":
            print("|X"*nbColonnes,"|")
        elif pion == "2":
            print("|O"*nbColonnes,"|")
        else:
            print("| "*nbColonnes,"|")
    print(" -"*nbColonnes)
    print(" 1 2 3 4 5 6 7")
print(Affichage(Plateau()))


