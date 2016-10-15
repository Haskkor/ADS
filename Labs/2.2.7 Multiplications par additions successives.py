import os

chiffre1 = input("Saisissez un premier chiffre : ")
chiffre2 = input("Saisissez un second chiffre : ")
result = 0

for i in range(chiffre2):
    result += chiffre1

print result

os.system("pause")
