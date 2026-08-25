import pygame
import sys
from settings import (SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BG_COLOR, BALL_SPEED_INCREMENT, POWERUP_DURATION,
                      BALL_SLOW_MULTIPLIER, TITLE_FONT_SIZE, SUBTITLE_FONT_SIZE, FONT_NAME, WHITE)
from sprites.paddle import Paddle
from sprites.ball import Ball
from sprites.level import create_level
from sprites.powerup import PowerUp
from game_state import GameState
from sound_manager import SoundManager

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()

title_font = pygame.font.Font(FONT_NAME, TITLE_FONT_SIZE)
subtitle_font = pygame.font.Font(FONT_NAME, SUBTITLE_FONT_SIZE)

def new_game_objects():
    paddle = Paddle()
    ball = Ball()
    state = GameState()
    bricks = create_level(state.level)
    powerups = pygame.sprite.Group()

    all_sprites = pygame.sprite.Group()
    all_sprites.add(paddle, ball)

    return paddle, ball, state, bricks, powerups, all_sprites

sounds = SoundManager()

paddle, ball, state, bricks, powerups, all_sprites = new_game_objects()

app_state = "menu"
level_transition_timer = 0
ball_slow_end_time = 0

def draw_text_center(text, font, color, y_offset=0):
    surface = font.render(text, True, color)
    rect = surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + y_offset))
    screen.blit(surface, rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if app_state == "menu" and event.key == pygame.K_SPACE:
                app_state = "playing"

            elif app_state == "playing" and event.key in (pygame.K_p, pygame.K_ESCAPE):
                app_state = "paused"

            elif app_state == "paused" and event.key in (pygame.K_p, pygame.K_ESCAPE):
                app_state = "playing"

            elif app_state == "game_over" and event.key == pygame.K_r:
                paddle, ball, state, bricks, powerups, all_sprites = new_game_objects()
                level_transition_timer = 0
                ball_slow_end_time = 0
                app_state = "playing"

    # ----------------------- GAME LOGIC --------------------------
    if app_state == "playing":
        if level_transition_timer > 0:
            level_transition_timer -= 1
        else:
            all_sprites.update()
            powerups.update()

            if pygame.sprite.collide_rect(ball, paddle) and ball.speed_y > 0:
                ball.bounce_off_paddle(paddle)
                sounds.play("bounce")

            hit_brick = pygame.sprite.spritecollide(ball, bricks, dokill=True)
            if hit_brick:
                ball.speed_y *= -1
                sounds.play("brick_break")
                for brick in hit_brick:
                    state.add_score(brick.points)
                    if brick.drops_powerup:
                        powerups.add(PowerUp(brick.rect.centerx, brick.rect.centery))

            caught_powerups = pygame.sprite.spritecollide(paddle, powerups, dokill=True)
            for pu in caught_powerups:
                sounds.play("powerup")
                if pu.type == "widen":
                    paddle.apply_widen(POWERUP_DURATION)
                elif pu.type == "life":
                    state.lives += 1
                elif pu.type == "slow":
                    ball.speed_x *= BALL_SLOW_MULTIPLIER
                    ball.speed_y *= BALL_SLOW_MULTIPLIER
                    ball_slow_end_time = pygame.time.get_ticks() + POWERUP_DURATION

            if ball_slow_end_time and pygame.time.get_ticks() > ball_slow_end_time:
                ball.speed_x /= BALL_SLOW_MULTIPLIER
                ball.speed_y /= BALL_SLOW_MULTIPLIER
                ball_slow_end_time = 0

            if ball.rect.top > SCREEN_HEIGHT:
                is_game_over = state.lose_life()
                if is_game_over:
                    app_state = "game_over"
                    sounds.play("game_over")
                else:
                    sounds.play("life_lost")
                    ball.reset()

            if len(bricks) == 0:
                state.next_level()
                bricks = create_level(state.level)
                ball.reset()
                ball.speed_x += BALL_SPEED_INCREMENT if ball.speed_x > 0 else -BALL_SPEED_INCREMENT
                ball.speed_y -= BALL_SPEED_INCREMENT
                level_transition_timer = FPS

    # ------------------------- DRAWING -------------------------
    screen.fill(BG_COLOR)

    if app_state == "menu":
        draw_text_center("BREAKOUT", title_font, WHITE, y_offset=-40)
        draw_text_center("Press SPACE to start", subtitle_font, WHITE, y_offset=20)
        draw_text_center("Control: ← → or A / D | Pause: P", subtitle_font, WHITE, y_offset=60)

    elif app_state in ("playing", "paused"):
        all_sprites.draw(screen)
        bricks.draw(screen)
        powerups.draw(screen)
        state.draw(screen)

        if level_transition_timer > 0:
            draw_text_center(f"Level {state.level + 1}", title_font, WHITE)

        if app_state == "paused":
            draw_text_center("PAUSED", title_font, WHITE, y_offset=-20)
            draw_text_center("Press P to continue", subtitle_font, WHITE, y_offset=30)

    elif app_state == "game_over":
        draw_text_center("GAME OVER", title_font, (255, 80, 80), y_offset=-40)
        draw_text_center(f"Score: {state.score}", subtitle_font, WHITE, y_offset=10)
        draw_text_center("Press R to play again", subtitle_font, WHITE, y_offset=50)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()