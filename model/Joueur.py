from model.Plateau import Plateau
from utils import de


from connectbdd import ConnectBdd


class Joueur:
    def __init__(self, nom, prenom) -> None:
        self.nom = nom
        self.prenom = prenom
        self.score = []
        self.position = (0, 0)
        # TODO enregistrer en BDD
        
    def play(self, plateau: Plateau):
        plateau.move(self.position, de())
        self.table = ConnectBdd()
        self.insert_bdd()

    def insert_bdd(self):
        print(self.nom, self.prenom)
        self.table.create_joueur("INSERT INTO joueurs (nom, prenom) VALUES (?, ?)", (self.nom, self.prenom))
        self.table.commit()


    
    def toString(self):
        return f'{self.nom} {self.prenom}\t\t{self.score}'