from model.Case import Case

ROWS = 9
COLS = 9

class Plateau:
    def __init__(self) -> None:
        print('plateau')
        self.render()
        
    def render(self):
        cases = []
        for row in range(ROWS):
            rowItems = []
            for col in range(COLS):
                if col == 0: # Première colonne
                    rowItems.append('x')
                elif row == 0 or row == ROWS // 2: # Première ligne et ligne du milieu
                    rowItems.append('x')
                elif row == ROWS - 1: # Dernière ligne
                    rowItems.append('x')
                elif col == COLS - 1 or col == COLS // 2: # Dernière colonne et colonne du milieu
                    rowItems.append('x')
                elif col == row or (col + row) + 1 == ROWS: # Diagonales
                    rowItems.append('x')
                else:
                    rowItems.append(' ') 
            cases.append(rowItems)
        
        print(cases)
        
    def move_joueur(self, to, nb_case):
        print('move', to, nb_case)