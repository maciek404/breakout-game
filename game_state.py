import pygame
from settings import STARTING_LIVES, FONT_NAME, FONT_SIZE, WHITE, SCREEN_WIDTH

class GameState:
    def __init__(self):
        self.score = 0
        self.lives = STARTING_LIVES
        self.level = 0
        self.font = pygame.font.Font(FONT_NAME, FONT_SIZE)

    def add_score(self, points):
        self.score += points

    def lose_life(self):
        self.lives -= 1
        return self.lives <= 0

    def next_level(self):
        self.level += 1

    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        lives_text = self.font.render(f"Lives: {self.lives}", True, WHITE)
        level_text = self.font.render(f"Level: {self.level + 1}", True, WHITE)

        screen.blit(score_text, (10, 10))

        lives_rect = lives_text.get_rect(topright=(SCREEN_WIDTH - 10, 10))
        screen.blit(lives_text, lives_rect)

        level_rect = level_text.get_rect(midtop=(SCREEN_WIDTH // 2, 10))
        screen.blit(level_text, level_rect)