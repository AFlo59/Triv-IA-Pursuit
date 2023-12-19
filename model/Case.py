from connectbdd import ConnectBdd


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
        self.walkable_cases = None
        self.table = ConnectBdd()
        
    def get_question(self, questions_id):
        theme_id = self.theme  # Sauvegardez le thème actuel de la case
        question_data = self.table.random_question(
            f"SELECT * FROM questions WHERE theme_id = {theme_id} AND questions_id NOT IN ({','.join(map(str, questions_id))}) ORDER BY RANDOM() LIMIT 1",
            questions_id
        )
        if question_data:
            self.theme = question_data[7]  # Mettez à jour le thème uniquement si une question est trouvée
        return question_data
    
    # AND questions_id NOT IN ({','.join(map(str, questions_id))})
    
    def set_walkable_cases(self, *args):
        self.walkable_cases = args
        print(self.position, self.walkable_cases)
        
    def toString(self):
        print('Case:', self.type_case, self.theme, self.walkable_cases)
