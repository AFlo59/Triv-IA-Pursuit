class Joueur:
    def __init__(self, nom, prenom) -> None:
        self.nom = nom
        self.prenom = prenom
        self.score = []
        # TODO enregistrer en BDD
    
    def stats(self):
        return f'{self.nom} {self.prenom}\t\t{self.score}'