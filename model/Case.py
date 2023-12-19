from connectbdd import ConnectBdd
from model.Plateau import Plateau


TYPE_CASE = {
    'theme': 0,
    'gain': 1,
    'raccourci' : 2,
    'null' : 4
}

class Case:
    def __init__(self) -> None:
        self.position = (None, None)
        self.type = 0
        self.plateau = Plateau()
        
    def get_question(self, theme_id):
        self.table = ConnectBdd()
        question_data = self.table.random_question(f"SELECT * FROM questions WHERE theme_id = {theme} ORDER BY RANDOM() LIMIT 1")
        return question_data
        




    

    
    def __init__(self, position, type_case = 0, theme = 0, graf = '󠁛󠁛󠁛⬛'):
        self.position = position
        self.type_case = type_case
        self.theme = theme
        self.graf = graf
        self.walkable_cases = None
        
    def get_question(self):
        # TODO get_question
        print('get question')
        return 'question'
    
    def set_walkable_cases(self, *args):
        self.walkable_cases = args
        print(self.position, self.walkable_cases)
        
    def toString(self):
        print('Case:', self.type_case, self.theme, self.walkable_cases)
