
from pathlib import Path
from tkinter import PhotoImage
import tkinter as tk
from utils import de
from PIL import ImageTk

from classes.db.connectbdd import connectbdd

class Joueur:
    def __init__(self, nom, prenom, partie, position=72) -> None:
        self.nom = nom
        self.prenom = prenom
        self.score = 0
        self.position = position
        self.partie = partie
        self.table = connectbdd()
        self.question_text = None  # Ajoutez cette ligne pour initialiser question_text
        self.choices_text = []
        self.reponse_correcte = False
        self.insert_bdd()
        self.avatar = Avatar(partie)
        case = self.partie.plateau.get_case(self.position)
        self.move(case)
        
    def move(self, case):
        self.avatar.move(case.center[0], case.center[1])
        self.position = case.node
        
    def insert_bdd(self):
        print(self.nom, self.prenom)
        self.table.create_joueur("INSERT INTO joueurs (nom, prenom, score) VALUES (?, ?, ?)",
                                  (self.nom, self.prenom, self.score))
        self.table.commit()

    def update_score_in_bdd(self):
        self.table.update_joueur_score("UPDATE joueurs SET score = ? WHERE nom = ? AND prenom = ?",
                                        (self.score, self.nom, self.prenom))
        self.table.commit()

    def play(self):
        self.partie.plateau.listen_cases(self)
        self.partie.plateau.move_joueur(self.position, de())

        # print(self.case.toString())


    def set_question(self, case, question_data):
        self.move(case)
        self.partie.plateau.unlisten_cases()
        self.question_text = question_data[1]
        print(self.question_text)
        self.choices_text = question_data[3:7]
        correct_answer = question_data[2]
        for i, choice in enumerate(self.choices_text, start=65):
            print(f"{chr(i)}. {choice}")
        reponse = input('Votre réponse (écrit simplement A, B, C ou D) :')
        if reponse.upper() == correct_answer.upper():
            print('Bonne réponse !')
            self.reponse_correcte = True
            self.play()
        else:
            print(f'Mauvaise réponse. La bonne réponse est {correct_answer}.')
            self.reponse_correcte = False

    
    def toString(self):
        return f'{self.nom} {self.prenom}\t\t{self.score}'
    
class Avatar():
    def __init__(self, partie) -> None:
        self.partie = partie
        self.photo = ImageTk.PhotoImage(file=Path('assets/avatar.png').resolve())
        print(Path('assets/avatar.png').resolve())
        self.id = partie.canvas.create_image(0, 0, anchor=tk.CENTER, image=self.photo)

    def move(self, x, y):
        print(x, y)
        self.partie.canvas.coords(self.id, x, y)