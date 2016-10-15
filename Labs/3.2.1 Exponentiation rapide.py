import os

def expo(x,n):
    print(x)
    print(n)
    print("")
    if n == 0:
        return 1
    elif n % 2 == 0:
        return expo(x * x,n / 2)
    else:
        return x * expo(x * x,(n - 1) / 2)

x = eval(input("Saisissez un x : "))
n = eval(input("Saisissez un n : "))

print(str(expo(x,n)))
    
os.system("pause")

##Si x = 3 et n = 3
##n impair
##on retourne 3 * (expo de 3 * 3, 1)
##expo de 9 et 1
##n est impair
##on retourne 3 * (expo de 9 * 9, 0)
##expo de 81 et 0
##n est égal à 0
##on retourne 1

