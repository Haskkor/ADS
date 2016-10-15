from random import randint
listeTs2 = [[0] * 5 for i in range(5)]
def rotationaDroite(m, listes1):
    a = m -1 
    for liste2 in listes1:
        t = 0
        while(t <= m -1 ):
            listeTs2[t][a] = liste2[t]
            t += 1          
        a -= 1

def rotationaGauche(m, listes):
    a = 0
    listeTs2 = [[0] * m for i in range(m)]
   
    for liste in listes:
        t = m - 1
        z = 0
        while(t >= 0 ):
            listeTs2[z][a] = liste[t]
            z += 1
            t -= 1
        a += 1
    for a in listeTs2:
        listeCadran = a
        print(listeCadran)
        
def rotation(n, listes, numCadran, boole):
    moitie = int (n / 2)
    
    listeCadran= [[0] * 3 for i in range(moitie)]
    if(numCadran == 1):
        for i in range(moitie):
            for j in range(moitie):
                listeCadran[i][j] = listes[i][j]

    if(numCadran == 2):
            t = 0
            for i in range(moitie, n):
                u = 0
                for j in range(moitie):
                    listeCadran[t][u] = listes[i][j]
                    u = u + 1
                t = t + 1
       
    if(numCadran == 3):
            t = 0
            for i in range(moitie, n):
                u = 0
                for j in range(moitie, n):
                    listeCadran[t][u] = listes[i][j]
                    u += 1
                t += 1
    if(numCadran == 4):
            t = 0
            for i in range(moitie):
                u = 0
                for j in range(moitie, n):
                    listeCadran[t][u] = listes[i][j]
                    u += 1
                t += 1
    print("Apres rotation du Cadran", numCadran)
    """ On effectue la roation à droite ou a gauche """
    
    if(boole == True):
        rotationaDroite(moitie, listeCadran)
    if(boole == False):
        rotationaGauche(moitie, listeCadran)
    
    """ On reaffecte listeCadran à listes """
    if(numCadran == 1):
        for i in range(moitie):
            for j in range(moitie):
                listes[i][j] = listeTs2[i][j]
                
    
    if(numCadran == 2):
            t = 0
            for i in range(moitie, n):
                u = 0
                for j in range(moitie):
                    listes[i][j] = listeTs2[t][u]
                    u = u + 1
                t = t + 1
       
    if(numCadran == 3):
            t = 0
            for i in range(moitie, n):
                u = 0
                for j in range(moitie, n):
                    listes[i][j] = listeTs2[t][u]
                    u += 1
                t += 1
    if(numCadran == 4):
            t = 0
            for i in range(moitie):
                u = 0
                for j in range(moitie, n):
                    listes[i][j] = listeTs2[t][u]
                    u += 1
                t += 1

