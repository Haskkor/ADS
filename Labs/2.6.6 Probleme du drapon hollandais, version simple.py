import os

def dutchflag(liste):
    a, b, c = 0, 0, 0
    for x in liste:
        if x == 1:
            a += 1
        elif x == 2:
            b += 1
        elif x == 3:
            c += 1
    for i in range(len(liste)):
        if i < a:	
            liste[i] = 1
        elif i < a+b:
            liste[i] = 2
        else:
            liste[i] = 3

liste = [3,2,1,2,3,1,1,3,2,1,3,1,1,3,2]
dutchflag(liste)
print(liste)

os.system("pause")
