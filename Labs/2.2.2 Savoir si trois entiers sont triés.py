import os

chiffre1 = input("Saisissez un premier chiffre : ")
chiffre2 = input("Saisissez un second chiffre : ")
chiffre3 = input("Saisissez un troisieme chiffre : ")

if chiffre3 > chiffre2 and chiffre2 > chiffre1:
    print("Les chiffres sont dans l'ordre croissant.")
else:
    print("Les chiffres ne sont pas dans l'ordre croissant.")

os.system("pause")
