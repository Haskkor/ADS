from alignements import *
from bases import *
from rotations import *
import pickle
import pygame, sys
from pygame.locals import *
pygame.init()
#           R   G   B
rouge =  (134,  0,  0)
rouge2 = ( 90,  0,  0)
blanc =  (255,255,255)
noir =   (  0,  0,  0)
black =  (  0,  0,  0)
gold =   (218,165, 32)
FONT1 = pygame.font.SysFont("comicsansms", 20)
logo = pygame.image.load('logo.png')
begin = False
end = False
choose = False
encours = True
effect = 50
# fontion pour dessiner un quandrant ***
def dessin_quad(plateau,Surface,i,f):
    pygame.draw.rect(Surface,rouge,((l1+5)+i*(65*len(plateau)//2),(h1+5)+f*(65*len(plateau)//2),63.33*len(plateau)//2,63.33*len(plateau)//2))
    for k in range(len(plateau)//2):
        for v in range(len(plateau)//2):
            if plateau[f*(len(plateau)//2)+v][i*(len(plateau)//2)+k] == 0:
                pygame.draw.circle(Surface,rouge2,((l1+43)+k*60+i*(63*(len(plateau)//2)),(h1+43)+v*60+f*(63*(len(plateau)//2))),13,0)
            if plateau[f*(len(plateau)//2)+v][i*(len(plateau)//2)+k] == 1:
                pygame.draw.circle(Surface,blanc,((l1+43)+k*60+i*(63*(len(plateau)//2)),(h1+43)+v*60+f*(63*(len(plateau)//2))),13,0)
            if plateau[f*(len(plateau)//2)+v][i*(len(plateau)//2)+k] == 2:
                pygame.draw.circle(Surface,noir,((l1+43)+k*60+i*(63*(len(plateau)//2)),(h1+43)+v*60+f*(63*(len(plateau)//2))),13,0)
# fontion pour dessiner tout le plateau
def dessin_plateau(plateau,Surface):
    pygame.draw.rect(Surface,blanc,(l1,h1,131.66*len(plateau)//2,131.66*len(plateau)//2))
    for i in range(0,2):
        for f in range(0,2):
            dessin_quad(plateau,Surface,i,f)
    pygame.display.update()
# fontion pour dessiner les fleches de pivotement
def fleches(plateau,Surface):
    left = pygame.image.load('left.png')
    up = pygame.image.load('up.png')
    right = pygame.image.load('right.png')
    down = pygame.image.load('down.png')
    leftpic = Surface.blit(left,(xleft,yleft))
    upperpic = Surface.blit(up,(xup,yup))
    rightpic = Surface.blit(right,(xright,yright))
    downpic = Surface.blit(down,(xdown,ydown))

# procedure initiale
inprogress = True
while inprogress:
    black = noir
    Surface = pygame.display.set_mode((1000,750))
    pygame.display.set_caption('PENTAGO - THE MIND TWISTING GAME')
    # procedure pour adapter les dimensions selon la taille du plateau
    if len(plateau) == 6:
        h1 = 160
        l1 = 80
        xaffiche , yaffiche = 0,0
        xnewgame , ynewgame = 0,0
        xquit, xquit = 0,0
        xleft,yleft = -10,90
        xup,yup = 13,75
        xright,yright = 460,90
        xdown, ydown =  13, 540
        xleftup,yleftup = 0,200
        xleftdown,yleftdown = 0,460
        xupleft,yupleft = 100,100
        xupright,yupright = 380,100
        xrightup,yrightup = 480,200
        xrightdown,yrightdown = 480,460
        xdownleft,ydownleft = 100,540
        xdownright,ydownright = 380,540
    elif len(plateau) == 8:
        h1 = 120
        l1 = 80
        xleft,yleft = -10,110
        xup,yup = 70,40
        xright,yright = 590,110
        xdown, ydown =  72, 630
        xleftup,yleftup = 0,200
        xleftdown,yleftdown = 0,468
        xupleft,yupleft = 152,60
        xupright,yupright = 424,60
        xrightup,yrightup = 608,196
        xrightdown,yrightdown = 608,464
        xdownleft,ydownleft = 152,648
        xdownright,ydownright = 424,648
    if begin:
        # procedure pour alterner entre la pose des pions et le pivotement des quadrent
        if choose:
            encours = False
        else:
            encours = True
        #procedure pour verifier si il y'a un aligenemt
        if check(len(plateau),plateau,5,j%2+1) or check(len(plateau),plateau,5,j):
            #procedure animation sonore si il y'a un gaganant
            if not end:
                if (check(len(plateau),plateau,5,1) and not check(len(plateau),plateau,5,2)) or (check(len(plateau),plateau,5,2) and not check(len(plateau),plateau,5,1)):
                    pygame.mixer.music.load("tada.wav")
                    pygame.mixer.music.play(1,0.0)
                if check(len(plateau),plateau,5,1) and check(len(plateau),plateau,5,2):
                    pygame.mixer.music.load("trombone.wav")
                    pygame.mixer.music.play(1,0.0)
            choose = False
            #procedure pour reinitialiser la sauvegarde
            empty = [0]
            pickle_out = open("etat.pickle","wb")
            pickle.dump(empty,pickle_out)
            pickle_out.close()
            encours = False
            # procedure pour afficher le nom vainqueur
            end = True
            if end:
                black = gold
                if check(len(plateau),plateau,5,1) and check(len(plateau),plateau,5,2):
                    black = noir
                    textt = str("match nul !")
                elif check(len(plateau),plateau,5,1):
                    textt = str("les blancs gagnants !")
                elif check(len(plateau),plateau,5,2):
                    textt = str("les noirs gagnants !")
            ring = False
            # affichage boutton rejouer
            newgame = str("Rejouer")
            textSurf = FONT1.render(newgame,True,noir,blanc)
            textRect = textSurf.get_rect()
            if 750 < X < 1050 and 450 < Y < 500:
                pygame.draw.rect(Surface,blanc,(750-effect,450,300,50))
                textRect.topleft = (800-effect,455)
            else:
                pygame.draw.rect(Surface,blanc,(750,450,300,50))
                textRect.topleft = (800,455)
            Surface.blit(textSurf, textRect)
            # affichage boutton quitter
            quit = str("Quitter")
            textSurf = FONT1.render(quit,True,noir,blanc)
            textRect = textSurf.get_rect()
            if 750 < X < 1050 and 550 < Y < 600:
                pygame.draw.rect(Surface,blanc,(750-effect,550,300,50))
                textRect.topleft = (800-effect,555)
            else:
                pygame.draw.rect(Surface,blanc,(750,550,300,50))
                textRect.topleft = (800,555)
            Surface.blit(textSurf, textRect)
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN :
                    X,Y = event.pos
                    #procedure boutton rejouer
                    if 750 < X < 1050 and 450 < Y < 500:
                        end = False
                        begin = False
                    #procedure boutton quitter
                    if 750 < X < 1050 and 550 < Y < 600:
                        inprogress = False
        # procedure pour un match nul
        full = 0
        for i in range(len(plateau)):
            if 0 in plateau[i]:
                 full += 1
        if full == 0:
            # procedure animation sonnore si matche nul
            if not end:
                pygame.mixer.music.load("trombone.wav")
                pygame.mixer.music.play(1,0.0)
            choose = False
            #procedure pour reinitialiser la sauvegarde
            empty = [0]
            pickle_out = open("etat.pickle","wb")
            pickle.dump(empty,pickle_out)
            pickle_out.close()
            encours = False
            end = True
            textt = ("match nul !")
            # affichage button rejouer
            newgame = str("Rejouer")
            textSurf = FONT1.render(newgame,True,noir,blanc)
            textRect = textSurf.get_rect()
            if 750 < X < 1050 and 450 < Y < 500:
                pygame.draw.rect(Surface,blanc,(750-effect,450,300,50))
                textRect.topleft = (800-effect,455)
            else:
                pygame.draw.rect(Surface,blanc,(750,450,300,50))
                textRect.topleft = (800,455)
            Surface.blit(textSurf, textRect)
            # affichage button quitter
            quit = str("Quitter")
            textSurf = FONT1.render(quit,True,noir,blanc)
            textRect = textSurf.get_rect()
            if 750 < X < 1050 and 550 < Y < 600:
                pygame.draw.rect(Surface,blanc,(750-effect,550,300,50))
                textRect.topleft = (800-effect,555)
            else:
                pygame.draw.rect(Surface,blanc,(750,550,300,50))
                textRect.topleft = (800,555)
            Surface.blit(textSurf, textRect)
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN :
                    X,Y = event.pos
                    # procedure boutton rejouer
                    if 750 < X < 1050 and 450 < Y < 500:
                        end = False
                        begin = False
                    # procedure boutton quitter
                    if 750 < X < 1050 and 550 < Y < 600:
                        inprogress = False
    # procedure pour alterner les affichage de tour
    if encours:
        if j == 1:
            textt = str("posez un pion blanc")
        if j == 2:
            textt = str("posez un pion noir")
    #proedure pour le pivoter un quandrant
    if choose:
        fleches(plateau,Surface)
        textt = str("pivotez un quandrent !")
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN :
                X,Y = event.pos
                if xupleft < X < xupleft+100 and yupleft < Y < yupleft+80:
                    rotat(len(plateau),plateau,1,True)
                    choose = False
                if xleftup < X < xleftup+80 and yleftup < Y < yleftup+120:
                    rotat(len(plateau),plateau,1,False)
                    choose = False
                if xleftdown < X < xleftdown+80 and yleftdown < Y < yleftdown + 120:
                    rotat(len(plateau),plateau,2,True)
                    choose = False
                if xdownleft < X < xdownleft+100 and ydownleft < Y < ydownleft+80:
                    rotat(len(plateau),plateau,2,False)
                    choose = False
                if xdownright< X < xdownright+80 and ydownright < Y < ydownright+80:
                    rotat(len(plateau),plateau,3,True)
                    choose = False
                if xrightdown < X < xrightdown+80 and yrightdown < Y < yrightdown+80:
                    rotat(len(plateau),plateau,3,False)
                    choose = False
                if xrightup < X < xrightup+80 and yrightup < Y < yrightup+80:
                    rotat(len(plateau),plateau,4,True)
                    choose = False
                if xupright < X < xupright+80 and yupright < Y < yupright+80:
                    rotat(len(plateau),plateau,4,False)
                    choose = False
                if j == 2:
                    textt = str("les blancs gagnants !")
                if j == 1:
                    textt = str("les noirs gagnants !")
    textSurf = FONT1.render(textt,True,black,blanc)
    textRect = textSurf.get_rect()
    textRect.topleft = (790,160)
    pygame.draw.rect(Surface,blanc,(750,150,300,50))
    Surface.blit(textSurf, textRect)
    # procedure pour afficher un menu interactif lors du jeu
    X, Y = pygame.mouse.get_pos()
    if encours:
        # affichage boutton sauvgarder
        X, Y = pygame.mouse.get_pos()
        save = str("sauvegarder")
        textSurf = FONT1.render(save,True,noir,blanc)
        textRect = textSurf.get_rect()
        if 750 < X < 1050 and 400 < Y < 450:
            pygame.draw.rect(Surface,blanc,(750-effect,400,300,50))
            textRect.topleft = (800-effect,405)
        else:
            pygame.draw.rect(Surface,blanc,(750,400,300,50))
            textRect.topleft = (800,405)
        Surface.blit(textSurf, textRect)
        # affichage button retour menu
        menu = str("retour au menu")
        textSurf = FONT1.render(menu,True,noir,blanc)
        textRect = textSurf.get_rect()
        if 750 < X < 1050 and 300 < Y < 350:
            pygame.draw.rect(Surface,blanc,(750-effect,300,300,50))
            textRect.topleft = (800-effect,305)
        else:
            pygame.draw.rect(Surface,blanc,(750,300,300,50))
            textRect.topleft = (800,305)
        Surface.blit(textSurf, textRect)
        # affichage button quitter
        quit = str("Quitter")
        textSurf = FONT1.render(quit,True,noir,blanc)
        textRect = textSurf.get_rect()
        if 750 < X < 1050 and 500 < Y < 550:
            pygame.draw.rect(Surface,blanc,(750-effect,500,300,50))
            textRect.topleft = (800-effect,505)
        else:
            pygame.draw.rect(Surface,blanc,(750,500,300,50))
            textRect.topleft = (800,505)
        Surface.blit(textSurf, textRect)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN :
                X,Y = event.pos
                # procedure pour la pose d'un pion
                for i in range(0,len(plateau)):
                    for k in range(0,len(plateau)):
                        if plateau[i][k] == 0:
                            if not end:
                                if ((l1+20)+k*61) < X < ((l1+61)+k*61) and ((h1+20)+61*i) < Y < ((h1+61)+i*61):
                                    plateau[i][k] = j
                                    j = j % 2 + 1
                                    choose = True
                # procedure button sauvgarder
                if 750 < X < 1050 and 400 < Y < 450:
                    pickle_out = open("etat.pickle","wb")
                    pickle.dump(plateau,pickle_out)
                    pickle_out = open("tour.pickle","wb")
                    pickle.dump(j%2+1,pickle_out)
                    pickle_out.close()
                # procedure button retour menu
                if 750 < X < 1050 and 300 < Y < 350:
                    j = 1
                    begin = False
                # procedure button retour Quitter
                if 750 < X < 1050 and 500 < Y < 550:
                    inprogress = False
    # procedure pour afficher le menu principale
    if begin:
        dessin_plateau(plateau,Surface)
    else:
        logopic = Surface.blit(logo,(100,100))
        X, Y = pygame.mouse.get_pos()
        # affichage button charger
        load = str("Charger ")
        textSurf = FONT1.render(load,True,noir,blanc)
        textRect = textSurf.get_rect()
        if 750 < X < 1050 and 200 < Y < 250:
            pygame.draw.rect(Surface,blanc,(750-effect,200,300,50))
            textRect.topleft = (800-effect,205)
        else:
            pygame.draw.rect(Surface,blanc,(750,200,300,50))
            textRect.topleft = (800,205)
        Surface.blit(textSurf, textRect)
        # affichage button partie 6x6
        six = str("nouvelle partie 6x6")
        textSurf = FONT1.render(six,True,noir,blanc)
        textRect = textSurf.get_rect()
        if 750 < X < 1050 and 300 < Y < 350:
            pygame.draw.rect(Surface,blanc,(750-effect,300,300,50))
            textRect.topleft = (800-effect,305)
        else:
            pygame.draw.rect(Surface,blanc,(750,300,300,50))
            textRect.topleft = (800,305)
        Surface.blit(textSurf, textRect)
        # affichage button partie 8x8
        eight = str("nouvelle partie 8x8")
        textSurf = FONT1.render(eight,True,noir,blanc)
        textRect = textSurf.get_rect()
        X, Y = pygame.mouse.get_pos()
        if 750 < X < 1050 and 400 < Y < 450:
            pygame.draw.rect(Surface,blanc,(750-effect,400,300,50))
            textRect.topleft = (800-effect,405)
        else:
            pygame.draw.rect(Surface,blanc,(750,400,300,50))
            textRect.topleft = (800,405)
        Surface.blit(textSurf, textRect)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN :
                #procedure boutton charger
                X,Y = event.pos
                pickle_in = open("etat.pickle","rb")
                see = pickle.load(pickle_in)
                if len(see) != 1:
                    if 750 < X < 1050 and 200 < Y < 250:
                        pickle_in = open("etat.pickle","rb")
                        plateau = pickle.load(pickle_in)
                        pickle_in = open("tour.pickle","rb")
                        j = int(pickle.load(pickle_in))%2+1
                        begin = True
                else:
                    begin=False
                # procedure boutton partie 6x6
                if 750 < X < 1050 and 300 < Y < 350:
                    j = 1
                    plateau = plateau0(6)
                    begin = True
                # procedure boutton partie 8x8
                if 750 < X < 1050 and 400 < Y < 450:
                    j = 1
                    plateau = plateau0(8)
                    begin = True
    if event.type == QUIT:
        inprogress = False
    pygame.display.update()

# coded by amir tifour, rachid medjoub and maxime ouvrard