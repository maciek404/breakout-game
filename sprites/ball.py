import pygame
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BALL_RADIUS, BALL_SPEED, BALL_COLOR

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        diameter = BALL_RADIUS * 2
        self.image = pygame.Surface((diameter, diameter), pygame.SRCALPHA)
        pygame.draw.circle(self.image, BALL_COLOR, (BALL_RADIUS, BALL_RADIUS), BALL_RADIUS)

        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        self.speed_x = BALL_SPEED * random.choice([-1, 1])
        self.speed_y = -BALL_SPEED

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left <= 0:
            self.rect.left = 0
            self.speed_x = abs(self.speed_x)

        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.speed_x = -abs(self.speed_x)

        if self.rect.top <= 0:
            self.rect.top = 0
            self.speed_y = abs(self.speed_y)

    def bounce_off_paddle(self, paddle):
        offset = (self.rect.centerx - paddle.rect.centerx) / (paddle.rect.width / 2)
        offset = max(-1, min(1, offset))

        min_offset = 0.25
        if -min_offset < offset < min_offset:
            if offset >= 0:
                offset = min_offset
            else:
                offset = -min_offset

        self.speed_x = BALL_SPEED * offset
        self.speed_y = -abs(self.speed_y)

    def reset(self):
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed_x = BALL_SPEED * random.choice([-1, 1])
        self.speed_y = -BALL_SPEED