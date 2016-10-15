from bases import *
import rotations
import random, sys, pygame, time, copy
import pygame


#*********************************************************************

# Compteur avec valeur nulle au début

#*********************************************************************


check = 0

#*********************************************************************

#Alignement de n'importe quel élément p

#*********************************************************************


def check(n,table,p,j):

    if vertical(n,table,p,j) or horizontale(n,table,p,j) or diagonal1(n,table,p,j) or diagonal2(n,table,p,j):

        check = 0

        return True 

    else:

        check = 0

        return False


#*********************************************************************

# Verification d'un alignement horizontal avec p elements

#*********************************************************************


def horizontale(n,table,p,j):

    check = 0

    for i in range (0,n):

        check = 0

        for k in range(0,n-1):

            if table [ i ][ k ] == j and table [ i ][ k + 1 ] == j:

                check = check + 1

            else:

                check = 0

            if check >= p-1:

                return True

    return False


#*********************************************************************

# Alignement vertical d'éléments p

#*********************************************************************


def vertical(n,table,p,j):

    check = 0

    for i in range (0,n):

        check = 0

        for k in range(0,n-1):

            if table [ k ][ i ] == j and table [ k+1 ][ i ] == j:

                check = check + 1

            else:

                check = 0

            if check >= p-1:

                return True

            elif k+2 == n:

                break

    return False


#*********************************************************************

# Alignement diagonal bas gauche / haut bas de p éléments

#*********************************************************************


def diagonal1(n,table,p,j):

    check = 0

    for i in range(2,n):

        check = 0

        for k in range(0,i):

            if table[k][i-k] == j and table[k+1][i-k-1] == j:

                check += 1

            else:

                check = 0

            if check >= p-1:

                return True

            elif k+1 == i or i-k == 0:

                break
    check = 0

    for i in range(0,n):

        check = 0

        for k in range(n-1,i-1,-1):

            if table[k][i-(k+1)] == j and table[k-1][i+1-(k+1)] == j:

                check += 1

            else:

                check = 0

            if check >= p-1:

                return True

    else:

        return False


#*********************************************************************

#Alignement diagonal haut gauche / bas droite de p éléments

#*********************************************************************


def diagonal2(n,table,p,j):

    check = 0

    for i in range(0,n-1):

        check = 0

        for k in range(0,n-1-i):

            if table[k+1][i+k+1] == j and table[k][i+k] == j:

                check+=1

            else:

                check=0

            if check >= p-1:

                return True

    check = 0

    for i in range(0,n-1):

        check = 0

        for k in range(n-1,i,-1):

            if table[k][k-i] == j and  table[k-1][k-i-1] == j:

                    check+=1

            else:

                check=0

            if check >= p-1:

                return True

    else:

        return False


#******************************************************************************************************************************************#


print("")


##print(check(5,table,4,1))
##print(check(3,table,1,1)) 
