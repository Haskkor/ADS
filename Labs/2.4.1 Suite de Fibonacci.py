import os

def fibo(nieme):
    if nieme == 0:
        return 0
    elif nieme == 1:
        return 1
    else:
        return fibo(nieme - 1) + fibo(nieme - 2)

n = input("Saisissez un nombre : ")

print(fibo(int(n)))

os.system("pause")
