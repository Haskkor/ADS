import os

def estdivis(nbr,divis):
    if nbr % divis == 0:
        return True
    else:
        return False

def sommdivis(nbr):
    somm = 0
    for i in range(1,nbr):
        if estdivis(nbr,i):
            somm += i
    return somm

def estparf(nbr):
    if sommdivis(nbr) == nbr:
        return True
    else:
        return False
                
def nbrparf(n):
    for i in range(n):
        if estparf(i):
            print(i)

n = 0

while n < 1 :
    n = eval(input("Saisissez un nombre de termes : "))

nbrparf(n)

os.system("pause")
