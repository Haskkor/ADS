import os

nbr = 0

while nbr <= 0: 
    nbr = eval(input("Saisissez un nombre de lignes : "))

for j in range(nbr,0,-1):
    print("*" * j)

os.system("pause")
