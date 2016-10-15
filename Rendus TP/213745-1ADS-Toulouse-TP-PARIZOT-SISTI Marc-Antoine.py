import os

__auteur__ = "Marc-Antoine_ID: 213745"

#########################
##### Puissance 4 #######
#########################
    ##+bonus##
    ##########

#on va entrer les lignes et colonnes pour jouer avec
#le plateau de taille qui nous convient
nbrlpl = eval(input("Combien de lignes voulez-vous ? : "))
nbrcpl = eval(input("Combien de colonnes voulez-vous? : "))
joueur= [1,2]

def afficherplateau(liste): #fonction qui va décrire le plateau
    for i in liste:
        ligne = "|"
        for j in i:
            if j == 0:
                ligne += "  |"
            elif j == 1:
                ligne += " x |"
            elif j == -1:
                ligne += " o |"
        print(ligne)

plateau = [[0] *nbrcpl  for i in range(nbrlpl)]# il va créer le plateau

afficherplateau(plateau)



def placerpion(joueur,liste): # on va faire choisir aux joueurs ou placer le pions
    ligne = eval(input("Saisissez un numero de ligne (1-"+ str(nbrlpl)+ ") :")) - 1
    colonne = eval(input("Saisissez un numero de colonne (1-"+ str(nbrcpl)+ ") :")) - 1
    while liste[ligne][colonne] != 0:
        ligne = eval(input("Saisissez un numero de ligne (1-"+ str(nbrlpl)+ ") :")) - 1
        colonne = eval(input("Saisissez un numero de colonne (1-"+ str(nbrcpl)+ ") :")) - 1
    liste[ligne][colonne] = joueur


def ordiplacepion(ordi,liste1): # on va faire jouer l'ordi
    ligne1 = random.randint(1,nbrlpl) -1 #une ligne au hazard
    colonne1 =random.randint(1,nbrcpl)-1# une colonne au hazard
    while liste[ligne1][colonne1] != 0:
        ligne1 = random.randint(1,nbrlpl)-1
        colonne1 =random.randint(1,nbrcpl)-1
    liste1[ligne1][colonne1] = ordi
    print("L'ordinateur a joué son pion ligne : " + str (ligne1) + "et colonne" +str(colonne1)+".")

def colonneplaine (liste):
    for i in liste: # on va vérifié dans liste si une rangé est rempli et renvoier valeur
        for j in i:
            if j == 0:
                return True
    return False


#def 4horizontal ():




#def 4verticale ():




#def 4diagohaut ():




#def 4diagobas ():


#def ungagnant ():
#désigne qui a gagner

while colonneplaine(plateau):
    placerpion(joueur,plateau)
    afficherplateau(plateau)
   

#if joueur ==1 :
   # print("victoire du joueur !")
    #affichplateau(plateau)
#elif ordi==1 :
   # print("victoire de l'ordi !")
   # affichplateau(plateau)
    
#else:
    #print("Match nul !")
   # affichplateau(plateau)





    
os.system("pause")
