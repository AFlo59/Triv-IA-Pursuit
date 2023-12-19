import pygame
import sys

# Taille de la fenêtre
WIDTH, HEIGHT = 800, 600

ROWS = 9
COLS = 9

class Game:

    start = False
    position_start = {'row': 4, 'col': 4}
    def __init__(self):
        # Initialisation de la grille de jeu avec des 'x' selon les conditions spécifiées
        self.cases = []
        for row in range(ROWS):
            rowItems = []
            for col in range(COLS):
                if col == 0 or row == 0 or row == ROWS // 2 or row == ROWS - 1 or col == COLS - 1 or col == COLS // 2 or col == row or (col + row) + 1 == ROWS:
                    rowItems.append('x')
                else:
                    rowItems.append(' ')
            self.cases.append(rowItems)
        # Position initiale du joueur
        
        self.position_player = self.position_start
        self.cases[self.position_player['row']][self.position_player['col']] = 'J'
        # self.cases[self.position_start[4][self.position_start[4]]] = 'S'

    def Move_right(self):
        row = self.position_player['row']
        col = self.position_player['col']
        if col < COLS -1:
            self.cases[row][col] = 'x'
            col += 1
            self.position_player['col'] = col
            self.cases[row][col] = 'J'

    def Move_left(self):
        row = self.position_player['row']
        col = self.position_player['col']
        if col > 0:
            self.cases[row][col] = 'x'
            col -= 1
            self.position_player['col'] = col
            self.cases[row][col] = 'J'

    def Move_up(self):
        row = self.position_player['row']
        col = self.position_player['col']
        if row > 0:
            self.cases[row][col] = 'x'
            row -= 1
            self.position_player['row'] = row
            self.cases[row][col] = 'J'

    def Move_down(self):
        # Fonction pour déplacer le joueur vers le bas
        row = self.position_player['row']
        col = self.position_player['col']
        if row < ROWS - 1:
            # Efface la position actuelle du joueur
            self.cases[row][col] = 'x'
            # Déplace le joueur vers le bas
            row += 1
            self.position_player['row'] = row
            # Met à jour la nouvelle position du joueur
            self.cases[row][col] = 'J'
    
    def Move_right_up(self):
        row = self.position_player['row']
        col = self.position_player['col']
        if row == col and row > 0:
            if row >= 4 and col <= 4:
                self.cases[row][col] = 'x'
                row -= 1 
                col += 1
                self.position_player['row'] = row
                self.position_player['col'] = col
                self.cases[row][col] = 'J'



def draw_board(screen, game):
    # Fonction pour dessiner le plateau de jeu
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, (255, 255, 255), (col * 50, row * 50, 50, 50), 2)
            font = pygame.font.Font(None, 36)
            text = font.render(game.cases[row][col], True, (255, 255, 255))
            screen.blit(text, (col * 50 + 20, row * 50 + 10))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pygame Player Movement")

    game = Game()

    clock = pygame.time.Clock()
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    game.Move_down()
                if event.key == pygame.K_UP:
                    game.Move_up()
                if event.key == pygame.K_LEFT:
                    game.Move_left()
                if event.key == pygame.K_RIGHT:
                    game.Move_right()
                if event.key == pygame.K_SPACE:
                    game.Move_right_up()

        screen.fill((0, 0, 0))
        draw_board(screen, game)

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()