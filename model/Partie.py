from pygame import Surface
from model.Interface import Interface
from model.Joueur import Joueur
from model.Plateau import Plateau
from utils import cls, de

MAX_JOUEUR = 6
interface_width = 500
interface_height = 800
interface_x = 1500 - interface_width
interface_y = 0

class Partie:
    def __init__(self, screen: Surface) -> None:
        self.current_joueur = None
        self.screen = screen
        self.plateau = Plateau(screen)
        self.interface = Interface(screen)
        self.run()
        
    def run(self):
        self.list_joueur = []
        # if self.inscription():
        #     self.start()
    
    def update(self):
        self.plateau.update()
          
    def inscription(self):
        new_joueur = True
        while new_joueur == True:
            nom = input('Votre nom :')
            prenom = input('Votre prenom :')
            
            joueur = Joueur(partie=self, nom=nom, prenom=prenom)
            
            if joueur:
                self.list_joueur.append(joueur)

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
        # Cas 1
        self.current_joueur = self.list_joueur[de(0, len(self.list_joueur) - 1)]
        
        #self.dashboard()
        self.play()
        
    def play(self):
        if self.current_joueur:
            self.current_joueur.play()
            # self.interface.update_joueur(self.current_joueur)


        
    def dashboard(self):
        cls()
        for joueur in self.list_joueur:
            print(joueur.toString())
            
        print()
        print('Joueur en cours:', self.show_current_joueur())

    def show_current_joueur(self):
        return self.current_joueur.toString()