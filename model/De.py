import random
class De:
    def __init__(self, faces = 6):
        self.faces = faces

    def randomize(self):
        return random.randint(1,self.faces)
    
    