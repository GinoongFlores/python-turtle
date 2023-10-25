
import PyGame

from PyGame.locals import * 
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


pygame.init()

display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
 
pygame.display.set_caption("03 Lab 1")

gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glTranslatef(0,0,-5)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    glRotatef(1,1,3,1)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glBegin(GL_LINES)

    # Front face
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)

    # Connect the corners to complete the square
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, 1, -1)

    # Back face
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(-1, 1, -1)

    glEnd()
    pygame.display.flip()
    pygame.time.wait(15)


