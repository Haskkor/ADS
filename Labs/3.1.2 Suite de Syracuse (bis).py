import os

def syrac(a,n,i):
    if i == n:
        return
    print(a, end=" ")
    if a % 2 == 0:
        i += 1
        syrac(a // 2,n,i)
    else:
        i += 1
        syrac(3 * a + 1,n,i)

a = eval(input("Saisissez a : "))
n = eval(input("Saisissez n : "))

syrac(a,n,0)
    
os.system("pause")
