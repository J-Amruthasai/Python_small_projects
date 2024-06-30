# Capstone Project - Turtle Crossing Game

import time
from turtle import *
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600,height=400)
screen.tracer(0)

screen.listen()

player= Player()
car_manager= CarManager()
scoreboard = ScoreBoard()


screen.onkey(player.go_up,"Up")


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    
    for car in car_manager.all_cars:
        if car.distance(player)<20:
            game_on=False
            scoreboard.game_over()


    if player.finished():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
        
        
