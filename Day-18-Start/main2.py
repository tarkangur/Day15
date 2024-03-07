import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
# color_list = ["silver", "dark gray", "gray", "dim gray", "black", "light slate gray", "slate gray",
#               "blue", "navy", "deep sky blue", "chocolate", "dark red", "red",
#               "dark magenta", "purple", "dark orchid", "dark green", "indian red", "lime", "gold"]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

tim.speed("fastest")
turn = [0, 90, 180, 270]
x = 0
while x < 10:
    x += 0.02
    tim.pensize(x)
    tim.color(random_color())
    direction = random.choice(turn)
    tim.right(direction)
    tim.forward(25)

screen = t.Screen()
screen.exitonclick()