import pygame
import sys

# Oyunun başlatılması
pygame.init()

# Ekran boyutu ve başlığı
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple GTA-like Game")

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Oyuncu karakteri
player_img = pygame.Surface((30, 30))
player_img.fill(WHITE)
player_rect = player_img.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
player_speed = 5

# Mermiler
bullet_img = pygame.Surface((10, 10))
bullet_img.fill(WHITE)
bullets = []

# Oyun döngüsü
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:  # W tuşu
                bullet = bullet_img.get_rect(center=player_rect.center)
                bullet.speed_x = 0
                bullet.speed_y = -10
                bullets.append(bullet)
            elif event.key == pygame.K_s:  # S tuşu
                bullet = bullet_img.get_rect(center=player_rect.center)
                bullet.speed_x = 0
                bullet.speed_y = 10
                bullets.append(bullet)
            elif event.key == pygame.K_a:  # A tuşu
                bullet = bullet_img.get_rect(center=player_rect.center)
                bullet.speed_x = -10
                bullet.speed_y = 0
                bullets.append(bullet)
            elif event.key == pygame.K_d:  # D tuşu
                bullet = bullet_img.get_rect(center=player_rect.center)
                bullet.speed_x = 10
                bullet.speed_y = 0
                bullets.append(bullet)

    # Mermilerin hareketi ve ekrandan çıkıp çıkmadığının kontrolü
    for bullet in bullets:
        bullet.x += bullet.speed_x
        bullet.y += bullet.speed_y
        if bullet.left > SCREEN_WIDTH or bullet.right < 0 or bullet.top > SCREEN_HEIGHT or bullet.bottom < 0:
            bullets.remove(bullet)

    # Oyuncunun hareketi
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    if keys[pygame.K_UP]:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN]:
        player_rect.y += player_speed

    # Ekran sınırlarını kontrol etme
    player_rect.x = max(0, min(SCREEN_WIDTH - player_rect.width, player_rect.x))
    player_rect.y = max(0, min(SCREEN_HEIGHT - player_rect.height, player_rect.y))

    # Oyuncuyu ve mermileri ekrana çizme
    screen.blit(player_img, player_rect)
    for bullet in bullets:
        screen.blit(bullet_img, bullet)

    pygame.display.flip()

    # Oyunu güncelleme
    pygame.display.update()

    # Oyun hızı
    pygame.time.Clock().tick(60)

# Oyunun kapatılması
pygame.quit()
sys.exit()
