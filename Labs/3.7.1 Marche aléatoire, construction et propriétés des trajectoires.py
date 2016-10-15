from random import *

def listepos(etapes, proba):
    liste = [0] * (etapes + 1)
    for i in range(1,etapes + 1):
        if random() > proba:
            liste[i] = liste[i - 1] - 1
        else:
            liste[i] = liste[i - 1] + 1
    return liste

def firstzero(liste):
    for i in range(1, len(liste)):
        if liste[i] == 0:
            return i
    return -1

def nbrzero(liste):
    nbr = 0
    for i in range(1, len(liste)):
        if liste[i] == 0:
            nbr += 1
    return nbr

def maxval(liste):
    listeabsolue = [abs(i) for i in liste]
    return max(listeabsolue), listeabsolue.index(max(listeabsolue))     

liste = listepos(10,0.5)
print(liste)
print(firstzero(liste))
print(nbrzero(liste))
print(maxval(liste))

