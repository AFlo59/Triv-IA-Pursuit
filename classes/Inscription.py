from functools import partial
from tkinter import Button, Entry, Frame, Label, StringVar
import tkinter as tk
from classes.Partie import Partie


class Inscription(Frame):
    def __init__(self, parent, partie: Partie, cb_end_inscription) -> None:
        super().__init__(parent, width=400, height=200, background='lightyellow2')

        self.partie = partie
        self.cb_end_inscription = cb_end_inscription

        frame_inputs = Frame(self, width=400, height=200)

        self.label = Label(frame_inputs, text='Inscription', justify=tk.CENTER, font=('Arial', 16))
        self.label.grid(row=0, columnspan=2)


        Label(frame_inputs, text="Nom").grid(row=1, column=0)
        self.nom = StringVar()
        self.nomEntry = Entry(frame_inputs, textvariable=self.nom)
        self.nomEntry.grid(row=1, column=1, padx=5, pady=5)

        Label(frame_inputs,text="Prénom").grid(row=2, column=0)  
        self.prenom = StringVar()
        self.prenomEntry = Entry(frame_inputs, textvariable=self.prenom)
        self.prenomEntry.grid(row=2, column=1, padx=5, pady=5)

        submit = partial(self.submit, self.nom, self.prenom)


        self.btCancel =Button(frame_inputs, text="Annuler", command=self.stop, relief=tk.FLAT)
        self.btCancel.grid(row=4, column=0, sticky=tk.EW, padx=5, pady=5)
        self.btOK = Button(frame_inputs, text="OK", command=submit, relief=tk.FLAT)
        self.btOK.grid(row=4, column=1, sticky=tk.EW, padx=5, pady=5)

        parent.bind('<Return>', lambda e: self.submit(self.nom, self.prenom))

        self.nomEntry.focus_set()
        frame_inputs.pack()
        
    def submit(self, nom, prenom):
        res = self.partie.inscription(nom.get(), prenom.get())
        if res:
            self.nom.set('')
            self.prenom.set('')
            self.nomEntry.focus_set()

    def stop(self):
        if len(self.partie.list_joueur) > 0:
            self.place_forget()
            self.cb_end_inscription()

