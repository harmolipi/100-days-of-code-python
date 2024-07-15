import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player: Player = Player()
car_manager: CarManager = CarManager()
scoreboard: Scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_forwards, "Up")

game_is_on: bool = True
while game_is_on:
    time.sleep(0.1)
    car_manager.update()
    scoreboard.update_scoreboard()

    if car_manager.is_in_contact_with_car(player):
        player.restart()
        car_manager.speed_up()
        scoreboard.show_game_over()
        game_is_on = False

    if player.is_at_finish_line():
        player.restart()
        car_manager.speed_up()
        scoreboard.increment_score()

    screen.update()

screen.exitonclick()
