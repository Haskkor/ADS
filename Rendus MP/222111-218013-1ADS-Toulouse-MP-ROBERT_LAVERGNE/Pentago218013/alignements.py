import copy

def poster(liste):
    for i in range(len(liste)):

        for j in range(len(liste[i])):
            if liste[i][j] == 0:
                print(" 0 ",end="")
            if liste[i][j] == 1:
                print(" 1 ",end="")
            if liste[i][j] == 2:
                print(" 2 ",end="")

        print()

def diagonal(liste,player):
    global nombredepion
    
    taille=len(plate)
    for i in range (0,len(liste)-1):
        cpt=0
        for j in range (taille):
        
            
            
            if liste[j][i+j]==player:
                cpt=cpt+1
            if cpt>=nombredepion:
                
                return True
                
            if liste[j][i+j]!= player:
                cpt=0
        taille=taille-1

    return False





def rotations(plate,rotation):
    column=[]
    line=[]

    for i in range (len(plate)):
        column.append([])
        
        for j in range (len(plate[i])):
            column[i].append(plate[j][i])
            
    for i in range (len(column)):
        

        rotation.append(column[i])
        rotation[i].reverse()
    
    return rotation


def zero(joueur):
    
    poster(plate)
    rotation=[]
    print("------")
    print(joueur)
    if diagonal(plate,joueur):

        return True


def un (joueur,rotation1):
    
    rotation=[]
    rotations(plate,rotation)
    rotation1.extend(rotation)
    poster(rotation1)
    rotation=[]
    print("-----")
    print(joueur)
    if diagonal(rotation1,joueur):

        return True
    
    

def deux(joueur,rotation1,rotation2):
    
    rotation=[]
    rotations(rotation1,rotation)
    
    rotation2.extend(rotation)
    poster(rotation2)
    rotation=[]
    
    print("------")
    print(joueur)
    if diagonal(rotation2,joueur):

        return True

   

def trois(joueur,rotation1,rotation2,rotation3):
    
    rotation=[]
    rotations(rotation2,rotation)
    rotation3.extend(rotation)
    poster(rotation3)
    rotation=[]
    
    
    print("-------")  
    if diagonal(rotation3,joueur):

        return True
      
        
def joueurbis(joueur):


    if joueur==1:

        if zero (joueur) or  un (joueur,rotation1) or  deux(joueur,rotation1,rotation2) or trois(joueur,rotation1,rotation2,rotation3):
            print("joueur 1 gagne")
            return True
        joueur=joueur%2+1
        rotation1=[]
        rotation2=[]
        rotation3=[]
        if zero (joueur) or  un (joueur,rotation1) or  deux(joueur,rotation1,rotation2) or trois(joueur,rotation1,rotation2,rotation3):
            print("joueur 2 gagne")
            return True
def joueur2bis(joueur):
    rotation1=[]
    rotation2=[]
    rotation3=[]
    

    if joueur ==2:
        if zero (joueur) or  un (joueur,rotation1) or  deux(joueur,rotation1,rotation2) or trois(joueur,rotation1,rotation2,rotation3):
            print("joueur 2 gagne")
            return True
        joueur=joueur%2+1
        rotation1=[]
        rotation2=[]
        rotation3=[]
        print(joueur)
        
        if zero (joueur) or  un (joueur,rotation1) or  deux(joueur,rotation1,rotation2) or trois(joueur,rotation1,rotation2,rotation3):
            print ("joueur 1 gagne")
            return True    
        

     
    






plate=[[1,2,0,0,0,0],[1,2,2,0,0,0],[0,1,2,0,0,0],[0,0,0,0,2,0],[0,0,0,1,0,2],[0,0,0,0,1,0]]

player=2

nombredepion=5


if joueur2bis(player) :
    print("ok")

if joueurbis(player):
    print("okiii")

