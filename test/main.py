import pygame
from Game.Partie import Partie
from Game.Joueur import Joueur

class Game:
    def __init__(self, screen, nom, prenom):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.partie = Partie()
        self.joueur = Joueur(nom, prenom, self.partie, x=4, y=4)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.joueur)

        # Define interface attributes
        self.interface_width = 500
        self.interface_height = 720
        self.interface_x = 1080 - self.interface_width
        self.interface_y = 0
        self.interface_bg_color = (255, 255, 255)
        self.interface_image = pygame.image.load('Triv-IA-Pursuit/test/interface_ui.png')
        self.interface_image = pygame.transform.scale(self.interface_image, (self.interface_width, self.interface_height))

    def gestion_des_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.joueur.velocity[0] = -1
        elif keys[pygame.K_RIGHT]:
            self.joueur.velocity[0] = 1
        else:
            self.joueur.velocity[0] = 0

        if keys[pygame.K_UP]:
            self.joueur.velocity[1] = -1
        elif keys[pygame.K_DOWN]:
            self.joueur.velocity[1] = 1
        else:
            self.joueur.velocity[1] = 0

    def update(self):
        self.joueur.move()
        # Update other game logic as needed

    def display(self):
        self.screen.fill((255, 255, 255))  # White background

        # Draw the game board on the left using sprites
        self.partie.plateau.all_sprites.update()  # Update the sprites
        self.partie.plateau.all_sprites.draw(self.screen)

        # Draw the interface on the right
        pygame.draw.rect(self.screen, self.interface_bg_color, (self.interface_x, self.interface_y, self.interface_width, self.interface_height))
        self.screen.blit(self.interface_image, (self.interface_x, self.interface_y))

        # Draw the player sprite
        self.all_sprites.update()  # Update the player sprite
        self.all_sprites.draw(self.screen)

        pygame.display.flip()

    def run(self):
        while self.running:
            self.gestion_des_event()
            self.update()
            self.display()
            self.clock.tick(30)

pygame.init()
screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption('Triv-IA-Pursuit')
game = Game(screen, "YourNom", "YourPrenom")
game.run()

pygame.quit()




# class Game:
#     def __init__(self, screen, nom, prenom):
#         self.screen = screen
#         self.running = True
#         self.clock = pygame.time.Clock()
#         self.partie = Partie()
#         self.joueur = Joueur(nom, prenom, self.partie, x=4, y=4)
#         self.all_sprites = pygame.sprite.Group()
#         self.all_sprites.add(self.joueur)

#         # Define interface attributes
#         self.interface_width = 500
#         self.interface_height = 720
#         self.interface_x = 1080 - self.interface_width
#         self.interface_y = 0
#         self.interface_bg_color = (255, 255, 255)
#         self.interface_image = pygame.image.load('test/assets/interface_ui.png')
#         self.interface_image = pygame.transform.scale(self.interface_image, (self.interface_width, self.interface_height))


#     def gestion_des_event(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 self.running = False
                
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_LEFT]:
#             self.joueur.velocity[0] = -1
#         elif keys[pygame.K_RIGHT]:
#             self.joueur.velocity[0] = 1
#         else:
#             self.joueur.velocity[0] = 0

#         if keys[pygame.K_UP]:
#             self.joueur.velocity[1] = -1
#         elif keys[pygame.K_DOWN]:
#             self.joueur.velocity[1] = 1
#         else:
#             self.joueur.velocity[1] = 0
    
#     def update(self):
#         self.joueur.move()
        # Update other game logic as needed
    
    # def display(self):
    #     self.screen.fill('white')
    #     # Draw the game board on the left
    #     for row in self.partie.plateau.cases:
    #         for case in row:
    #             pygame.draw.rect(self.screen, (200, 200, 200), pygame.Rect(case.position[0] * 50, case.position[1] * 50, 50, 50))
    #             font = pygame.font.Font(None, 36)
    #             text = font.render(str(case.theme), True, (0, 0, 0))
    #             self.screen.blit(text, (case.position[0] * 50 + 20, case.position[1] * 50 + 20))
    #     # Draw the interface on the right
    #     pygame.draw.rect(self.screen, self.interface_bg_color, (self.interface_x, self.interface_y, self.interface_width, self.interface_height))
    #     self.screen.blit(self.interface_image, (self.interface_x, self.interface_y))
        
    #     self.all_sprites.draw(self.screen)
    #     pygame.display.flip()     
#         def display(self):
#             self.screen.fill('white')
#             # Draw the game board on the left using sprites
#             self.partie.plateau.all_sprites.draw(self.screen)
#             # Draw the interface on the right
#             pygame.draw.rect(self.screen, self.interface_bg_color, (self.interface_x, self.interface_y, self.interface_width, self.interface_height))
#             self.screen.blit(self.interface_image, (self.interface_x, self.interface_y))
            
#             self.all_sprites.draw(self.screen)
#             pygame.display.flip()
    
#     def run(self):
#         while self.running:
#             self.gestion_des_event()
#             self.update()
#             self.display()
#             self.clock.tick(30)

# pygame.init()
# screen = pygame.display.set_mode((1080, 720))
# pygame.display.set_caption('Triv-IA-Pursuit')
# game = Game(screen, "YourNom", "YourPrenom")
# game.run()

# pygame.quit()


        


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








