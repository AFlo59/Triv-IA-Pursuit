
from utilss import de

from connectbdd import ConnectBdd

class Joueur:
    def __init__(self, nom, prenom, partie, position=0) -> None:
        self.nom = nom
        self.prenom = prenom
        self.score = 0
        self.position = position
        self.partie = partie
        self.table = ConnectBdd()
        # self.insert_bdd()
        self.play()
        

    def insert_bdd(self):
        print(self.nom, self.prenom)
        self.table.create_joueur("INSERT INTO joueurs (nom, prenom, score) VALUES (?, ?, ?)",
                                  (self.nom, self.prenom, self.score))
        self.table.commit()

    def update_score_in_bdd(self):
        self.table.update_joueur_score("UPDATE joueurs SET score = ? WHERE nom = ? AND prenom = ?",
                                        (self.score, self.nom, self.prenom))
        self.table.commit()

    def play(self):
        self.partie.plateau.listen_cases(self)
        self.case = self.partie.plateau.move_joueur(self.position, de())
        if self.case is not None:
            self.case.get_question()
                # Reste du code
        else:
            print(self.case)
            print("Erreur: La case n'a pas été correctement initialisée.")

        # print(self.case.toString())


    def set_question(self, question_data):
        self.partie.plateau.unlisten_cases()
        question_text = question_data[1]
        print(question_text)
        choices = question_data[3:7]
        correct_answer = question_data[2]
        for i, choice in enumerate(choices, start=65):
            print(f"{chr(i)}. {choice}")
        reponse = input('Votre réponse (écrit simplement A, B, C ou D) :')
        if reponse.upper() == correct_answer.upper():
            print('Bonne réponse !')
            # if self.case == Plateau.camemberts:
            #    self.score +=1
            self.play()
        else:
            print(f'Mauvaise réponse. La bonne réponse est {correct_answer}.')

    
    def toString(self):
        return f'{self.nom} {self.prenom}\t\t{self.score}'
    
