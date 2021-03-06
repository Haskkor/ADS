import pygame, sys
from pygame.locals import*

# Timer
clock = pygame.time.Clock()

def newslope(slp):
    return (slp - 1.732)/(1+slp*1.732)

def midpoint(p1,p2):
    return ((p1[0]+p2[0])/2,(p2[1]+p1[1])/2)

def slope(p1,p2):
    x = (p2[0]-p1[0])
    y = (p1[1]-p2[1])
    if x == 0 or y==0:
        return (y/3,x/3)
    s = float(y)/x 
    return s

def firstpoint(p1,p2):
    return (p1[0]+(p2[0]-p1[0])/3,p1[1]-(p1[1]-p2[1])/3)

def secondpoint(p1,p2,ns,s):
    x = int((-s*(p2[1]-p1[1])+p2[0]+ns*s*p1[0])/(1+s*ns))
    y = int(-ns*(x-p1[0])+p1[1])
    return (x,y)

screen = pygame.display.set_mode((700,540))
pygame.display.set_caption('Koch')

occu = 5
  
while 1:
    screen.fill((255,255,255))
    a =[(150,375),(550,375),(350,29),(150,375)]
    pygame.draw.polygon(screen, (200, 0, 0),(a[0],a[1],a[2]),1)
  
    pygame.display.update()
    clock.tick(3)
    for n in range(occu):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        i = 0
        while i < len(a)-1:
            s = slope(a[i],a[i+1])
            first=firstpoint(a[i],a[i+1]) 
            third=firstpoint(a[i+1],a[i])
            mp = midpoint(a[i],a[i+1])
            if type(s) != type(0.1):
                second = (mp[0]+s[0],mp[1]+s[1])
            else:
                ns = newslope(s)
                second=secondpoint(first,mp,ns,s) 
            pygame.draw.line(screen, (255,255,255),first,third,4)
            pygame.draw.line(screen, (200, 0, 0),first,second,1)
            pygame.draw.line(screen, (200, 0, 0),second,third,1)
            a = a[:i+1]+[first,second,third]+a[i+1:]
            i += 4
        pygame.display.update()
        clock.tick(3)
