import os

nbr = 0
multip1 = "1"
multip2 = "1"
multip3 = "1"
addit1 = 2
addit2 = 1

while nbr <= 0: 
    nbr = eval(input("Saisissez un nombre de lignes : "))

for i in range(nbr):
    result = eval(multip1)
    print(multip1 + " * " + multip1 + " = " + str(result*result))
    multip1 += "1"

print("")

for i in range(nbr):
    result = eval(multip2)
    result2 = nbr * result + addit1
    print(str(nbr) + " * " + multip2 + " + " + str(addit1) + " = " + str(result2))
    multip2 += str(addit1)
    addit1 += 1

print("")

for i in range(nbr):
    result = eval(multip3)
    result2 = (nbr - 1) * result + addit2
    print(str(nbr-1) + " * " + multip3 + " + " + str(addit2) + " = " + str(result2))
    addit2 += 1
    multip3 += str(addit2)

print("")

multip4 = str(nbr)
addit3 = nbr - 2
for i in range(nbr):
    result = eval(multip4)
    result3 = nbr * result + addit3
    print(str(nbr) + " * " + multip4 + " + " + str(addit3) + " = " + str(result3))
    multip4 += str(addit3 + 1)
    addit3 -= 1

os.system("pause")
