import pygame
from settings import (SCREEN_WIDTH, SCREEN_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_SPEED, PADDLE_COLOR,
                      PADDLE_Y_OFFSET, PADDLE_WIDEN_MULTIPLIER, PADDLE_RADIUS)

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.base_width = PADDLE_WIDTH
        self.image = self._draw_image(PADDLE_WIDTH)

        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - PADDLE_Y_OFFSET

        self.speed = PADDLE_SPEED
        self.widen_end_time = 0

    def _draw_image(self, width):
        surface = pygame.Surface((width, PADDLE_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(
            surface, PADDLE_COLOR,
            (0, 0, width, PADDLE_HEIGHT),
            border_radius=PADDLE_RADIUS
        )
        return surface

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        if self.widen_end_time and pygame.time.get_ticks() > self.widen_end_time:
            self.set_width(self.base_width)
            self.widen_end_time = 0

    def apply_widen(self, duration_ms):
        self.set_width(int(self.base_width * PADDLE_WIDEN_MULTIPLIER))
        self.widen_end_time = pygame.time.get_ticks() + duration_ms

    def set_width(self, new_width):
        center = self.rect.center
        self.image = self._draw_image(new_width)
        self.rect = self.image.get_rect()
        self.rect.center = center