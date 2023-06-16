import pygame
import random

# Defining some constants
SCREEN_WIDTH = 288
SCREEN_HEIGHT = 512
PIPE_GAP = 100
PIPE_SPEED = 2
GRAVITY = 0.15
JUMP_VELOCITY = -5


class Bird:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT / 2
        self.velocity = 0
        self.image = pygame.image.load('bird.png')

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

        # Make sure the bird doesn't go off the screen
        if self.y < 0:
            self.y = 0
            self.velocity = 0
        elif self.y > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT
            self.velocity = 0

    def jump(self):
        self.velocity = JUMP_VELOCITY


class Pipe:
    def __init__(self, x):
        self.x = x
        self.gap_y = random.randint(100, SCREEN_HEIGHT - 100 - PIPE_GAP)
        self.top_height = self.gap_y - PIPE_GAP / 2
        self.bottom_height = SCREEN_HEIGHT - self.gap_y - PIPE_GAP / 2
        self.image_top = pygame.image.load('pipe_top.png')
        self.image_bottom = pygame.image.load('pipe_bottom.png')

    def update(self):
        self.x -= PIPE_SPEED

    def offscreen(self):
        if self.x < -self.image_top.get_width():
            return True
        else:
            return False

    def collision(self, bird):
        bird_rect = pygame.Rect(bird.x, bird.y, bird.image.get_width(), bird.image.get_height())
        top_pipe_rect = pygame.Rect(self.x, 0, self.image_top.get_width(), self.top_height)
        bottom_pipe_rect = pygame.Rect(self.x, SCREEN_HEIGHT - self.bottom_height, self.image_bottom.get_width(),
                                       self.bottom_height)

        if bird_rect.colliderect(top_pipe_rect) or bird_rect.colliderect(bottom_pipe_rect):
            return True
        else:
            return False


class FlappyBird:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.bird = Bird()
        self.pipes = []
        self.score = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.jump()

            # Update bird
            self.bird.update()


