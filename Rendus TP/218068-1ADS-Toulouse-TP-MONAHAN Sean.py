# 2.1 - grille au debut de la partie
plateau = [0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]
for ligne in plateau:
    for x in ligne:
        print(x,'', end='')
    print ('\n')

# 2.2 decoupage du plateau en plusieurs listes
# plateau = [L1], [L2], [L3], [L4], [L5], [L6], [L7]

L1 = L2 = L3 = L4 = L5 = L6 = L7 = [0,0,0,0,0,0]
l = eval(input())  #choisir la liste
a = eval(input())  #choisir l'emplacement(i)
def conversion(l):
        if l[a] == 0:
            s.insert(a,'')
        elif l[a] == 1:
            s.insert(a,'x')
        else:
            s.insert(a,'o')
print(l)


#plateau avec les bords
plateau2 = [["|",0,"|",0,"|",0,"|",0,"|",0,"|",0,"|",0,"|"],["|",0,"|",0,"|",0,"|",0,"|",0,"|",0,"|",0,"|"],["|",0,"|",0,"|",0,"|",0,"|",0,"|",0,"|",0,"|"],["|",0,"|",0,"|",0,"|",0,"|",0,"|",0,"|",0,"|"],["|",0,"|",0,"|",0,"|",0,"|",0,"|",0,"|",0,"|"],["|",0,"|",0,"|",0,"|",0,"|",0,"|",0,"|",0,"|"]]
for ligne2 in plateau2:
    for x in ligne2:
        print(x,'', end='')
    print ('\n')

#2.3.1 calcul d'une hauteur de colonne
#C colonne n°p
#C1 = L1[0],...,L6[0]

p = eval(input())  #choisir la colonne
n = 0              #nbr de pions
C = [L1[p-1], L2[p-1], L3[p-1], L4[p-1], L5[p-1], L6[p-1] ]
def nbpions(plateau):
    if L1[p-1] == 0:    #0 = pas de pion donc n ne change pas
        n = n
    else:
        n = n+1         #n != 0 il y a un pion donc n=n+1

    if L2[p-1] == 0:
        n = n
    else:
        n = n+1

    if L3[p-1] == 0:
        n = n
    else:
        n = n+1

    if L4[p-1] == 0:
        n = n
    else:
        n = n+1

    if L5[p-1] == 0:
        n = n
    else:
        n = n+1

    if L6[p-1] == 0:
        n = n
    else:
        n = n+1

print(n)

# 2.3.2 - fonction montrant si une colonne est pleine

p = eval(input("choisir la colonne: "))
C = [L1[p-1], L2[p-1], L3[p-1], L4[p-1], L5[p-1], L6[p-1] ]
def Cplein(plateau):
    if L1[p-1] == 0:
        print("la colonne n'est pas pleine")
    else:
        print("la colonne est pleine") #les pions tombent, donc si une case de la premiere ligne a un pion la colonne est remplie.


# 2.3.3 Pose d'un pion d'un joueur

def joueur(plateau):
    j = eval(input("choisir une colonne non pleine entre 1 et 7: "))
print(j)


# 2.3.4 pose d'un pion par l'ordinateur

def AI(plateau):
    k = randint(1,7)
print(k)















