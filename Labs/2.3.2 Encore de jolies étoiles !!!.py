import os

nbr = 0

while nbr <= 0: 
    nbr = eval(input("Saisissez un nombre de lignes : "))

for j in range(1,nbr+1):
    ligne = ' ' * (nbr-j) + "*" * (2*j-1)
    print(ligne)

os.system("pause")
