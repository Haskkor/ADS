import os

def somcoef(liste):
    somme = 0
    for ligne in liste:
        for i in ligne:
            somme += i
    return somme

def verifcoefligne(valeur, numligne, liste):
    somme = 0 
    for i in liste[numligne]:
        somme += i
    if somme == valeur:
        return True
    else:
        return False

def verifcoefcol(valeur, numcol, liste):
    somme = 0 
    for ligne in liste:
        somme += ligne[numcol]
    if somme == valeur:
        return True
    else:
        return False

def verifcoefdiag(valeur, numdiag, liste):
    somme = 0
    if numdiag == 0:
        diag = 0
        for ligne in liste:
            somme += ligne[diag]
            diag += 1
    if numdiag == 1:
        diag = len(liste[0]) - 1
        for ligne in liste:
            somme += ligne[diag]
            diag -= 1
    if somme == valeur:
        return True
    else:
        return False

def verifcarremagique(liste):
    coef = somcoef(liste) // 3
    for i in range(len(liste)):
        if not verifcoefligne(coef,i,liste):
            return False
        if not verifcoefcol(coef,i,liste):
            return False
        if not verifcoefdiag(coef,0,liste):
            return False
        if not verifcoefdiag(coef,1,liste):
            return False
    return True

def carremagiquenormal(liste):
    borneMax = len(liste) * len(liste[0])
    normal = False
    for i in range(borneMax):
        for j in range(len(liste)):
            for k in range(len(liste[j])):
                if liste[j][k] == i + 1:
                    normal = True
        if not normal:
            return normal
        if i + 1 == borneMax:
            return normal
        else:
            normal = False

liste = [[6,7,2],[1,5,9],[8,12,4]]

print("La somme de tous les coefficients est : " + str(somcoef(liste)))
valeur = eval(input("Saisissez une valeur : "))
numligne = eval(input("Saisissez un numero de ligne (0 - 2) : "))
print(verifcoefligne(valeur,numligne,liste))
valeur = eval(input("Saisissez une valeur : "))
numcol = eval(input("Saisissez un numero de colonne (0 - 2) : "))
print(verifcoefcol(valeur,numcol,liste))
valeur = eval(input("Saisissez une valeur : "))
numdiag = eval(input("Saisissez un numero de diagonale (0 - 1) : "))
print(verifcoefdiag(valeur,numdiag,liste))
print("Carre magique : " + str(verifcarremagique(liste)))
print("Carre magique normal : " + str(carremagiquenormal(liste)))

os.system("pause")
