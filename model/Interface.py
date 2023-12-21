from pygame import Surface
from pygame.sprite import Sprite
import pygame as pg

from model.Joueur import Joueur


class Interface:
    def __init__(self, screen: Surface) -> None:
        pg.draw.rect(screen, pg.Color('red'), pg.Rect(1000, 0, 500, 800))
        print(f'eeeeeeee')        
        interface_bg_color = (255, 0, 0)
        interface_image = pg.image.load('model/interface.jpg')
        interface_image = pg.transform.scale(interface_image, (500, 800))
        interface_rect = pg.Rect(1000, 0, 500, 800)
        pg.draw.rect(screen, interface_bg_color, interface_rect)
        screen.blit(interface_image, (1000, 0))


    def update_joueur(self, joueur: Joueur):
        print(joueur.toString())

    def update_question(self, joueur: Joueur):
        # Affiche les questions et les choix dans l'interface
        question_text = joueur.question_text
        choices_text = joueur.choices

        # self.draw_text(self.screen, question_text, self.interface_x + 10, self.interface_y + 10, font_size=24)
        # for i, choice in enumerate(choices_text):
        #     self.draw_text(self.screen, choice, interface_x + 10, interface_y + 50 + i * 30)

    # Fonction pour dessiner du texte sur l'écran
    def draw_text(screen, text, x, y, font_size=20, color=(255, 255, 255)):
        font = pg.font.Font(None, font_size)
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, (x, y))