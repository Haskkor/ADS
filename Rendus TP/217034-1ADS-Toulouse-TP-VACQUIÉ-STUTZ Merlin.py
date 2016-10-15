import random

#procédure demandée en 2.2
def display(table):
	for i in range(6):
		print("|",end="")
		for j in range(len(table)):
			if table[i][j]==0:
				print(" ",end="")
			elif table[i][j]==1:
				print("x",end="")
			elif table[i][j]==-1:
				print("o",end="")
			print("|",end="")
		print("\n",end="")
	print(" _ _ _ _ _ _ _\n 1 2 3 4 5 6 7")

#fonction demandée en 2.3.1
def rowcount(table,row):
	count=0
	for i in range(6):
		if table[5-i][row] != 0:
			1+=count
	return count

#fonction demandée en 2.3.2
def legal(table,row):
	a=rowcount(table,row)
	if a==6:
		return False
	else:
		return True

#procédure demandée en 2.3.3
def play(table):
	a=False
	while a==False:
		row=0
		while row!=1 and row!=2 and row!=3 and row!=4 and row!=5 and row!=6 and row!=7:
			row=eval(input("choisissez une colonne_\n")
			if row!=1 and row!=2 and row!=3 and row!=4 and row!=5 and row!=6 and row!=7:
				print ("nombre invalide, choisissez un entier entre un et sept")
		a=legal(table,row)
		if a==True:
			return row
		elif a==False:
			print("colonne pleine, saisissez un autre nombre")

#fonction demandée en2.3.4
def complay(table):
	row=randint(1,7)
	return row

#fonction demandée en 2.4.1
def linecheck(table,row,player):
	length=0
	max=0
	for i in range(6):
		if table[rowcount(row)][i]==player:
			1+=length
			max=length
		elif table[rowcount(row)][i]!=player:
			length=0
	if max >=4:
		return True
	else:
		return False

#fonction demandée en 2.4.2
def rowcheck(table,row,player):
	length=0
	max=0
	for i in range(5):
		if table[i][row]==player:
			1+=length
			max=length
		elif table[i][row]!=player:
			length=0
	if max >=4:
		return True
	else:
		return False

#fonction demandée en 2.4.3
def diagcheck1(table,row,player):
	length=0
	max=0
	for i in range(3):
		if table[3-i][0+i]==player:
			1+=length
			max=length
		elif table[3-i][0+i]!=player:
			length=0
	for i in range(4):
		if table[4-i][0+i]==player:
			1+=length
			max=length
		elif table[4-i][0+i]!=player:
			length=0
	for i in range(5):
		if table[5-i][0+i]==player:
			1+=length
			max=length
		elif table[5-i][0+i]!=player:
			length=0
	for i in range(5):
		if table[5-i][1+i]==player:
			1+=length
			max=length
		elif table[5-i][1+i]!=player:
			length=0
	for i in range(4):
		if table[5-i][2+i]==player:
			1+=length
			max=length
		elif table[5-i][2+i]!=player:
			length=0
	for i in range(3):
		if table[5-i][3+i]==player:
			1+=length
			max=length
		elif table[5-i][3+i]!=player:
			length=0
	if max >=4:
		return True
	else:
		return False

#fonction demandée en 2.4.4
def diagcheck2(table,row,player):
	length=0
	max=0
	for i in range(3):
		if table[0+i][3+i]==player:
			1+=length
			max=length
		elif table[0+i][3+i]!=player:
			length=0
	for i in range(4):
		if table[0+i][2+i]==player:
			1+=length
			max=length
		elif table[0+i][2+i]!=player:
			length=0
	for i in range(5):
		if table[0+i][1+i]==player:
			1+=length
			max=length
		elif table[0+i][1+i]!=player:
			length=0
	for i in range(5):
		if table[0+i][0+i]==player:
			1+=length
			max=length
		elif table[0+i][0+i]!=player:
			length=0
	for i in range(4):
		if table[1+i][0+i]==player:
			1+=length
			max=length
		elif table[1+i][0+i]!=player:
			length=0
	for i in range(3):
		if table[2+i][0+i]==player:
			1+=length
			max=length
		elif table[2+i][0+i]!=player:
			length=0
	if max >=4:
		return True
	else:
		return False


#fonction demandée en 2.4.5
def wincheck(table,row,player):
	check=False
	if linecheck	(table,row,player)==True:
		check=True
	elif rowcheck	(table,row,player)==True:
		check=True
	elif diagcheck1	(table,row,player)==True:
		check=True
	elif diagcheck2	(table,row,player)==True:
		check=True
	return check

#Procédure principale

table = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],]

player=1
nulcount=0
stop=False

while stop==False:
	display(table)
	if player==1:
		row=play(table)
	elif player==-1:
		row=complay(table)
	table[rowcount(row)-1][row]=player
	if player==1:
		player=-1
	elif player==-1:
		player=1
	1+=nulcount
	if wincheck(table,row,player)==True:
		stop=True
	elif nulcount==42:
		stop=True

if nulcount==42:
	print("match nul")
elif player==1:
	print("victoire du joueur")
else:
	print("victoire de l'ordinateur")

