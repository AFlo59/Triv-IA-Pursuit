import math
from pygame import Surface
from model.Case import TYPE_CASE, Case
import networkx as nx
from pygame.sprite import Group
import matplotlib.pyplot as plt
from model.Joueur import Joueur

from utils import get_rotation_angle, getEquidistantPoints, rotate_array

ROWS = 9
COLS = 9

# 1 SQL
# 2 Python
# 3 IA
# 4 Git
# 5 Agile
# 6 Terminal

themes = [('red', 1), ('blue', 2), ('yellow', 3), ('purple', 4), ('green', 5), ('orange', 6)]
start_theme = ('azure', 0)

class Plateau(Group):
    def __init__(self, screen: Surface = None) -> None:
        super().__init__()

        self.cases = []
        self.screen = screen
        self.G = nx.Graph()
        self.render()
        
        
        
    def render(self):
        self.setup()
        
        for node in self.G.nodes:
            case = self.get_case(node)
            case.render(self)
            
        self.draw(self.screen)
    
    def setup(self):
        node_cercles = 42
        node_rayons = 5
        nb_rayons = 6
        center = (400, 300)
        rayon = 200
        
        camemberts = themes[:]
        themes_clone = themes[:]
        
        # create circle
        rotate_index = 0
        angle_rotation = math.radians(360 / node_cercles)
        
        for i in range(node_cercles):
            type = 0
            position = (
                        center[0] + rayon * math.cos(angle_rotation * i),
                        center[1] + rayon * math.sin(angle_rotation * i)
                    )
            angle = get_rotation_angle(center, position)
            
            if i % (nb_rayons + 1) == 0:
                rotate_index += 1
                type = TYPE_CASE['gain']
                self.G.add_node(i, **{
                    'case': Case(screen=self.screen, type_case=type, theme=camemberts.pop(), position=position, angle=angle, node=i)
                })
                themes_clone = rotate_array(themes, rotate_index)
            else:
                self.G.add_node(i, **{
                    'case': Case(screen=self.screen, theme=themes_clone.pop(), position=position, angle=angle, node=i)
                })
            
        for i in range(node_cercles):
            self.G.add_edge(i, (i + 1) % node_cercles)
            
        # create rayons 
        first_nodes_rayon = []
        last_nodes_rayon = []
        list_node_rayon = []
        for rayon in range(nb_rayons):
            themes_clone = rotate_array(themes, rayon)
            start = self.G.number_of_nodes()
            
            list_node = []
            for i in range(node_rayons):
                t = themes_clone.pop()
                c = Case(screen=self.screen, type_case=TYPE_CASE['theme'], theme=t, node = start + i)
                self.G.add_node(start + i, **{ 'case': c })
                list_node.append(start + i)

            for i in range(node_rayons):
                next_node_index = start + i + 1
                if next_node_index in self.G.nodes:
                    self.G.add_edge(start + i, next_node_index)
            
            list_node_rayon.append(list_node)
            first_nodes_rayon.append(list(self.G.nodes)[start])
            last_nodes_rayon.append(list(self.G.nodes)[-1])

        # create and connect central node to rayon
        self.G.add_node(self.G.number_of_nodes(), **{
                    'case': Case(screen=self.screen, type_case=TYPE_CASE['start'], theme=start_theme, position=center, node=self.G.number_of_nodes())
                })

        central = list(self.G.nodes)[-1]
        for last_node_rayon in last_nodes_rayon:
            self.G.add_edge(central, last_node_rayon)
            
        # connect rayons to circle
        idx_list_node = 0
        list_node_rayon = list_node_rayon[::-1]
        for i in range(node_cercles):
            if i % (nb_rayons + 1) == 0:
                self.G.add_edge(i, first_nodes_rayon.pop())

                if idx_list_node < len(list_node_rayon):
                    angle = get_rotation_angle(self.get_case(central).position, self.get_case(i).position)
                    points = getEquidistantPoints(self.get_case(central).position, self.get_case(i).position, node_rayons + 1)
                    points = rotate_array(points, 1)
                    print(points)
                    
                    idx = 0
                    list_reversed = list_node_rayon[idx_list_node][::-1]
                    for node in list_reversed:
                        self.get_case(node).set_position(points[idx])
                        self.get_case(node).set_rotation(angle)
                        idx += 1
                    
                    idx_list_node += 1
                    
        # nx.draw_spectral(self.G, with_labels=True)
        # plt.show()

    def move_joueur(self, start, distance) -> Case:
        self.set_disable_all()
        cases_possible = self.show_possibilities(start, distance)
        print(f'Cases possibles depuis {start} distance {distance} :', cases_possible)

        for case in cases_possible:
            self.get_case(case).highlight()
            
    def show_possibilities(self, start, distance):
        path_lengths = nx.single_source_shortest_path_length(self.G, start)
        nodes_at_distance = [node for node, dist in path_lengths.items() if dist == distance]

        return nodes_at_distance

    def get_case(self, node_id) -> Case:
        return self.G.nodes[node_id]['case']
    
    def listen_cases(self, joueur: Joueur):
        for case in self.G.nodes:
            self.get_case(case).attach_joueur(joueur)

    def unlisten_cases(self):
        for case in self.G.nodes:
            self.get_case(case).detach_joueur()

    def set_disable_all(self):
        for case in self.G.nodes:
            self.get_case(case).set_disable(True)
