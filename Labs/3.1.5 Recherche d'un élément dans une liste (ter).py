import os

def cherchlist(liste,elem,i):
    if liste[0] == elem:
        return i
    else:
        if len(liste) > 1:
            i += 1
            return cherchlist(liste[1:],elem,i)
        else:
            return -1

liste = [4,6,5,2,986,5,34,5,21,84,321]
elem = eval(input("Saisissez un element : "))

print(str(cherchlist(liste,elem,0)))
    
os.system("pause")
