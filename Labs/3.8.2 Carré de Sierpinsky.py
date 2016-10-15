import pygame
import sys

white = (255, 255, 255)

black = (0, 0, 0)

def sierpinskiCarpet(points, level, window):

    if level == 0:
        pygame.draw.polygon(window, black, (points[0],points[1],points[2],points[3]))
    else:
        x_0 = points[0]
        x_02 = points[2]
        x_1 = (points[0]/3)*2 +  (points[2])/3
        x_2 = (points[0])/3   + ((points[2])/3)*2
 
        y_0 = (points[1])
        y_02 = (points[3])
        y_1 = ((points[1])/3) + (points[3])/3
        y_2 = (((points[1])/3)*2) + ((points[2])/3)*2


        top1 = (points[0], points[1], x_1, y_2)
        top2 = (x_1, y_0, x_2, y_2)
        top3 = (x_2, y_0, x_02, y_2)

        med1 = (x_0, y_2, x_1, y_1)
        med3 = (x_2, y_2, x_02, y_1)

        bottom1 = (x_0, y_1, x_1, y_02)
        bottom2 = (x_1, y_1, x_2, y_02)
        bottom3 = (x_2, y_1, points[2], points[3])


        sierpinskiCarpet(top1, level - 1, window)
        sierpinskiCarpet(top2, level - 1, window)
        sierpinskiCarpet(top3, level - 1, window)
        sierpinskiCarpet(med1, level - 1, window)
        sierpinskiCarpet(med3, level - 1, window)
        sierpinskiCarpet(bottom1, level - 1, window)
        sierpinskiCarpet(bottom2, level - 1, window)
        sierpinskiCarpet(bottom3, level - 1, window)


def main():
    #get the depth from the system arguemtns
    depth = 3
    #set up the window using GraphWin
    
    size = [600, 600]
    window = pygame.display.set_mode(size)

    pygame.display.set_caption("Sierpinski Carpet")
    #set the corrdiantes of the window
    #window.setCoords(-0.1, -0.1, 1.1, 1.1)
    #list the starting points for the first square
    points = [0, 2, 2, 0]

    #call the function with the points
    sierpinskiCarpet(points, depth, window)
    #close the window when clicked
    window.getMouse()

main()
