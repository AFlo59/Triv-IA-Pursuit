import pygame as pg
from model.Joueur import Joueur

from model.Partie import Partie

SCREEN_WIDTH = 1200
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

        interface_width = 300
        interface_height = SCREEN_HEIGHT  # même hauteur que votre fenêtre de jeu
        interface_x = SCREEN_WIDTH - interface_width  #  positionne l'interface à droite
        interface_y = 0  #  positionne l'interface en haut de l'écran

        interface_bg_color = (255, 0, 0)
        interface_image = pg.image.load('model/interface.jpg')
        interface_image = pg.transform.scale(interface_image, (interface_width, interface_height))  # redimensionner l'image

        interface_rect = pg.Rect(interface_x, interface_y, interface_width, interface_height)
        pg.draw.rect(screen, interface_bg_color, interface_rect)
            #pour afficher l'image de l'interface
        screen.blit(interface_image, (interface_x, interface_y))

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