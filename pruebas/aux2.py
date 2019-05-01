import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class Driver:
    def __init__(self, fps):
        self.fps = fps
        self.vel = 0.1
    
    def setMove(self, time, x, y, z):
        self.iterations = float(time * self.fps)
        self.x = x / self.iterations
        self.y = y / self.iterations
        self.z = z / self.iterations

    def makeMove(self):
        glTranslatef(self.x, self.y, self.z)
        self.iterations -= 1

        return (self.iterations == 0)

    def triggerKeysf(self):
        keys = pygame.key.get_pressed()
        vel = self.vel

        if(keys[pygame.K_LEFT]):
            glTranslatef(vel, 0, 0)
        if(keys[pygame.K_RIGHT]):
            glTranslatef(-vel, 0 ,0)
        if(keys[pygame.K_UP]):
            glTranslatef(0, -vel, 0)
        if(keys[pygame.K_DOWN]):
            glTranslatef(0, vel, 0)
        if(keys[pygame.K_g]):
            glTranslatef(0, 0, -vel)
        if(keys[pygame.K_t]):
            glTranslatef(0, 0, vel)
        if(keys[pygame.K_j]):
            glRotatef(-2, 0, 1, 0)
        if(keys[pygame.K_l]):
            glRotatef(2, 0, 1, 0)
        if(keys[pygame.K_k]):
            glRotatef(-2, 1, 0, 0)
        if(keys[pygame.K_i]):
            glRotatef(2, 1, 0, 0)

    def triggerKeys(self, obj):
        keys = pygame.key.get_pressed()
        vel = self.vel

        if(keys[pygame.K_LEFT]):
            obj.move(-vel, 0, 0)
        if(keys[pygame.K_RIGHT]):
            obj.move(vel, 0, 0)
        if(keys[pygame.K_UP]):
            obj.move(0, vel, 0)
        if(keys[pygame.K_DOWN]):
            obj.move(0, -vel, 0)