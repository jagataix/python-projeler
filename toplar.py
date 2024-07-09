import pygame
import random

# Ekran boyutları
WIDTH, HEIGHT = 800, 600

# Renkler
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Top sınıfı
class Ball:
    def __init__(self, x, y, z, radius, speed_x, speed_y, speed_z):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.speed_z = speed_z

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.z += self.speed_z

    def check_collision(self):
        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.speed_x *= -1
        if self.y - self.radius <= 0 or self.y + self.radius >= HEIGHT:
            self.speed_y *= -1
        if self.z - self.radius <= 0 or self.z + self.radius >= 200:  # 3D düzlemde z ekseninde hareket etmesi
            self.speed_z *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), self.radius)

# Ana program
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("3D Kutu İçinde Toplar")
    clock = pygame.time.Clock()

    balls = []
    for _ in range(10):
        x = random.randint(50, WIDTH - 50)
        y = random.randint(50, HEIGHT - 50)
        z = random.randint(50, 150)  # 3D düzlemde rastgele z koordinatı
        radius = random.randint(10, 20)
        speed_x = random.randint(-5, 5)
        speed_y = random.randint(-5, 5)
        speed_z = random.randint(-3, 3)  # 3D düzlemde rastgele hızlar
        balls.append(Ball(x, y, z, radius, speed_x, speed_y, speed_z))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        # Topları hareket ettir ve çarpışmayı kontrol et
        for ball in balls:
            ball.move()
            ball.check_collision()
            ball.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
