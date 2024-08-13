import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()  # Initialize the clock

# Defining the color
black = (0, 0, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):  # Use double underscores for the constructor
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))  # Fill with red color
        self.rect = self.image.get_rect()
        self.rect.center = (400, 400)
        self.velocity = pygame.math.Vector2(0, 0)

    def update(self):
        self.velocity.y += 0.5  # Gravity
        self.rect.y += self.velocity.y

        # Basic platform collision
        if self.rect.bottom > 550:
            self.rect.bottom = 550
            self.velocity.y = 0

player = Player()
all_sprites = pygame.sprite.Group(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    all_sprites.update()

    screen.fill(black)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()