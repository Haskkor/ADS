###############################################################################
#Une fonction prenant en paramètre un entier n et retournant une liste à deux #
#dimensions de n lignes et n colonnes dont toutes les valeurs valent 0.       #
###############################################################################

def platesize(plate,line):

    for i in range (3):
        plate.append ([])

        for j in range (3):
            plate[i].append(0)

    return plate

###############################################################################
#Une procédure réalisant l’affichage des valeurs d’une liste à deux dimensions#
#passée en paramètres.                                                        #
###############################################################################

def poster(liste):
    for i in range(len(liste)):

        for j in range(len(liste[i])):
            if liste[i][j] == 0:
                print(" 0 ",end="")
            if liste[i][j] == 1:
                print(" 1 ",end="")
            if liste[i][j] == 2:
                print(" 2 ",end="")

        print()

line= 3

plate=[]
platesize(plate,line)

poster(plate)
print(plate)
