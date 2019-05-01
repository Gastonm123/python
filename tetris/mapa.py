import pygame, math, numpy
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

threshold = 0.0005

def isInside(box, vertex): 
    if gt(vertex[0], box[0][0]): 
        if lt(vertex[1], box[1][1]): 
            if lt(vertex[0], box[2][0]): 
                if gt(vertex[1], box[3][1]): 
                    return True
    
    return False

def lt(a, b):
    return (a-b < -threshold)
def le(a, b):
    return (lt(a, b) or math.fabs(a-b) < threshold)
def ge(a, b):
    return (not lt(a, b))
def gt(a, b):
    return (not le(a, b))

def isInsideCubo(cubo, vertex, config):
    ans = [False for i in range(4)]

    if config[0]:
        if gt(vertex[0], cubo[0][0]):
            ans[0] = True
    elif ge(vertex[0], cubo[0][0]):
        ans[0] = True

    if config[1]:
        if lt(vertex[1], cubo[1][1]):
            ans[1] = True
    elif le(vertex[1], cubo[1][1]):
        ans[1] = True

    if config[2]:
        if lt(vertex[0], cubo[2][0]):
            ans[2] = True
    elif le(vertex[0], cubo[2][0]):
        ans[2] = True

    if config[3]:
        if gt(vertex[1], cubo[3][1]):
            ans[3] = True
    elif ge(vertex[1], cubo[3][1]):
        ans[3] = True

    def aux(a, b):
        return a and b

    return reduce(aux, ans) 


class Mapa:
    mapBorder = (
        (-1.1, 1.6, 0),
        (1.1, 1.6, 0),
        (1.1, 1.5, 0),
        (-1.1, 1.5, 0),

        (1, 1.5, 0),
        (1.1, 1.5, 0),
        (1.1, -1.1, 0),
        (1, -1.1, 0),

        (-1.1, -1.1, 0),
        (1.1, -1.1, 0),
        (1.1, -1.2, 0),
        (-1.1, -1.2, 0),

        (-1.1, 1.5, 0),
        (-1, 1.5, 0),
        (-1, -1.1, 0),
        (-1.1, -1.1, 0)
    )

    grilla = (
        [x for x in numpy.arange(-0.9, 1, 0.1)],
        [y for y in numpy.arange(-1, 1.5, 0.1)]
    )

    def __init__(self):
        self.vertices = Mapa.mapBorder[4:]
        self.mapBorder = Mapa.mapBorder
        self.cubos = []
        self.lines = {}
        self.puntaje = 0

    def draw(self):
        glBegin(GL_QUADS)
        glColor3f(0.25, 0.25, 0.25)
        for index in range(0, len(self.mapBorder), 4):
            glVertex3fv(self.mapBorder[index])
            glVertex3fv(self.mapBorder[index+1])
            glVertex3fv(self.mapBorder[index+2])
            glVertex3fv(self.mapBorder[index+3])
        glEnd()

        glBegin(GL_LINES)
        glColor3f(0.25, 0.25, 0.25)
        for x in Mapa.grilla[0]:
            glVertex3fv((x, -1.1, 0))
            glVertex3fv((x, 1.5, 0))
        for y in Mapa.grilla[1]:
            glVertex3fv((-1.1, y, 0))
            glVertex3fv((1.1, y, 0))
        glEnd()

        map(lambda c: c.draw(), self.cubos)

    def collide(self, obj, direction): #direction es la direccion del ultimo movimiento 
        _direction = {
            "up":    (0, 1),
            "down":  (2, 3),
            "left":  (0, 3),
            "right": (1, 2),
            "": (0, 1, 2, 3)
        }
        _config    = {
            "up":     (0, 0, 0, 1),
            "down":   (0, 1, 0, 0),
            "left":   (0, 0, 1, 0),
            "right":  (1, 0, 0, 0),
            "": (0,0,0,0)
        }

        vertices = _direction[direction]
        
        for index in range(0, len(self.vertices), 4):
            border = self.vertices[index:index+4]
            for cubo in obj.cubos:
                if isInside(border, cubo[vertices[0]]): #no es necesario checkear los dos
                    return True
        
        
        config = _config[direction]

        for mapaObj in self.cubos:
            for cubo in obj.cubos:
                """ si se mueve de costado basta un vertice adentro del mapa para
                    determinar la colision. De otra manera ambos vertices tienen
                    que estar dentro del mapa """
                if direction in ["left", "right", ""]: 
                    if isInsideCubo(mapaObj, cubo[vertices[0]], config):
                        return True
                    if isInsideCubo(mapaObj, cubo[vertices[1]], config):
                        return True
                elif isInsideCubo(mapaObj, cubo[vertices[0]], config):
                    if isInsideCubo(mapaObj, cubo[vertices[1]], config):
                        return True

        return False

    def checkLine(self, line):
        if len(self.lines[line]) < 20:
            return

        self.multiplicador += 1

        for cubo in self.lines[line]:
            self.cubos.remove(cubo)

        self.lines.pop(line)

        for upperLine in range(line+1, 16):
            if upperLine in self.lines:
                for cubo in self.lines[upperLine]:
                    cubo.move(0, -1, 0)

                self.lines[upperLine-1] = self.lines[upperLine]
                self.lines.pop(upperLine)
                     
    puntaje = {
        "linea": 200,
        1: 1, 
        2: 1.25,
        3: 1.5,
        4: 2
    }

    def pasarCubos(self, cubos):
        self.cubos.extend(cubos)
        self.multiplicador = 0

        for cubo in cubos:
            y_cubo = math.trunc(cubo[0][1] * 10)

            if y_cubo in self.lines:
                self.lines[y_cubo].append(cubo)
                self.checkLine(y_cubo)
            else:
                self.lines[y_cubo] = [cubo]

        if self.multiplicador:
            puntajePorLineas = Mapa.puntaje['linea'] * self.multiplicador
            bonus = puntajePorLineas * Mapa.puntaje[self.multiplicador]
            self.puntaje += bonus

        