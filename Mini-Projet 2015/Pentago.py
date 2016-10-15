import pentagoGUI
import pygame

import rotations
import bases
import alignements
import sauvegarde
import sons
import constants
import animation

""" FONCTION PRINCIPALE """

###############################
### 4.4 LA PROCEDURE DE JEU ###
###############################

# Création d'un plateau de 6 cases sur 6 cases
size = 6
board = bases.create_list(size)
# Initialisation du joueur et du nombre de coups nécessaires
player = 1
align = 5
# Initialise l'écran
pentagoGUI.init_screen()
# Efface le curseur par défaut de la souris
pygame.mouse.set_visible(False)
# Initialisation du booléen indiquant si la partie continue ou non
run = True
# Initialisation du booléen indiquant si un pion a été posé ou non
pawn_played = False
# Initialisation du booléen indiquant si un joueur a gagné ou qu'il y a match nul
finish = False
# Initialisation de l'horloge
clock = pygame.time.Clock()
# Initialisation de la position de l'animation
frame_pos = constants.frame_pos

# Joue tant que personne n'a gagné, qu'il reste de la place sur le plateau et qu'on ne quitte
# pas la partie
while run:

    # Récupère la position de la souris
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Dessine le plateau et le joueur en cours et affiche si le joueur doit poser
    # un pion ou tourner un quadrant
    pentagoGUI.clear_screen()
    pentagoGUI.draw_board(board)
    if not pawn_played and not finish:
        pentagoGUI.print_player_turn(player)
    elif pawn_played and not finish:
        pentagoGUI.prepare_rotate_quad(board)
    elif finish:
        win = pentagoGUI.game_over(player,bases.is_full(board))
        if win and frame_pos < constants.frame_end:
            animation.play_anim(frame_pos)
            frame_pos += 10

    # Parcourt les évènements 
    for event in pygame.event.get():
        # Si l'utilisateur quitte le programme
        if event.type == pygame.QUIT:
            run = False
        # Si l'utilisateur clique dans la fenêtre
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not pawn_played and not finish:
                pawn_played = pentagoGUI.put_pawn(board,player,mouse_x,mouse_y)
            elif pawn_played and not finish:
                pawn_played = pentagoGUI.rotate_quad(mouse_x,mouse_y,board)
                if player == 1 and not pawn_played:
                    player = 2
                elif player == 2 and not pawn_played:
                    player = 1
            elif finish:
                run = pentagoGUI.retry_leave(mouse_x,mouse_y)
                if run:
                    player = 1
                    board = bases.create_list(size)
                    finish = False
                    pawn_played = False
                    frame_pos = constants.frame_pos
                    sons.reboot_sounds()
            board,player,pawn_played = sauvegarde.load_save(mouse_x,mouse_y,board,player,pawn_played)

    if alignements.is_align(size,board,align,player) or bases.is_full(board):
        finish = True
    
    pentagoGUI.blit_cursor(mouse_x,mouse_y)
    clock.tick(30)
    
    pentagoGUI.display_update()

pygame.quit()
