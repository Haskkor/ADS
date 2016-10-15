import os

def cherchlist(liste,elem):
    if liste[0] == elem:
        return True
    else:
        if len(liste) > 1:
            return cherchlist(liste[1:],elem)
        else:
            return False

liste = [4,6,5,2,986,5,34,5,21,84,321]
elem = eval(input("Saisissez un element : "))

if cherchlist(liste,elem):
    print("Element present.")
else:
    print("Element absent.")
    
os.system("pause")
