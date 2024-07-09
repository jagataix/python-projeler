import pygame
import random

# Oyun alanı boyutları
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
BLOCK_SIZE = 20

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Tetromino şekilleri
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[1, 1], [1, 1]]  # O
]

class Tetromino:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shape = random.choice(SHAPES)
        self.color = random.choice([RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW, ORANGE])

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

    def draw(self, surface):
        for y in range(len(self.shape)):
            for x in range(len(self.shape[0])):
                if self.shape[y][x]:
                    pygame.draw.rect(surface, self.color, (self.x * BLOCK_SIZE + x * BLOCK_SIZE,
                                                            self.y * BLOCK_SIZE + y * BLOCK_SIZE,
                                                            BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(surface, BLACK, (self.x * BLOCK_SIZE + x * BLOCK_SIZE,
                                                       self.y * BLOCK_SIZE + y * BLOCK_SIZE,
                                                       BLOCK_SIZE, BLOCK_SIZE), 2)

class TetrisGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Tetris')
        self.clock = pygame.time.Clock()

        self.board = [[BLACK for _ in range(SCREEN_WIDTH // BLOCK_SIZE)] for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]
        self.current_piece = Tetromino(3, 0)

        self.game_over = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move_piece(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    self.move_piece(1, 0)
                elif event.key == pygame.K_DOWN:
                    self.move_piece(0, 4)
                elif event.key == pygame.K_UP:
                    self.current_piece.rotate()
                    if self.check_collision(0, 0):
                        self.current_piece.rotate()
                        self.current_piece.rotate()
                        self.current_piece.rotate()

    def move_piece(self, dx, dy):
        if not self.check_collision(dx, dy):
            self.current_piece.x += dx
            self.current_piece.y += dy
        elif dy > 0:
            self.lock_piece()

    def lock_piece(self):
        for y in range(len(self.current_piece.shape)):
            for x in range(len(self.current_piece.shape[0])):
                if self.current_piece.shape[y][x]:
                    self.board[self.current_piece.y + y][self.current_piece.x + x] = self.current_piece.color
        self.clear_lines()
        self.current_piece = Tetromino(3, 0)
        if self.check_collision(0, 0):
            self.game_over = True

    def clear_lines(self):
        new_board = [row for row in self.board if any(block == BLACK for block in row)]
        lines_cleared = len(self.board) - len(new_board)
        self.board = [[BLACK for _ in range(SCREEN_WIDTH // BLOCK_SIZE)] for _ in range(lines_cleared)] + new_board

    def check_collision(self, dx, dy):
        for y in range(len(self.current_piece.shape)):
            for x in range(len(self.current_piece.shape[0])):
                if self.current_piece.shape[y][x]:
                    next_x = self.current_piece.x + x + dx
                    next_y = self.current_piece.y + y + dy
                    if next_x < 0 or next_x >= len(self.board[0]) or \
                            next_y >= len(self.board) or \
                            (next_y >= 0 and self.board[next_y][next_x] != BLACK):
                        return True
        return False

    def draw(self):
        self.screen.fill(WHITE)

        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                pygame.draw.rect(self.screen, self.board[y][x], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(self.screen, BLACK, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

        self.current_piece.draw(self.screen)

        if self.game_over:
            font = pygame.font.SysFont(None, 36)
            text = font.render('GAME OVER', True, RED)
            self.screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))

        pygame.display.flip()

    def run(self):
        fall_time = 0
        fall_speed = 500  # milisaniye

        while not self.game_over:
            self.handle_events()
            fall_time += self.clock.get_rawtime()
            self.clock.tick()

            if fall_time >= fall_speed:
                self.move_piece(0, 1)
                fall_time = 0

            self.draw()

        pygame.quit()

if __name__ == '__main__':
    game = TetrisGame()
    game.run()
