import pygame as pg

from model.Partie import Partie
from model.Plateau import Plateau

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
REFRESH_DELAY=30 #ms

def init():
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pg.DOUBLEBUF, 8)
    partie = Partie(screen)
    
    clock = pg.time.Clock()
    running = True

    pg.event.set_allowed([pg.QUIT, pg.KEYDOWN])
    
    while running:
        for event in pg.event.get():
            # if event.type == pg.KEYDOWN:
            #     if event.key == pg.K_DOWN:
            #         w.update()

            # if event.type == pg.MOUSEBUTTONDOWN:
            #     for i, cell in enumerate(w.flatCells):
            #         if cell.rect.collidepoint(event.pos):
            #             cell.onClick(event)

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