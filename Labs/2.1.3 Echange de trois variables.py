import os

x = input("x : ")
y = input("y : ")
z = input("z : ")

print("x :", x, "y :", y, "z :", z)

temp = x
x = y
y = z
z = temp

print("x :", x, "y :", y, "z :", z)

os.system("pause")
