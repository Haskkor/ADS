import os

def fibo(nbr):
    if nbr == 0:
        return 0
    elif nbr == 1:
        return 1
    else:
        return fibo(nbr - 1) + fibo(nbr - 2)

nbr = eval(input("Saisissez un numero : "))
print(str(fibo(nbr)))
    
os.system("pause")

##0 = 0
##1 = 1
##2 = 1
##3 = 2
##4 = 3
##5 = 5
##6 = 8
##7 = 13
##8 = 21
##9 = 34
##10 = 55
