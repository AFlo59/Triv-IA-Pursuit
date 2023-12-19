from model.Case import TYPE_CASE, Case

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
next_pos_possible = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

class Plateau:
    def __init__(self) -> None:
        self.cases = []
        self.render()
        
    def render(self):
        self.setup()
        graf = ''
        for row in self.cases:
            for item in row:
                graf = f'{graf}{item.graf}'
            graf = f'{graf}\r\n'
        
        print(graf) 
            
        
    def setup(self):
        i = 0
        for row in range(ROWS):
            rowItems = []
            if i == len(themes) - 1:
                i = 0
                
            for col in range(COLS):
                if ((col == row == 0) or
                    (col == COLS // 2 and row == 0) or
                    (col == COLS - 1 and row == 0) or  
                    
                    (row == ROWS - 1 and col == 0) or
                    (row == ROWS - 1 and col == COLS // 2) or
                    (row == ROWS - 1 and col == COLS - 1)):
                        if len(camemberts) > 0:
                            item = camemberts.pop()
                            c = Case(position=(col, row), type_case=TYPE_CASE['theme'], theme=item[1], graf=item[0])
                            rowItems.append(c)
                elif col == 0: # Première colonne
                    rowItems.append(Case((col, row), TYPE_CASE['theme'], themes[i][1], themes[i][0]))
                elif row == 0 or row == ROWS // 2: # Première ligne et ligne du milieu
                    rowItems.append(Case((col, row), TYPE_CASE['theme'], themes[i][1], themes[i][0]))
                elif row == ROWS - 1: # Dernière ligne
                    rowItems.append(Case((col, row), TYPE_CASE['theme'], themes[i][1], themes[i][0]))
                elif col == COLS - 1 or col == COLS // 2: # Dernière colonne et colonne du milieu
                    rowItems.append(Case((col, row), TYPE_CASE['theme'], themes[i][1], themes[i][0]))
                elif col == row or (col + row) + 1 == ROWS: # Diagonales
                    rowItems.append(Case((col, row), TYPE_CASE['theme'], themes[i][1], themes[i][0]))
                else:
                    rowItems.append(Case((col, row), TYPE_CASE['null'])) 
                    
                i += 1
                if i == len(themes) - 1:
                    i = 0
                    
            self.cases.append(rowItems)
            
        for row_idx in range(len(self.cases)):
            for col_idx in range(len(self.cases[row_idx])):
                self.cases[row_idx][col_idx].set_walkable_cases(self.find_walkable_cases((row_idx, col_idx), []))
        
    def find_walkable_cases(self, position, walkable_cases = [], next_position = 0):
        n = next_pos_possible[next_position]
        next_position_id = next_position + 1
        
        if next_position_id  >= len(next_pos_possible):
            return walkable_cases
        
        try:
            row = position[0] + n[0]
            col = position[1] + n[1]
            if row >= 0 and col >= 0:
                next_case = self.cases[row][col]
                if next_case.type_case < 4:
                    walkable_cases.append(next_case)
                
            self.find_walkable_cases(position, walkable_cases, next_position_id)
        except:
            self.find_walkable_cases(position, walkable_cases, next_position_id)

        return walkable_cases

    def move_joueur(self, to, nb_case) -> Case:
        print('move', to, nb_case)
        return self.cases[0][1]