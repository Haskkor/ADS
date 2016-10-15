
##########################
###AFFICHAGE DU PLATEAU###
##########################

##paramètre du début
plateau = [[" "]*7 for i in range(6)] ##le nombre de colonne et de ligne


def affichageplateau():  ##le plateau
    for ligne in plateau:
        for x in ligne:
            print('|',x,'|',end='')
        print('\n')

def numerotation(): ##le numéro de chaque colonne
    print (' ','_','  ','_','  ','_','  ','_','  ','_','  ','_','  ','_')
    print('\n')
    print (' ',1,'  ',2,'  ',3,'  ',4,'  ',5,'  ',6,'  ',7)

def joueur1(): ##Quel case le joueur 1 veut jouer
    print("joueur 1 ")
   # ligne = eval(input("saisir la ligne : "))
    colonne = eval(input("saisir la colonne : "))

    plateau[5][colonne-1] = 0    ##car ça commence a 0 donc "-1" pour le remettre en normal
    print(affichageplateau())

def joueur2(): ##Quel case le joueur 2 veut jouer
    print("joueur 2 ")
   # ligne = eval(input("saisir la ligne : "))
    colonne = eval(input("saisir la colonne : "))

    plateau[5][colonne-1] = "x"
    print(affichageplateau())
    

affichageplateau()
numerotation()
joueur1()
joueur2()





## j'ai essayé mais je n'y arrive plus...
