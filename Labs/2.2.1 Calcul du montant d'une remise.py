import os

remise = 0
montant = input("Saisissez un montant : ")
montant = float(montant)

if montant >= 100 and montant <= 500:
    remise = montant / 100 * 5
elif montant > 500:
    remise = montant / 100 * 8
    
print "La remise est de : " + str(remise)

os.system("pause")
