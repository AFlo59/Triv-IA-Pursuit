from connectbdd import ConnectBdd


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
        
    def get_question(self):
        self.table = ConnectBdd()
        question_data = self.table.random_question('SELECT texte_question, bonne_reponse, choix1, choix2, choix3, choix4 FROM questions ORDER BY RANDOM() LIMIT 1')
        question_text = question_data[0]
        print(question_text)
        # TODO get_question
        
        self.table.commit()
        self.table.close()



    

    