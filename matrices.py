import math
import numpy as np


def translate(pos):
    tx, ty, tz = pos
    return np.array([
        [1,0,0,0],
        [0,1,0,0],
        [0,0,1,0],
        [tx,ty,tz,1]
    ])
def rotate_x(a):
    return np.array([
        [1,0,0,0],
        [0, math.cos(a), math.sin(a), 0],
        [0,-math.sin(a), math.cos(a), 0],
        [0,0,0,1]
    ])

def rotate_y(n):
    return np.array([
         [math.cos(n), 0, -math.sin(n), 0],
         [0,   1,   0,   0],
         [math.sin(n), 0, math.cos(n), 0],
         [0 ,  0,   0,   1]
    ])

def rotate_z(n):
    return np.array([
         [math.cos(n), math.sin(n), 0, 0],
         [-math.sin(n), math.cos(n), 0, 0],
         [0,   0,   1,   0],
         [0,   0 ,  0,   1]
    ])

def scale(n):
    return np.array([
        [n, 0, 0, 0],
        [0, n, 0, 0],
        [0, 0, n, 0],
        [0, 0, 0, 1]
    ])

