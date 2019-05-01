import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from aux import *
from aux2 import *

""" schedule = (
    (2, 2, 0, 0),
    (4, -4, 0, 0),
    (2, 2, 0, 0),
    (2, 0, 2, 0),
    (4, 0, -4, 0),
    (2, 0, 2, 0)
) """

def main():
    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50)

    glTranslatef(0, 0, -5)
    glEnable(GL_DEPTH_TEST)

    clock = pygame.time.Clock()
    d = Driver(60)
    p = Pyramid()
    i = 0

    #d.setMove(*schedule[i])
    while True:
        clock.tick(60)
        
        """ if d.makeMove():
            i = (i+1) % len(schedule)
            d.setMove(*schedule[i]) """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        
        d.triggerKeysf()

        #glRotatef(2, 1, 3, 6) #velocidad, vector rotacion
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        p.draw()
        pygame.display.flip()

main()