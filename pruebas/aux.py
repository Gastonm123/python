import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class Pyramid:
    vertices = (
        (-1, -1, -1),
        (1, -1, -1),
        (1, -1, 1),
        (-1, -1, 1),
        (0, 1, 0),
    )

    edges = (
        (0, 1),
        (0, 3),
        (0, 4),
        (1, 4),
        (1, 2),
        (2, 4),
        (2, 3),
        (3, 4)
    )

    surfaces = (
        (0, 1, 4),
        (1, 2, 4),
        (2, 3, 4),
        (3, 0, 4),
        (0, 1, 2, 3)
    )

    def __init__(self):
        self.edges = Pyramid.edges
        self.vertices = Pyramid.vertices#list(map(lambda x: list(x), Pyramid.vertices))
        self.surfaces = Pyramid.surfaces

    def draw(self):
        self.drawSides()

        glLineWidth(5)
        glBegin(GL_LINES)

        glColor3f(1, 1, 0)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])

        glEnd()

    def drawSides(self):
        glBegin(GL_TRIANGLES)

        glColor3f(0, 1, 0.5)
        for surface in self.surfaces[:-1]:
            for vertex in surface:
                glVertex3fv(self.vertices[vertex])
        
        glEnd()
        glBegin(GL_QUADS)

        for surface in self.surfaces[-1:]:
            for vertex in surface:
                glVertex3fv(self.vertices[vertex])
        
        glEnd()

    def move(self, x, y, z):
        self.vertices = list(map(lambda vertex: (vertex[0]+x, vertex[1]+y, vertex[2]+z), self.vertices))
