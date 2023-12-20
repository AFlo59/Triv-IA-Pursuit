import pygame.sprite
from utils.utils import de

class Joueur(pygame.sprite.Sprite):
    def __init__(self, nom, prenom, partie, x, y) -> None:
        pygame.sprite.Sprite.__init__(self)
        try:
            self.image = pygame.image.load("player.png")
        except FileNotFoundError:
            # Provide a default image or print a message
            print("Player image not found. Using a default image.")
            self.image = pygame.Surface((30, 30))  # Placeholder surface
            self.image.fill((255, 255, 255))  # Placeholder color
        self.rect = self.image.get_rect(x=x, y=y)
        self.nom = nom
        self.prenom = prenom
        self.score = []
        self.position = (0, 0)
        self.partie = partie
        self.speed = 5
        self.velocity = [0, 0]

    def play(self):
        case = self.partie.plateau.move_joueur(self.position, de())
        print(case.toString())

    def toString(self):
        return f'{self.nom} {self.prenom}\t\t{self.score}'

    def move(self):
        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
