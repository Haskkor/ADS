import os

def anag(c1,c2):
    for i in range(len(c1)):
        if c1[i] not in c2:
            return False
    return True

chaine1 = ""
chaine2 = ""

while chaine1 == "" :
    chaine1 = input("Saisissez la premiere chaine : ")
while chaine2 == 1 or len(chaine1) != len(chaine2):
    chaine2 = input("Saisissez la deuxième chaine : ")

result = anag(chaine1,chaine2)
print(result)

os.system("pause")
