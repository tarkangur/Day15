import turtle as t
import random

jim = t.Turtle()
jim.color("red")
jim.shape("turtle")

# for _ in range(15):
#     jim.pendown()
#     jim.forward(10)
#     jim.penup()
#     jim.forward(10)

side = 3
color_list = ["silver", "dark gray", "gray", "dim gray", "black", "light slate gray", "slate gray",
              "blue", "navy", "deep sky blue", "chocolate", "dark red", "red",
              "dark magenta", "purple", "dark orchid", "dark green", "indian red", "lime", "gold"]
while side < 11:
    turn = 360 / side
    color = random.choice(color_list)
    for _ in range(side):
        jim.pencolor(color)
        jim.forward(100)
        jim.right(turn)
    side += 1








screen = t.Screen()
screen.exitonclick()
