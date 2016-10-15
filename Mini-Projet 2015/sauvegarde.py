""" Gestion de la sauvegarde et du chargement d'une partie de Pentago. """

##################################
### 5.1 SAUVEGARDER UNE PARTIE ###
##################################

import pickle
import os
import pygame

import pentagoGUI
import sons
from constants import *

save_ok = False
load_ok = False
time_save = 40
time_load = 40

def print_load_save():
    """ Affiche les boutons "Sauvegarder" et "Quitter". """
    global load_ok
    global save_ok
    global time_save
    global time_load
    screen = pentagoGUI.get_screen()
    fixedtext = pentagoGUI.get_fixedtext()
    screen.blit(fixedtext[2][0], fixedtext[2][1])
    screen.blit(fixedtext[3][0], fixedtext[3][1])
    pygame.draw.rect(screen,text_color,fixedtext[2][2],2)
    pygame.draw.rect(screen,text_color,fixedtext[3][2],2)
    if save_ok and time_save > 0:
        screen.blit(fixedtext[4][0], fixedtext[4][1])
        time_save -= 1
    if load_ok and time_load:
        screen.blit(fixedtext[5][0], fixedtext[5][1])
        time_load -= 1
    if time_save <= 0:
        time_save = 40
        save_ok = False
    if time_load <= 0:
        time_load = 40
        load_ok = False
        
def load_save(pos_x,pos_y,board,player,pawn_played):
    """ Contrôle si l'utilisateur clique sur le bouton pour sauvegarder la partie ou le
    bouton pour la charger. """
    fixedtext = pentagoGUI.get_fixedtext()
    global load_ok
    global save_ok
    if pos_x > fixedtext[2][1].left and pos_x < fixedtext[2][1].right and \
       pos_y > fixedtext[2][1].top and pos_y < fixedtext[2][1].bottom:
        save_game(board,player,pawn_played)
        save_ok = True
        sons.play_clic()
    elif pos_x > fixedtext[3][1].left and pos_x < fixedtext[3][1].right and \
       pos_y > fixedtext[3][1].top and pos_y < fixedtext[3][1].bottom:
        load_ok = True
        sons.play_clic()
        return load_game(board,player,pawn_played)
    return board,player,pawn_played

def save_game(board,player,pawn_played):
    """ Sauvegarde le plateau de jeu, le joueur en cours ainsi que le booléen indiquant
    si le joueur a déja joué un pion dans un fichier. """
    game_to_save = [0] * 3
    game_to_save[0] = board
    game_to_save[1] = player
    game_to_save[2] = pawn_played
    file = open(file_name,"wb")
    pickler = pickle.Pickler(file)
    pickler.dump(game_to_save)

def load_game(board,player,pawn_played):
    """ Charge les données sauvegardées au sein d'une variable si le fichier existe. """
    game_to_save = [0] * 3
    if os.path.exists(file_name):
        file = open(file_name,"rb")
        pickler = pickle.Unpickler(file)
        game_to_save = pickler.load()
        file.close()
        board = game_to_save[0]
        return board,game_to_save[1],game_to_save[2]
    else:
        return board,player_pawn_played
