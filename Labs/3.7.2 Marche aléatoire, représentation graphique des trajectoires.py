import pygame
from random import *

WIDTH = 800
HEIGHT = 600

pygame.display.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((23, 23, 23))
pygame.display.set_caption('Marche aléatoire')

def initdisplay():
    pygame.draw.line(screen, (180,180,180), (20, HEIGHT / 2), (WIDTH - 20, HEIGHT / 2))
    pygame.draw.line(screen, (180,180,180), (20, 20), (20, HEIGHT - 20))
    pygame.display.flip()

def listepos(etapes, proba):
    liste = [0] * (etapes + 1)
    for i in range(1,etapes + 1):
        if random() > proba:
            liste[i] = liste[i - 1] - 1
        else:
            liste[i] = liste[i - 1] + 1
    return liste

def maxval(liste):
    listeabsolue = [abs(i) for i in liste]
    return max(listeabsolue)

def dessincourbe(etapes, proba):

    liste = listepos(etapes, proba)
    xtrait = 760 / etapes
    ytrait = 280 / maxval(liste)
    
    y = 0
    y = HEIGHT / 2
    x = 20
    oldy = HEIGHT - ytrait
    
    for i in range(1, len(liste)):
        
        if liste[i] > liste[i - 1]:
            oldy = y
            y = y + ytrait
        else:
            oldy = y
            y = y - ytrait

        x += xtrait
        
        pygame.draw.line(screen, (255,0,0), (x - xtrait, oldy), (x, y))

    pygame.display.flip()
    
initdisplay()
dessincourbe(250, 0.5)

