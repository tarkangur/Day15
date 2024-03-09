from turtle import Screen
import time
import snake
import food
import scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = snake.Snake()
food = food.Food()
score = scoreboard.ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    kontrol = 0
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score_add()
        score.score_write()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()
    for i in snake.segments[1:]:
        if snake.head.distance(i) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()
