#Pour l'affichage du plateau

def Back(initiale):
    initiale=[[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]

    for i in range (0,6): 
        for j in range (0,7):
            if initiale [i][j]==0:
                initiale[i][j]= ' '

            elif initiale [i][j]==1:
                initiale[i][j]= 'o'

            elif initiale [i][j]==-1:
                initiale[i][j]= 'x'

    return initiale
    initialeb= Back(initiale)
    
    import copy
    initialeb = copy.deepcopy(initiale)
print( Back('initiale'))
    


#L'organisation des cases

for i in range (0,6): 
    for j in range (0,7):
        print (initialeb[j]) 
        print ('\n')
print(' ' + '1'+ '       ' +'2' + '     ' + '3' + '     ' + '4' + '     ' + '5' + '     '+ '6' + '     ' + '7') 
        
            
            









    
