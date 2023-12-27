from tkinter import Tk
import tkinter as tk
from classes.Interface import Interface
from classes.Plateau import Plateau
from utils import de

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
INTERFACE_WIDTH = 250
MAX_JOUEUR = 6

class Partie(Tk):
    def __init__(self):
        super().__init__()

        self.canvas = tk.Canvas(self, width=SCREEN_WIDTH - INTERFACE_WIDTH, height=SCREEN_HEIGHT)
        self.canvas.grid(column=0, row=0)
        self.plateau = Plateau(self.canvas)

        self.frame_interface = tk.Frame(self, width=INTERFACE_WIDTH, height=600, background='azure')
        self.frame_interface.grid(column=1, row=0, sticky=tk.NS)
        self.interface = Interface(self.frame_interface)

        self.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")

        self.current_joueur = None
        self.list_joueur = []

        self.plateau.render()

    def run(self):
        self.mainloop()

    def start(self):
        self.current_joueur = self.list_joueur[de(0, len(self.list_joueur) - 1)]
        self.play()
        
    def play(self):
        if self.current_joueur:
            self.current_joueur.play()
            
        for joueur in self.list_joueur:
            if joueur.score > 6:
                pass

    def update(self):
        self.interface.update(self.current_joueur)

    def show_current_joueur(self):
        return self.current_joueur.toString() if self.current_joueur else 'Aucun joueur en cours.'
    