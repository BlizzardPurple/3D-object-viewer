import pyglet
import pyglet.gl as gl
import math

class particle:

    def __init__(self, position, mass, velocity):
        self.position = position
        self.mass = mass
        self.velocity= velocity
        self.speed = math.sqrt(self.velocity[0]**2 + self.velocity[1]**2)
        self.momentum = self.mass * self.speed
        self.pointsdraw = pyglet.graphics.vertex_list(1,('v2f/stream', self.position), ('c3B', [0,0,255]))

    def move(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.position.vertices = self.position

def resize(width,height, zoom, x, y):
    gl.glMatrixMode(gl.GL_MODELVIEW)
    gl.glLoadIdentity()
    gl.glOrtho(-width, width, -height, height, -1, 1)
    gl.glViewport(0, 0, width, height)
    gl.glOrtho(-zoom, zoom, -zoom, zoom, -1, 1)
    gl.glTranslated(-x,-y,0)

class mywindow(pyglet.window.Window):

    def __init__(self, width, height, name):
        super().__init__(width, height, name, resizable = True)

        gl.glClearColor (1,1,1,1)
        gl.glPointSize (5)

        #WindowVars
        self.width = width
        self.height = height
        self.name = name
        self.zoom = 1
        self.x = 0
        self.y = 0
        self.time = 0
        self.key = None
        self.mainparticle = particle([0,0], 10, [1,0])

    def on_draw(self, dt = 0.002):
        self.clear()
        self.mainparticle.pointsdraw.draw(pyglet.gl.GL_POINTS)
        self.mainparticle.move()

    def on_resize(self, width, height):
        gl.glMatrixMode(gl.GL_MODElVIEW)
        gl.glLoadIdentity()
        gl.glOrtho(-width, width, -height, height, -1, 1)
        gl.glViewport(0,0,width,height)
        gl.glOrtho(-self.zoom, self.zoom, -self.zoom, self.zoom, -1, 1)