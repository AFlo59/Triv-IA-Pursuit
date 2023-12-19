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
        




    

    