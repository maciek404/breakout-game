from turtle import Turtle

class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("#FFFFFF")
        self.penup()
        self.goto(position)
        self.move_x = 0
        self.move_y = 0
        self.is_moving = False

    def start(self):
        self.move_x = 2
        self.move_y = 2
        self.is_moving = True

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.move_x *= -1

    def bounce_y(self):
        self.move_y *= -1

    def bounce_from_paddle(self, paddle):
        hit_position = self.xcor() - paddle.xcor()
        self.move_x = max(-3, min(3, hit_position / 10))
        self.move_y = abs(self.move_y)

    def reset(self, position):
        self.goto(position)
        self.move_x = 0
        self.move_y = 0
        self.is_moving = False