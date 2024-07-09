import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Ekran boyutları
WIDTH, HEIGHT = 800, 600

# Renkler
WHITE = (1, 1, 1)
BLUE = (0, 0, 1)
YELLOW = (1, 1, 0)
RED = (1, 0, 0)

# Kamera pozisyonu ve bakış açısı
camera_x, camera_y, camera_z = 0, 0, 10
look_x, look_y, look_z = 0, 0, 0

# Dönme açıları ve hızları
angle1, angle2, angle3 = 0, 0, 0
speed1, speed2, speed3 = 1, 2, 3

def draw_half_sphere(radius, num_slices, num_stack, color1, color2):
    for i in range(num_slices):
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(num_stack + 1):
            phi = (i / num_slices) * 2 * math.pi
            theta = (j / num_stack) * math.pi
            x = radius * math.cos(phi) * math.sin(theta)
            y = radius * math.sin(phi) * math.sin(theta)
            z = radius * math.cos(theta)
            
            if y > 0:
                glColor3fv(color1)
            else:
                glColor3fv(color2)
                
            glVertex3f(x, y, z)
            
            phi = ((i + 1) / num_slices) * 2 * math.pi
            theta = (j / num_stack) * math.pi
            x = radius * math.cos(phi) * math.sin(theta)
            y = radius * math.sin(phi) * math.sin(theta)
            z = radius * math.cos(theta)
            
            if y > 0:
                glColor3fv(color1)
            else:
                glColor3fv(color2)
                
            glVertex3f(x, y, z)
        glEnd()

def display():
    global angle1, angle2, angle3, speed1, speed2, speed3

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Kamera pozisyonu ve bakış açısı
    gluLookAt(camera_x, camera_y, camera_z, look_x, look_y, look_z, 0, 1, 0)

    # Kürelerin dönme hareketleri
    glPushMatrix()
    glTranslatef(-2, 0, 0)  # Sol küre
    glRotatef(angle1, 1, 0, 0)
    draw_half_sphere(1, 30, 30, BLUE, YELLOW)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(2, 0, 0)  # Sağ küre
    glRotatef(angle2, 0, 1, 0)
    draw_half_sphere(1, 30, 30, RED, YELLOW)
    glPopMatrix()

    glPushMatrix()
    glRotatef(angle3, 0, 0, 1)  # Ortadaki küre
    draw_half_sphere(1, 30, 30, BLUE, RED)
    glPopMatrix()

    # Ekranı güncelle
    pygame.display.flip()
    pygame.time.wait(10)

    angle1 += speed1  # Dönme hızları
    angle2 += speed2
    angle3 += speed3

def main():
    global angle1, angle2, angle3, speed1, speed2, speed3, camera_x, camera_y, camera_z, look_x, look_y, look_z

    pygame.init()
    pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (WIDTH/HEIGHT), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    speed1 += 1
                elif event.key == pygame.K_DOWN:
                    speed1 -= 1
                elif event.key == pygame.K_LEFT:
                    speed2 -= 1
                elif event.key == pygame.K_RIGHT:
                    speed2 += 1
                elif event.key == pygame.K_SPACE:
                    speed3 += 1
                elif event.key == pygame.K_BACKSPACE:
                    speed3 -= 1
                elif event.key == pygame.K_w:
                    angle1 += 10
                elif event.key == pygame.K_s:
                    angle1 -= 10
                elif event.key == pygame.K_a:
                    angle2 -= 10
                elif event.key == pygame.K_d:
                    angle2 += 10
                elif event.key == pygame.K_q:
                    angle3 -= 10
                elif event.key == pygame.K_e:
                    angle3 += 10
                elif event.key == pygame.K_i:
                    camera_y += 5
                elif event.key == pygame.K_k:
                    camera_y -= 5
                elif event.key == pygame.K_j:
                    camera_x += 5
                elif event.key == pygame.K_l:
                    camera_x -= 5
                elif event.key == pygame.K_u:
                    camera_z += 5
                elif event.key == pygame.K_o:
                    camera_z -= 5
                elif event.key == pygame.K_r:
                    look_y += 5
                elif event.key == pygame.K_f:
                    look_y -= 5
                elif event.key == pygame.K_t:
                    look_x += 5
                elif event.key == pygame.K_g:
                    look_x -= 5
                elif event.key == pygame.K_y:
                    look_z += 5
                elif event.key == pygame.K_h:
                    look_z -= 5

        display()

if __name__ == "__main__":
    main()
