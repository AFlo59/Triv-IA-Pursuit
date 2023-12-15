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
            print('nom', nom)
            prenom = input('Votre prenom :')
            print('prénom', prenom)
            
            self.list_joueur.append(Joueur(nom=nom, prenom=prenom))

            if len(self.list_joueur) == MAX_JOUEUR:
                 new_joueur = False
            
            new_joueur_input = input('Nouveau joueur ? O/n')
            if new_joueur_input == 'n':
                new_joueur = False
                
        return True
    
    def start(self):
        print('start')
        print(self.list_joueur)