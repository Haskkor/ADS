import os

def transfo(chaine):
    if chaine == "":
        return 0
    else:
        return int(chaine)

def karatsuba(x,y):
    if x < 10 or y < 10:
        return x * y
    
    m = max([len(str(x)), len(str(y))])
    n = (m + 1) // 2
    z = 10 ** n

    x, y, z = str(x), str(y), str(z)
    temp = len(z)-1

    a = transfo(x[:-temp])
    b = transfo(x[-temp:])
    c = transfo(y[:-temp])
    d = transfo(y[-temp:])

    u = karatsuba(a, c)
    v = karatsuba(a + b, c + d)
    w = karatsuba(b, d)
    
    return u * (10 ** (2 * n)) + (v - u - w) * (10 ** n) + w

x = eval(input("Nombre un premier nombre : "))
y = eval(input("Nombre un deuxieme nombre : "))
print(str(karatsuba(x,y)))

os.system("pause")
