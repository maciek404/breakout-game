from turtle import Turtle

class Block(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=0.8, stretch_len=4.8)
        self.goto(position)
        self.color(color)
