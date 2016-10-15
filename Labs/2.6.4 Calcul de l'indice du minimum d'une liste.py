import os

# ATTENTION : il y a ici, 2 solutions de proposées pour le même problème

def indexpluspetit(liste):
    temp = liste[0]
    ind = 0
    for i in range(1,len(liste)):
        if liste[i] < temp:
            temp = liste[i]
            ind = i
    return ind

def indexpluspetit2(liste):
    pluspetit = min(liste)
    return liste.index(pluspetit)

liste = [5,62,7,9,356,2,165,48,6,651,3]

print("L'indice du plus petit element est : " + str(indexpluspetit(liste)))

os.system("pause")
