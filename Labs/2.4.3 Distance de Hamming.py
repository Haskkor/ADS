import os

def hamm(c1,c2):
    count = 0
    for i in range(len(c1)):
        if c1[i] != c2[i]:
            count += 1
    return count

chaine1 = ""
chaine2 = ""

while chaine1 == "" :
    chaine1 = input("Saisissez la premiere chaine : ")
while chaine2 == 1 or len(chaine1) != len(chaine2):
    chaine2 = input("Saisissez la deuxième chaine : ")

result = hamm(chaine1,chaine2)
print(result)

os.system("pause")
