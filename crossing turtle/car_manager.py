from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.create_car()

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            random_y = random.randint(-250, 250)
            new_car = Turtle()
            new_car.setheading(180)
            new_car.shape("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random_y)
            new_car.shapesize(1, 2)
            self.all_cars.append(new_car)

    def move(self, number):
        move_distance = STARTING_MOVE_DISTANCE * number
        for car in self.all_cars:
            car.forward(move_distance)
