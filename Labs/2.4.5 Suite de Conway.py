import os

def findresult(res):
    cnt = 1
    result = ""
    for i in range(len(res)):
        if i + 1 <= len(res) - 1 :
            if res[i+1] == res[i]:
                cnt += 1
                continue
        result = result + str(cnt) + res[i]
        cnt = 1
    return result
                
def conw(n):
    result = "1"
    print("Terme 1 = " + result)
    for i in range(n) :
        result = findresult(result)
        print("Terme " + str(i + 2) + " = " + result)

n = 0

while n < 1 :
    n = eval(input("Saisissez un nombre de termes : "))

conw(n)

os.system("pause")
