import os

def romains(dictio,rom):
    if len(rom) > 0:
        if rom[0:2] in dictio:
            return romains(dictio,rom[2:]) + dictio[rom[0:2]]
        elif rom[0] in dictio:
            return romains(dictio,rom[1:]) + dictio[rom[0]]
    else:
        return 0
             
dictio = {'I' : 1, 'IV' : 4, 'V': 5, 'IX' : 9, 'X' : 10, 'XL' : 40, 'L' : 50, 'XC' : 90, 'C' : 100, 'CD' : 400, 'D' : 500, 'CM' : 900, 'M' : 1000}
rom = input("Entrez un chiffre romain : ")
print(str(romains(dictio,rom)))

os.system("pause")


