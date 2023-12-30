
from pathlib import Path
import tkinter as tk
from utils import de
from PIL import ImageTk, Image

from classes.db.connectbdd import connectbdd

class Joueur:
    def __init__(self, nom, prenom, partie, position=72, **kwargs) -> None:
        self.nom = nom
        self.prenom = prenom
        self.score = 0
        self.position = position
        self.partie = partie
        self.table = connectbdd()
        self.question_text = None
        self.choices_text = []
        self.reponse_correcte = False
        self.insert_bdd()
        couleur = 'vert' if 'couleur' not in kwargs else kwargs.pop('couleur')
        self.avatar = Avatar(partie, couleur)
        case = self.partie.plateau.get_case(self.position)
        self.move(case)
        
    def move(self, case):
        self.case = case
        self.avatar.move(case.center[0], case.center[1])
        self.position = case.node
        
    def insert_bdd(self):
        self.table.create_joueur("INSERT INTO joueurs (nom, prenom) VALUES (?, ?)",
                                  (self.nom, self.prenom))
        self.table.commit()

    def update_score_in_bdd(self):
        self.table.update_joueur_score("UPDATE joueurs SET score = ? WHERE nom = ? AND prenom = ?",
                                        (self.score, self.nom, self.prenom))
        self.table.commit()

    def set_question(self, case, question_data):
        self.partie.plateau.unlisten_cases()
        self.move(case)
        self.question_text = question_data[1]
        self.choices_text = question_data[3:7]
        self.good_answer = question_data[2]

        self.partie.update()

    def answer(self, value):
        self.question_text = None
        if value == self.good_answer:
            if self.case.type_case == TYPE_CASE['gain']:
                self.score += 1
                self.avatar.win(self.case.theme[1])
                self.update_score_in_bdd()
            
            self.play()
        else:
            print(f'Mauvaise réponse. La bonne réponse est {self.good_answer}.')
            self.partie.play(next_player=True)


    def play(self):
        self.partie.plateau.listen_cases(self)
        self.partie.plateau.move_joueur(self.position, de())
        self.partie.update()

from classes.Case import TYPE_CASE

class Avatar():
    def __init__(self, partie, couleur) -> None:
        self.x = 0
        self.y = 0
        self.partie = partie
        self.couleur = couleur
        self.pion = ImageTk.PhotoImage(file=Path(f'assets/p_{couleur}.png').resolve())
        self.id = self.partie.plateau.create_image(self.x, self.y, image=self.pion, anchor=tk.CENTER)

    def move(self, x, y):
        self.x = x
        self.y = y
        self.partie.plateau.coords(self.id, x, y)

    def win(self, theme):
        cam = Image.open(Path(f'assets/c_{theme}.png').resolve())
        pion_img = Image.open(Path(f'assets/p_{self.couleur}.png').resolve())
        pion_img.alpha_composite(cam)

        self.pion = ImageTk.PhotoImage(image=pion_img)
        self.id = self.partie.plateau.create_image(self.x, self.y, image=self.pion, anchor=tk.CENTER)