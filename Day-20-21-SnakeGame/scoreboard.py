from turtle import Turtle

FONT = ('Arial', 24, 'normal')
ALIGN = "center"

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.score_write()

    def score_clear(self):
        self.clear()

    def score_add(self):
        self.score += 1
        return self.score

    def game_over(self):
        self.teleport(0,0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def score_write(self):
        self.score_clear()
        self.teleport(0, 265)
        self.color("red")
        self.write(f"score: {self.score}", align=ALIGN, font=FONT)
        self.hideturtle()
