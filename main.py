from classes.Joueur import Joueur
from classes.Partie import Partie

def init():
    partie = Partie()
    joueur = Joueur('KUIL', 'Maxime', partie)
    partie.current_joueur = joueur
    partie.play()
    partie.run()

if __name__ == '__main__':
    init()
