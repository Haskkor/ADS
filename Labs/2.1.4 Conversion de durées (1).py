import os

temps = eval(input("Saisissez en temps en secondes : "))

print(str(temps) + " secondes = ")

heures = temps // 3600
print(str(heures) + " heures,")

minutes = (temps % 3600) // 60
print(str(minutes) + " minutes,")

secondes = (temps % 3600) % 60
print(str(secondes) + " secondes.")

os.system("pause")
