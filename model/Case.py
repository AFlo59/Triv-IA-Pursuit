TYPE_CASE = {
    'theme': 0,
    'gain': 1,
    'raccourci' : 2,
    'null' : 4
}

class Case:
    def __init__(self) -> None:
        self.position = (None, None)
        self.type = 0
        
    def get_question(self):
        # TODO get_question
        print('get question')
        return 'question'