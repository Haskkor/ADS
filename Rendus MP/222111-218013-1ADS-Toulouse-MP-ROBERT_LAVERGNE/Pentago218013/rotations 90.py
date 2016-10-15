################################################################################
#Même chose pour réaliser cette fois une rotation de 90 degrés dans le sens    #
#contraire des aiguilles d’une montre.                                         #
################################################################################


def platesize(line,column,plate):
    
       
    cpt=0
        
    if cpt != (line*line):
        for i in range (line):
            plate.append ([])
            
            for j in range (line):
                nbr = eval(input("Rentrez un nombre entre 0 et 2 = "))
                plate[i].append(nbr)
                cpt=cpt+1
            
        if cpt==(ligne*ligne):
            
            return plate   



def afficheplateau(liste):
    for i in range(len(liste)):
        
        for j in range(len(liste[i])):
            if liste[i][j] == 0:
                print("0",sep="",end="")
            if liste[i][j] == 1:
                print("1",sep="",end="")
            if liste[i][j] == 2:
                print("2",sep="",end="")
        print()

    
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


rotation=[]
plate = [[1,2,0,0,0,0],[1,0,2,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,0,0],[0,0,0,0,1,0]]


afficheplateau(plate)

rotations(plate,rotation)
print ("")
afficheplateau(rotation)



