import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


circle_return = 0

while circle_return < 361:
    tim.color(random_color())
    tim.circle(100)
    tim.left(5)
    circle_return += 5

screen = t.Screen()
screen.exitonclick()
