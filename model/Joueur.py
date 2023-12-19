from model.Case import Case
from model.Plateau import Plateau
from utils import de


from connectbdd import ConnectBdd


class Joueur:
    def __init__(self, nom, prenom) -> None:
        self.nom = nom
        self.prenom = prenom
        self.score = []
        self.position = (0, 0)
        self.case = Case()
        self.table = ConnectBdd()
        # TODO enregistrer en BDD
        
    def play(self, plateau: Plateau):
        plateau.move(self.position, de())
        self.insert_bdd()
        

    def insert_bdd(self):
        print(self.nom, self.prenom)
        self.table.create_joueur("INSERT INTO joueurs (nom, prenom) VALUES (?, ?)", (self.nom, self.prenom))
        self.table.commit()

    def get_answer(self):
        question_data = self.case.get_question()
        question_text = question_data[0]
        print(question_text)
        choices = question_data[2:6]
        correct_answer = question_data[1]
        for i, choice in enumerate(choices, start=65):
            print(f"{chr(i)}. {choice}")
        reponse = input('Votre réponse (écrit simplement A, B, C ou D) :')
        if reponse.upper() == correct_answer.upper():
            print('Bonne réponse !')
        else:
            print(f'Mauvaise réponse. La bonne réponse est {correct_answer}.')
        

    def score_joueur(self):
        

    
    def toString(self):
        return f'{self.nom} {self.prenom}\t\t{self.score}'