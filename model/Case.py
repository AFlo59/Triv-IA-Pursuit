TYPE_CASE = {
    'theme': 0,
    'gain': 1,
    'raccourci' : 2,
    'start': 3,
    'null' : 4
}

class Case:
    def __init__(self, type_case = 0, theme = 0, graf = '󠁛󠁛󠁛⬛'):
        self.type_case = type_case
        self.theme = theme
        self.graf = graf
        
    def get_question(self):
        # TODO get_question
        print('get question')
        return 'question'
            
    def toString(self):
        print('Case:', self.type_case, self.theme)