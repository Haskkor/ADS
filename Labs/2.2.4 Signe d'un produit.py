import os

chiffre1 = input("Saisissez un premier chiffre : ")
chiffre2 = input("Saisissez un second chiffre : ")

if chiffre1 * chiffre2 < 0:
    print("Le produit des 2 nombres est negatif.")
elif chiffre1 * chiffre2 == 0:
    print("Le produit des 2 nombres est nul.")
elif chiffre1 * chiffre2 > 0:
    print("Le produit des 2 nombres est positif.")

os.system("pause")
