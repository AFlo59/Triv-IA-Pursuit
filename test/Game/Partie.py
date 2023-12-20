from .Joueur import Joueur
from .Plateau import THEME_COLORS, Plateau
from utils.utils import cls, de

MAX_JOUEUR = 6

class Partie:
    def __init__(self) -> None:
        self.current_joueur = None
        self.plateau = Plateau(theme_colors=THEME_COLORS)  # Pass THEME_COLORS to Plateau

        self.run()

    def run(self):
        self.list_joueur = []
        self.display_welcome_message()  # New: Display a welcome message

        if self.inscription():
            self.start()

    def display_welcome_message(self):
        print("Bienvenue dans Triv-IA-Pursuit!")
        print("Avant de commencer, veuillez vous enregistrer.")

    def inscription(self):
        new_joueur = True

        while new_joueur:
            nom = input('Votre nom : ')
            prenom = input('Votre prénom : ')

            # Crée un objet Joueur
            joueur = Joueur(nom=nom, prenom=prenom, partie=self, x=4, y=4)  # <- Provide initial position

            # Vérifie si le joueur est valide avant de l'ajouter à la liste
            if joueur:
                self.list_joueur.append(joueur)

                # Vérifie si le nombre maximal de joueurs est atteint
                if len(self.list_joueur) == MAX_JOUEUR:
                    new_joueur = False
                else:
                    new_joueur_input = input('Nouveau joueur ? O/n ')
                    if new_joueur_input.lower() != 'o':
                        new_joueur = False
            else:
                print(f"Impossible d'enregistrer {nom} {prenom}")

        return True

    def start(self):
        # Cas 1: Si la liste des joueurs n'est pas vide
        if self.list_joueur:
            # Choisi un joueur aléatoire pour commencer
            self.current_joueur = self.list_joueur[de(0, len(self.list_joueur) - 1)]
            self.dashboard()
            self.play()
        else:
            print("Aucun joueur enregistré. La partie ne peut pas commencer.")

    def play(self):
        if self.current_joueur:
            # Laisse le joueur en cours jouer
            self.current_joueur.play()

    def dashboard(self):
        # Efface l'écran
        cls()

        # Affiche les informations de chaque joueur
        for joueur in self.list_joueur:
            print(joueur.toString())

        print()
        print('Joueur en cours:', self.show_current_joueur())

    def show_current_joueur(self):
        if self.current_joueur:
            return self.current_joueur.toString()
        else:
            return "Aucun joueur en cours."
