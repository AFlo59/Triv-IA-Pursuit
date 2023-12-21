import pygame as pg
from model.Joueur import Joueur

from model.Partie import Partie

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
REFRESH_DELAY=30 #ms

def init():
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pg.DOUBLEBUF, 8)
    partie = Partie(screen)

    # debug
    partie.list_joueur = [Joueur('KUIL', 'Maxime', partie, 10)]
    partie.start()
    # fin debug


    clock = pg.time.Clock()
    running = True

    pg.event.set_allowed([pg.QUIT, pg.KEYDOWN])
    
    while running:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                #print(event.pos)
                for node in partie.plateau.G.nodes:
                    case = partie.plateau.get_case(node)
                    if case.case_graf.rect.collidepoint(event.pos):
                        case.on_click()

            if event.type == pg.QUIT:
                running = False
        
        pg.display.flip()

        clock.tick(FPS)

        if REFRESH_DELAY > 0:
            pg.event.pump()
            pg.time.delay(REFRESH_DELAY)
            partie.update()
            
        #print(clock.get_fps())
        
# def init():
#     partie = Partie()

if __name__ == '__main__':
    init()