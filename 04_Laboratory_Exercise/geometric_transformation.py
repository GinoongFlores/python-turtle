import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def draw_cube():
    glBegin(GL_TRIANGLES)

    # Front face
    glColor3f(1, 0, 0)  # Red
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)

    # Left face 
    glColor3f(0, 1, 0)  # Green
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, 1, 1)

    # Right face
    glColor3f(0, 0, 1)  # Blue
    glVertex3f(1, 1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)

    # Back face
    glColor3f(1, 1, 0)  # Yellow
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, 1, -1)

    # Top face
    glColor3f(1, 0, 1)  # Magenta
    glVertex3f(-1, 1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, 1, 1)

    # Bottom face
    glColor3f(0, 1, 1)  # Cyan
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)

    glEnd()


def main():
    pygame.init()

    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    pygame.display.set_caption("03 Lab 1")

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0, 0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            glTranslatef(0, 0.1, 0) # Move up
            glRotatef(-1, 1, 0, 0) # Rotate around the x-axis
        if keys[pygame.K_s]:
            glTranslatef(0, -0.1, 0) # Move down
            glRotatef(1, 1, 0, 0) # Rotate around the x-axis
        if keys[pygame.K_a]:
            glTranslatef(-0.1, 0, 0) # Move left
            glRotatef(-1, 0, 1, 0) # Rotate around the y-axis
        if keys[pygame.K_d]:
            glTranslatef(0.1, 0, 0) # Move right
            glRotatef(1, 0, 1, 0) # Rotate around the y-axis

        glRotatef(-1, 1, 0, 0) # Rotate around the x-axis
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        draw_cube()

        pygame.display.flip()
        pygame.time.wait(15)


if __name__ == '__main__':
    main()