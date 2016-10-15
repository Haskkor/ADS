import os

def trirapide(liste):
    inf = []
    pivot = []
    sup = []
    if len(liste) < 2:
        return liste
    piv = liste[0]
    for i in liste:
        if i < piv:
            inf.append(i)
        elif i > piv:
            sup.append(i)
        else:
            pivot.append(i)
    return trirapide(inf) + pivot + trirapide(sup)

liste = [51,69,5,6,53,28,7,9,18,20,15,5]

print(liste)
liste = trirapide(liste)
print(liste)

os.system("pause")

# La méthode consiste à placer un élément du tableau (appelé pivot) à 
# sa place définitive, en permutant tous les éléments de telle sorte que 
# tous ceux qui sont inférieurs au pivot soient à sa gauche et que tous 
# ceux qui sont supérieurs au pivot soient à sa droite.

# Cette opération s'appelle le partitionnement. Pour chacun des 
# sous-tableaux, on définit un nouveau pivot et on répète l'opération 
# de partitionnement. Ce processus est répété récursivement, jusqu'à ce 
# que l'ensemble des éléments soit trié.