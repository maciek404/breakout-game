import pygame
import random
from settings import SCREEN_HEIGHT, POWERUP_SIZE, POWERUP_SPEED, POWERUP_COLORS

POWERUP_TYPES = ["widen", "slow", "life"]

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.type = random.choice(POWERUP_TYPES)

        self.image = pygame.Surface((POWERUP_SIZE, POWERUP_SIZE))
        self.image.fill(POWERUP_COLORS[self.type])

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.speed_y = POWERUP_SPEED

    def update(self):
        self.rect.y += self.speed_y

        if self.rect.top > SCREEN_HEIGHT:
            self.kill()