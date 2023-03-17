import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#Object instances for Turtle and Cars
turtle = Player()
cars = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(turtle.move, "Up")

game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_cars()

    #Collision detection with turtle and car
    for car in cars.all_cars:
        if car.distance(turtle)<20:
            scoreboard.game_over()
            game_is_on = False

    #Successful crossing detection
    if turtle.is_at_finish():
        turtle.go_to_start()
        cars.level_up()
        scoreboard.increase_level()



screen.exitonclick()
