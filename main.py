from tkinter import Canvas, Tk
import tkinter as tk
from classes.Inscription import Inscription
from classes.Joueur import Joueur
from classes.Partie import Partie
from PIL import Image, ImageTk

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('Trivial Pursuit')
        self.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")

        self.images = []

        partie = Partie(self)

        # partie.inscription('KUIL', 'Maxime')
        # partie.inscription('KUIL2', 'Maxime', couleur='jaune')
        # partie.play()

        c = self.overlay(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, fill='yellow', alpha=.8)
        inscription = Inscription(self, partie, lambda: c.place_forget())
        inscription.place(relx=.5, rely=.5, anchor=tk.CENTER)

        partie.place(x=0, y=0)

    def overlay(self, x1, y1, x2, y2, **kwargs):
        canvas = Canvas(self, width=x2, height=y2, highlightthickness=0)

        if 'alpha' in kwargs:
            alpha = int(kwargs.pop('alpha') * 255)
            fill = kwargs.pop('fill')
            fill = self.winfo_rgb(fill) + (alpha,)
            image = Image.new('RGBA', (x2-x1, y2-y1), fill)
            self.images.append(ImageTk.PhotoImage(image))
            canvas.create_image(x1, y1, image=self.images[-1], anchor='nw')
        canvas.create_rectangle(x1, y1, x2, y2, **kwargs)
        canvas.place(x=0, y=0)
        return canvas

if __name__ == '__main__':
    app = App()
    app.mainloop()
