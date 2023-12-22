import pygame
from pygame.sprite import Group

TYPE_CASE = {
    'theme': 0,
    'gain': 1,
    'raccourci' : 2,
    'null' : 4
}

class Case(Group):
    def __init__(self, position, type_case=0, theme=0, graf='󠁛󠁛󠁛⬛', theme_colors=None):
        self.position = position
        self.type_case = type_case
        self.theme = theme
        self.graf = graf
        self.walkable_cases = None
        self.sprites = Group()
        
    def get_question(self):
        # TODO get_question
        print('get question')
        return 'question'
    
    def set_walkable_cases(self, *args):
        self.walkable_cases = args
        print(self.position, self.walkable_cases)
        
    def toString(self):
        print('Case:', self.type_case, self.theme, self.walkable_cases)
        return f'Case: {self.type_case}, Theme: {self.theme}, Walkable Cases: {self.walkable_cases}'