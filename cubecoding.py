import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Ekran boyutları
WIDTH, HEIGHT = 800, 600

# Küpün başlangıç boyutu
cube_scale = 1.0

# Köşe noktaları, (x, y, z) formatında
CUBE_VERTICES = [
    (-1, -1, -1),
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, 1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, 1, 1)
]


# Yüzeylerin köşe noktaları eşleşmeleri
CUBE_EDGES = (
    (0, 1, 2, 3),
    (4, 5, 6, 7),
    (0, 4, 5, 1),
    (1, 5, 6, 2),
    (2, 6, 7, 3),
    (3, 7, 4, 0)
)

# Her yüzey için renkler
SURFACE_COLORS = [
    (1.0, 0.0, 0.0),  # Kırmızı
    (0.0, 1.0, 0.0),  # Yeşil
    (0.0, 0.0, 1.0),  # Mavi
    (1.0, 1.0, 0.0),  # Sarı
    (1.0, 0.0, 1.0),  # Mor
    (0.0, 1.0, 1.0)   # Cyan
]

def draw_cube():
    for i, surface in enumerate(CUBE_EDGES):
        glBegin(GL_QUADS)
        glColor3fv(SURFACE_COLORS[i])
        for vertex in surface:
            glVertex3fv(tuple([v * cube_scale for v in CUBE_VERTICES[vertex]]))
        glEnd()

def main():
    global cube_scale
    
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("3D Görünüm")
    
    gluPerspective(60, (WIDTH/HEIGHT), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            cube_scale += 0.1
        if keys[pygame.K_DOWN]:
            cube_scale -= 0.1

        glRotatef(2, 14, 16, 6)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        glClearColor(1.0, 0.65, 0.0, 1.0)  # Arka plan rengini turuncu yap
        draw_cube()
        
        pygame.display.flip()
        clock.tick(200)

    pygame.quit()

if __name__ == "__main__":
    main()
