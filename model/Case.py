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
        
    def get_question(self):
        self.questions_id = []
        question_data = self.table.random_question(
            f"SELECT * FROM questions WHERE theme_id = {self.theme} AND questions_id NOT IN ({','.join(map(str, self.questions_id))}) ORDER BY RANDOM() LIMIT 1" )
        self.questions_id.append(question_data[0])
        # for i in self.questions_id:
        #     if i == question_data[0]:
        #         self.get_question()
        # else:
        return question_data
    
    
    def set_walkable_cases(self, *args):
        self.walkable_cases = args
        print(self.position, self.walkable_cases)
        
    def toString(self):
        print('Case:', self.type_case, self.theme, self.walkable_cases)

