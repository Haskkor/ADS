""" Gère l'animation se déclenchant lors de la victoire d'un joueur. """

##############################
### 5.2 ANIMATION VICTOIRE ###
##############################

import pygame

import pentagoGUI
from constants import *

def init_frames():
    frames = []
    frames.append(pygame.image.load(r"assets\frame-1.png"))
    frames.append(pygame.image.load(r"assets\frame-2.png"))
    frames.append(pygame.image.load(r"assets\frame-3.png"))
    frames.append(pygame.image.load(r"assets\frame-4.png"))
    frames.append(pygame.image.load(r"assets\frame-5.png"))
    frames.append(pygame.image.load(r"assets\frame-6.png"))
    return frames

def play_anim(i):
    frames = init_frames()
    screen = pentagoGUI.get_screen()
    frame = (i // 30) % len(frames)
    screen.blit(frames[frame],(i,height // 4))
