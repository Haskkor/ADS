import pygame
from pygame.locals import *

# Initialisation de la police
pygame.font.init()

##################
### CONSTANTES ###
##################

WIDTH = 600
HEIGHT = 600
SIZE = (WIDTH  - 200) / 3
COLOR_LIGHT = (61, 61, 61)
COLOR_UNLIGHT = (23, 23, 23)
SIZE_BUTTON = (100, 30)
COLOR_P1 = (150, 90, 130)
RADIUS = (SIZE - 15) / 2
COLOR_P2 = (210, 155, 190)
PADDING = 10
FONT = pygame.font.SysFont("jokerman", 20)
TEXT = ""
TEXTNEW = "NEW"
TEXTQUIT = "QUIT"

###############
### SPRITES ###
###############

image_cross = pygame.image.load(r"cross.png")
image_circle = pygame.image.load(r"circle.png")
image_cross_rect = image_cross.get_rect()
image_circle_rect = image_circle.get_rect()

image_circle_rect.x = -100
image_circle_rect.y = -100
image_cross_rect.x = -100
image_cross_rect.y = -100

#################
### VARIABLES ###
#################

table = [[0] * 3 for i in range(3)]
tablesprites = [[0] * 3 for i in range(3)]
player = 1
player_start = 1

pygame.display.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((176, 176, 176))
pygame.display.set_caption('Morpion')

#################
### AFFICHAGE ###
#################

def display():
    global TEXTPOSNEW
    global TEXTPOSQUIT

    screen.fill((176, 176, 176))
    
    for x in range(3):
        for y in range(3):
            if table[x][y] == 0:
                screen.fill(COLOR_UNLIGHT, 
                                 (x * (SIZE + 1) + WIDTH / 2 - SIZE * 3 / 2, 
                                  y * (SIZE + 1) + HEIGHT / 2 - SIZE * 3 / 2, 
                                  SIZE - 1,
                                  SIZE - 1))
            else:
                screen.fill(COLOR_LIGHT, 
                                 (x * (SIZE + 1) + WIDTH / 2 - SIZE * 3 / 2, 
                                  y * (SIZE + 1) + HEIGHT / 2 - SIZE * 3 / 2, 
                                  SIZE - 1,
                                  SIZE - 1))
                
    textrender = FONT.render(TEXT, 1, (96,96,96))
    textrendernew = FONT.render(TEXTNEW, 1, (96,96,96))
    textrenderquit = FONT.render(TEXTQUIT, 1, (96,96,96))
    
    textpos = textrender.get_rect()
    TEXTPOSNEW = textrendernew.get_rect()
    TEXTPOSQUIT = textrenderquit.get_rect()
    
    textpos.centerx = screen.get_rect().centerx
    textpos.centery = screen.get_rect().centery + 250
    TEXTPOSNEW.centerx = screen.get_rect().centerx + 250
    TEXTPOSNEW.centery = screen.get_rect().centery - 150
    TEXTPOSQUIT.centerx = screen.get_rect().centerx + 250
    TEXTPOSQUIT.centery = screen.get_rect().centery - 100
    
    screen.blit(textrender, textpos)
    screen.blit(textrendernew, TEXTPOSNEW)
    screen.blit(textrenderquit, TEXTPOSQUIT)

    for x in tablesprites:
        for y in x:
            if y != 0:
                screen.blit(y[0],y[1])
    
    pygame.display.flip()

#######################################
### AJOUT D'UNE CASE POUR LE JOUEUR ###
#######################################

def add():
    x = int((pygame.mouse.get_pos()[0] - WIDTH / 2 + SIZE * 3 / 2) / SIZE)
    y = int((pygame.mouse.get_pos()[1] - HEIGHT / 2 + SIZE * 3 / 2) / SIZE)
    if x >= 0 and x < len(table):
        if y >= 0 and y < len(table[x]):
            if table[x][y] == 0:
                table[x][y] = player

                if player == 1:
                    tablesprites[x][y] = (pygame.image.load(r"circle.png"), (x * SIZE + PADDING + WIDTH / 2 - SIZE * 3 / 2, y * SIZE + PADDING + HEIGHT / 2 - SIZE * 3 / 2))
                else:
                    tablesprites[x][y] = (pygame.image.load(r"cross.png"), (x * SIZE + PADDING + WIDTH / 2 - SIZE * 3 / 2, y * SIZE + PADDING + HEIGHT / 2 - SIZE * 3 / 2))
                    
                return True
    return False

####################################
### VERIFIE SI LE JOUEUR A GAGNE ###
####################################

def win(player):
    x = int((pygame.mouse.get_pos()[0] - WIDTH / 2 + SIZE * 3 / 2) / SIZE)
    y = int((pygame.mouse.get_pos()[1] - HEIGHT / 2 + SIZE * 3 / 2) / SIZE)
    colonne = ligne = diagonal = 0
    for col, value in enumerate(table[x]):
        if value == player:
            colonne += 1
    for row, value in enumerate([table[0][y], table[1][y], table[2][y]]):
        if value == player:
            ligne += 1
    for row, value in enumerate([table[0][0], table[1][1], table[2][2]]):
        if value == player:
            diagonal += 1
    if diagonal != 3:
        diagonal = 0
        for row, value in enumerate([table[2][0], table[1][1], table[0][2]]):
            if value == player:
                diagonal += 1
    if diagonal == 3 or colonne == 3 or ligne == 3:
        return True
    else:
        return False

#######################################################
### VERIFIE SI LE JOUEUR PEUT SELECTIONNER UNE CASE ###
#######################################################

def can_play():
    for x in range(3):
        for y in range(3):
            if table[x][y] == 0:
                return True
    return False

############################
### CHANGEMENT DE JOUEUR ###
############################

def next(player):
    if player == 1:
        return 2
    else:
        return 1

#######################################
### DEMARRAGE D'UNE NOUVELLE PARTIE ###
#######################################

def newgame():
    global TEXTPOSNEW
    x = int(pygame.mouse.get_pos()[0])
    y = int(pygame.mouse.get_pos()[1])
    if x > TEXTPOSNEW.left and x < TEXTPOSNEW.right and y > TEXTPOSNEW.top and y < TEXTPOSNEW.bottom:
        return True

#####################
### QUITTE LE JEU ###
#####################

def quitgame():
    global TEXTPOSQUIT
    x = int(pygame.mouse.get_pos()[0])
    y = int(pygame.mouse.get_pos()[1])
    if x > TEXTPOSQUIT.left and x < TEXTPOSQUIT.right and y > TEXTPOSQUIT.top and y < TEXTPOSQUIT.bottom:
        return True
    
###########################
### FONCTION PRINCIPALE ###
###########################
            
display()

previous = (-1, -1)
run = True
wingame = False
while run:
    event = pygame.event.wait()
    display()
    if event.type == MOUSEBUTTONDOWN:
        # Si le joueur clique sur une case
        if add() and not wingame:
            if win(player):
                TEXT = "Joueur " + str(player) + " est une bite !"
                wingame = True
            elif not can_play():
                TEXT = "Match nul !"
            player = next(player)
        # Si le joueur clique sur le bouton "new"
        elif newgame():
            wingame = False
            TEXT = ""
            table = [[0] * 3 for i in range(3)]
            tablesprites = [[0] * 3 for i in range(3)]
            previous = (-1, -1)
            player = player_start
            player_start = next(player_start)
        # Si le joueur clique sur le bouton "exit"
        elif quitgame():
            run = False
    elif event.type == QUIT:
        run = False

pygame.quit()
