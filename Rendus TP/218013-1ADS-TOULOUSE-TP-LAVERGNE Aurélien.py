

#########################
#ALGORITHMIQUE EN PYTHON#
#########################


#[consigne 2.1] IMPLEMENTATION DU PLATEAU#


plateau = [[0]*7 for i in range(6)]

plateau[0][6] = "0 |"
plateau[1][6] = "0 |"
plateau[2][6] = "0 |"
plateau[3][6] = "0 |"
plateau[4][6] = "0 |"
plateau[5][6] = "0 |"
for ligne in plateau:
    for x in ligne:
        print('|', x, end=' ')
    print('\n')
plateau2 = [[ 1, 2, 3, 4, 5, 6, 7] for i in range(1)]
for ligne in plateau2:
    for y in ligne:
        print(' ',y, end=' ')
    print('\n')


#[consigne 2.2] AFFICHAGE DU PLATEAU#

plateau = [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]
plateau[0][6] = "0 |"
plateau[1][6] = "0 |"
plateau[2][6] = "0 |"
plateau[3][6] = "0 |"
plateau[4][6] = "0 |"
plateau[5][6] = "0 |"
for ligne in plateau:
    for x in ligne:
        print('|', x, end=' ')
    print('\n')
plateau2 = [[ 1, 2, 3, 4, 5, 6, 7] for i in range(1)]
for ligne in plateau2:
    for y in ligne:
        print(' ',y, end=' ')
    print('\n')

n= input(("Entrez le numéro de la ligne à jouer: "))

b= input(("Entrez le numéro de la colonne à jouer: "))



    
