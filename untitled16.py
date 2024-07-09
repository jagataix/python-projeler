import pygame
import sys
import math

# Ekran boyutları
WIDTH, HEIGHT = 800, 600
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2

# Renkler
YELLOW = (200, 100, 0)
PINK = (300, 192, 203)

# Pygame başlat
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Kalp Deseni")

clock = pygame.time.Clock()

def draw_heart(scale):
    # Kalp desenini çizmek için noktaların listesi
    points = []
    for t in range(0, 360):
        x = 16 * (math.sin(math.radians(t)) ** 3)
        y = 13 * math.cos(math.radians(t)) - 5 * math.cos(2 * math.radians(t)) - 2 * math.cos(3 * math.radians(t)) - math.cos(4 * math.radians(t))
        points.append((x * scale + CENTER_X, -y * scale + CENTER_Y))

    # Kalp desenini çiz
    pygame.draw.polygon(screen, PINK, points)
    pygame.draw.lines(screen, YELLOW, False, points, 2)

# Ana döngü
running = True
scale = 5.0
scale_factor = 0.2

while running:
    screen.fill(YELLOW)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Kalp desenini çiz
    draw_heart(scale)

    # Ekranı güncelle
    pygame.display.flip()
    clock.tick(200)

    # Ölçek faktörünü güncelle ve sınırla
    scale += scale_factor
    if scale < 5 or scale > 50:
        scale_factor *= -1

pygame.quit()
sys.exit()
