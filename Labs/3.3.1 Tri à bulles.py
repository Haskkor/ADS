import os

def triabulle(liste):
    invers = True
    while invers:
        invers = False
        for i in range(1,len(liste)):
            if liste[i] < liste[i-1]:
                liste[i],liste[i-1] = liste[i-1],liste[i]
                invers = True
            
liste = [51,69,5,6,53,28,7,9,18,20,15,5]

print(liste)
triabulle(liste)
print(liste)

os.system("pause")
