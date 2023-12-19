import pygame
from pygame.locals import QUIT
from model.Partie import Partie
from model.Plateau import Plateau
from model.Joueur import Joueur
from model.Case import Case
from utils import de

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
FPS = 30

# Colors
WHITE = (255, 255, 255)

# Create the game
partie = Partie()

# Create the Pygame screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Board Game")

# Clock to control the frame rate
clock = pygame.time.Clock()


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                
                mouse_x, mouse_y = pygame.mouse.get_pos()
                clicked_row = mouse_y // 50
                clicked_col = mouse_x // 50
                print(f"Clicked on row {clicked_row}, column {clicked_col}")

    # Draw the game board
    screen.fill(WHITE)
    
    # Draw the game board from the Plateau class
    for row in partie.plateau.cases:
        for case in row:
            pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(case.position[0] * 50, case.position[1] * 50, 50, 50))
            font = pygame.font.Font(None, 36)
            text = font.render(str(case.theme), True, (0, 0, 0))
            screen.blit(text, (case.position[0] * 50 + 20, case.position[1] * 50 + 20))

    # Update the display
    pygame.display.flip()


    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()




        


#     start = False
#     position_start = {'row': 4, 'col': 4}

#     def Move_right(self):
#         row = self.position_player['row']
#         col = self.position_player['col']
#         if col < COLS -1:
#             self.cases[row][col] = 'x'
#             col += 1
#             self.position_player['col'] = col
#             self.cases[row][col] = 'J'

#     def Move_left(self):
#         row = self.position_player['row']
#         col = self.position_player['col']
#         if col > 0:
#             self.cases[row][col] = 'x'
#             col -= 1
#             self.position_player['col'] = col
#             self.cases[row][col] = 'J'

#     def Move_up(self):
#         row = self.position_player['row']
#         col = self.position_player['col']
#         if row > 0:
#             self.cases[row][col] = 'x'
#             row -= 1
#             self.position_player['row'] = row
#             self.cases[row][col] = 'J'

#     def Move_down(self):
#         # Fonction pour déplacer le joueur vers le bas
#         row = self.position_player['row']
#         col = self.position_player['col']
#         if row < ROWS - 1:
#             # Efface la position actuelle du joueur
#             self.cases[row][col] = 'x'
#             # Déplace le joueur vers le bas
#             row += 1
#             self.position_player['row'] = row
#             # Met à jour la nouvelle position du joueur
#             self.cases[row][col] = 'J'
    
#     def Move_right_up(self):
#         row = self.position_player['row']
#         col = self.position_player['col']
#         if row == col and row > 0:
#             if row >= 4 and col <= 4:
#                 self.cases[row][col] = 'x'
#                 row -= 1 
#                 col += 1
#                 self.position_player['row'] = row
#                 self.position_player['col'] = col
#                 self.cases[row][col] = 'J'








