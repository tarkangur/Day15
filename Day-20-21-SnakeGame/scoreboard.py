from turtle import Turtle


FONT = ('Arial', 24, 'normal')
ALIGN = "center"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.penup()
        self.score_write()

    def score_clear(self):
        self.clear()

    def score_add(self):
        self.score += 1
        return self.score

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.score_write()

    def score_write(self):
        self.score_clear()
        self.teleport(0, 265)
        self.color("red")
        self.write(f"score: {self.score} High Score: {self.highscore}", align=ALIGN, font=FONT)
        self.hideturtle()
