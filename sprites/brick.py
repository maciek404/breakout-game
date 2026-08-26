import pygame
import random
from settings import BRICK_WIDTH, BRICK_HEIGHT, BRICK_COLORS, BRICK_POINTS, POWERUP_CHANCE, BRICK_RADIUS

class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, row):
        super().__init__()

        self.image = pygame.Surface((BRICK_WIDTH, BRICK_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(
            self.image, BRICK_COLORS[row],
            (0, 0, BRICK_WIDTH, BRICK_HEIGHT),
            border_radius=BRICK_RADIUS
        )

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.points = BRICK_POINTS[row]
        self.drops_powerup = random.random() < POWERUP_CHANCE
