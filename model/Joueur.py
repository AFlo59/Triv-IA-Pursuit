from model.Case import Case
from utils import de


from connectbdd import ConnectBdd


class Joueur:
    def __init__(self, nom, prenom, partie) -> None:
        self.nom = nom
        self.prenom = prenom
        self.score = []
        self.position = (0, 0)
        # TODO enregistrer en BDD
        
    def play(self, plateau: Plateau):
        plateau.move(self.position, de())
    
    def toString(self):
        return f'{self.nom} {self.prenom}\t\t{self.score}'