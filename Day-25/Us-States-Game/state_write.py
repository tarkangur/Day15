from turtle import Turtle
FONT = ('Arial', 8, 'normal')


class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def correct_write(self, x, y, state):
        self.goto(x, y)
        self.write(state, align="center", font=FONT)
