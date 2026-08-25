import pygame
from settings import (BRICK_ROWS, BRICK_COLS, BRICK_WIDTH, BRICK_HEIGHT, BRICK_PADDING, BRICK_TOP_OFFSET,
                      BRICK_SIDE_OFFSET)
from sprites.brick import Brick

LEVELS = [
    [
        "0000000000",
        "1111111111",
        "2222222222",
        "3333333333",
        "4444444444",
    ],
    [
        "....00....",
        "...1111...",
        "..222222..",
        ".33333333.",
        "4444444444",
    ],
    [
        "0.0.0.0.0.",
        ".1.1.1.1.1",
        "2.2.2.2.2.",
        ".3.3.3.3.3",
        "4.4.4.4.4.",
    ],
    [
        "0000000000",
        "1........1",
        "2........2",
        "3........3",
        "4444444444",
    ],
]

def create_level(level_index):
    layout = LEVELS[level_index % len(LEVELS)]
    bricks = pygame.sprite.Group()

    for row_index, row in enumerate(layout):
        for col_index, char in enumerate(row):
            if char == ".":
                continue

            row_color = int(char)
            x = BRICK_SIDE_OFFSET + col_index * (BRICK_WIDTH + BRICK_PADDING)
            y = BRICK_TOP_OFFSET + row_index * (BRICK_HEIGHT + BRICK_PADDING)
            brick = Brick(x, y, row_color)
            bricks.add(brick)

    return bricks

def total_levels():
    return len(LEVELS)

# def create_brick_wall():
#     bricks = pygame.sprite.Group()
#
#     for row in range(BRICK_ROWS):
#         for col in range(BRICK_COLS):
#             x = BRICK_SIDE_OFFSET + col * (BRICK_WIDTH + BRICK_PADDING)
#             y = BRICK_TOP_OFFSET + row * (BRICK_HEIGHT + BRICK_PADDING)
#             brick = Brick(x, y, row)
#             bricks.add(brick)
#
#     return bricks
