from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")

    def move(self):
        x = self.xcor()
        y = self.ycor()
        if y + 10 > 290:
            new_x = x + 10
            new_y = y - 10
            self.setheading(-45)
            self.forward(10)
        elif y - 10 < - 290:
            new_x = x + 10
            new_y = y + 10
            self.setheading(45)
            self.forward(10)
        else:
            new_x = x + 10
            if self.heading() == 45:
                new_y = y + 10
            else:
                new_y = y - 10
            self.forward(10)

