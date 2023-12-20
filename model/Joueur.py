from model.Case import Case
from model.Plateau import Plateau
from utils import de


from connectbdd import ConnectBdd


class Joueur:
    def __init__(self, nom, prenom, partie) -> None:
        self.nom = nom
        self.prenom = prenom
        self.score = 0
        self.position = (0, 0)
        self.partie = partie
        self.table = ConnectBdd()
        self.case= None
        # self.insert_bdd()
        

    def insert_bdd(self):
        print(self.nom, self.prenom)
        self.table.create_joueur("INSERT INTO joueurs (nom, prenom) VALUES (?, ?)", (self.nom, self.prenom))
        self.table.commit()

    def play(self):
        self.case = self.partie.plateau.move_joueur(self.position, de())
        self.case.get_question()
        self.get_answer()
        # print(self.case.toString())


    def get_answer(self):
        question_data = self.case.get_question()
        question_text = question_data[1]
        print(question_text)
        choices = question_data[3:7]
        correct_answer = question_data[2]
        for i, choice in enumerate(choices, start=65):
            print(f"{chr(i)}. {choice}")
        reponse = input('Votre réponse (écrit simplement A, B, C ou D) :')
        if reponse.upper() == correct_answer.upper():
            print('Bonne réponse !')
            self.play()
        else:
            print(f'Mauvaise réponse. La bonne réponse est {correct_answer}.')


    def toString(self):
        return f'{self.nom} {self.prenom}\t\t{self.score}'
    

    def scoring(self):
        while self.reponse.upper() == self.correct_answer.upper() and self.case == Plateau.camemberts:
            self.score +=1
    
