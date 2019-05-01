import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
    
class Cubo:
    vertices = (
        (0, 0, 0),
        (0.1, 0, 0),
        (0.1, -0.1, 0),
        (0, -0.1, 0)
    )

    def __init__(self, abs_pos, color):
        self.vertices = Cubo.vertices
        self.pos = abs_pos
        self.color = color
        self.corrimiento = (0, 0, 0)

    def getPos(self):
        return self.pos

    def move(self, x, y, z):
        self.corrimiento = (
            self.corrimiento[0] + x/10.0,
            self.corrimiento[1] + y/10.0,
            self.corrimiento[2] + z/10.0
        )

        self.pos[0] += x/10.0
        self.pos[1] += y/10.0
        self.pos[2] += z/10.0

    def getVertex(self):
        return map(lambda v: (
            v[0]+self.pos[0], v[1]+self.pos[1], v[2]+self.pos[2]
            ), self.vertices)

    def rotate(self, degrees):
        rad = degrees / 180.0 * math.pi
        
        self.pos[0] -= self.corrimiento[0]
        self.pos[1] -= self.corrimiento[1]

        x, y, _ = self.pos

        self.pos[0] = x * math.cos(rad) - y * math.sin(rad) 
        self.pos[1] = x * math.sin(rad) + y * math.cos(rad)

        self.pos[0] += self.corrimiento[0]
        self.pos[1] += self.corrimiento[1]

    def draw(self):
        glBegin(GL_QUADS)
        glColor3f(*self.color)

        for vertex in self.getVertex():    
            glVertex3fv(vertex)
        
        glEnd()

        glBegin(GL_LINES)
        glColor3f(0.5, 0.5, 0.5)
        
        vertices = self.getVertex()
        edges = (
            0, 2,
            1, 3,
            0, 1,
            0, 3
        )
        
        for index in edges:
            glVertex3fv(vertices[index])

        glEnd()

    def __getitem__(self, n):
        return self.getVertex()[n]