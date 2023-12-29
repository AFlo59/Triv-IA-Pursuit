from tkinter import Frame, Label, Radiobutton, StringVar
import tkinter as tk
from classes.Joueur import Joueur


class Interface(Frame):
    def __init__(self, container, width, height) -> None:
        super().__init__(container, width=width, height=height, background='azure', borderwidth=0)

        self.joueur = None

        self.txt_joueur = StringVar()
        self.txt_question = StringVar()
        self.txt_prop1 = StringVar()
        self.txt_prop2 = StringVar()
        self.txt_prop3 = StringVar()
        self.txt_prop4 = StringVar()

        txt_joueur = Label(self, font="Arial 16", textvariable=self.txt_joueur, background='azure', anchor=tk.NW)
        txt_joueur.place(x=0, y=10, width=250, height=30)

        self.questions_data = Frame(self, width=250, height=600, background='azure')
        self.questions_data.place(y=50)

        txt_question = Label(self.questions_data, textvariable=self.txt_question, background='azure', anchor=tk.W, wraplength=225, justify=tk.LEFT, width=250)
        txt_question.grid(column=0, row=1, sticky=tk.W)


        v = StringVar()
        bt_prop1 = Radiobutton(self.questions_data, textvariable=self.txt_prop1, anchor=tk.W, wraplength=225, background='azure', borderwidth=0, variable=v, value='A', command=lambda: self.onClick('A'), justify=tk.LEFT)
        bt_prop1.grid(column=0, row=2, sticky=tk.EW)

        bt_prop2 = Radiobutton(self.questions_data, textvariable=self.txt_prop2, anchor=tk.W, wraplength=225, background='azure', borderwidth=0, variable=v, value='B', command=lambda: self.onClick('B'), justify=tk.LEFT)
        bt_prop2.grid(column=0, row=3, sticky=tk.EW)

        bt_prop3 = Radiobutton(self.questions_data, textvariable=self.txt_prop3, anchor=tk.W, wraplength=225, background='azure', borderwidth=0, variable=v, value='C', command=lambda: self.onClick('C'), justify=tk.LEFT)
        bt_prop3.grid(column=0, row=4, sticky=tk.EW)

        bt_prop4 = Radiobutton(self.questions_data, textvariable=self.txt_prop4, anchor=tk.W, wraplength=225, background='azure', borderwidth=0, variable=v, value='D', command=lambda: self.onClick('D'), justify=tk.LEFT)
        bt_prop4.grid(column=0, row=5, sticky=tk.EW)
        self.questions_data.place_forget()


    def update(self, joueur: Joueur):
        self.questions_data.place_forget()
        self.joueur = joueur
        self.txt_joueur.set(f'{joueur.nom} {joueur.prenom}: {joueur.score}')
        if joueur.question_text is not None:
            self.txt_question.set(joueur.question_text)
            self.txt_prop1.set(joueur.choices_text[0])
            self.txt_prop2.set(joueur.choices_text[1])
            self.txt_prop3.set(joueur.choices_text[2])
            self.txt_prop4.set(joueur.choices_text[3])

            self.questions_data.place(y=50)

   # def update_score(self):


    def onClick(self, value):
        self.joueur.answer(value)

