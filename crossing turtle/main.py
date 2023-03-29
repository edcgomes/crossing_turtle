import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossing Turtle")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
scoreboard.track_score()
car = CarManager()
car.hideturtle()

screen.listen()
screen.onkey(player.move, "Up")
screen.update()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move(scoreboard.number)
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() >= 280:
        player.end_line()
        scoreboard.number += 1
        scoreboard.track_score()

screen.exitonclick()
