import pygame as pg
from model.Joueur import Joueur
from model.Partie import Partie
from model.Interface import Interface

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800
FPS = 60
REFRESH_DELAY = 30  # ms



def init():
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pg.DOUBLEBUF, 8)
    pg.display.set_caption('Triv-IA-Pursuit')
    partie = Partie(screen)
    interface = Interface(screen)


    # Debug
    partie.list_joueur = [Joueur('KUIL', 'Maxime', partie, 10)]
    partie.start()
    # fin debug

    clock = pg.time.Clock()
    running = True
    inscription_done = False

    pg.event.set_allowed([pg.QUIT, pg.KEYDOWN])

    while running:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                for node in partie.plateau.G.nodes:
                    case = partie.plateau.get_case(node)
                    if case.case_graf.rect.collidepoint(event.pos):
                        case.on_click()

            if event.type == pg.QUIT:
                running = False

        # Call the inscription_page method inside the loop
        # screen.fill(('white'))
        new_player = partie.inscription_page()

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
            # if event.type == pg.QUIT:
            #     running = False
            # for joueur in partie.list_joueur:
                # if joueur.score > 6:
            #     print(f'Bravo {joueur} ! Tu as gagné cette partie de TrivIA Pursuit !!!')

        pg.display.flip()

        clock.tick(FPS)

        # Check if a new player is added or if the inscription is finished
        if not new_player:
            inscription_done = True
            screen.fill('black')
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
                
            partie.update()
            
        #print(clock.get_fps())

if __name__ == '__main__':
    init()
