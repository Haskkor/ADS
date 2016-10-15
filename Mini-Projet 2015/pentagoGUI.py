""" Interface graphique du Pentago. """

#######################################
### 4.1 AFFICHAGE DU PLATEAU DE JEU ###
#######################################

import pygame
from pygame.locals import *

import bases
import rotations
from constants import *
import sons
import sauvegarde

# Initialisation de l'image du curseur
cursor = pygame.image.load(r"assets/cursor.png")

def init_screen():
    """ Initialise la fenêtre du programme. """
    pygame.display.init()
    pygame.font.init()
    global screen
    global FONT
    global TABLESPRITES
    global FIXEDTEXT
    FONT = pygame.font.SysFont("arial", 25)
    screen = pygame.display.set_mode((width, height))
    screen.fill(color_back)
    pygame.display.set_caption('Pentago')
    TABLESPRITES = fill_tablesprites()
    FIXEDTEXT = fill_tabletexts()

def get_screen():
    """ Retourne la surface d'affichage. """
    return screen

def get_fixedtext():
    """ Retourne la liste des textes. """
    return FIXEDTEXT

def clear_screen():
    """ Vide l'écran en le remplissant avec la couleur de fond. """
    screen.fill(color_back)

def blit_cursor(mouse_x,mouse_y):
    """ Affiche l'image personnalisée de curseur à l'emplacement de la souris. """
    screen.blit(cursor,(mouse_x,mouse_y))

def fill_tabletexts():
    """ Remplit un tableau contenant la définition des boutons dont le texte ne change
    pas du jeu : Sauvegarder, Charger, Rejouer, Quitter... """
    table = [[0] * 4 for i in range(6)]
    
    text_retry = "Rejouer"
    text_leave = "Quitter"
    text_save = "Sauvegarder"
    text_load = "Charger"
    text_save_ok = "Fait"
    text_load_ok = "Fait"

    textrender_retry = FONT.render(text_retry, 1, text_color)
    textrender_leave = FONT.render(text_leave, 1, text_color)
    textrender_save = FONT.render(text_save, 1, text_color)
    textrender_load = FONT.render(text_load, 1, text_color)
    textrender_save_ok = FONT.render(text_save_ok, 1, text_color)
    textrender_load_ok = FONT.render(text_load_ok, 1, text_color)

    textpos_retry = textrender_retry.get_rect()
    textpos_leave = textrender_leave.get_rect()
    textpos_save = textrender_save.get_rect()
    textpos_load = textrender_load.get_rect()
    textpos_save_ok = textrender_save_ok.get_rect()
    textpos_load_ok = textrender_load_ok.get_rect()

    textpos_retry.left = screen.get_rect().right - screen.get_rect().width // 5
    textpos_retry.top = screen.get_rect().top + screen.get_rect().height // 12 * 2
    textpos_leave.left = screen.get_rect().right - screen.get_rect().width // 5
    textpos_leave.top = screen.get_rect().top + screen.get_rect().height // 12 * 3
    textpos_save.left = screen.get_rect().left + screen.get_rect().width // 5
    textpos_save.top = screen.get_rect().top + screen.get_rect().height - \
                        screen.get_rect().height // 8
    textpos_load.left = screen.get_rect().left + screen.get_rect().width // 5 * 2
    textpos_load.top = screen.get_rect().top + screen.get_rect().height - \
                        screen.get_rect().height // 8
    textpos_save_ok.left = textpos_save.left
    textpos_save_ok.top = textpos_save.top - textpos_save_ok.height - 10
    textpos_load_ok.left = textpos_load.left
    textpos_load_ok.top = textpos_load.top - textpos_load_ok.height - 10

    table[0] = [textrender_retry,textpos_retry,(textpos_retry.left-5, \
                    textpos_retry.top-5,textpos_retry.width+10,textpos_retry.height+10)]
    table[1] = [textrender_leave,textpos_leave,(textpos_leave.left-5,textpos_leave.top-5, \
                    textpos_leave.width+10,textpos_leave.height+10)]
    table[2] = [textrender_save,textpos_save,(textpos_save.left-5, \
                    textpos_save.top-5,textpos_save.width+10,textpos_save.height+10)]
    table[3] = [textrender_load,textpos_load,(textpos_load.left-5, \
                    textpos_load.top-5,textpos_load.width+10,textpos_load.height+10)]
    table[4] = [textrender_save_ok,textpos_save_ok,(textpos_save_ok.left-5, \
                    textpos_save_ok.top-5,textpos_save_ok.width+10,textpos_save_ok.height+10)]
    table[5] = [textrender_load_ok,textpos_load_ok,(textpos_load_ok.left-5, \
                    textpos_load_ok.top-5,textpos_load_ok.width+10,textpos_load_ok.height+10)]
    return table

def fill_tablesprites():
    """ Remplit un tableau de sprites contenant les images de flèches devant être affichées
    pour permettre la rotation d'un quadrant, leur position, le quadrant qu'elles doivent
    permettre de faire tourner ainsi que le sens de rotation. """
    table = [[0] * 4 for i in range(8)]
    table[0] = (pygame.image.load(r"assets/arrow_top_left.png"),(screen.get_width()//5 \
                    +(size//2)-arrow_width//2,screen.get_height()//5-arrow_height), \
                    1,False)
    table[1] = (pygame.image.load(r"assets/arrow_top_right.png"),(screen.get_width()//5 \
                    +size+(size//2)-arrow_width//2,screen.get_height()//5-arrow_height), \
                    2,True)
    table[2] = (pygame.image.load(r"assets/arrow_up_right.png"), (screen.get_width()//5 \
                    +size*2,screen.get_height()//5+(size//2)-arrow_width//2), \
                    2,False)
    table[3] = (pygame.image.load(r"assets/arrow_down_right.png"),(screen.get_width()//5 \
                    +size*2,screen.get_height()//5+size+(size//2)-arrow_width//2), \
                    4,True)
    table[4] = (pygame.image.load(r"assets/arrow_bot_right.png"),(screen.get_width()//5 \
                    +size+(size//2)-arrow_width//2,screen.get_height()//5+size*2), \
                    4,False)
    table[5] = (pygame.image.load(r"assets/arrow_bot_left.png"),(screen.get_width()//5 \
                    +(size//2)-arrow_width//2,screen.get_height()//5+size*2), \
                    3,True)
    table[6] = (pygame.image.load(r"assets/arrow_down_left.png"), (screen.get_width()//5 \
                    -arrow_height,screen.get_height()//5+size+(size//2)-arrow_width//2), \
                    3,False)
    table[7] = (pygame.image.load(r"assets/arrow_up_left.png"),(screen.get_width()//5 \
                    -arrow_height,screen.get_height()//5+(size//2)-arrow_width//2), \
                    1,True)
    return table

def draw_board(board):
    """ Dessine le plateau de jeu. Quatre quadrants définis par : une
    couleur de bordure, une couleur de remplissage, une couleur d'emplacements
    de pions, une position en x (taille de l'écran divisée par 5 + taille
    du quadrant), une position en y (similaire à x), une taille, une
    taille de bordure, et un quadrant de la liste à deux dimensions. """
    quad = 0
    for i in range(2):
        for j in range(2):
            draw_quad(border_color,quad_color,screen.get_width()//5+size*j,
                      screen.get_height()//5+size*i,size,border_size,find_quad(quad,board),
                      hole_color,player1_color,player2_color,player_size,empty_size)
            quad += 1
    sauvegarde.print_load_save()

def find_quad(quad,board):
    """ Renvoie la partie de plateau nécessaire au dessin des cases de pions
    de découpant la liste à deux dimensions initiales. """
    n = len(board)
    temp_board = bases.create_list(n//2)
    x,y = 0,0
    
    if quad == 0:
        x_start,x_end,y_start,y_end = 0,n//2,0,n//2
    elif quad == 1:
        x_start,x_end,y_start,y_end = 0,n//2,n//2,n
    elif quad == 2:
        x_start,x_end,y_start,y_end = n//2,n,0,n//2
    elif quad == 3:
        x_start,x_end,y_start,y_end = n//2,n,n//2,n
        
    for i in range(x_start,x_end):
        for j in range(y_start,y_end):
            temp_board[x][y] = board[i][j]
            y += 1
        x += 1
        y = 0

    return temp_board
    
def draw_quad(border_color,quad_color,pos_x,pos_y,size,border_size,board,hole_color,
              player1_color,player2_color,player_size,empty_size):
    """ Dessine un quadrant du plateau de jeu. Dessine le carré rempli,
    dessine la bordure puis dessine les emplacements de pions. """
    pygame.draw.rect(screen,quad_color,(pos_x,pos_y,size,size))
    pygame.draw.rect(screen,border_color,(pos_x,pos_y,size,size), border_size)
    circle_x = (size // (len(board) * 2)) + pos_x
    circle_y = (size // (len(board) * 2)) + pos_y

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                pygame.draw.circle(screen,hole_color,(circle_x,circle_y),empty_size)
            elif board[i][j] == 1:
                pygame.draw.circle(screen,player1_color,(circle_x,circle_y),player_size)
            elif board[i][j] == 2:
                pygame.draw.circle(screen,player2_color,(circle_x,circle_y),player_size)
            circle_x += size // len(board)  
        circle_y += size // len(board)
        circle_x = (size // (len(board) * 2)) + pos_x

def game_over(player,board_full):
    """ Affiche le résultat de la partie ainsi que les boutons pour recommencer ou quitter
    la partie. """
    if board_full:
        text = "Match nul"
        win = False
    else:
        text = "Joueur {} gagne".format(player)
        sons.play_win()
        win = True
    
    textrender = FONT.render(text, 1, text_color)
    textpos = textrender.get_rect()
    textpos.left = screen.get_rect().right - screen.get_rect().width // 5
    textpos.top = screen.get_rect().top + screen.get_rect().height // 12
    
    screen.blit(textrender, textpos)
    screen.blit(FIXEDTEXT[0][0], FIXEDTEXT[0][1])
    screen.blit(FIXEDTEXT[1][0], FIXEDTEXT[1][1])

    pygame.draw.rect(screen,text_color,(textpos.left-5,textpos.top-5,textpos.width+10, \
                                       textpos.height+10),2)
    pygame.draw.rect(screen,text_color,FIXEDTEXT[0][2],2)
    pygame.draw.rect(screen,text_color,FIXEDTEXT[1][2],2)

    return win
    
def retry_leave(pos_x,pos_y):
    """ Contrôle si l'utilisateur clique sur le bouton pour continuer la partie ou le
    bouton pour la quitter et renvoie le résultat. """
    if pos_x > FIXEDTEXT[0][1].left and pos_x < FIXEDTEXT[0][1].right and \
       pos_y > FIXEDTEXT[0][1].top and pos_y < FIXEDTEXT[0][1].bottom:
        sons.play_clic()
        return True
    elif pos_x > FIXEDTEXT[1][1].left and pos_x < FIXEDTEXT[1][1].right and \
       pos_y > FIXEDTEXT[1][1].top and pos_y < FIXEDTEXT[1][1].bottom:
        sons.play_clic()
        return False
    
def display_update():
    """ Met à jour la fenêtre du programme. """
    pygame.display.update()

##########################
### 4.2 POSE D'UN PION ###
##########################

def print_player_turn(player):
    """ Affiche un texte indiquant quel joueur doit jouer dans le tour courant. """
    if player == 1:
        text = "Pion blanc"
    elif player == 2:
        text = "Pion noir"
    textrender = FONT.render(text, 1, text_color)
    textpos = textrender.get_rect()
    textpos.left = screen.get_rect().right - screen.get_rect().width // 5
    textpos.top = screen.get_rect().top + screen.get_rect().height // 12
    screen.blit(textrender, textpos)
    pygame.draw.rect(screen,text_color,(textpos.left-5,textpos.top-5,textpos.width+10, \
                                       textpos.height+10),2)
   
def put_pawn(board,player,pos_x,pos_y):
    """ Prend en paramètre une liste à deux dimensions réprésentant le plateau de jeu,
    la surface sur laquelle il sera dessiné, les coordonnées de la souris et un entier
    indiquant quel joueur est en train de jouer. """
    case_x = (pos_y - (screen.get_height() // 5)) // ((size * 2) // len(board))
    case_y = (pos_x - (screen.get_width() // 5)) // ((size * 2) // len(board))
    if case_x >= 0 and case_x < len(board) and case_y >= 0 and case_y < len(board) and \
       board[case_x][case_y] == 0:
        board[case_x][case_y] = player
        sons.play_clic()
        return True
    else:
        return False

##################################
### 4.3 ROTATION D'UN QUADRANT ###
##################################

def rotate_quad(pos_x,pos_y,board):
    """ Réalise la rotation du quadrant en elle-même. """
    for sprite in TABLESPRITES:
        if pos_x > sprite[1][0] and pos_x < (sprite[1][0] + sprite[0].get_rect().width) \
           and pos_y > sprite[1][1] and pos_y < (sprite[1][1] + sprite[0].get_rect().height):
            sons.play_clic()
            rotations.quadrant_rotate(len(board),board,sprite[2],sprite[3])
            return False
    return True

def prepare_rotate_quad(board):
    """ Permet au joueur de faire tourner un des quadrants. Affiche les flèches, affiche
    le texte indiquant qu'il faut faire tourner un quadrant puis réalise la rotation. """
    text = "Tourner quadrant"
    textrender = FONT.render(text, 1, text_color)
    textpos = textrender.get_rect()
    textpos.left = screen.get_rect().right - screen.get_rect().width // 5
    textpos.top = screen.get_rect().top + screen.get_rect().height // 12
    screen.blit(textrender, textpos)
    pygame.draw.rect(screen,text_color,(textpos.left-5,textpos.top-5,textpos.width+10, \
                                       textpos.height+10),2)
    for sprite in TABLESPRITES:
        screen.blit(sprite[0],sprite[1])
