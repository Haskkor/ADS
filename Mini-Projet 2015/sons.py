""" Gesion des sons du Pentago. """

##############################
### 5.2 ANIMATIONS SONORES ###
##############################

import pygame
import pentagoGUI

pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)
clic_sound = pygame.mixer.Sound(r"assets/click.wav")
win_sound = pygame.mixer.Sound(r"assets/win.wav")
draw_sound = pygame.mixer.Sound(r"assets/draw.wav")
play_win_ok = False
play_draw_ok = False

def play_clic():
    """ Joue le son du clic sur un bouton. """
    global clic_sound
    clic_sound.play()

def play_win():
    """ Joue le son de la victoire. """
    global win_sound
    global play_win_ok
    if not play_win_ok:
        win_sound.play()
        play_win_ok = True

def play_draw():
    """ Joue le son d'une partie finissant sur une égalité. """
    global draw_sound
    global play_draw_ok
    if not play_draw_ok:
        draw_sound.play()
        play_draw_ok = True

def reboot_sounds():
    """ Permet aux sons de victoire et d'égalité d'être rejoués. """
    global play_win_ok
    global play_draw_ok
    play_win_ok = False
    play_draw_ok = False
