from classes.Joueur import Joueur
from tkinter import Canvas
from classes.db.connectbdd import connectbdd
from utils import get_rotated_points

TYPE_CASE = {
    'theme': 0,
    'gain': 1,
    'raccourci' : 2,
    'start': 3,
    'null' : 4
}

class Case():
    def __init__(self, canvas = Canvas, type_case = 0, theme = 0, node = -1):
        super().__init__()
        
        self.canvas = canvas
        self.type_case = type_case
        self.theme = theme
        self.node = node
        self.questions_id = []
        self.table = connectbdd()
        
        self.joueur = None
        self.disable = True
        self.size = 25
        self.color = theme[0]
        self.case_graf = None

    def render(self, position, angle):
        self.case_graf = Case_graf(self.canvas, color=self.theme[0], position=position, angle=angle, node=self.node)
        self.case_graf.render(position, angle)

    def setup_event_listener(self):
       self.canvas.tag_bind(self.case_graf.id, "<Button-1>", self.on_click)
    
    @property
    def position(self):
        return self.case_graf.position
    
    @property
    def center(self):
        return self.case_graf.center
    
    def on_click(self, ev):
        if self.disable == False and self.joueur is not None:
            self.joueur.set_question(self, self.get_question())

    def attach_joueur(self, joueur: Joueur):
        self.joueur = joueur

    def detach_joueur(self):
        self.joueur = None
        self.reset_highlight()

    def set_disable(self, state = False):
        self.disable = state

    def highlight(self):
        #print('highlight:', self.toString())
        self.set_disable(False)
        self.case_graf.highlight()

    def reset_highlight(self):
        self.case_graf.reset_highlight()
        
    def get_question(self):
        full_sql_query = f"SELECT * FROM questions WHERE theme_id = {self.theme[1]} AND questions_id NOT IN ({','.join(map(str, self.questions_id))}) ORDER BY RANDOM() LIMIT 1"
        #print(f"Executing SQL query: {full_sql_query}")
        
        question_data = self.table.random_question(full_sql_query)
        self.questions_id.append(question_data[0])
        return question_data
    
    def update(self):
        pass
        
    def toString(self):
        return (self.node, self.disable, self.type_case, self.theme)


class Case_graf():
    def __init__(self, canvas: Canvas, color, position, angle, node):
        self.size = 30
        self.color = color
        self.position = position
        self.canvas = canvas
        self.angle = angle
        self.node = node
        self.id = None
        self.highlight_graf = None

        x, y = position
        self.vertices = [
            [x, y],
            [x + self.size, y],
            [x + self.size, y + self.size],
            [x, y + self.size],
        ]
        self.center = (x + self.size/2, y + self.size/2)

        self.render(position, angle)
        
    def render(self, position, angle):
        self.position = position
        self.angle = angle
        
        self.id = self.canvas.create_polygon(get_rotated_points(self.vertices, angle, self.center), fill=self.color)
        #self.canvas.create_text(self.center[0], self.center[1], text=self.node, font="Arial 16")

    def highlight(self):
        self.highlight_graf = Highlight(self.canvas, self.vertices)
    
    def reset_highlight(self):
        if self.highlight_graf is not None:
            self.canvas.delete(self.highlight_graf.id)
            self.highlight_graf = None

class Highlight(Canvas):
    def __init__(self, canvas: Canvas, vertices=None):
        x0, y0 = vertices[0]
        x1, y1 = vertices[2]
        self.id = canvas.create_oval(x0, y0, x1, y1, width=5)