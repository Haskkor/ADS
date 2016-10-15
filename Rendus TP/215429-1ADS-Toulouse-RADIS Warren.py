                        #tableau#
plateau = [[0]*7 for i in range(8)]

plateau[6] = "-------"
plateau[7][0] = 1
plateau[7][1] = 2
plateau[7][2] = 3
plateau[7][3] = 4
plateau[7][4] = 5
plateau[7][5] = 6
plateau[7][6] = 7

for ligne in plateau:

    for x in ligne:

        print(x,' ',end='')

    print('\n')
    
                        #calcul de la colone 2#
    
s = len(plateau[2])

#print (s)#

                        #saisi du pion#

A = eval (input ("entrer le numéro de colonne comprit entre 1 et 7: "))
B = plateau [0][A-1]="X"

for ligne in plateau:
    for x in ligne:
        print(x, ' ',end='')
    print('\n')

