from functools import partial
from tkinter import Button, Entry, Frame, Label, StringVar
import tkinter as tk
from tkinter.ttk import Combobox
from classes.Partie import Partie


class Inscription(Frame):
    def __init__(self, parent, partie: Partie, cb_end_inscription) -> None:
        super().__init__(parent)

        self.partie = partie
        # callback venant de main.py pour fermer l'inscription + overlay
        self.cb_end_inscription = cb_end_inscription

        frame_inputs = Frame(self, padx=30, pady=30)

        self.label = Label(frame_inputs, text='Inscription', justify=tk.CENTER, font=('Arial', 16))
        self.label.grid(row=0, columnspan=2, padx=20)


        Label(frame_inputs, text="Nom", justify=tk.LEFT).grid(row=1, column=0, sticky=tk.W)
        self.nom = StringVar()
        self.nomEntry = Entry(frame_inputs, textvariable=self.nom)
        self.nomEntry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        Label(frame_inputs, text="Prénom").grid(row=2, column=0, sticky=tk.W)  
        self.prenom = StringVar()
        self.prenomEntry = Entry(frame_inputs, textvariable=self.prenom)
        self.prenomEntry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        self.couleurs = ['Orange', 'Jaune', 'Vert', 'Bleu', 'Rose', 'Marron']
        Label(frame_inputs,text="Couleur du pion").grid(row=3, column=0, sticky=tk.W) 
        self.combo = Combobox(frame_inputs, state='readonly', values=self.couleurs)
        self.combo.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)
        self.combo.current(0)

        submit = partial(self.submit, self.nom, self.prenom, self.combo)


        self.btCancel =Button(frame_inputs, text="Annuler", command=self.stop, relief=tk.FLAT)
        self.btCancel.grid(row=5, column=0, sticky=tk.EW, padx=5, pady=5)
        self.btOK = Button(frame_inputs, text="OK", command=submit, relief=tk.FLAT)
        self.btOK.grid(row=5, column=1, sticky=tk.EW, padx=5, pady=5)

        parent.bind('<Return>', lambda e: self.submit(self.nom, self.prenom, self.combo))

        self.nomEntry.focus_set()
        frame_inputs.pack()
        
    def submit(self, nom, prenom, combo):
        couleur = combo.get()
        res = self.partie.inscription(nom.get(), prenom.get(), couleur=couleur.lower())
        if res:
            self.nom.set('')
            self.prenom.set('')
            c = list(self.combo['values'])
            c.remove(couleur)
            self.combo['values'] = c
            self.combo.current(0)
            self.nomEntry.focus_set()
        else:
            self.stop()

    def stop(self):
        if len(self.partie.list_joueur) > 0:
            self.place_forget()
            self.cb_end_inscription()
            self.partie.play()

