import os

mot = input("Saisissez un mot : ")
trouv = True

for ind in range(len(mot)//2):
    if mot[ind] != mot[-ind - 1]:
        trouv = False

if trouv:
    print("Le mot est un palindrome.")
else:
    print("Le mot n'est pas un palindrome.")

os.system("pause")
