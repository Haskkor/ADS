import os

# ATTENTION : il y a ici, 2 solutions de proposées pour le même problème

def comptoccu(elem,liste):
    nbr = 0
    for x in liste:
        if x == elem:
            nbr += 1
    return nbr

def comptoccu2(elem,liste):
	return liste.count(elem)

liste = ["a","b","c","d","e","e","e","b","a"]
elem = input("Saisissez un element : ")

print("Votre element est present " + str(comptoccu(elem,liste)) + " fois.")

os.system("pause")
