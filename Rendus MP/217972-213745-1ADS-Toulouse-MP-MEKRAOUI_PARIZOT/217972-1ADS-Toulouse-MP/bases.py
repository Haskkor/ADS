def getListe(n):
    liste = []
    for i in range(n):
        liste.append([])
        for j in range(n):
            liste[i].append(0)
    return liste

def afficheListe(liste):
    for i in range(len(liste)):
        print()
        for j in range(len(liste)):
            print ( liste[i][j], sep = " ", end=" ")
        print()



