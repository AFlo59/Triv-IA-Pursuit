from utils import de


class Joueur:
    def __init__(self, nom, prenom, partie, position=0) -> None:
        self.nom = nom
        self.prenom = prenom
        self.score = []
        self.position = position
        self.partie = partie
        
    def play(self):
        self.partie.plateau.listen_cases(self)
        self.partie.plateau.move_joueur(self.position, de())
    
    def set_question(self, question):
        self.partie.plateau.unlisten_cases()
        print(question)

    def toString(self):
        return f'{self.nom} {self.prenom}\t\t{self.score}'