from pygame.sprite import Sprite
import pygame as pg
from pygame.sprite import Group

from model.Joueur import Joueur

TYPE_CASE = {
    'theme': 0,
    'gain': 1,
    'raccourci' : 2,
    'start': 3,
    'null' : 4
}

class Case(Sprite):
    def __init__(self, screen: pg.Surface = None, type_case = 0, theme = 0, position = (0, 0), node = -1):
        super().__init__()
        
        self.type_case = type_case
        self.theme = theme
        self.screen = screen
        self.node = node
        self.position = position

        self.joueur = None
        self.disable = True
        self.size = 25
        self.color = pg.Color(theme[0])

        self.image = pg.Surface((self.size, self.size))
        self.rect = self.image.get_rect(center=position)
        
        pg.draw.rect(self.image, self.color, (0, 0, self.size, self.size))
        # image = pg.transform.rotate(self.image , 20)
        # self.screen.blit(image, self.rect)

        
        # self.image = pg.Surface((50, 50))
        # #self.image.fill(pg.Color(theme[0]))
        # print(position)
        # pg.draw.circle(self.image, pg.Color(theme[0]), center=position, radius=RAYON)
        # self.rect = self.image.get_rect()
    
    def set_position(self, position):
        self.position = position
        self.rect = self.image.get_rect(center=position)
        self.update()

    def render(self, group: Group):
        group.add(self)
        self.update()
    
    def on_click(self):
        if self.disable == False and self.joueur is not None:
            self.joueur.set_question(self.get_question())
            #print(self.toString())

    def attach_joueur(self, joueur: Joueur):
        self.joueur = joueur

    def detach_joueur(self):
        self.joueur = None
        self.reset_highlight()

    def set_disable(self, state = False):
        self.disable = state

    def highlight(self):
        self.set_disable(False)
        print('highlight:', self.toString())
        image = pg.transform.scale(self.image, (self.size + 10, self.size + 10))
        self.screen.blit(image, self.rect)
        self.update()

    def reset_highlight(self):
        image = pg.transform.scale(self.image, (self.size, self.size))
        self.screen.blit(image, self.rect)
        self.update()
        
    def get_question(self):
        # TODO get_question
        return f'question theme {self.theme}'
            
    def toString(self):
        return (self.node, self.disable, self.type_case, self.theme)