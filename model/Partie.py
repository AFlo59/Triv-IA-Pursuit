from model.De import De
from model.Joueur import Joueur

MAX_JOUEUR = 6

class Partie:
    def __init__(self) -> None:
        self.de = De()
        
    def run(self):
        self.list_joueur = []
        if self.inscription():
            self.start()
        
    def inscription(self):
        new_joueur = True
        while new_joueur == True:
            nom = input('Votre nom :')
            prenom = input('Votre prenom :')
            
            joueur = Joueur(nom=nom, prenom=prenom)
            
            if joueur:
                self.list_joueur.append()

                if len(self.list_joueur) == MAX_JOUEUR:
                    new_joueur = False
                
                new_joueur_input = input('Nouveau joueur ? O/n')
                if new_joueur_input == 'n':
                    new_joueur = False
            else:
                print(f"Impossible d'enregistrer {nom} {prenom}")
                new_joueur_input = False
                
        return True
    
    def start(self):
        print('start')
        print(self.list_joueur)
        
    def dashboard(self):
        # TODO Créer un dashboard
        pass 