
quadrant = 0 #Initialise la valeur du quadrant à 0
s = True or False
stockage2 = 0

##########################################
## Permet de tourner un quadrant choisi ##
##########################################
def Rotation(liste,quadrant):
    stock = [[0,0,0],[0,0,0],[0,0,0]]
    stock[0][2] = liste[quadrant][0][0]
    stock[1][2] = liste[quadrant][0][1]
    stock[2][2] = liste[quadrant][0][2]
    stock[0][1] = liste[quadrant][1][0]
    stock[2][1] = liste[quadrant][1][2]
    stock[0][0] = liste[quadrant][2][0]
    stock[1][0] = liste[quadrant][2][1]
    stock[2][0] = liste[quadrant][2][2]
    stock[1][1] = liste[quadrant][1][1]
    liste[quadrant] = stock
    return liste



############################################################################
# 3 Rotations dans le sens des aiguilles d'une montre pour le sens inverse #
############################################################################

def RotationsInverse(liste,quadrant):
    Rotation(liste,quadrant)
    Rotation(liste,quadrant)
    Rotation(liste,quadrant)

#########################################################
# Permet de choisir le quadrant et son sens de rotation #
#########################################################
def RotationsQuadrant(quadrant,s,liste):
    if quadrant == 0:
        if s == True:
            liste = Rotation(liste,quadrant)
        elif s == False:
            liste = RotationsInverse(liste,quadrant)
    if quadrant == 1:
        if s == True:
            liste = Rotation(liste,quadrant)
        elif s == False:
            liste= RotationsInverse(liste,quadrant)
    if quadrant == 2:
        if s == True:
            liste = Rotation(liste,quadrant)
        elif s == False:
            liste = RotationsInverse(liste,quadrant)
    if quadrant == 3:
        if s == True:
            liste = Rotation(liste,quadrant)
        elif s == False:
            liste = RotationsInverse(liste,quadrant)
    return (liste)



######################################################################
##  Permet la conversion d'une liste à 3 Dimensions en 2 Dimensions ##
######################################################################
def ConvertLISTE(liste):
    stockage2 = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
    for h in range(0,6):
        for g in range(0,6):
            if g<3 and h<3:
                stockage2[h][g] = liste[0][h][g]
            if g>=3 and h>=3:
                stockage2[h][g] = liste[3][h-3][g-3]
            if g<3 and h>=3:
                stockage2[h][g] = liste[2][h-3][g]
            if g>=3 and h<3:
                stockage2[h][g] = liste[1][h][g-3]
    return stockage2

