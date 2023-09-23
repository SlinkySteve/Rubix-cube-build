import pygame
import sys
import OpenGL.GL as gl
import OpenGL.GLU as glu
import math

# Initialize Pygame
pygame.init()

# Set up the Pygame window
screen = pygame.display.set_mode((800, 600), pygame.OPENGL|pygame.DOUBLEBUF)
pygame.display.set_caption("Rubik's Cube")

# Enable depth testing
gl.glEnable(gl.GL_DEPTH_TEST)

# Set up the perspective transform
gl.glMatrixMode(gl.GL_PROJECTION)
gl.glLoadIdentity()
glu.gluPerspective(45, (screen.get_width() / screen.get_height()), 0.1, 50.0)

# Set the default matrix mode to GL_MODELVIEW
gl.glMatrixMode(gl.GL_MODELVIEW)

# Set the clear color
gl.glClearColor(0.0, 0.0, 0.0, 1.0)

# Define the vertices of the cube
vertices = [
    (1, 1, 1),
    (1, 1, -1),
    (1, -1, -1),
    (1, -1, 1),
    (-1, 1, 1),
    (-1, 1, -1),
    (-1, -1, -1),
    (-1, -1, 1)
]

# Define the edges of the cube
edges = [
    (0, 1),
    (0, 3),
    (0, 4),
    (1, 2),
    (1, 5),
    (2, 3),
    (2, 6),
    (3, 7),
    (4, 5),
    (4, 7),
    (5, 6),
    (6, 7)
]

# Define the colors of the cube faces
colors = [
    (1, 0, 0),  
    (0, 1, 0),  
    (0, 0, 1),  
    (1, 1, 0),  
    (1, 0, 1),  
    (0, 1, 1)
]

# Define the surface normals for the cube faces
surface_normals = [
    (1, 0, 0),  
    (-1, 0, 0),  
    (0, 1, 0),  
    (0, -1, 0),  
    (0, 0, 1),  
    (0, 0, -1)
]

# Define the vertices for each face of the cube
faces = [
    [0, 1, 2, 3],  
    [1, 5, 6, 2],  
    [5, 4, 7, 6],  
    [4, 0, 3, 7],  
    [4, 5, 1, 0],  
    [3, 2, 6, 7]  
]

# Initialize the rotation angle
angle = 0
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Handle WASD key press events
            if event.key == pygame.K_w:
                angle += 1
            elif event.key == pygame.K_a:
                angle += 1
            elif event.key == pygame.K_s:
                angle -= 1
            elif event.key == pygame.K_d:
                angle -= 1

    # Clear the color and depth buffers
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

    # Reset the current matrix to the identity matrix
    gl.glLoadIdentity()

    # Move the cube back in the scene
    gl.glTranslatef(0, 0, -5)

    # Rotate the cube
    gl.glRotatef(angle, 1, 1, 1)

    # Draw the cube
    for face in faces:
        gl.glBegin(gl.GL_QUADS)
        for vertex in face:
            gl.glColor3fv(colors[faces.index(face)])
            gl.glNormal3fv(surface_normals[faces.index(face)])
            gl.glVertex3fv(vertices[vertex])
        gl.glEnd()

    # Draw the edges of the cube
    gl.glColor3fv((0, 0, 0))
    gl.glBegin(gl.GL_LINES)
    for edge in edges:
        for vertex in edge:
            gl.glVertex3fv(vertices[vertex])
    gl.glEnd()

    # Update the angle and redraw the scene
    pygame.display.flip()
    pygame.time.wait(10)

'''while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the color and depth buffers
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

        # Reset the current matrix to the identity matrix
        gl.glLoadIdentity()

        # Move the cube back in the scene
        gl.glTranslatef(0, 0, -5)

        # Rotate the cube
        gl.glRotatef(angle, 1, 1, 1)

        # Draw the cube
        for face in faces:
            gl.glBegin(gl.GL_QUADS)
            for vertex in face:
                gl.glColor3fv(colors[faces.index(face)])
                gl.glNormal3fv(surface_normals[faces.index(face)])
                gl.glVertex3fv(vertices[vertex])
            gl.glEnd()

        # Draw the edges of the cube
        gl.glColor3fv((0, 0, 0))
        gl.glBegin(gl.GL_LINES)
        for edge in edges:
            for vertex in edge:
                gl.glVertex3fv(vertices[vertex])
        gl.glEnd()

        # Update the angle and redraw the scene
        angle += 0.1
        pygame.display.flip()
        pygame.time.wait(10)'''


