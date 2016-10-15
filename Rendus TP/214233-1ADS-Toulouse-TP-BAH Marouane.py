
plateau = [[0] *7 for i in range(6)] # crée un plateau de 6 lignes et 7 colonnes

for ligne in plateau: # la variable ligne prend la valeur de plateau
    for x in ligne:   
        print("|",x,'',end='')
    print('\n')
plateau0 = plateau [0] 
plateau1 = plateau [1] 
plateau2 = plateau [2] 
plateau3 = plateau [3]
plateau4 = plateau [4] 
plateau5 = plateau [5] 


plateautotal = (plateau0,plateau1,plateau2,plateau3,plateau4,plateau5)
for pl in plateau0:
    if pl != 0 :
        print("*")
    else:
        print("**")
            
            
    
        
