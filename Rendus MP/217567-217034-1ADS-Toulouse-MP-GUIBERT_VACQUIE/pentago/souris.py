#inputs de la souris

def CCPJ(coorX,coorY,table,click):    #Check Click Position Joué
    clickControle1=1        #Variable qui sert à vérifié si le joueur à cliqué sur un case libre pendant son tour(pour click=1)
    posel=0
    posec=0

    if click==1:  #Check de la position joué 
        
            if coorX>=120.00 and coorY>=90.00 and coorX<420.00 and coorY<390.00:
                cadrant=0
                posel,posec=0, 0
                print(cadrant)
                

            elif coorX>420.00 and coorY>=90.00 and coorX<=720.00 and coorY<390.00:
                cadrant=1
                posel,posec=0, 1
                print(cadrant)

            elif coorX>=120.00 and coorY>390.00 and coorX<420.00 and coorY<=690.00:
                cadrant=2
                posel,posec=1,0
                print(cadrant)

            elif coorX>420.00 and coorY>390.00 and coorX<=720.00 and coorY<=690.00:
                cadrant=3
                posel,posec=1,1
                print(cadrant)
                print(posel," ",posec)

            else:
                return table, 1

            for i in range(0,3):
                for j in range(0,3):     #Place le pion du joueur dans la case clické

                    if table[cadrant][i][j]=="": 
                        if coorX>=120+j*100+posec*300 and coorX<220+j*100+posec*300 and coorY>=90+i*100+posel*300 and coorY<190+i*100+posel*300:
        
                            table[cadrant][i][j]=joueur
                            clickControle1=0
                            print(table)
                            break
                        

            return table, clickControle1
    else:
            return table, clickControle1


def CCRC(coorX,coorY,table,click):    #Check Click Rotation Cadrant
        clickControle2=0      #Variable qui sert à vérifié si le joueur à cliqué sur une flèche pendant le tour de rotation(pour click=2)
        
        if click==2:
        
            if coorX>=245 and coorX<=310 and coorY>=20 and coorY<=85:
                rotate(table, 0, 1)
                return 0
                        
            elif coorX>=725 and coorX<=790 and coorY>=210 and coorY<=275:
                rotate(table,1, 1)
                return 0

            elif coorX>=540 and coorX<=605 and coorY>=695 and coorY<=760:
                rotate(table, 3, 1)
                return 0
                
            elif coorX>=50 and coorX<=110 and coorY>=510 and coorY<=575:
                rotate(table, 2, 1)
                return 0
                
            elif coorX>=50 and coorX<=110 and coorY>=210 and coorY<=275:
                rotate(table, 0, 0)
                return 0

            elif coorX>=540 and coorX<=605 and coorY>=20 and coorY<=85:
                rotate(table, 1, 0)
                return 0
            
            elif coorX>=725 and coorX<=790 and coorY>=510 and coorY<=575:
                rotate(table, 3, 0)
                return 0

            elif coorX>=245 and coorX<=310 and coorY>=695 and coorY<=760:
                rotate(table, 2, 0)
                return 0
            
            else:
                clickControle2=2
                print("totoclick")
                return clickControle2
            
        return 0
