import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
# TODO 1. Create a Turtle that can move up and down the screen with up arrow and down arrow
player = Player()
# TODO 4. Update scoreboard
score = ScoreBoard()

cars = CarManager()


screen.onkey(fun=player.move_up, key="Up")
# screen.onkey(fun=player.move_down, key="Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # TODO 2. create cars that move from right edge of screen to left edge along y axis
    cars.create_cars()
    cars.car_movement()
    for car in cars.car_list:
        # TODO 3. detect collision with cars
        if car.distance(player) < 22:
            score.game_over()
            game_is_on = False
    if player.finish_line():
        score.next_level()
        player.next_level()
        cars.increase_speed()


# cars.detect_wall()



screen.exitonclick()
