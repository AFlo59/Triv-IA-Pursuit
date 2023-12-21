import math
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
    return [(lerp(p1[0], p2[0], 1./n * i), lerp(p1[1], p2[1], 1./n * i)) for i in range(n)]

def distribute_points_equidistant(start_point, end_point, n):
    """
    Distribue des points égaux entre deux points sur une ligne.

    Args:
        start_point: Les coordonnées du point de départ.
        end_point: Les coordonnées du point d'arrivée.
        n: Le nombre de points souhaités.

    Returns:
        Une liste des coordonnées des points.
    """

    x1, y1 = start_point
    x2, y2 = end_point

    step = (x2 - x1) / (n - 1)

    points = []
    for i in range(n):
        x = x1 + i * step
        points.append((x, y1))

    return points

def get_rotation_angle(start_point, end_point):
    """
    Calcul l'angle de rotation d'un rectangle.

    Args:
        start_point: Les coordonnées du point de départ du rectangle.
        end_point: Les coordonnées du point d'arrivée du rectangle.

    Returns:
        L'angle de rotation du rectangle en degrés.
    """

    y_1, x_1 = start_point
    y_2, x_2 = end_point

    angle = math.atan2(y_2 - y_1, x_2 - x_1)
    angle = angle * 180 / math.pi

    return angle