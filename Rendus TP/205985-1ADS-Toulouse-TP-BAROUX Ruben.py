def initiialisation(): # question bonus
    n = int(input("Saisissez le nombre de lignes: "))

    # On verifie que n et m sont positif, sinon on redemande n et m

    while n <= 3:
        n = int(input("Saisissez le nombre de lignes: "))

    m = int(input("Saisissez le nombre de colonnes: "))
    while m <= 3:
        m = int(input("Saisissez le nombre de colonnes: "))
        print('/n')
    p = 0
    while p != 0:
        if  3<= m <= 5:
            p = 3
        elif 6<= m <=8:
            p = 4
        elif 0<= m <= 2:
            p = 0
        else:
            p = m - 3


    plateau(n, m)


def plateau(n, m):  # création du plateau 2.2



    plateau = [[""] * m for i in range(n)]
    for ligne in plateau:
        for x in plateau:
            print('|  ', end='')
        print('|')
    for colonne in plateau:
        print(' -', end=" ")

    print(' 1   2   3   4   5   6   7', end='')    # n'arrive pas a la faire passer dessous

    '''for i in range(1, n + 1):                    #cela serait utiliser pour afficher ou les joueurs ont placé leurs pions
        for j in range(1, m + 1):
            if plateau[i-1][j-1] == True:
                print('X', end='')
            else:
                print('O', end='')'''


def coup(plateau, n, m):  #2.3.1 il faut pouvoir compter une colonne
    l = [int(x) for x in n]      # pour que l soit une liste
    print(l)
                                # ensuite il daudrait pouvoir comparer les listes a chaque indice
                                # et ensuite stoker la valeur pour pouvoir l'utiliser par la suite



initiialisation()
