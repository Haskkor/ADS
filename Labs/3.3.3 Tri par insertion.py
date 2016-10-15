import os

def triinser(liste):
    if liste[0] > liste[1]:
        liste[0], liste[1] = liste[1], liste[0]
    for i in range(2,len(liste)):
        ind = 0
        for j in range(i):
            if liste[j] < liste[i]:
                ind = j + 1
        temp = liste[i]
        for k in range(i,ind,-1):
            liste[k] = liste[k-1]
        liste[ind] = temp
        print(liste)

liste = [51,69,5,6,53,28,7,9,18,20,15,5]

print(liste)
triinser(liste)
print(liste)

os.system("pause")
