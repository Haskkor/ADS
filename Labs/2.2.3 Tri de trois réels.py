import os

chiffre1 = eval(input("Saisissez un premier chiffre : "))
chiffre2 = eval(input("Saisissez un second chiffre : "))
chiffre3 = eval(input("Saisissez un troisieme chiffre : "))

while chiffre1 > chiffre2 or chiffre1 > chiffre3 or chiffre2 > chiffre3:
    if chiffre1 > chiffre2:
        chiffre1, chiffre2 = chiffre2, chiffre1
    elif chiffre2 > chiffre3:
        chiffre2, chiffre3 = chiffre3, chiffre2
    elif chiffre1 > chiffre3:
        chiffre1, chiffre3 = chiffre3, chiffre1

print("Les chiffres dans l'ordre croissant : " + str(chiffre1) + " " +
      str(chiffre2) + " " + str(chiffre3))

os.system("pause")

    
