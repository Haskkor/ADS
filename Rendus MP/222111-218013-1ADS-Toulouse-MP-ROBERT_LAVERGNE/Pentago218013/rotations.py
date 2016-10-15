
################################################################################
#Une procédure prenant en paramètre un entier m et une liste à deux dimensions #    #
#de m lignes et m colonnes. Cette procédure réalisera une rotation de cette    #
#liste de 90 degrés dans le sens des aiguilles d’une montre.                   #
################################################################################

def platesize(line,column,plate):

    for i in range (line):
        plate.append ([])

        for j in range (column):
            plate[i].append(0)

    return plate

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

def rotation(plate):
    column=[]
    line=[]
    rotation=[]
    for i in range (len(plate)):
        column.append([])

        line.append(plate[i])
        for j in range (len(plate[i])):
            column[i].append(plate[j][i])

    for i in range (len(column)):

        rotation.append(column[i])
        rotation[i].reverse()


    print(plate)
    print(line)
    print(column)
    print("")
    print(rotation)
plate=[]
line=eval (input("Rentrez un nombre égal de colonne et de ligne = "))
column=line
platesize(line,column,plate)
poster(plate)
rotation(plate)



        
