import os
import random

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
def de(start = 1, faces = 6):
    return random.randint(start, faces)