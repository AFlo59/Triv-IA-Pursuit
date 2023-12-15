from Joueur import Joueur
class Partie:

    def init(self):
        self.joueurs = []

    # def run():

    def inscription(self, nom_joueur):
        if len(self.joueurs) < 6:
            nouveau_joueur = Joueur(nom_joueur)
            self.joueurs.append(nouveau_joueur)
            print(f"{nom_joueur} à été inscrit à la partie.!")
        else:
            print("La partie est complète. Impossible d'ajouter plus de joueurs.")

    # def start():