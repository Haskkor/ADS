###############################################################################
#Une procédure prenant en paramètre un entier n supposé pair, une liste à deux#
#dimensions de n lignes et n colonnes, un entier représentant le numéro du    #
#quadrant et un booléen indiquant le sens de rotation.                        #                               #
###############################################################################

import copy

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

def etend(plate,plateend):

    for i in range (len(plate)):

        plate[i].extend(plateend[i])

def reuni ():
    temp=[]

    case1=copy.deepcopy(plate1)
    case2=copy.deepcopy(plate2)
    case3=copy.deepcopy(plate3)
    case4=copy.deepcopy(plate4)
    
    etend (case1,case3)
    etend (case2,case4)
    temp.extend(case1)
    temp.extend(case2)
    poster(temp)

def rotations(plate,rotation):
    column=[]
    line=[]

    for i in range (len(column)):

        rotation.append(column[i])
        rotation[i].reverse()

    return rotation

rotation=[]
plate1=[[0,1],[2,0]]
plate2=[[2,1],[0,1]]
plate3=[[2,2],[0,1]]
plate4=[[0,0],[2,0]]

while 1<2:

    a=eval(input("Rentrez un numéro de plateau entre 1 et 4 = "))

    if a==1:
        print("Plateau avant rotation")

        reuni()

        rotation=[]

        rotations(plate1,rotation)

        plate1=rotation

        print("======LISTE APRES ROTATION======")

        reuni()

        plate1=rotation


    if a==2:
        print("Plateau avant rotation")
        reuni()

        rotation=[]

        rotations(plate2,rotation)

        plate2=rotation

        print("======LISTE APRES ROTATION======")

        reuni()

        plate2=rotation

    if a==3:
        print("Plateau avant rotation")
        print(plate3)
        reuni()

        rotation=[]

        poster(plate3)
        rotations(plate3,rotation)

        plate3=rotation

        print(rotation)
        print("======LISTE APRES ROTATION======")

        reuni()

        plate3=rotation

    if a==4:
        print("Plateau avant rotation")
        reuni()

        rotation=[]

        rotations(plate4,rotation)

        plate4=rotation

        print("======LISTE APRES ROTATION======")

        reuni()

        plate4=rotation
        
