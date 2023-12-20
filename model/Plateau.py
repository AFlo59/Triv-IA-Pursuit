from model.Case import TYPE_CASE, Case
import networkx as nx

from utils import rotate_array

ROWS = 9
COLS = 9
# 1 SQL
# 2 Python
# 3 IA
# 4 Git
# 5 Agile
# 6 Terminal

themes = [('#FF0000', 1), ('🟦', 2), ('🟨', 3), ('🟪', 4), ('🟩', 5), ('🟧', 6)]

class Plateau:
    def __init__(self) -> None:
        self.cases = []
        self.G = nx.Graph()
        self.render()
        
    def render(self):
        self.setup()
    
    def setup(self):
        node_cercles = 42
        node_rayons = 4
        nb_rayons = 6
        
        camemberts = themes[:]
        themes_clone = themes[:]
        
        # create circle
        rotate_index = 0
        for i in range(node_cercles):
            type = 0
            if i % (nb_rayons + 1) == 0:
                rotate_index += 1
                type = TYPE_CASE['gain']
                self.G.add_node(i, **{
                    'case': Case(type_case=type, theme=camemberts.pop())
                })
                themes_clone = rotate_array(themes, rotate_index)
            else:
                self.G.add_node(i, **{
                    'case': Case(theme=themes_clone.pop())
                })
            
        for i in range(node_cercles):
            self.G.add_edge(i, (i + 1) % node_cercles)
            
        # create rayons 
        last_nodes_rayon = []
        first_nodes_rayon = []
        for rayon in range(nb_rayons):
            themes_clone = rotate_array(themes, rayon)
            start = self.G.number_of_nodes()

            for i in range(node_rayons):
                self.G.add_node(start + i, **{
                    'case': Case(type_case=TYPE_CASE['theme'], theme=themes_clone.pop())
                })
                
            for i in range(node_rayons):
                self.G.add_edge(start + i, (start + i + 1))
            
            first_nodes_rayon.append(list(self.G.nodes)[start])
            last_nodes_rayon.append(list(self.G.nodes)[-1])

        # create and connect central node to rayon
        self.G.add_node(self.G.number_of_nodes(), **{
                    'case': Case(type_case=TYPE_CASE['start'])
                })

        central = list(self.G.nodes)[-1]
        for last_node_rayon in last_nodes_rayon:
            self.G.add_edge(central, last_node_rayon)
            
        # connect rayons to circle
        for i in range(node_cercles):
            if i % (nb_rayons + 1) == 0:
                self.G.add_edge(i, first_nodes_rayon.pop())
    
    def get_case(self, node_id) -> Case:
        return self.G.nodes[node_id]['case']
    
    def setup_old(self):
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
                        item = camemberts.pop()
                        c = Case((row, col), TYPE_CASE['gain'], item[1], item[0])
                        if ((col == row == 0) or (col == COLS - 1 and row == 0) 
                            or (row == ROWS - 1 and col == 0) or (row == ROWS - 1 and col == COLS - 1)):
                            c.on_diagonale = True
                        rowItems.append(c)
                    
                elif col == 0: # Première colonne
                    rowItems.append(Case((row, col), TYPE_CASE['theme'], themes[i][1], themes[i][0]))
                elif row == 0 or row == ROWS // 2: # Première ligne et ligne du milieu
                    rowItems.append(Case((row, col), TYPE_CASE['theme'], themes[i][1], themes[i][0]))
                elif row == ROWS - 1: # Dernière ligne
                    rowItems.append(Case((row, col), TYPE_CASE['theme'], themes[i][1], themes[i][0]))
                elif col == COLS - 1 or col == COLS // 2: # Dernière colonne et colonne du milieu
                    rowItems.append(Case((row, col), TYPE_CASE['theme'], themes[i][1], themes[i][0]))
                elif col == row or (col + row) + 1 == ROWS: # Diagonales
                    c = Case((row, col), TYPE_CASE['theme'], themes[i][1], themes[i][0])
                    c.on_diagonale = True
                    rowItems.append(c)
                else:
                    rowItems.append(Case((row, col), TYPE_CASE['null'])) 
                    
                if row == ROWS // 2 and col == COLS // 2:
                    rowItems[len(rowItems) - 1].type_case = TYPE_CASE['start']
                    
                i += 1
                if i == len(themes) - 1:
                    i = 0
                    
            self.cases.append(rowItems)
            
        for row_idx in range(len(self.cases)):
            for col_idx in range(len(self.cases[row_idx])):
                self.cases[row_idx][col_idx].set_walkable_cases(self.find_walkable_cases((row_idx, col_idx), []))
        
    def find_walkable_cases(self, position, walkable_cases = [], next_position = 0):
        n = next_pos_possible[next_position]
        case = self.cases[position[0]][position[1]]
        next_position_id = next_position + 1
        
        if next_position_id  >= len(next_pos_possible):
            return walkable_cases
        
        try:
            row = position[0] + n[0]
            col = position[1] + n[1]
            if row >= 0 and col >= 0:
                next_case = self.cases[row][col]
                if next_case.type_case < 4:
                    if case.on_diagonale == next_case.on_diagonale == True:
                        walkable_cases.append(next_case)
                    elif case.on_diagonale == next_case.on_diagonale == False:
                        walkable_cases.append(next_case)
                    elif case.type_case == 1 or case.type_case == 3:
                        walkable_cases.append(next_case)
                
            self.find_walkable_cases(position, walkable_cases, next_position_id)
        except:
            self.find_walkable_cases(position, walkable_cases, next_position_id)

        return walkable_cases

    def move_joueur(self, to, nb_case) -> Case:
        print('move', to, nb_case)
        return self.cases[0][1]
>>>>>>> origin/maxime
