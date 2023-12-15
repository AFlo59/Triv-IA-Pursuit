from model.Case import Case

ROWS = 6
COLS = 6

class Plateau:
    def __init__(self) -> None:
        print('plateau')
        self.render()
        
    def render(self):
        cases = []
        for col in range(COLS):
            for row in range(ROWS):
                if col == 0 or row == 0:
                    cases.append('x')
                elif col == COLS - 1 or row == ROWS - 1:
                    cases.append('x')
                else:
                    cases.append('')  
        
        print(cases)
        
    def move_joueur(self, to, nb_case):
        print('move', to, nb_case)