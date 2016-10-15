import os

borneBasse = input("Saisissez une borne basse : ")
borneHaute = input("Saisissez une borne haute : ")

if borneBasse % 2 == 0:
    borneBasse += 2
else:
    borneBasse += 1

for i in range(borneBasse,borneHaute,2):
    print i

os.system("pause")
