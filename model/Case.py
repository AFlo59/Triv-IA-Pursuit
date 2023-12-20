from pygame.sprite import Sprite
import pygame as pg
from pygame.sprite import Group

TYPE_CASE = {
    'theme': 0,
    'gain': 1,
    'raccourci' : 2,
    'start': 3,
    'null' : 4
}

class Case(Sprite):
    def __init__(self, screen: pg.Surface = None, type_case = 0, theme = 0, position = (0, 0)):
        super().__init__()
        
        self.type_case = type_case
        self.theme = theme
        self.screen = screen
        
        self.image = pg.Surface((50, 50))
        self.image.fill(pg.Color(theme[0]))
        self.rect = pg.Rect(position, (50, 50))
        
        # self.image = pg.Surface((50, 50))
        # #self.image.fill(pg.Color(theme[0]))
        # print(position)
        # pg.draw.circle(self.image, pg.Color(theme[0]), center=position, radius=RAYON)
        # self.rect = self.image.get_rect()
        
    def render(self, group: Group):
        group.add(self)
        self.update()
    
    def set_rect(self, x, y):
        self.rect.centerx = x
        self.rect.centery = y
        self.update()
        
    def get_question(self):
        # TODO get_question
        print('get question')
        return 'question'
            
    def toString(self):
        print('Case:', self.type_case, self.theme)