n = eval(input("Entrer un nombre de lignes/colonnes: ")) #Sert a parametrer le nombre de lignes et le nombre de colonnes

def plateau(n):#Défini le plateau en fonction de l'entier n
    plateau = [[0] * n for i in range(n)]
    print(plateau(n))

def verifListe(liste):
    print(liste)


