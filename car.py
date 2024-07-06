import random
from turtle import Turtle


class Car(Turtle):
    def __init__(self, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)

        y_cord = random.randint(-280, 280)
        self.goto(300, y_cord)

    def move(self, move_distance):
        new_x = self.xcor() - move_distance
        self.goto(new_x, self.ycor())
