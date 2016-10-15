#déroulement de la partie/features autour du jeu

def Sauvegarde(table,click,coorX,coorY):    #Permet d'enregistrer la partie
    stockT=[[["","",""],["","",""],["","",""]],[["","",""],["","",""],["","",""]],[["","",""],["","",""],["","",""]],[["","",""],["","",""],["","",""]]]
    stockC=0
    
    if coorX>=770 and coorX<=950 and coorY>=122 and coorY<=147:
        
        if click==1:
            FST=open(SauvegardeT.py, 'wb')              #Fichier Stock Table
            FST.write(str(table))
            FST.close()

            FSC=open('SauvegardeC.txt', 'w')            #Fichier Stock Click
            FSC.write("2")#     <------- si click=1 on met click=2 dans la Sauvergarde, car lorsqu'on va apellé la Sauvegarde, les clics vont s'intervertir dans le While InProgress
            FSC.close()#                                                                                                                            et on reviendra à 1                            
            
            
        elif click==2:
            FST=open('SauvegardeT.py', 'w')
            FST.write(str(table))
            FST.close()

            FSC=open('SauvegardeC.txt', 'w')
            FSC.write("1")#     <------ Même chose ici
            FSC.close
            
        if click==2:
            click=1

        else:
            click=2


def JouerSauvegarde(table,click,coorX,coorY):   #Permet de jouer la partie enregistrée
    
    if click==0:
        
        if coorX>=590 and coorX<=903 and coorY>=460 and coorY<=508:
            FST=open('SauvegardeT.py', 'r')
            table=FST.read()
            FST.close()

            FSC=open('SauvegardeC.txt', 'r')
            click=FSC.read()
            FSC.close()
            
            window.fill(GREY)
            print
            return table, click
        else:
            return table, click
    else:
        return table,click

def NewGame(coorX,coorY,table,click,joueur,clickControle1,clickControle2): #Initialisation les variables pour nouvelle partie
    
    if click==0: #Click=0 signifie que l'on est sur la page de démarage avec ecrit Pentago

        if coorX>=140 and coorX<=408 and coorY>=460 and coorY<=508:     #Check Position Button Nouvelle Partie

            table=[[["","",""],["","",""],["","",""]],[["","",""],["","",""],["","",""]],[["","",""],["","",""],["","",""]],[["","",""],["","",""],["","",""]]]
            affichage(table)
            joueur=1
             
            return table,click,joueur,0,0

        else:
            return table,click,joueur,0,0

    else:
    
        if coorX>770 and coorX<960 and coorY>90 and coorY<118 :     #Check position button Nouvelle partie en jeu
            
            table=[[["","",""],["","",""],["","",""]],[["","",""],["","",""],["","",""]],[["","",""],["","",""],["","",""]],[["","",""],["","",""],["","",""]]]
            click=2
            joueur=1
            affichage(table)
            return table,click,joueur,1,0

        else:
            return table,click,joueur,clickControle1,clickControle2


def Quit(coorX,coorY):

    if coorX>770 and coorX<870 and coorY>150 and coorY<176:
        a=True
        return a
    
        

def TDJ(joueur,click,clickControle2):    #Tour De Jeux
        
    if click==2:    
        if joueur==1:
            
            if clickControle2==2:
                return joueur
            
            else:
                joueur=2
                affichageEcran(joueur,click,Vwin)
                return joueur

        elif joueur==2:
            if clickControle2==2:
                return joueur
            
            else:
                joueur=1
                affichageEcran(joueur,click,Vwin)

                return joueur

    else:    
        return joueur
    
    affichageEcran(joueur,click)

