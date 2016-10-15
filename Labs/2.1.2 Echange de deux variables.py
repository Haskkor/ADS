import os

print("Echange avec affectation multiple : ")
print("")

var1, var2 = 1, 2
print("Variable 1 : ", str(var1), "Variable 2 : ", str(var2))
var1, var2 = var2, var1
print("Variable 1 : ", str(var1), "Variable 2 : ", str(var2))

print("")
print("Echange sans affectation multiple : ")
print("")

var1 = 1
var2 = 2
print("Variable 1 : ", str(var1), "Variable 2 : ", str(var2))
temp = var1
var1 = var2
var2 = temp
print("Variable 1 : ", str(var1), "Variable 2 : ", str(var2))

print("")
print("Echange avec les opérateurs + et - : ")
print("")

var1, var2 = 1, 2
print("Variable 1 : ", str(var1), "Variable 2 : ", str(var2))
var1 += var2
var2 = var1 - var2
var1 -= var2
print("Variable 1 : ", str(var1), "Variable 2 : ", str(var2))

os.system("pause")
