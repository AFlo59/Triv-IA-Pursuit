from utils import de


class Joueur:
    def __init__(self, nom, prenom, partie) -> None:
        self.nom = nom
        self.prenom = prenom
        self.score = []
        self.position = (0, 0)
        self.partie = partie
        
    def play(self):
        case = self.partie.plateau.move_joueur(self.position, de())
        print(case.toString())
    
    def toString(self):
        return f'{self.nom} {self.prenom}\t\t{self.score}'