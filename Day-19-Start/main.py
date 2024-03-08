import turtle
jim = turtle.Turtle()
screen = turtle.Screen()

jim.speed("fastest")
def move_forward():
    jim.forward(10)
def move_backward():
    jim.backward(10)
def turn_left():
    jim.left(10)
def turn_right():
    jim.right(10)
def clear():
    jim.clear()
    jim.teleport(0,0)
    jim.setheading(0)

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()