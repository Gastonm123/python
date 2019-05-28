import pyglet
from pyglet.gl import *
from pyglet import clock

window = pyglet.window.Window()
clock.set_fps_limit(60)

@window.event
def on_draw():
    clock.tick()
    mx = window.width // 2
    my = window.height // 2
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glBegin(GL_QUADS)
    glVertex2f(mx-10, my+10)
    glVertex2f(mx+10, my+10)
    glVertex2f(mx+10, my-10)
    glVertex2f(mx-10, my-10)
    glEnd()

pyglet.app.run()