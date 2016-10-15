import os

def fusion(liste1,liste2) :
    if liste1 == []:
        return liste2
    if liste2 == []:
        return liste1
    
    if liste1[0] < liste2[0]:
        return [liste1[0]] + fusion(liste1[1:], liste2)
    else:
        return [liste2[0]] + fusion(liste1, liste2[1:])


def trifusion(liste) :
    if len(liste) <= 1:
        return liste
    
    liste1 = [liste[x] for x in range(len(liste) // 2)]
    liste2 = [liste[x] for x in range(len(liste) // 2, len(liste))]
    
    return fusion(trifusion(liste1),trifusion(liste2))


liste = [51,69,5,6,53,28,7,9,18,20,15,5]

print(liste)
liste = trifusion(liste)
print(liste)

os.system("pause")


# https://openclassrooms.com/courses/le-tri-fusion
