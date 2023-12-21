import os
import random

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
def de(start = 1, faces = 6):
    return random.randint(start, faces)

def rotate_array(arr, start):
    return arr[start:] + arr[:start]

def lerp(v0, v1, i):
    return v0 + i * (v1 - v0)

def getEquidistantPoints(p1, p2, n):
    return [(lerp(p1[0], p2[0], 1./n * i), lerp(p1[1], p2[1], 1./n * i)) for i in range(n + 1)]