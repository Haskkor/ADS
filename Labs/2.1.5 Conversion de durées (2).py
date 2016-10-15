import os

heures = eval(input("Saisissez un nombre d'heures : "))
minutes = eval(input("Saisissez un nombre de minutes : "))
secondes = eval(input("Saisissez un nombre de secondes : "))

print(str(heures) + " heures, " + str(minutes) + " minutes, " + str(secondes) + " secondes : ")

total = secondes + minutes * 60 + heures * 3600
print(str(total) + " secondes.")

os.system("pause")
