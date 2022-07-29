import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
# RAND_Y = random.randint(-250, 250)
# RAND_X = random.randint(-270, 270)


class CarManager:

    def __init__(self):
        self.car_list = []
        self.create_cars()
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chc = random.randint(1, 6)
        if random_chc == 2:
            car = Turtle("square")
            car.turtlesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            car.setheading(180)
            rand_y = random.randint(-250, 250)
            car.goto(x=300, y=rand_y)
            self.car_list.append(car)

    def car_movement(self):
        for car in self.car_list:
            car.forward(self.move_speed)
            # self.detect_wall(car)

    def increase_speed(self, ):
        self.move_speed += MOVE_INCREMENT
    # def detect_wall(self, car):
    #     if car.xcor() < -270:
    #         rand_y = random.randint(-250, 250)
    #         car.goto(x=300, y=rand_y)




