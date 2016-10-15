import os

def dutchflag(liste):
    a, b, c = 0, 0, len(liste) - 1
    while b <= c:
        if liste[b] == 2:
            b += 1
        elif liste[b] == 1:
            liste[a], liste[b] = liste[b], liste[a]
            a += 1
            b += 1
        elif liste[b] == 3:
            liste[b], liste[c] = liste[c], liste[b]
            c -= 1

liste = [3,2,1,2,3,1,1,3,2,1,3,1,1,3,2]

dutchflag(liste)
print(liste)

os.system("pause")
