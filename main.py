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
    partie = Partie(screen)

    # Debug
    partie.list_joueur = [Joueur('KUIL', 'Maxime', partie, 10)]

    clock = pg.time.Clock()
    running = True
    inscription_done = False

    pg.event.set_allowed([pg.QUIT, pg.KEYDOWN])

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # Call the inscription_page method inside the loop
        # screen.fill(('white'))
        new_player = partie.inscription_page()

        pg.display.flip()

        clock.tick(FPS)

        # Check if a new player is added or if the inscription is finished
        if not new_player:
            inscription_done = True
            screen.fill('white')
            partie.render()

        # Commence le jeu après la fin de l'inscription
        if inscription_done:
            # Move the following lines inside the if block
            partie.start()
        

        if REFRESH_DELAY > 0:
            pg.event.pump()
            pg.time.delay(REFRESH_DELAY)

            # Move the following lines inside the if block
            if inscription_done:
                partie.update()
                partie.dashboard()
                

if __name__ == '__main__':
    init()