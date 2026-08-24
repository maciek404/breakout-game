from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = 3
        self.color("#F2E94E")
        self.penup()
        self.hideturtle()
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(-500, 400)
        self.write(f"LIVES: {self.lives}", align="left", font=("Courier", 20, "bold"))
        self.goto(500, 400)
        self.write(f"SCORE: {self.score}", align="right", font=("Courier", 20, "bold"))

    def increase_score(self):
        self.score += 10
        self.refresh()

    def decrease_lives(self):
        self.lives -= 1
        self.refresh()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Courier", 36, "bold"))

    def win_game(self):
        self.clear()
        self.goto(0,0)
        self.write("YOU WIN!", align="center", font=("Courier", 36, "bold"))