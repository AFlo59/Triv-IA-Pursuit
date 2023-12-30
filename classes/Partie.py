from tkinter import Frame
import tkinter as tk
from classes.Interface import Interface
from classes.Joueur import Joueur
from classes.Plateau import Plateau
from utils import de, rotate_array

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
INTERFACE_WIDTH = 250
MAX_JOUEUR = 6

class Partie(Frame):
    def __init__(self, container):
        super().__init__(container, highlightthickness=0)

        self.plateau = Plateau(self, width=SCREEN_WIDTH - INTERFACE_WIDTH, height=SCREEN_HEIGHT)
        self.plateau.grid(column=0, row=0, sticky=tk.NS)

        self.interface = Interface(self, width=INTERFACE_WIDTH, height=SCREEN_HEIGHT)
        self.interface.grid(column=1, row=0, sticky=tk.NS)

        self.current_joueur = None
        self.list_joueur = []

    def inscription(self, nom, prenom, **kwargs):
        if len(self.list_joueur) <= MAX_JOUEUR:
            self.list_joueur.append(Joueur(nom=nom, prenom=prenom, partie=self, **kwargs))
            return True
        
        return False

    def play(self, next_player = False):
        idx = de(0, len(self.list_joueur) - 1) if next_player == False else 1

        self.list_joueur = rotate_array(self.list_joueur, idx)

        self.current_joueur = self.list_joueur[0]
        self.current_joueur.play()

    def update(self):
        self.interface.update(self.current_joueur)