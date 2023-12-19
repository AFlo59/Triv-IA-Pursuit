TYPE_CASE = {
    'theme': 0,
    'gain': 1,
    'raccourci' : 2,
    'null' : 4
}

class Case:
    def __init__(self, position, type_case = 0, theme = 0, graf = '󠁛󠁛󠁛⬛'):
        self.position = position
        self.type_case = type_case
        self.theme = theme
        self.graf = graf
        self.walkable_cases = []
        
    def get_question(self):
        # TODO get_question
        print('get question')
        return 'question'
    
    def set_walkable_cases(self, cases):
        self.walkable_cases = cases
        print(self.position, self.walkable_cases)
        print(len(self.walkable_cases))
        
    def toString(self):
        print('Case:', self.type_case, self.theme, self.walkable_cases)