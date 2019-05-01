import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from mapa import Mapa
from cubo import Cubo
from pieza import Pieza

def main():
    pygame.init()
    pygame.font.init()
    display = (800, 800)
    screen = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, 1, 0.5, 50)
    glTranslatef(0, 0, -5)

    clock = pygame.time.Clock()
    lock = {}
    p = Pieza()
    p.move(0, 15, 0)
    vel = 0.125
    m = Mapa()
    pase_max = 4
    pase = [0, pase_max]

    while True:
        clock.tick(40)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print "Puntaje " + str(m.puntaje)
                pygame.quit()
                quit()


        """Controles"""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and not 'up' in lock:
            p.secure_rotate(90, m)
            lock['up'] = 8
            if pase[1]:
                pase = [7, pase[1]-1] #pase de 7 frames para reacomodar una pieza
        if keys[pygame.K_DOWN]: # and not 'down' in lock:
            p.secure_move("down", -3*vel, m)
        if keys[pygame.K_SPACE] and not 'space' in lock:
            while p.secure_move("down", -0.75, m):
                pass
            lock['space'] = 8
        if keys[pygame.K_LEFT] and not 'left' in lock:
            p.secure_move("left", -0.5, m)
            p.secure_move("left", -0.5, m)
            lock['left'] = 4
        if keys[pygame.K_RIGHT] and not 'right' in lock:
            p.secure_move("right", 0.5, m)
            p.secure_move("right", 0.5, m)
            lock['right'] = 4
        if keys[pygame.K_p]:
            raw_input("continue?")

        
        """Drawing"""
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
       
        m.draw()
        p.draw()
            
        pygame.display.flip()


        """Ending"""
        if not pase[0]: 
            if not p.secure_move("down", -1*vel, m):
                m.pasarCubos(p.cubos)
                p = Pieza()
                p.secure_move("up", 15, m)

                if m.collide(p, ""):
                    print "Game Over"
                    raw_input("End?")
                    print "Puntaje " + str(m.puntaje)
                    pygame.display.quit()
                    quit()

            pase[1] = pase_max

        pase[0] = 0 if pase[0]-1 < 0 else pase[0]-1
        for key in lock.keys():
            lock[key] -= 1
            
            if lock[key] == 0:
                lock.pop(key)

main()