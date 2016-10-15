# fontion pour dessiner un plateau de taille nxn
def plateau0(n):
    return [[0 for j in range (n)] for i in range (n)]
# fontion pour afficher un plateau en mode console
def affichage(plateau):
    for ligne in plateau:
        line = ""
        for i in ligne:
            if i == 0:
                line += "0 "
            if i == 1:
                line += "1 "
            if i == 2:
                line += "2 "
        print (line)
j = 1
plateau = plateau0(6)

# coded by amir tifour, rachid medjoub and maxime ouvrard