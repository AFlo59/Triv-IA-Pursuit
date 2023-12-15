from model.Partie import Partie
from model.Plateau import Plateau


def init():
    partie = Partie()
    partie.run()
    plateau = Plateau()

if __name__ == '__main__':
    init()