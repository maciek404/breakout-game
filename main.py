from turtle import Screen, RawTurtle, TPen
from paddle import Paddle
from ball import Ball
from block import Block
from scoreboard import Scoreboard


PADDLE_HOME_POSITION = (0, -350)
BALL_HOME_POSITION = (0, -330)
BLOCK_X_POSITION = -500
BLOCK_Y_POSITION = 100
BLOCKS = []
COLORS = [
    "#F2E94E",
    "#F2C14E",
    "#E76F51",
    "#D62828",
    "#9B5DE5",
    "#00BBF9",
    "#00F5D4",
    "#70E000",
    "#38B000",
    "#FF6B35"
]
BLOCKS_DESTROYED = 0

screen = Screen()
screen.setup(width=1200, height=900)
screen.bgcolor("#111111")
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle(PADDLE_HOME_POSITION)
ball = Ball(BALL_HOME_POSITION)
scoreboard = Scoreboard()
for color in COLORS:
    row = []
    for _ in range(11):
        position = (BLOCK_X_POSITION, BLOCK_Y_POSITION)
        block = Block(position, color)
        block.color('black', color)
        BLOCK_X_POSITION += 100
        row.append(block)
    BLOCKS.append(row)
    BLOCK_Y_POSITION += 20
    BLOCK_X_POSITION = -500
total_blocks = sum(len(row) for row in BLOCKS)

screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")
screen.onkey(ball.start, "space")

while scoreboard.lives > 0:
    screen.update()
    ball.move()

    if ball.xcor() > 580 or ball.xcor() < -580:
        ball.bounce_x()

    if ball.ycor() < -330 and ball.distance(paddle) < 100:
        ball.bounce_from_paddle(paddle)

    if ball.ycor() > 430:
        ball.bounce_y()
    for row in BLOCKS:
        for block in row:
            if block.isvisible():
                if (
                    abs(ball.xcor() - block.xcor()) < 50
                    and abs(ball.ycor() - block.ycor()) < 12
                ):
                    block.hideturtle()
                    ball.bounce_y()
                    scoreboard.increase_score()
                    BLOCKS_DESTROYED += 1
                    if BLOCKS_DESTROYED == total_blocks:
                        scoreboard.win_game()
                        break
                    break

    if ball.ycor() < -470:
        scoreboard.decrease_lives()
        if scoreboard.lives > 0:
            ball.reset(BALL_HOME_POSITION)
            paddle.goto(PADDLE_HOME_POSITION)
        else:
            scoreboard.game_over()

screen.exitonclick()