import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.car_move()
    if player.ycor() > 290:
        player.level_up()
        car_manager.car_level_up()
        scoreboard.level += 1
        scoreboard.update_level()
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
