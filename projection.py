import math
import numpy as np

class Projection:
    def __init__(self,render):
        Near = render.camera.near_plane
        Far = render.camera.far_plane
        Right = math.tan(render.camera.h_fov / 2)
        Left = -Right
        Top = math.tan(render.camera.v_fov / 2)
        Bottom = -Top

        m00 = 2 / (Right - Left)
        m11 = 2 / (Top - Bottom)
        m22 = (Far + Near) / (Far - Near)
        m32 = -2*Near*Far / (Far - Near)
        self.projection_matrix = np.array([
            [m00, 0,0,0],
            [0, m11,0,0],
            [0,0,m22,1],
            [0, 0, m32, 0]
        ])

        HW, HH = render.H_Width, render.H_Height
        self.to_screen_matrix = np.array([
            [HW, 0, 0, 0],
            [0, -HH, 0, 0],
            [0, 0, 1, 0],
            [HW, HH, 0, 1]
        ])