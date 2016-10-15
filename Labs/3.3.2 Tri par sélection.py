import os

def triselec(liste):
    for i in range(len(liste)):
        indpluspetit = i
        for j in range(i+1,len(liste)):
            if liste[j] < liste[indpluspetit]:
                indpluspetit = j
        liste[i],liste[indpluspetit] = liste[indpluspetit],liste[i]
        
liste = [51,69,5,6,53,28,7,9,18,20,15,5]

print(liste)
triselec(liste)
print(liste)

os.system("pause")
