stockage = 0

#################################################################
##  Permet le passage d'une liste 2 Dimensions en 3 Dimensions ##
#################################################################

def ConvertListe(plateau):
    stockage = [[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]]
    stockage[0][0][0] = plateau[0][0]
    stockage[0][0][1] = plateau[0][1]
    stockage[0][0][2] = plateau[0][2]
    stockage[0][1][0] = plateau[1][0]
    stockage[0][1][1] = plateau[1][1]
    stockage[0][1][2] = plateau[1][2]
    stockage[0][2][0] = plateau[2][0]
    stockage[0][2][1] = plateau[2][1]
    stockage[0][2][2] = plateau[2][2]

    stockage[1][0][0] = plateau[0][3]
    stockage[1][0][1] = plateau[0][4]
    stockage[1][0][2] = plateau[0][5]
    stockage[1][1][0] = plateau[1][3]
    stockage[1][1][1] = plateau[1][4]
    stockage[1][1][2] = plateau[1][5]
    stockage[1][2][0] = plateau[2][3]
    stockage[1][2][1] = plateau[2][4]
    stockage[1][2][2] = plateau[2][5]

    stockage[2][0][0] = plateau[3][0]
    stockage[2][0][1] = plateau[3][1]
    stockage[2][0][2] = plateau[3][2]
    stockage[2][1][0] = plateau[4][0]
    stockage[2][1][1] = plateau[4][1]
    stockage[2][1][2] = plateau[4][2]
    stockage[2][2][0] = plateau[5][0]
    stockage[2][2][1] = plateau[5][1]
    stockage[2][2][2] = plateau[5][2]

    stockage[3][0][0] = plateau[3][3]
    stockage[3][0][1] = plateau[3][4]
    stockage[3][0][2] = plateau[3][5]
    stockage[3][1][0] = plateau[4][3]
    stockage[3][1][1] = plateau[4][4]
    stockage[3][1][2] = plateau[4][5]
    stockage[3][2][0] = plateau[5][3]
    stockage[3][2][1] = plateau[5][4]
    stockage[3][2][2] = plateau[5][5]
    return stockage


