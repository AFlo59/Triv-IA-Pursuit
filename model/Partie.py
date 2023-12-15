from Joueur import Joueur
class Partie:

    def __init__(self):
        self.joueurs = []

    def inscription(self, nom_joueur):
        if len(self.joueurs) < 6:
            nouveau_joueur = Joueur(nom_joueur)
            self.joueurs.append(nouveau_joueur)
            print(f"{nom_joueur} à été inscrit à la partie.!")
        else:
            print("La partie est complète. Impossible d'ajouter plus de joueurs.")

    def afficher_joueurs(self):
        print("Joueurs inscrits :")
        for joueur in self.joueurs:
            print(joueur)
            
