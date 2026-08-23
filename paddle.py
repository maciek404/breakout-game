from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.goto(position)

    def move_right(self):
        self.forward(20)

    def move_left(self):
        self.backward(20)