import os

def syrac(a,n):
    for i in range(n):
        print(a)
        if a % 2 == 0:
            a = a // 2
        else:
            a = 3 * a + 1

a = 0
n = 0

while a < 1 :
    a = eval(input("Saisissez a : "))
while n < 1 :
    n = eval(input("Saisissez n : "))

syrac(a,n)

os.system("pause")
