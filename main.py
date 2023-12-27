from pathlib import Path
from classes.Joueur import Joueur
from classes.Partie import Partie
# from classes.Interface import Interface
import tkinter as tk

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def init():
    main = tk.Tk()
    canvas = tk.Canvas(main, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    canvas.pack(anchor=tk.CENTER, expand=True)

    partie = Partie(canvas)
    joueur = Joueur('KUIL', 'Maxime', partie)
    partie.current_joueur = joueur
    partie.play()

    main.mainloop()
    
    

if __name__ == '__main__':
    init()
