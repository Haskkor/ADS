import os

def combien(nombre,liste):
    num = 0
    for i in liste:
        temp = str(i)
        if int(temp[0]) == nombre:
            num += 1
    return num

def nombresnombres(liste):
    dictio = dict()
    for i in range(1,9):
        dictio[i] = combien(i,liste)
    return dictio

nombres = [80,99,20,53,59,15,81,40,52,24,20,42,15,5,87,23,25,9,82,11]

print(nombres)
print(nombresnombres(nombres))

os.system("pause")
