
import pygame,sys
from random import randint
from pygame.locals import *
from bases import*
from rotations import*
from alignements import*

##couleur
WHITE =(255,255,255)
RED = (255,0,0)
BLACK =(0,0,0)
GREEN = (0,170,0)
BROWN = (178,34,3)

##fenetre
pygame.init()
screen = pygame.display.set_mode((1000,730))
screen.fill(GREEN)
pygame.display.set_caption(" PENTAGO ")

#/////////////VARIABLES IMAGES OBJETS
cadre = pygame.image.load("roberto2.jpg").convert()
cadre = pygame.transform.scale(cadre,(600,600))

cadre2 = pygame.image.load("cadre2.jpg").convert()
cadre2 = pygame.transform.scale(cadre2,(850,650))

atout = pygame.image.load("salva.jpg").convert()
atout = pygame.transform.scale(atout,(120,120))

pentagologo = pygame.image.load("pentagologo.jpg").convert()

blocnote = pygame.image.load("callepin.jpg").convert()
blocnote = pygame.transform.scale(blocnote,(200,300))

fondrouge = pygame.image.load("fondrouge.jpg").convert()
fondrouge = pygame.transform.scale(fondrouge,(900,100))

dealwithit=pygame.image.load("dealwithit.gif").convert()

fedora=pygame.image.load("fedora.jpg").convert()
fedora = pygame.transform.scale(fedora,(400,400))
fedora = pygame.transform.flip(fedora,1,0)

#bouton sauvegarde
sauvegarde = pygame.font.SysFont(None, 30)
textsave = sauvegarde.render("SAUVEGARDER", True, BLACK,WHITE)
textsavepos = textsave.get_rect()
textsavepos.topleft = (810,600)

#zone pour les quadrants
q1 = pygame.Rect(150,100,250,250)
q3 = pygame.Rect(400,100,250,250)
q2 = pygame.Rect(150,350,250,250)
q4 = pygame.Rect(400,350,250,250)

##FLECHES
arrow1d = pygame.image.load("arrow2.png").convert()
arrow1d.set_colorkey(WHITE) #transparence
arrow2d = arrow1d.copy()#creation des  autres fleches a partir de la première fleche
arrow3d = arrow1d.copy()
arrow4d = arrow1d.copy()
arrow1g = arrow1d.copy()
arrow2g = arrow1d.copy()
arrow3g = arrow1d.copy()
arrow4g = arrow1d.copy()

arrow1d = pygame.transform.rotate(arrow1d,-45)#fleche quadrant1  droite
arrow1d = pygame.transform.scale(arrow1d,(70,70))#on met la fleche a la bonne taille
arrow_q1droite=arrow1d.get_rect(topleft=(275,0))#zone pour detection des clics

arrow1g = pygame.transform.rotate(arrow1g,45)#fleche q1  gauche
arrow1g = pygame.transform.scale(arrow1g,(70,70))
arrow1g = pygame.transform.flip(arrow1g,0,1)#on pivote la fleche dans le bon sens
arrow_q1gauche=arrow1g.get_rect(topleft=(25,215))

arrow3g = pygame.transform.rotate(arrow3g,-45)#fleche q3  gauche
arrow3g = pygame.transform.scale(arrow3g,(70,70))
arrow3g = pygame.transform.flip(arrow3g,1,0)
arrow_q3gauche=arrow3g.get_rect(topleft=(475,0))
    
arrow3d = pygame.transform.rotate(arrow3d,45)#fleche q3  droite
arrow3d = pygame.transform.scale(arrow3d,(70,70))
arrow3d = pygame.transform.flip(arrow3d,1,1)
arrow_q3droite=arrow3d.get_rect(topleft=(700,215))

arrow2d = pygame.transform.rotate(arrow2d,45)#fleche q2  droite
arrow2d = pygame.transform.scale(arrow2d,(70,70))
arrow2d = pygame.transform.flip(arrow2d,0,0)
arrow_q2droite=arrow2d.get_rect(topleft=(25,465))

arrow2g = pygame.transform.rotate(arrow2g,-45)#fleche q2 gauche
arrow2g = pygame.transform.scale(arrow2g,(70,70))
arrow2g = pygame.transform.flip(arrow2g,0,1)
arrow_q2gauche=arrow2g.get_rect(topleft=(275,650))

arrow4g = pygame.transform.rotate(arrow4g,45)#fleche q4  gauche
arrow4g = pygame.transform.scale(arrow4g,(70,70))
arrow4g = pygame.transform.flip(arrow4g,1,0)
arrow_q4gauche=arrow2d.get_rect(topleft=(700,465))

arrow4d = pygame.transform.rotate(arrow4d,-45)#fleche q4  droite
arrow4d = pygame.transform.scale(arrow4d,(70,70))
arrow4d = pygame.transform.flip(arrow4d,1,1)
arrow_q4droite=arrow4d.get_rect(topleft=(475,650))

#///////////FONCTIONS
def drawquadrant(plat,surf,quadrant):

    taille = quadrant.width
    x = quadrant.left
    y = quadrant.top
    bgq = pygame.draw.polygon(surf,RED,((x,y),(x+taille,y),(x+taille,y+taille),(x,y+taille)))#fond quadrant
    cq  = pygame.draw.polygon(surf,BLACK,((x,y),(x+taille,y),(x+taille,y+taille),(x,y+taille)),5)#contour quadrant
    if quadrant == q1:
        quad=1
    if quadrant == q2:
        quad=2
    if quadrant == q3:
        quad=3
    if quadrant == q4:
        quad=4
    incre=250//(len(plat)//2)
    for i in range(len(plat)//2):
        for j in range(len(plat)//2):
            if getQuad(len(plat),plat,quad)[i][j]==0:
                clr=BROWN
            if getQuad(len(plat),plat,quad)[i][j]==1:
                clr=WHITE
            if getQuad(len(plat),plat,quad)[i][j]==2:
                clr=BLACK
            pygame.draw.circle(surf,clr,(x+incre//2+j*incre,y+incre//2+i*incre),20)

def drawplateau(plat,surf):
    screen.blit(blocnote,(780,100))
    screen.blit(cadre,(100,55))
    drawquadrant(plat,surf,q1)
    drawquadrant(plat,surf,q2)
    drawquadrant(plat,surf,q3)
    drawquadrant(plat,surf,q4)


def pion(plat,surf,player):
    if player == 1:
        texte=" aux blancs de jouer !"
    if player == 2:
        texte=" aux noirs de jouer ! "
        
    #textband
    
    fontplayer = pygame.font.SysFont("georgia.ttf", 20)
    textplayer = fontplayer.render(texte, True, BLACK,WHITE) #texte qui s'affiche dans le carnet selon le tour
    textplayer.set_colorkey(WHITE)
    textplayerpos = textplayer.get_rect()
    textplayerpos.topleft = (810,150)
    screen.blit(textplayer, textplayerpos)
    #bouton suavegarde
    screen.blit(textsave, textsavepos)

    pygame.display.update()
    #pion
    inProgress= True
    while inProgress:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button==1:
                xpos = event.pos[0]
                ypos = event.pos[1]
                incre = 250//(len(plat)//2)
                for i in range(len(plat)):
                    for j in range(len(plat)):              
                        if xpos<203+j*incre and xpos>163+j*incre and ypos>113+i*incre and ypos<153+i*incre: #detection par iteratiosn de coordonées pour savoir dans quel rond le clic se situe
                            if plat[i][j]==0:
                                plat[i][j]=player
                                drawplateau(plat,screen)
                                pygame.display.update()
                                pionsound= pygame.mixer.Sound("posepion.wav")
                                pionsound.play()
                                return True
                                inProgress = False
                        if textsavepos.collidepoint(xpos,ypos):#detection par collision de pixel pour savoir si on a cliqué sur sauvegarder, ce qui met fin au tour
                            surf.fill(GREEN)
                            sauvegarde(plat,surf,player)
                            pygame.display.update()
                            return False
                            inProgress=False




def arrowdetector():
    quadrant = 0
    rotation = True
    inProgress= True
    while inProgress:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button==1:
                xpos = event.pos[0]
                ypos = event.pos[1]
                if arrow_q1droite.collidepoint(xpos,ypos):
                    quadrant = 1
                    rotation = False
                    inProgress=False
                if arrow_q1gauche.collidepoint(xpos,ypos):
                    quadrant = 1
                    rotation = True
                    inProgress=False
                if arrow_q2droite.collidepoint(xpos,ypos):
                    quadrant = 2
                    rotation = False
                    inProgress=False
                if arrow_q2gauche.collidepoint(xpos,ypos):
                    quadrant = 2
                    rotation = True
                    inProgress=False
                if arrow_q3droite.collidepoint(xpos,ypos):
                    quadrant = 3
                    rotation = False
                    inProgress=False
                if arrow_q3gauche.collidepoint(xpos,ypos):
                    quadrant = 3
                    rotation = True
                    inProgress=False
                if arrow_q4droite.collidepoint(xpos,ypos):
                    quadrant = 4
                    rotation = False
                    inProgress=False
                if arrow_q4gauche.collidepoint(xpos,ypos):
                    quadrant = 4
                    rotation = True
                    inProgress=False
                    
        pygame.display.update()
    return (quadrant,rotation)


def makeitrotate(plat,surf):
    screen.blit(arrow1d,(275,0))
    screen.blit(arrow1g,(25,215))
    screen.blit(arrow3g,(475,0))
    screen.blit(arrow3d,(700,215))
    screen.blit(arrow2d,(25,465))
    screen.blit(arrow2g,(275,650))
    screen.blit(arrow4g,(700,465))
    screen.blit(arrow4d,(475,650))
    
    data = arrowdetector()
    dataquad =data[0]
    datarot = data[1]
    rotationQuad(plat,len(plat),data[0],data[1])
    surf.fill(GREEN)
    drawplateau(plat,surf)

def ecransauvegarde(surf):
    
    surf.blit(fondrouge,(50,250))

    #case1
    
    slotonefont = pygame.font.SysFont("georgia.ttf", 80)
    textslotone = slotonefont.render("1", True, BLACK,WHITE)
    textslotonepos = textslotone.get_rect()
    textslotonepos.topleft = (325,275)
    surf.blit(textslotone, textslotonepos)
    pygame.draw.rect(screen, BLACK, textslotonepos,5)
    #case2
    
    slottwofont = pygame.font.SysFont("georgia.ttf", 80)
    textslottwo = slottwofont.render("2", True, BLACK,WHITE)
    textslottwopos = textslottwo.get_rect()
    textslottwopos.topleft = (475,275)
    surf.blit(textslottwo, textslottwopos)
    pygame.draw.rect(screen, BLACK, textslottwopos,5)
    #case3
    
    slotthreefont = pygame.font.SysFont("georgia.ttf", 80)
    textslotthree = slotthreefont.render("3", True, BLACK,WHITE)
    textslotthreepos = textslotthree.get_rect()
    textslotthreepos.topleft = (625,275)
    surf.blit(textslotthree, textslotthreepos)
    pygame.draw.rect(screen, BLACK, textslotthreepos,5)

    
    pygame.display.update()
    file = 0
    inProgress=True
    while inProgress:
        for event in pygame.event.get():
            if event.type == QUIT:
                inProgress = False
            if event.type == MOUSEBUTTONDOWN and event.button==1:
                xpos = event.pos[0]
                ypos = event.pos[1]
                if textslotonepos.collidepoint(xpos,ypos):
                    file = "file1.txt"
                    inProgress=False
                if textslottwopos.collidepoint(xpos,ypos):
                    file = "file2.txt"
                    inProgress=False
                if textslotthreepos.collidepoint(xpos,ypos):
                    file = "file3.txt"
                    inProgress=False
    return file
IA = 0 #variable qui sert a savoir si la aprtie sauvegardée était contre l'IA,, vaut 8 pour False et 9 pour True
def sauvegarde(plat,surf,player):
    #textband
    
    selecsave = pygame.font.SysFont("georgia.ttf", 50)
    textselecsave = selecsave.render("Choisissez l'emplacment de votre sauvegarde", True, BLACK,WHITE)
    textselecsavepos = textselecsave.get_rect()
    textselecsavepos.topleft = (100,150)
    screen.blit(textselecsave, textselecsavepos)
    
    slot=ecransauvegarde(surf)
    fichier = open(slot,'w')
    print(plat)
    global IA
    fichier.write(str(plat)+str(player)+str(IA))
    fichier.close()

 
resettour = 0 #variable qui sert a recuperer le tour en cours dans la partie sauvegarder
def continuerpartie(surf):
    #textband
    
    selecsave = pygame.font.SysFont("georgia.ttf", 50)
    textselecsave = selecsave.render(" Choisissez l'emplacment de partie à poursuivre ", True, BLACK,WHITE)
    textselecsavepos = textselecsave.get_rect()
    textselecsavepos.topleft = (100,150)
    screen.blit(textselecsave, textselecsavepos)
    
    slot=ecransauvegarde(surf)
    fichier = open(slot,'r')
    contenu = fichier.read()
    fichier.close()
    
    plat2=contenu.replace(",","")
    plat2=plat2.replace("[","")
    plat2=plat2.replace("]","")
    plat2=plat2.replace(" ","")
    plat2=list(plat2)
    print(plat2)
    

    newplat=[]
    cpt=0
    for j in range(int((len(plat2)-1)**(0.5))):
        stock = []
        for i in range(int((len(plat2)-1)**(0.5))):
            stock.append(int(plat2[cpt]))
            cpt+=1
        newplat.append(stock)
    global resettour
    resettour=int(plat2[len(plat2)-2])#recupere le tour en cours
    global IA
    IA=int(plat2[len(plat2)-1])#recupere si IA ou non
    print(resettour)
    return newplat

def animationvictoire():
    positionf = fedora.get_rect()
    positionf.topleft=(300,0)
    positiond=dealwithit.get_rect()
    positiond.topleft=(340,0)
    lol=pygame.mixer.Sound("OSS 117 - T'es mauvais Jack !.wav")
    lol.play()
    cpt=0
    for x in range(25):
        if cpt%2==0:
            screen.fill(GREEN)
        else:
            screen.fill(RED)
        cpt+=1
        positionf = positionf.move(0, 7)
        screen.blit(fedora, positionf)
        pygame.display.update()
        pygame.time.delay(100)
    for x in range(25):
        if cpt%2==0:
            screen.fill(GREEN)
        else:
            screen.fill(RED)
        cpt+=1
        screen.blit(fedora, positionf)
        screen.blit(dealwithit, positiond)
        positiond = positiond.move(0, 9)
        screen.blit(dealwithit, positiond)
        pygame.display.update()
        pygame.time.delay(100)
    pygame.time.delay(4500)
    lol=pygame.mixer.Sound("NGNL - Omega Good Job.wav")
    lol.play()
    pygame.time.delay(1500)


def gameIA(surf,plat,vic,status):
    surf.fill(GREEN)
    pygame.display.update()
    tour = status
    victory=False
    while victory == False:
        if tour == 1:
            inProgress= True
            while inProgress:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        inProgress = False
                    drawplateau(plat,surf)
                    statut = pion(plat,surf,tour)
                    if statut == False:
                        inProgress=False
                        victory=True
                    if statut == True:
                        makeitrotate(plat,surf)
                        tour=2
                    if victoire(len(plat),plat,vic,tour):
                        inProgress = False
                        victory = True
                        animationvictoire()
                        tour=1
                    inProgress=False
                pygame.display.update()
        if tour == 2:
            drawplateau(plat,surf)
            while 1:
                x=randint(0,len(plat)-1)
                y=randint(0,len(plat)-1)
                if plat[x][y]==0:
                    plat[x][y]=2
                    break
            IAquad=randint(1,4)
            IAsens=randint(0,1)
            if IAsens==1:
                IAsens=True
            if IAsens==0:
                IAsens=False
            rotationQuad(plat,len(plat),IAquad,IAsens)
            lol=pygame.mixer.Sound("IAsound.wav")
            lol.play()
            drawplateau(plat,surf)
            tour=1
            if victoire(len(plat),plat,vic,tour):
                victory=True
                animationvictoire()
                tour=2
            pygame.display.update()
            
            

def game(surf,plat,vic,status):

    inProgress= True
    tour = status
    while inProgress:
        for event in pygame.event.get():
            if event.type == QUIT:
                inProgress = False
            drawplateau(plat,surf)
            statut = pion(plat,surf,tour)
            if statut== True:
                makeitrotate(plat,surf) #la variable statut sert a gerer quand on clic sur sauvegarder, voir fonction pion
            if statut == False:
                inProgress=False
            if victoire(len(plat),plat,vic,tour):
                animationvictoire()
                inProgress = False
            if tour==1:
                tour=2
            else:
                tour=1
        
        pygame.display.update()
        
def homepage(surf):
    surf.blit(pentagologo,(0,0))

    #boutonnouvellepartie
    fontjouer = pygame.font.SysFont(None, 80)
    textjouer = fontjouer.render("  Nouvelle Partie  ", True, BLACK,WHITE)
    textjouerpos = textjouer.get_rect()
    textjouerpos.topleft = (270,200)
    surf.blit(textjouer, textjouerpos)
    pygame.draw.rect(screen, BLACK, textjouerpos,6)

    #boutoncontunierpartie
    fontcontinue = pygame.font.SysFont(None, 80)
    textcontinue = fontcontinue.render("  Continuer Partie  ", True, BLACK,WHITE)
    textcontinuepos = textcontinue.get_rect()
    textcontinuepos.topleft = (260,300)
    surf.blit(textcontinue, textcontinuepos)
    pygame.draw.rect(screen, BLACK, textcontinuepos,6)

    pygame.display.update()

    #bandeau format plateau 2joueurs
    formatplat2 = pygame.font.SysFont(None, 40)
    textformatplat2 = formatplat2.render(" 2 joueurs: selectionner la taille du plateau ", True, BLACK,WHITE)
    textfp2pos = textformatplat2.get_rect()
    textfp2pos.topleft = (200,455)
    
    
    #bouton  plateau 6 2 joueurs
    bouttonplat6 = pygame.font.SysFont(None, 80)
    textplat6 = bouttonplat6.render(" 6 ", True, BLACK,WHITE)
    textplat6.set_colorkey(WHITE)
    textplat6pos = textplat6.get_rect()
    textplat6pos.topleft = (305,500)
    #bouton  plateau 8 2 joueurs
    bouttonplat8 = pygame.font.SysFont(None, 80)
    textplat8 = bouttonplat8.render(" 8 ", True, BLACK,WHITE)
    textplat8.set_colorkey(WHITE)
    textplat8pos = textplat8.get_rect()
    textplat8pos.topleft = (405,500)
    #bouton  plateau 10 2 joueurs
    bouttonplat10 = pygame.font.SysFont(None, 80)
    textplat10 = bouttonplat10.render(" 10 ", True, BLACK,WHITE)
    textplat10.set_colorkey(WHITE)
    textplat10pos = textplat10.get_rect()
    textplat10pos.topleft = (505,500)

    #bouton  IA
    bouttonIA = pygame.font.SysFont(None, 40)
    textIA = bouttonIA.render(" jeu contre l'IA: selectionner la taille du plateau ", True, BLACK,WHITE)
    textIApos = textIA.get_rect()
    textIApos.topleft = (147,290)
    #bouton  plateau 6 IA
    bouttonplat6IA = pygame.font.SysFont(None, 80)
    textplat6IA = bouttonplat6IA.render(" 6 ", True, BLACK,WHITE)
    textplat6IA.set_colorkey(WHITE)
    textplat6posIA = textplat6IA.get_rect()
    textplat6posIA.topleft = (305,350)
    #bouton  plateau 8 IA
    bouttonplat8IA = pygame.font.SysFont(None, 80)
    textplat8IA = bouttonplat8IA.render(" 8 ", True, BLACK,WHITE)
    textplat8IA.set_colorkey(WHITE)
    textplat8posIA = textplat8IA.get_rect()
    textplat8posIA.topleft = (405,350)
    #bouton  plateau 10 IA
    bouttonplat10IA = pygame.font.SysFont(None, 80)
    textplat10IA = bouttonplat10IA.render(" 10 ", True, BLACK,WHITE)
    textplat10IA.set_colorkey(WHITE)
    textplat10posIA = textplat10IA.get_rect()
    textplat10posIA.topleft = (505,350)

    #bandeau trololo
    trololo = pygame.font.SysFont(None, 15)
    texttrololo = trololo.render("*Jérémy, champion du monde 2015 de Pentago ", True, WHITE,BLACK)
    texttrololo.set_colorkey(BLACK)
    texttrololopos = texttrololo.get_rect()
    texttrololopos.topleft = (200,455)

    pygame.display.update()
    dimension = 0
    inProgress= True
    while inProgress:
        for event in pygame.event.get():
            if event.type == QUIT:
                inProgress = False
            if event.type == MOUSEBUTTONDOWN and event.button==1:
                xpos = event.pos[0]
                ypos = event.pos[1]
                if textcontinuepos.collidepoint(xpos,ypos):
                    surf.fill(GREEN)
                    return(continuerpartie(surf))
                    inProgress=False
                if textjouerpos.collidepoint(xpos,ypos):
                    surf.fill(GREEN)
                    surf.blit(cadre2,(50,50))
                    surf.blit(textIA,textIApos)
                    pygame.draw.rect(screen, RED, textIApos,5)
                    surf.blit(pentagologo,(0,0))
                    surf.blit(textformatplat2, textfp2pos)
                    pygame.draw.rect(screen, RED, textfp2pos,5)
                    surf.blit(textplat6, textplat6pos)
                    pygame.draw.rect(screen, BLACK, textplat6pos,5)
                    surf.blit(textplat8, textplat8pos)
                    pygame.draw.rect(screen, BLACK, textplat8pos,5)
                    surf.blit(textplat10, textplat10pos)
                    pygame.draw.rect(screen, BLACK, textplat10pos,5)
                    surf.blit(textplat6IA, textplat6posIA)
                    pygame.draw.rect(screen, BLACK, textplat6posIA,5)
                    surf.blit(textplat8IA, textplat8posIA)
                    pygame.draw.rect(screen, BLACK, textplat8posIA,5)
                    surf.blit(textplat10IA, textplat10posIA)
                    pygame.draw.rect(screen, BLACK, textplat10posIA,5)

                    screen.blit(atout,(300,140))
                    surf.blit(texttrololo, (450,160))
                    
                    pygame.display.update()
                if textplat6posIA.collidepoint(xpos,ypos):
                    dimension = 60
                    inProgress=False
                if textplat8posIA.collidepoint(xpos,ypos):
                    dimension = 80
                    inProgress=False
                if textplat10posIA.collidepoint(xpos,ypos):
                    dimension = 100
                    inProgress=False
                if textplat6pos.collidepoint(xpos,ypos):
                    surf.fill(GREEN)
                    dimension=6
                    inProgress=False
                if textplat8pos.collidepoint(xpos,ypos):
                    surf.fill(GREEN)
                    dimension=8
                    inProgress=False
                if textplat10pos.collidepoint(xpos,ypos):
                    surf.fill(GREEN)
                    dimension=10
                    inProgress=False
                    
                    


    pygame.display.update()
    return dimension

while 1:
    #procedure finale
    screen.fill(GREEN)
    etat= homepage(screen)
    if type(etat) == list:
        screen.fill(GREEN)
        plateau=etat
        if IA==9:
            gameIA(screen,plateau,5,resettour)
        else:
            IA=8
            game(screen,plateau,5,resettour)
    if etat == 60:
        IA=9
        plateau = getListe(6)
        gameIA(screen,plateau,5,1)
    if etat == 80:
        IA=9
        plateau = getListe(8)
        gameIA(screen,plateau,5,1)
    if etat == 100:
        IA=9
        plateau = getListe(10)
        gameIA(screen,plateau,5,1)
    if etat==6 or etat==8 or etat==10:
        IA=8
        plateau = getListe(etat)
        game(screen,plateau,5,1)
    









