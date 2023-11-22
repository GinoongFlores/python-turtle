import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def draw_cube():
    glBegin(GL_TRIANGLES)

    # Front face
    
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)

    # Left face
    
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, 1, 1)

    # Right face
 
    glVertex3f(1, 1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)

    # Back face
  
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, 1, -1)

    # Top face
   
    glVertex3f(-1, 1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, 1, 1)

    # Bottom face
 
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)

    glEnd()

def draw_object():
    
       # First pair
    glPushMatrix()
    glColor3f(0, 0.4, 0)  # Light Green
    glScalef(1, 1, 1)  # Original size
    draw_cube()
    glPopMatrix()

    # Second pair
    glPushMatrix()
    glColor3f(0, 0.6, 0)  # Medium Light Green
    glScalef(0.75, 0.75, 0.75)  # 75% size
    draw_cube()
    glPopMatrix()

    # Third pair
    glPushMatrix()
    glColor3f(0, 0.8, 0)  # Medium Dark Green
    glScalef(0.5, 0.5, 0.5)  # 50% size
    draw_cube()
    glPopMatrix()

    # Fourth pair
    glPushMatrix()
    glColor3f(0, 1, 0)  # Dark Green
    glScalef(0.25, 0.25, 0.25)  # 25% size
    draw_cube()
    glPopMatrix()

    
def main():
    pygame.init()

    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    pygame.display.set_caption("05 Lab 1")

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0, 0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            glTranslatef(0, 0.1, 0)
        if keys[pygame.K_s]:
            glTranslatef(0, -0.1, 0)
        if keys[pygame.K_a]:
            glTranslatef(-0.1, 0, 0)
        if keys[pygame.K_d]:
            glTranslatef(0.1, 0, 0)

        glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        draw_object()

        pygame.display.flip()
        pygame.time.wait(15)


if __name__ == '__main__':
    main()