import os
from decimal import *

def histo(dictio):
    som = 0
    for val in dictio.values():
        som += val
    for clef,val in dictio.items():
        temp = val / som * 100
        if temp > 10:
            temp = str(temp)
            temp = temp[:5]
            ligne = clef + " :" + temp + " % "
        else:
            temp = str(temp)
            temp = temp[:4]
            ligne = clef + " : " + temp + " % "
        temp = val * 100 // som
        if (float(temp) + 0.5) < (val / som * 100): 
            for i in range(temp + 1):
                ligne += "*"
        else:
            for i in range(temp):
                ligne += "*"
        print(ligne)        

dictio = {'i' : 3, 'o' : 1, 'n': 1, 'm' : 1, 'l' : 1, 'c' : 1, 'b' : 1,
          'a' : 3, 'f' : 1, 'e' : 2, 's' : 1, 'r' : 1, 'u' : 2, 't' : 3}
histo(dictio)

os.system("pause")
