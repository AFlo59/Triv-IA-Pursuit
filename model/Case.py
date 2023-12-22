import math
from connectbdd import ConnectBdd


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
    def __init__(self, screen: pg.Surface = None, type_case = 0, theme = 0, position = (0, 0), angle=.0, node = -1):
        super().__init__()
        
        self.type_case = type_case
        self.theme = theme
        self.screen = screen
        self.node = node
        self.position = position
        self.angle = angle
        self.questions_id = []
        self.table = ConnectBdd()
        
        self.joueur = None
        self.disable = True
        self.size = 25
        self.color = pg.Color(theme[0])
        
        self.case_graf = Case_sprite(self, screen, pg.Color(theme[0]), position, self.angle)
        self.number_sprite = Number_sprite(screen, self, position, node)
    
    def set_position(self, position):
        self.case_graf.set_position(position)
        self.number_sprite.set_position(position)
        
    def set_rotation(self, angle):
        self.case_graf.set_rotation(angle)

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
        self.number_sprite.highlight()
        self.update()

    def reset_highlight(self):
        self.case_graf.reset_highlight()
        self.update()
        
    def get_question(self):
        full_sql_query = f"SELECT * FROM questions WHERE theme_id = {self.theme[1]} AND questions_id NOT IN ({','.join(map(str, self.questions_id))}) ORDER BY RANDOM() LIMIT 1"
        print(f"Executing SQL query: {full_sql_query}")
        
        question_data = self.table.random_question(full_sql_query)
        self.questions_id.append(question_data[0])
        return question_data
    
    def update(self):
        self.draw(self.screen)
        
    def toString(self):
        return (self.node, self.disable, self.type_case, self.theme)
    
class Case_sprite(Sprite):
    def __init__(self, group, screen, color, position, angle):
        super().__init__(group)

        self.size = 30
        self.color = color
        self.position = position
        self.screen = screen
        self.angle = angle

        self.image = pg.Surface((self.size, self.size), pg.SRCALPHA)
        
        pg.draw.rect(self.image, self.color, (0, 0, self.size, self.size))
        self.set_rotation(angle)
        
    def set_position(self, position):
        self.position = position
        self.rect = self.image.get_rect(center=position)
        self.update()
        
    def set_rotation(self, angle):
        self.angle = angle
        self.image = pg.transform.rotate(self.image , self.angle)
        self.rect = self.image.get_rect(center=self.position)
        
    def highlight(self):
        self.image = pg.transform.smoothscale(self.image, (self.size + 20, self.size + 20))
        self.rect = self.image.get_rect(center=self.position)
        
    def reset_highlight(self):
        self.image = pg.transform.smoothscale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect(center=self.position)
    
class Number_sprite(Sprite):
    def __init__(self, screen, group, position, node):
        super().__init__(group)
        self.position = position
        self.node = node
        self.screen = screen
        
        pg.font.init()
        self.set_text(node)
        
    def set_text(self, text=''):
        font = pg.font.SysFont('Arial', 12)
        text = font.render(f'{self.node}', True, pg.Color('darkolivegreen'))
        self.image = pg.Surface((50, 50), pg.SRCALPHA)

        W = text.get_width()
        H = text.get_height()
        self.image.blit(text, [25 - W/2, 25 - H/2])
        self.rect = self.image.get_rect(center=self.position)
        
    def set_position(self, position):
        self.position = position
        self.rect = self.image.get_rect(center=position)
        
    def highlight(self):
        self.set_text(self.node)
        self.set_position(self.position)