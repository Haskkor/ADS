import os

def freqlettres(chaine):
    dictio = dict()
    chaine = chaine.lower()
    for i in chaine:
        if i in "abcdefghijklmnopqrstuvwxyz":
            if i in dictio:
                dictio[i] += 1
            else:
                dictio[i] = 1
    return dictio

def pangramme(chaine):
    chaine = chaine.lower()
    for i in "abcdefghijklmnopqrstuvwxyz":
        if i not in chaine:
            return False
    return True

phrase = input("Saisissez une phrase : ")
print("Dictionnaire des occurrences de: " + phrase)
dictio = freqlettres(phrase)
print(dictio)
print("Pangramme : " + str(pangramme(phrase)))

os.system("pause")
