import pygame
from pygame.sprite import Sprite
from .Case import TYPE_CASE

# Use THEME_COLORS for theme numbers
THEME_COLORS = {
    1: (255, 0, 0),    # Rouge
    2: (0, 0, 255),    # Bleu
    3: (225, 240, 9),  # Jaune
    4: (217, 9, 240),  # Violet
    5: (9, 240, 56),   # Vert
    6: (240, 163, 9),  # Orange
}

CASE_SIZE = 30

class CaseSprite(pygame.sprite.Sprite):
    def __init__(self, case, theme_colors):
        super().__init__()
        self.case = case  # Assign the case to an instance variable
        self.image = pygame.Surface((CASE_SIZE, CASE_SIZE))
        emoji_key = ord(case.graf[0]) if case.graf else None  # Convert the first character of emoji to its Unicode code point
        self.image.fill(theme_colors.get(emoji_key, (255, 255, 255)))  # Use emoji_key as the key
        self.rect = self.image.get_rect(topleft=(case.position[0] * CASE_SIZE, case.position[1] * CASE_SIZE))

    def update(self):
        # Mettre à jour les propriétés du sprite en fonction de la case
        if self.case.type_case == TYPE_CASE['theme']:
            theme_color = THEME_COLORS.get(self.case.theme, (255, 255, 255))  # Use theme information here
            self.image.fill(theme_color)
        else:
            self.image.fill((255, 255, 255))  # Couleur par défaut

        self.rect.topleft = (self.case.position[0] * CASE_SIZE, self.case.position[1] * CASE_SIZE)  # Position du sprite

    def draw(self, surface):
        # Afficher le sprite sur la surface donnée
        surface.blit(self.image, self.rect.topleft)