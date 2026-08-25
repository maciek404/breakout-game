import pygame
import random
from settings import BRICK_WIDTH, BRICK_HEIGHT, BRICK_COLORS, BRICK_POINTS, POWERUP_CHANCE

class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, row):
        super().__init__()

        self.image = pygame.Surface((BRICK_WIDTH, BRICK_HEIGHT))
        self.image.fill(BRICK_COLORS[row])

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.points = BRICK_POINTS[row]
        self.drops_powerup = random.random() < POWERUP_CHANCE
