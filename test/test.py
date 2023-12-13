import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

vertices = (
    (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5),
    (0.5, -0.5, 0.5), (0.5, 0.5, 0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5)
)
quads = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
)

def create_cube():
    cube = glGenLists(1)
    glNewList(cube, GL_COMPILE)
    glBegin(GL_QUADS)
    for quad in quads:
        for vertex in quad:
            glVertex3fv(vertices[vertex])
    glEnd()
    glEndList()
    return cube

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -20)

    cube_size = 0.9
    cube_positions = [i * cube_size for i in range(5)] 
    cube_colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1)]
    angle = 0
    spinning = False
    rotation_x = 0

    glEnable(GL_DEPTH_TEST)

    step_size = 1.1 * cube_size

    cube = create_cube()

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    spinning = not spinning
                elif event.key == pygame.K_LEFT:
                    cube_positions = [x - step_size for x in cube_positions]
                elif event.key == pygame.K_RIGHT:
                    cube_positions = [x + step_size for x in cube_positions]

        if spinning:
            angle += 1

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        glRotatef(angle, 0, 0, 1)
        
        for position, color in zip(cube_positions, cube_colors):
            glPushMatrix()
            glTranslatef(position, 0, 0)
            glColor3fv(color)
            glScalef(cube_size, cube_size, cube_size)
            glRotatef(rotation_x, 1, 0, 0)
            glCallList(cube)
            glPopMatrix()

        glPopMatrix()

        pygame.display.flip()
        clock.tick(60)

main()
