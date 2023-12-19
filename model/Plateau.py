from model.Case import Case

ROWS = 9
COLS = 9

# 1 SQL
# 2 Python
# 3 IA
# 4 Git
# 5 Agile
# 6 Terminal

themes = [('🟥', 1), ('🟦', 2), ('🟨', 3), ('🟪', 4), ('🟩', 5), ('🟧', 6)]
camemberts = [('🍓', 1), ('💙', 2), ('💛', 3), ('💜', 4), ('💚', 5), ('🧡', 6)]

class Plateau:
    def __init__(self) -> None:
        print('plateau')
        self.rowItems = []
        self.render()
        
    def render(self):
        self.setup()
        print(self.rowItems)
        # for row in self.rowItems:
        #     for item in row:
        #         if item is Case:
        #             print(item.graf)
            
        
    def setup(self):
        cases = []   
        i = 0
        for row in range(ROWS):
            if i == len(themes) - 1:
                i = 0
                
            for col in range(COLS):
                if ((col == row == 0) or
                    (col == COLS // 2 and row == 0) or
                    (col == COLS - 1 and row == 0) or  
                    
                    (row == ROWS - 1 and col == 0) or
                    (row == ROWS - 1 and col == COLS // 2) or
                    (row == ROWS - 1 and col == COLS - 1)):
                        item = camemberts.pop()
                        self.rowItems.append(Case((col, row), item[0], item[1]))
                elif col == 0: # Première colonne
                    self.rowItems.append(Case((col, row), themes[0], themes[1]))
                elif row == 0 or row == ROWS // 2: # Première ligne et ligne du milieu
                    self.rowItems.append(Case((col, row), themes[0], themes[1]))
                elif row == ROWS - 1: # Dernière ligne
                    self.rowItems.append(Case((col, row), themes[0], themes[1]))
                elif col == COLS - 1 or col == COLS // 2: # Dernière colonne et colonne du milieu
                    self.rowItems.append(Case((col, row), themes[0], themes[1]))
                elif col == row or (col + row) + 1 == ROWS: # Diagonales
                    self.rowItems.append(Case((col, row), themes[0], themes[1]))
                else:
                    self.rowItems.append(' ') 
                    
                i += 1
                if i == len(themes) - 1:
                    i = 0
                    
            cases.append(self.rowItems)
        
    def move_joueur(self, to, nb_case):
        print('move', to, nb_case)