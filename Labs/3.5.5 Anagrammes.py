import os

def anag(mot):
    if len(mot) <= 1:
        return(mot)
    elif len(mot) == 2:
        return list(set([mot,mot[1]+mot[0]]))
    else:
        return list(set([mot[i] + d for i in range(len(mot)) for d in anag(mot[:i]+mot[i+1:])]))
 
mot = input("Saisissez un mot : ")
print(anag(mot))

os.system("pause")

##albi
##pour i dans le mot
##    pour d dans anag(""+"lbi")
##        a + res anag(""+"lbi")
##
##lbi
##pour i dans le mot
##    pour d dans anag(""+"bi")
##        l + res anag(""+"bi")
##
##bi + ib
##lbi + lib
##
##lbi
##pour i dans le mot
##    pour d dans anag("l"+"i")
##        b + res anag("l"+"i")
##
##li il
##bil bli
##...
##ilb ibl
##albi alib abil abli ailb aibl
##...
##bali...
