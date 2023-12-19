import pygame
from pygame.locals import QUIT
from model.Partie import Partie


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