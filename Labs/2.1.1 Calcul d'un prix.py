import os

prix_unitaire = eval(input("Saisissez un prix unitaire : "))
taux_tva = eval(input("Saisissez un taux de TVA : "))
nbr_articles = eval(input("Saisissez un nombre d'articles : "))

print("Le montant total est : " + str((prix_unitaire + (prix_unitaire / 100 * taux_tva)) * nbr_articles))

os.system("pause")
