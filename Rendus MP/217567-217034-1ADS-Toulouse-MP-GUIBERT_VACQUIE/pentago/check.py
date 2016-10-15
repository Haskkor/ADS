#checkem' quints

def linecheck(table,line):
    check=0
    
    if table[line][0]==table[line][1] and table[line][0]==table[line][2] and table[line][0]==table[line][3] and table[line][0]==table[line][4] and table[line][0]!="":
        check=table[line][0]
		
    elif table[line][1]==table[line][2] and table[line][1]==table[line][3] and table[line][1]==table[line][4] and table[line][1]==table[line][5] and table[line][1]!="":
    	check=table[line][1]
		
    return check


def rowcheck(table, row):#copy of above for now
    
	if table[row][0]==table[row][1] and table[row][0]==table[row][2] and table[row][0]==table[row][3] and table[row][0]==table[row][4] and table[row][0]!="":
		check=table[row][0]
		
	elif table[row][1]==table[row][2] and table[row][1]==table[row][3] and table[row][1]==table[row][4] and table[row][1]==table[row][5] and table[row][1]!="":
		check=table[row][1]
		
def diagcheck(table, diag):
    
	#valeur de diag:
	#deux diagonales sont plus grandes que 5: les plus grandes et celles juste à coté (petites)
	#pour les diagonales partant en haut à gauche: la grande est 1, la petite inférieure est 2 et la petite supérieure est 3
	#pour les diagonales partant en bas à droite: la grande est 4, la petite inférieure est 5 et la petite supérieure est 6
	
	check=0
	if diag==1:
		if table[0][0]==table[1][1] and table[0][0]==table[2][2] and table[0][0]==table[3][3] and table[0][0]==table[4][4] and table[0][0]!="":
			check=table[0][0]
			
		elif table[5][5]==table[1][1] and table[5][5]==table[2][2] and table[5][5]==table[3][3] and table[5][5]==table[4][4] and table[5][5]!="":
			check=table[5][5]
	
	elif diag==2:
		if table[1][0]==table[2][1] and table[1][0]==table[3][2] and table[1][0]==table[4][3] and table[1][0]==table[5][4] and table[1][0]!="":
			check=table[1][0]
			
	elif diag==3:
		if table[0][1]==table[1][2] and table[0][1]==table[2][3] and table[0][1]==table[3][4] and table[0][1]==table[4][5] and table[0][1]!="":
			check=table[0][1]
			
	elif diag==4:
		if table[0][5]==table[1][4] and table[0][5]==table[2][3] and table[0][5]==table[3][2] and table[0][5]==table[4][1] and table[0][5]!="":
			check=table[0][0]
			
		elif table[5][0]==table[1][4] and table[5][0]==table[2][3] and table[5][0]==table[3][2] and table[5][0]==table[4][1] and table[5][0]!="":
			check=table[5][5]
	
	elif diag==5:
		if table[1][5]==table[2][4] and table[1][5]==table[3][3] and table[1][5]==table[4][2] and table[1][5]==table[5][1] and table[1][5]!="":
			check=table[1][5]
			
	elif diag==6:
		if table[0][4]==table[1][3] and table[0][4]==table[2][2] and table[0][4]==table[3][1] and table[0][4]==table[4][0] and table[0][4]!="":
			check=table[0][4]
			
	return check


def wincheck(table):
	#input table à 3 dimensions
	#output la valeur ju joueur gagnant ou 3 si ex-equo ou 4 si plateau plein sans vainqueur
    
	wincount=0
	win1=0
	win2=0
	extra=0
	tampon=convert(table)
	for i in range(6):
		if linecheck(tampon,i)!=0:
			wincount=wincount+1
			
			if wincount<2 and win1==0:
				win1=linecheck(tampon,i)
				
			elif wincount==2 and win1!=linecheck(tampon,i):
				win2=linecheck(tampon,i)
				
	for i in range(6):
		if rowcheck(tampon,i)!=0:
			wincount=wincount+1
			
			if wincount<2 and win1==0:
				win1=rowcheck(tampon,i)
				
			elif wincount==2 and win1!=rowcheck(tampon,i):
				win2=rowcheck(tampon,i)
	for i in range(6):
		if diagcheck(tampon,i)!=0:
			wincount=wincount+1
			
			if wincount<2 and win1==0:
				win1=diagcheck(tampon,i)
				
			elif wincount==2 and win1!=diagcheck(tampon,i):
				win2=diagcheck(tampon,i)
				
	if win1!=0 and win2==0:
		return win1
	elif win1!=0 and win2!=0:
		return 3
	for i in range(6):
		for j in range(6):
			if tampon[i][j]=="":
				extra=1
	if extra==1:
		return 0
	else:
		return 4
