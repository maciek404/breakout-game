from turtle import Screen, RawTurtle
from paddle import Paddle
from ball import Ball
from block import Block
from scoreboard import Scoreboard


PADDLE_HOME_POSITION = (0, -350)
BALL_HOME_POSITION = (0, -330)
BLOCK_X_POSITION = -500
BLOCK_Y_POSITION = 100
BLOCKS = []
COLORS = ["#590d22", "#800f2f", "#a4133c", "#c9184a", "#ff4d6d", "#ff758f", "#ff8fa3", "#ffb3c1", "#ffccd5", "#fff0f3"]

screen = Screen()
screen.setup(width=1200, height=900)
screen.bgcolor("black")
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

screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

while scoreboard.lives > 0:
    screen.update()
    ball.move()

    if ball.xcor() > 580 or ball.xcor() < -580:
        ball.bounce_x()

    if ball.ycor() < -330 and ball.distance(paddle) < 100:
        ball.bounce_y()

    if ball.ycor() > 430:
        ball.bounce_y()
    for row in BLOCKS:
        y = 61
        for block in row:
            if ball.ycor() > y and ball.distance(block) < 50:
                block.goto(10000, 10000)
                block.hideturtle()
                ball.bounce_y()
                scoreboard.increase_score()
        y += 25

    if ball.ycor() < -470:
        scoreboard.decrease_lives()
        ball.bounce_y()
        ball.goto(BALL_HOME_POSITION)
scoreboard.game_over()
screen.exitonclick()