import os

def cubes(n):
    print(n)
    if n == 1:
        return 1
    else:
        return n**3 + cubes(n - 1)

n = eval(input("Saisissez n : "))


print(cubes(n))
    
os.system("pause")
