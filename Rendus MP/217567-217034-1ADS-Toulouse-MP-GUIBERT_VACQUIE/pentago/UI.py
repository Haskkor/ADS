#procédures de l'UI


def checkForQuit():
    for event in pygame.event.get((QUIT, KEYUP)):
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
                   
        

def affichage(table):
    #On test les valeurs des cases dans notre liste pour mettre la couleur correspondante
        table=convert(table)
        
        for i in range(0,6):            #Affichage Rond Plateau
            for j in range(0,6):
        
                if table[i][j]== "":
                    pygame.draw.circle(window, RED2,(170+j*100,140+i*100),25)

                elif table[i][j]==1:
                    pygame.draw.circle(window, WHITE,(170+j*100,140+i*100),25)

                elif table[i][j]==2:
                    pygame.draw.circle(window, BLACK,(170+j*100,140+i*100),25)



def affichageEcran(joueur, click,Vwin):
    #Cette fonction s'occupe de l'affichage dans l'écran à droite
    
    #print("Vwin base : ", Vwin)
    if click==1 and joueur==1:                              #Tour des blancs
        police=pygame.font.Font('freesansbold.ttf', 22)
        texteB=police.render('Au tour des', True, BLACK,GREY)
        texteB2=police.render('Blanc',True,BLACK,GREY)
        texteRectB=texteB.get_rect()
        texteRectB2=texteB2.get_rect()
        texteRectB.topleft=(830,550)
        texteRectB2.topleft=(860,572)
        window.blit(texteB, texteRectB)
        window.blit(texteB2,texteRectB2)

    if click==1 and joueur==2:                              #Tour des noirs
        police=pygame.font.Font('freesansbold.ttf', 22)
        texteN=police.render('Au tour des', True, BLACK,GREY)
        texteN2=police.render('Noir',True,BLACK,GREY)
        texteRectN=texteN.get_rect()
        texteRectN2=texteN2.get_rect()
        texteRectN.topleft=(830,550)
        texteRectN2.topleft=(865,572)
        window.blit(texteN, texteRectN)
        window.blit(texteN2,texteRectN2)

    if click==2:                                            #Tournez un cadran
        police=pygame.font.Font('freesansbold.ttf', 22)
        texteC=police.render('Tournez un ',True,BLACK,GREY)
        texteC2=police.render('Cadran',True,BLACK,GREY)
        texteRectC=texteC.get_rect()
        texteRectC2=texteC2.get_rect()
        texteRectC.topleft=(830,550)
        texteRectC2.topleft=(849,572)
        window.blit(texteC,texteRectC)
        window.blit(texteC2,texteRectC2)

    if Vwin==1:                                             #Victoire des blanc
        #print("Vwin : ",Vwin)
        police=pygame.font.Font('freesansbold.ttf', 22)
        texteWB1=police.render(' Les blanc ',True,BLACK,GREY)
        texteWB2=police.render('Gagnent ',True,BLACK,GREY)
        texteRectWB1=texteWB1.get_rect()
        texteRectWB2=texteWB2.get_rect()
        texteRectWB1.topleft=(840,550)
        texteRectWB2.topleft=(845,572)
        window.blit(texteWB1, texteRectWB1)
        window.blit(texteWB2,texteRectWB2)
        
    if Vwin==2:                                             #Victoire des noirs
        #print("Vwin : ",Vwin)
        police=pygame.font.Font('freesansbold.ttf', 22)
        texteWN1=police.render(' Les noirs  ',True,BLACK,GREY)
        texteWN2=police.render('Gagnent  ',True,BLACK,GREY)
        texteRectWN1=texteWN1.get_rect()
        texteRectWN2=texteWN2.get_rect()
        texteRectWN1.topleft=(840,550)
        texteRectWN2.topleft=(843,572)
        window.blit(texteWN1, texteRectWN1)
        window.blit(texteWN2,texteRectWN2)

    if Vwin==3:                                             #Match Nul(Les deux gagnent)
        #print("Vwin : ",Vwin)
        police=pygame.font.Font('freesansbold.ttf', 22)
        texteNul1=police.render(' Match ',True,BLACK,GREY)
        texteNul2=police.render(' Nul ',True,BLACK,GREY)
        texteRectNul1=texteNul1.get_rect()
        texteRectNul2=texteNul2.get_rect()
        texteRectNul1.topleft=(840,550)
        texteRectNul2.topleft=(845,572)
        window.blit(texteNul1, texteRectNul1)
        window.blit(texteNul2,texteRectNul2)
                                                            
    if Vwin==4:                                             #Aucun Gagnant
        police=pygame.font.Font('freesansbold.ttf', 22)
        texteAG1=police.render(' Aucun ',True,BLACK,GREY)
        texteAG2=police.render('Gagnant ',True,BLACK,GREY)
        texteRectAG1=texteAG1.get_rect()
        texteRectAG2=texteAG2.get_rect()
        texteRectAG1.topleft=(840,550)
        texteRectAG2.topleft=(845,572)
        window.blit(texteAG1, texteRectAG1)
        window.blit(texteAG2,texteRectAG2)
        
