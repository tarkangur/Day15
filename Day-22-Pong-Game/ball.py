from turtle import Turtle
import random
STARTING_HEAD = [45, -45, 135, -135]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.setheading(random.choice(STARTING_HEAD))
        self.move_speed = 0.1

    def paddle_hit(self):
        x = self.xcor()
        y = self.ycor()
        if x + 10 > 330 and self.heading() == 45:
            x -= 10
            y += 10
            self.setheading(135)
        elif x + 10 > 330 and self.heading() == 315:
            x -= 10
            y -= 10
            self.setheading(225)
        elif x - 10 < -330 and self.heading() == 225:
            x += 10
            y -= 10
            self.setheading(315)
        elif x - 10 < -330 and self.heading() == 135:
            x += 10
            y += 10
            self.setheading(45)
        self.move_speed *= 0.9

    def move(self):
        x = self.xcor()
        y = self.ycor()
        if y + 10 > 290 and self.heading() == 45:
            x += 10
            y -= 10
            self.setheading(315)
        elif y - 10 < - 290 and self.heading() == 315:
            x += 10
            y += 10
            self.setheading(45)
        elif y + 10 > 290 and self.heading() == 135:
            x += 10
            y -= 10
            self.setheading(225)
        elif y - 10 < - 290 and self.heading() == 225:
            x += 10
            y += 10
            self.setheading(135)
        else:
            self.forward(10)

    def restart_l(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.setheading(random.choice(STARTING_HEAD[2:4]))

    def restart_r(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.setheading(random.choice(STARTING_HEAD[0:2]))

