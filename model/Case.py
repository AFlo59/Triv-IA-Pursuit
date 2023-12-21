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

class Case(Group):
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
        
        self.case_graf = Case_sprite(self, screen, pg.Color(theme[0]), position)
        self.number_sprite = Number_sprite(self, position, node)

        # image = pg.transform.rotate(self.image , 20)
        # self.screen.blit(image, self.rect)

        
        # self.image = pg.Surface((50, 50))
        # #self.image.fill(pg.Color(theme[0]))
        # print(position)
        # pg.draw.circle(self.image, pg.Color(theme[0]), center=position, radius=RAYON)
        # self.rect = self.image.get_rect()
    
    def set_position(self, position):
        self.case_graf.set_position(position)
        self.number_sprite.set_position(position)

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
        print('highlight:', self.toString())
        self.set_disable(False)
        self.case_graf.highlight()

    def reset_highlight(self):
        self.case_graf.reset_highlight()
        
    def get_question(self):
        # TODO get_question
        return f'question theme {self.theme}'
            
    def toString(self):
        return (self.node, self.disable, self.type_case, self.theme)
    
class Case_sprite(Sprite):
    def __init__(self, group, screen, color, position):
        super().__init__(group)

        self.size = 25
        self.color = color
        self.position = position
        self.screen = screen

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
        
    def highlight(self):
        image = pg.transform.scale(self.image, (self.size + 10, self.size + 10))
        self.screen.blit(image, self.rect)
        self.update()
        
    def reset_highlight(self):
        image = pg.transform.scale(self.image, (self.size, self.size))
        self.screen.blit(image, self.rect)
        self.update()
    
class Number_sprite(Sprite):
    def __init__(self, group, position, node):
        super().__init__(group)
        
        pg.font.init()
        font = pg.font.SysFont('Arial', 12)
        text = font.render(f'{node}', True, pg.Color('white'))
        self.image = pg.Surface((50, 50))
        self.rect = self.image.get_rect(center=position)

        W = text.get_width()
        H = text.get_height()
        self.image.blit(text, [25 - W/2, 25 - H/2])
        
    def set_position(self, position):
        self.position = position
        self.rect = self.image.get_rect(center=position)
        self.update()