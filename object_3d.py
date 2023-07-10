import pygame as pg
from matrices import *
from numba import njit

@njit(fastmath=True)
def any_func(arr,a,b):
    return np.any((arr==a)|(arr==b))

class Object3D:
    def __init__(self, render, vertices, faces):
        self.render = render
        self.vertices = np.array([np.array(v) for v in vertices])
        self.faces = np.array([np.array(f) for f in faces])
        #self.vertices = np.array([            (0, 0, 0, 1),            (0, 1, 0, 1),            (1, 1, 0, 1),            (1, 0, 0, 1),           (0, 0, 1, 1),            (0, 1, 1, 1),            (1, 1, 1, 1),            (1, 0, 1, 1)        ])
        #self.faces = np.array([            (0,1,2,3),            (4,5,6,7),            (0,4,5,1),            (2,3,7,6),            (1,2,6,5),            (0,3,7,4)])
        self.font = pg.font.SysFont('Arial', 30, bold = True)
        self.color_faces = [(pg.Color('white'), face) for face in self.faces]
        self.movement_flag, self.draw_vertices = True, False
        self.label = ''

    def draw(self):
        self.screen_projection()
        self.movement()

    def movement(self):
        if self.movement_flag:
            self.rotate_y(pg.time.get_ticks() % 0.005)

    def screen_projection(self):
        vertices = self.vertices @ self.render.camera.camera_matrix()
        vertices = vertices @ self.render.projection.projection_matrix
        vertices /= vertices[:, -1].reshape(-1,1)
        vertices[(vertices > 2) | (vertices < -2)] = 0
        vertices = vertices @ self.render.projection.to_screen_matrix
        vertices = vertices[:, :2]

        for index, color_face in enumerate(self.color_faces): #11:42
            color, face = color_face
            polygon = vertices[face]
            if not any_func(polygon, self.render.H_Width, self.render.H_Height):
                pg.draw.polygon(self.render.screen, color, polygon, 1)
                if self.label:
                    text = self.font.render(self.label[index], True, pg.Color('white'))
                    self.render.screen.blit(text,polygon[-1])
            if self.draw_vertices:
                for vertex in vertices:
                    if not any_func(self.render.H_Width, self.render.H_Width):
                        pg.draw.circle(self.render.screen, pg.Color('white'), vertex, 2)

    def translate(self, pos):
        self.vertices = self.vertices @ translate(pos)

    def scale(self, scale_to):
        self.vertices = self.vertices @ scale(scale_to)

    def rotate_x(self, angle):
        self.vertices = self.vertices @ rotate_x(angle)

    def rotate_y(self, angle):
        self.vertices = self.vertices @ rotate_y(angle)

    def rotate_z(self, angle):
        self.vertices = self.vertices @ rotate_z(angle)

class Axes(Object3D):
    def __init__(self, render):
        super().__init__(render)
        self.vertices = np.array([
            (0,0,0,1),
            (1,0,0,1),
            (0,1,0,1),
            (0,0,1,1)
        ])
        self.faces = np.array([
            (0,1),(0,2),(0,3)
        ])
        self.colors = [pg.Color('red'), pg.Color('green'), pg.Color('blue')]
        self.color_faces = [(color, face) for color, face in zip(self.colors, self.faces)]
        self.draw_vertices = False
        self.label = 'XYZ'

