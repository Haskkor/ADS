import os

nbr = input("Saisissez un nombre de carres : ")
somme = 0

for i in range(nbr+1):
    somme = somme + i * i

print("Somme des n premiers carres : " + str(somme))

os.system("pause")
