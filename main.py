import pygame as pg
from model.Joueur import Joueur
from model.Partie import Partie

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
REFRESH_DELAY = 30  # ms

def init():
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pg.DOUBLEBUF, 8)
    partie = Partie(screen)  # Initialiser Partie après Pygame

    # Debug
    partie.list_joueur = [Joueur('KUIL', 'Maxime', partie, 10)]

    clock = pg.time.Clock()
    running = True

    pg.event.set_allowed([pg.QUIT, pg.KEYDOWN])

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # Call the inscription_page method inside the loop
        new_player = partie.inscription_page()

        pg.display.flip()

        clock.tick(FPS)

        if REFRESH_DELAY > 0:
            pg.event.pump()
            pg.time.delay(REFRESH_DELAY)
            partie.update()

            # Affiche le tableau de bord après la page d'inscription
            partie.dashboard()

        # Check if a new player is added or if the inscription is finished
        if not new_player:
            running = False

if __name__ == '__main__':
    init()
