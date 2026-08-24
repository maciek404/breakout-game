from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("#F2E94E")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.goto(position)

    def move_right(self):
        if self.xcor() < 490:
            self.forward(20)

    def move_left(self):
        if self.xcor() > -490:
            self.backward(20)