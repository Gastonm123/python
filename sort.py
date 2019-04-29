import math
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
from aux2 import Driver

class Sorter:
    def __init__(self, size):
        self.list = [i+1 for i in range(size)]
        random.shuffle(self.list)
        self.colors = [(1, 1, 1) for i in range(size)]
        self.remainingLen = size
        self.it = 0

    def draw(self):
        glBegin(GL_QUADS)
        for index, item in enumerate(self.list):
            glColor3f(*self.colors[index])

            index = index/10.0
            item = item/10.0
            vertices = (
                (index, 0, 0),
                (index, item, 0),
                (index+0.1, item, 0),
                (index+0.1, 0, 0),
            )
            
            for vertex in vertices:
                glVertex3fv(vertex)
        glEnd()

    def sort(self):
        if self.it == self.remainingLen:
            self.it = 0
            self.remainingLen -= 1
            self.colors[self.remainingLen] = (0, 1, 0) #set to green

        if self.it == len(self.list):
            return

        self.colors[self.it] = (1, 1, 0)
        if self.it > 0:
            self.colors[self.it-1] = (1, 1, 1)
            if self.list[self.it-1] > self.list[self.it]:
                temp = self.list[self.it-1]
                self.list[self.it-1] = self.list[self.it]
                self.list[self.it] = temp

        self.it += 1

class FastSorter:
    def __init__(self, size):
        self.colors = [(1,1,1) for i in range(size)]
        self.list = [i+1 for i in range(size)]
        random.shuffle(self.list)
        self.clock = pygame.time.Clock()

    def draw(self):
        self.clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        #draw itself
        glBegin(GL_QUADS)
        for index, item in enumerate(self.list):
            glColor3f(*self.colors[index])

            index = index/10.0
            item = item/10.0
            vertices = (
                (index, 0, 0),
                (index, item, 0),
                (index+0.1, item, 0),
                (index+0.1, 0, 0),
            )
            
            for vertex in vertices:
                glVertex3fv(vertex)
        glEnd()

        pygame.display.flip()
    
    def merge(self, a, m, b):
        temp = []
        middle = m
        begin = a
        fixedb = b if b < len(self.list) else b-1
        
        while a < middle or m < b:
            fixedm = m if m < b else a

            self.colors[fixedm] = (1, 0, 0)
            self.colors[a] = (1, 0, 0)
            self.colors[middle] = (0.5, 0.5, 1)
            self.colors[begin] = (0, 1, 0)
            self.colors[fixedb] = (0, 1, 0)
            self.draw()

            self.colors[a] = (1, 1, 1)
            self.colors[fixedm] = (1, 1, 1)
            
            if a < middle and m < b:
                temp.append(min(self.list[a], self.list[m]))
                if self.list[a] < self.list[m]:
                    a += 1
                else:
                    m += 1
            elif a < middle:
                temp.append(self.list[a])
                a += 1
            elif m < b:
                temp.append(self.list[m])
                m += 1
        
        for i in range(begin, b):
            self.colors[i] = (1, 0, 0)
            self.colors[begin] = (0, 1, 0)
            self.colors[fixedb] = (0, 1, 0)
            self.draw()
            self.colors[i] = (1, 1, 1)

            self.list[i] = temp[i-begin]
        
        self.colors[begin] = (1, 1, 1)
        self.colors[fixedm] = (1, 1, 1)

    def sort(self, a, b):
        m = math.floor((a+b) / 2)

        if m == a:
            return
        
        self.sort(a, m)
        self.sort(m, b)

        self.merge(a, m, b)     

def main():
    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, 1, 0.5, 50)

    glTranslatef(-2,-2, -7)

    d = Driver(60)
    s = FastSorter(40)
    s.sort(0, 40)
    while True:
        s.draw()
    """ while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        d.triggerKeysf()
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        s.draw()
        s.sort()
        pygame.display.flip() """

main()