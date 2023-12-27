from tkinter import Canvas
from classes.Plateau import Plateau
from utils import cls, de

MAX_JOUEUR = 6
interface_width = 500
interface_height = 800
interface_x = 1500 - interface_width
interface_y = 0

class Partie:
    def __init__(self, canvas: Canvas) -> None:
        self.current_joueur = None
        self.canvas = canvas
        self.plateau = Plateau(canvas)
        self.run()
        self.render()


    def run(self):
        self.list_joueur = []

    def render(self):
        self.plateau.render()
    
    def update(self):
        self.plateau.update()

    def start(self):
        self.current_joueur = self.list_joueur[de(0, len(self.list_joueur) - 1)]
        self.play()
        
    def play(self):
        if self.current_joueur:
            self.current_joueur.play()
            print('play')
            
        for joueur in self.list_joueur:
            if joueur.score > 6:
                pass
            # self.interface.update_joueur(self.current_joueur)
        
    def dashboard(self):
        #cls()
        for joueur in self.list_joueur:
            print(joueur.toString())
            
            print()
            
            if self.current_joueur:
                print('Joueur en cours:', self.show_current_joueur())
            else:
                print('Aucun joueur en cours.')

    def show_current_joueur(self):
        return self.current_joueur.toString() if self.current_joueur else 'Aucun joueur en cours.'
    