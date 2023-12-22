
from pathlib import Path
from utils import de
import pygame as pg
from pygame.sprite import Group

from connectbdd import ConnectBdd

class Joueur:
    def __init__(self, nom, prenom, partie, position=72) -> None:
        self.nom = nom
        self.prenom = prenom
        self.score = 0
        self.position = position
        self.partie = partie
        self.table = ConnectBdd()
        self.question_text = None  # Ajoutez cette ligne pour initialiser question_text
        self.choices_text = []
        self.reponse_correcte = False
        self.insert_bdd()
        self.sprite = Avatar(self.partie.screen)
        #self.partie.screen.blit(self.sprite.sprite.image, self.partie.screen.get_rect())
        # case = self.partie.plateau.get_case(self.position)
        # self.move(case)
        
    def move(self, case):
        self.sprite.move(case.position[0], case.position[1])
        
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
    
    
class Avatar(Group):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.render()
    
    def render(self):
        self.sprite = pg.sprite.Sprite(self)
        self.sprite.image = pg.image.load(Path('avatar.png').resolve())
        self.sprite.rect = self.sprite.image.get_rect(center=(25, 25))
        self.update()
        
    def move(self, x, y):
        print('move')
        self.remove(self.sprite)
        self.render()
        self.sprite.rect.move_ip(x - 25, y - 25)
    
    def update(self):
        self.draw(self.screen)
