import os

annee = eval(input("Saisissez une année (entre 1900 et 2099) : "))

n = annee - 1900
a = n % 19
b = (7 * a + 1) // 19
c = (11 * a - b + 4) % 29
d = n // 4
e = (n - c + d + 31) % 7

print("Date de pâques : 31 mars + ", str(25 - c - e), " jours.")

os.system("pause")
